import twint

c = twint.Config()

#for k in ky:
c.Search = "flood"
c.Limit= 300
c.Min_likes = 1
c.Custom["tweet"] = ["id", "username","tweet"]
c.Output="/Users/cosmos/Desktop/SIH - MAIN/sih/BACKEND/WebScrapping/data_30_custom_columns.json"
c.Store_json=True
#c.Store_object = True
c.Hide_output = True

twint.run.Search(c)