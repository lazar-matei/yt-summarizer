
import pandas as pd
import re

from youtube_transcript_api import YouTubeTranscriptApi
from summarizer import summarize_transcripts
from settings import _NO_VIDEOS_TO_CONSIDER


def get_summaries():
    urls = _read_urls()
    transcripts, videos = _get_transcripts_from_urls(urls[:_NO_VIDEOS_TO_CONSIDER])
    summarized = summarize_transcripts(transcripts)
    return summarized, videos


def _read_urls():
    df = pd.read_excel('data/urls.xlsx', sheet_name='Sheet1')
    return df.iloc[:, 0].tolist()


def _get_transcripts_from_urls(urls):

    transcripts = []
    videos = []

    for video_url in urls:
        video_id = _get_video_id(video_url)
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
        except Exception as e:
            transcript = None

        full_text = _make_full_text_from_transcript(transcript)

        if transcript:
            transcripts.append(full_text)
            videos.append(video_url)
    
    return transcripts, videos


def _make_full_text_from_transcript(transcript):
    if not transcript:
        return None
    return ' '.join(obj['text'] for obj in transcript)


def _get_video_id(url):
    # Generat cu GPT. Posibil sa nu fie completa

    # Extract the video ID from the URL using a regular expression
    match = re.search(r'(?<=v=)[^&]+', url)
    if match:
        video_id = match.group()
    else:
        # If no match is found, return None or raise an exception
        video_id = None
    return video_id