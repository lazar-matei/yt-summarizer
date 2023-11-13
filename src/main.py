
from transcripts import get_summaries
from categorize import send_transcripts_to_boxes


if __name__ == "__main__":
    summaries, videos = get_summaries()
    send_transcripts_to_boxes(summaries, videos)

