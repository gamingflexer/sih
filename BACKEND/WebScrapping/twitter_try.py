import twint

c = twint.Config()
c.Username = "RahulGandhi"
c.Limit = 100
c.Store_csv = True
c.Output = "xyx.csv"
c.Lang = "en"
c.Translate = True
c.TranslateDest = "it"
twint.run.Search(c)
