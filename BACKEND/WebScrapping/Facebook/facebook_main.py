from facebook_scraper import get_posts
import pandas as pd

df_ori = pd.DataFrame(columns=['post_id', 'text', 'post_text', 'shared_text', 'time', 'image',
                               'image_lowquality', 'images', 'images_description', 'images_lowquality',
                               'images_lowquality_description', 'video', 'video_duration_seconds',
                               'video_height', 'video_id', 'video_quality', 'video_size_MB',
                               'video_thumbnail', 'video_watches', 'video_width', 'likes', 'comments',
                               'shares', 'post_url', 'link', 'user_id', 'username', 'user_url',
                               'is_live', 'factcheck', 'shared_post_id', 'shared_time',
                               'shared_user_id', 'shared_username', 'shared_post_url', 'available',
                               'comments_full', 'reactors', 'w3_fb_url', 'reactions', 'reaction_count',
                               'image_id', 'image_ids', 'fetched_time'])

HASHTAG = ''

for post in get_posts(hashtag=HASHTAG, pages=40, extra_info=True, cookies='facebook.com_cookies.txt'):
    print(post)
    dataframe = post
    df = pd.DataFrame.from_dict(dataframe, orient='index')
    df = df.transpose()
    df_ori = df_ori.append(df)

df_ori.to_csv(r'Scrapped_FB.csv', index=False)

file = open('..//abc.json', 'w', encoding='utf-8')
file.write(df_ori)
file.close()
