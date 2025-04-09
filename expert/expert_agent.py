from expert.schema import MobileApp, UserAppRequest
from experta import KnowledgeEngine, Fact, Rule, DefFacts, AS, L, W, P, AND, OR, NOT, TEST, MATCH

class ExpertAgent(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield MobileApp(name="WhatsApp", price="Free", app_type="Messaging", platform="Android", monetization_model="Free", user_rating="4.4", age_rating="3+", popularity="High", dowload_count=1000000000)
        yield MobileApp(name="Facebook", price="Free", app_type="Social Media", platform="Android", monetization_model="Free", user_rating="4.0", age_rating="13+", popularity="High", download_count=500000)
        yield MobileApp(name="Instagram", price="Free", app_type="Social Media", platform="Android", monetization_model="Free", user_rating="4.5", age_rating="13+", popularity="High", download_count=500000)
        yield MobileApp(name="Snapchat", price="Free", app_type="Social Media", platform="Android", monetization_model="Free", user_rating="4.3", age_rating="13+", popularity="High", download_count=500000)
        yield MobileApp(name="Twitter", price="Free", app_type="Social Media", platform="Android", monetization_model="Free", user_rating="4.2", age_rating="17+", popularity="High", download_count=500000)
        yield MobileApp(name="LinkedIn", price="Free", app_type="Social Media", platform="Android", monetization_model="Free", user_rating="4.1", age_rating="17+", popularity="High", download_count=500000)
        yield MobileApp(name="TikTok", price="Free", app_type="Social Media", platform="Android", monetization_model="Free", user_rating="4.6", age_rating="12+", popularity="High", download_count=500000)
        yield MobileApp(name="Pinterest", price="Free", app_type="Social Media", platform="Android", monetization_model="Free", user_rating="4.7", age_rating="12+", popularity="High", download_count=500000)
        yield MobileApp(name="Reddit", price="Free", app_type="Social Media", platform="Android", monetization_model="Free", user_rating="4.8", age_rating="17+", popularity="High", download_count=500000)
        yield MobileApp(name="YouTube", price="Free", app_type="Video Streaming", platform="Android", monetization_model="Free", user_rating="4.9", age_rating="17+", popularity="High", download_count=500000)


    @Rule(
        UserAppRequest(app_type=MATCH.user_cat, download_count_from=MATCH.min_dl),
        MobileApp(app_type=MATCH.user_cat, download_count=MATCH.app_dl, name=MATCH.app_name),
        TEST(lambda app_dl, min_dl: app_dl >= min_dl)
    )
    def recommend_app(self, app_name):
        print(f"✅ You might like: {app_name}")