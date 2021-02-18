from TikTokApi import TikTokApi
import pandas as pd

verifyFp = "verify_kkmup6my_DSi6YaCI_Sc4v_4Vmx_AjJJ_mWhrDDVZDWI5"
api = TikTokApi.get_instance(custom_verifyFp = verifyFp)

# data struct to extract relevant fields
def simple_dict(tiktok_dict):
  to_return = {}
  to_return['user_name'] = tiktok_dict['author']['uniqueId']
  to_return['user_id'] = tiktok_dict['author']['id']
  to_return['video_id'] = tiktok_dict['id']
  to_return['video_desc'] = tiktok_dict['desc']
  to_return['video_time'] = tiktok_dict['createTime']
  to_return['video_length'] = tiktok_dict['video']['duration']
  to_return['video_link'] = 'https://www.tiktok.com/@{}/video/{}?lang=en'.format(to_return['user_name'], to_return['video_id'])
  to_return['n_likes'] = tiktok_dict['stats']['diggCount']
  to_return['n_shares'] = tiktok_dict['stats']['shareCount']
  to_return['n_comments'] = tiktok_dict['stats']['commentCount']
  to_return['n_plays'] = tiktok_dict['stats']['playCount']
  return to_return

username = 'leylannis'
n_videos = 2000
liked_videos = api.userLikedbyUsername(username, count=n_videos)
liked_videos = [simple_dict(v) for v in liked_videos]
liked_videos_df = pd.DataFrame(liked_videos)
liked_videos_df.to_csv('{}_liked_videos.csv'.format(username), index=False)