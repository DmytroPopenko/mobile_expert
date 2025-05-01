from expert.schema import MobileApp, UserAppRequest
from experta import KnowledgeEngine, Fact, Rule, DefFacts, AS, L, W, P, AND, OR, NOT, TEST, MATCH
from expert.utils import load_apps_info

class ExpertAgent(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.df = load_apps_info()
        self.output_list = []

    @DefFacts()
    def _initial_action(self):
        for _, row in self.df.iterrows():
            yield MobileApp(
                name=row['track_name'],
                size=row['size_bytes'],
                price=row['price'],
                category=row['prime_genre'],
                rating_count=row['rating_count_tot'],
                user_rating=row['user_rating'],
                age_rating=row['cont_rating'],   
            )
        
    @Rule(
        UserAppRequest(category=MATCH.user_cat, user_rating=MATCH.expected_rating),
        MobileApp(category=MATCH.user_cat, user_rating=MATCH.rating, name=MATCH.app_name),
        TEST(lambda expected_rating, rating: rating >= expected_rating)
    )
    def recommend_app(self, app_name):
        print(f"✅ You might like: {app_name}")
        self.output_list.append(app_name)
    