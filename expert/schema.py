from experta import Fact, Field

class MobileApp(Fact):
    name = Field(str, mandatory=True)
    price = Field(float, mandatory=True)
    category = Field(str, mandatory=True)
    size = Field(int, mandatory=True)
    rating_count = Field(int, mandatory=True)
    user_rating = Field(float, mandatory=True)
    age_rating = Field(str, mandatory=True) 

class UserAppRequest(Fact):
    price = Field(float, mandatory=False, default=0)
    category = Field(str, mandatory=False)
    size = Field(int, mandatory=False, default=0)
    rating_count = Field(int, mandatory=False, default=0)
    user_rating = Field(float, mandatory=False, default=0)
    age_rating = Field(str, mandatory=False) 