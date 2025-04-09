from experta import Fact, Field

class MobileApp(Fact):
    name = Field(str, mandatory=True)
    price = Field(str, mandatory=True)
    app_type = Field(str, mandatory=True)
    platform = Field(str, mandatory=True)
    monetization_model = Field(str, mandatory=True)
    user_rating = Field(str, mandatory=True)
    age_rating = Field(str, mandatory=True)
    popularity = Field(str, mandatory=True)
    download_count = Field(int, default=0)

class UserAppRequest(Fact):
    name = Field(str, mandatory=False)
    price = Field(str, mandatory=False)
    app_type = Field(str, mandatory=False)
    platform = Field(str, mandatory=False)
    monetization_model = Field(str, mandatory=False)
    user_rating = Field(str, mandatory=False)
    age_rating = Field(str, mandatory=False)
    popularity = Field(str, mandatory=False)
    download_count_from = Field(int, default=0)
    download_count_to = Field(int, default=0)