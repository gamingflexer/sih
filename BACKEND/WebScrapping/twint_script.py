# pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
import twint

c = twint.Config()

# for k in ky:
c.Search = "flood"
c.Limit = 300
c.Min_likes = 1
# c.Custom["tweet"] = ["id", "username","tweet",'date','time','language',"name","mentions", "urls", "photos",
# "replies_count", "retweets_count", "likes_count", "hashtags","cashtags",'link','']
c.Output = "xyx.json"
c.Store_json = True
# c.Store_object = True
c.Hide_output = True

twint.run.Search(c)
