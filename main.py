from dotenv import load_dotenv
from mongoengine import connect
from config.config import Config 
from tweetformation.save_tweets import SaveTweet
from models.account_twitter import AccountTwitter
from util.load_accounts_twitter import load_db_accounts
from tweetformation.clean_tweets import CleanTweets
from tweetformation.classify_tweeets import ClassifyTweet
from tweetformation.show_result import ShowResult



def validate_account_twitter(account):
    account = AccountTwitter.objects(account=account).first()
    return account is None

def load_information():
    accounts = load_db_accounts()['accounts']

    for account in accounts:
        if validate_account_twitter(account["account"]):
            account_twitter =  AccountTwitter(
                name=account["name"], 
                account=account["account"]
                )
            account_twitter.save()




def app_run():
    

    
    load_dotenv()
    config = Config()
    data_connection = config.get_connectiondb()

    if(config.get_enviroment() == "prod"):
        connect(
                name=data_connection["name"],
                host=data_connection["host"],
                username=data_connection["username"],
                password=data_connection["password"],
                authentication_source="admin"
            )
    else:
            
        connect(data_connection["name"])

    load_information()

    save_tweet = SaveTweet()
    save_tweet.main()
    clean_tweets = CleanTweets()
    clean_tweets.main()
    classifytweet = ClassifyTweet()
    classifytweet.main()
    show_result = ShowResult()
    print(show_result.get_result_stores())


app_run()
