from models.tweet_clean import TweetClean
from models.account_twitter import AccountTwitter

class ShowResult:

    def __init__(self):
        pass

    def get_result_stores(self):
        result = []
        accounts = AccountTwitter.objects

        for account in accounts:
            account_result = {
                                "store":'',
                                "amount":0
                                }
            account_result["store"] = account.account
            account_result["amount"] = TweetClean.objects(
                                stores=account.account,
                                complaint=True

                                ).count()
            result.append(account_result)
        
        return result

