
import pandas as pd
import random


def send_transcripts_to_boxes(summaries, videos):
    categorized = _append_categories_to_summaries(summaries, videos)
    categorized.to_excel('data/emails.xlsx', sheet_name='Sheet1', index=False)


def _append_categories_to_summaries(summaries, videos):
    df = _create_dataframe(summaries, videos)
    return _append_to_person(df)


def _create_dataframe(summaries, videos):
    return pd.DataFrame({
        'url': videos,
        'summary': summaries,
    })


def _append_to_person(df):
    df['email'] = df.apply(lambda row: _to_whom(row), axis=1)
    return df


def _to_whom(row):
    people_df = _read_people()
    belongs_to = random.randint(0, people_df.size-1)
    return people_df.iloc[belongs_to]['email']


def _read_people():
    df = pd.read_excel('data/urls.xlsx', sheet_name='Sheet3', header=None)
    df.columns = ['email']
    return df


if __name__ == "__main__":
    list1 = ['asd asd asd ', 'bcd bas bas', 'ccc ccc ccc']
    list2 = ['v1', 'v2', 'v3']
    # send_transcripts_to_boxes(list1, list2)

    _to_whom([])