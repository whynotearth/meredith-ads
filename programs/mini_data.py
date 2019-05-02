from facebook_business.api import FacebookAdsApi

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.ad import Ad

class File:
    def write(self, filename, content):
        file = open(filename, "w")
        file.write(content + "\n")
        file.close()

    def append(self, filename, content):
        file = open(filename, "a")
        file.write(content.encode("utf-8") + "\n")
        file.close()

File = File()

def arrayToTSVLine(array):
    line = ""
    for elem in array:
        line += "\"" + elem + "\"" + "\t"
    return line[:-1]

output_filename = raw_input("Enter the name of your output (example: meredith.tsv)\n$: ")

# Meredith Marketing App ID
app_id = '2126327730779495'

# Meredith Marketing App Secret Key
app_secret = '821717cc16a74b138af2c9070d8c2ff7'

# Meredith Marketing App Access Token

# WARNING : Don't forget to remove this line before push
access_token = ''

# Facebook ADS Api Initialization
FacebookAdsApi.init(app_id, app_secret, access_token)

# Ad Accounts Initialization ( with all the campaigns )
account = AdAccount('act_495346300520002')

File.write(output_filename, arrayToTSVLine([
    "ad_id".upper(),
    "campaign_id".upper(),
    "account_id".upper(),
    "adset_id".upper(),
    "clicks".upper(),
    "spend".upper(),
    "reach".upper(),
    "impressions".upper()
]))

for ad in account.get_ads(fields, params=params):

    # Ad Initialization
    current_ad = Ad(ad["id"])

    fields = [
        'spend',
        'clicks',
        'ad_id',
        'adset_id',
        'account_id',
        'campaign_id',
        'reach',
        'impressions',
        'social_spend'
    ]

    params = {
        'date_presets': 'lifetime'
    }

    # Get all insights above from current AD
    ad_insights = current_ad.get_insights(fields, params)

    if ad_insights:
        data = ad_insights[0]

        # IDS
        ad_id = data["ad_id"]
        adset_id = data["adset_id"]
        account_id = data["account_id"]
        campaign_id = data["campaign_id"]

        # METRICS
        impressions = data["impressions"]
        reach = data["reach"]
        clicks = data["clicks"]
        spend = data["spend"]

        File.append(output_filename, arrayToTSVLine([
            ad_id,
            campaign_id,
            account_id,
            adset_id,
            clicks,
            spend,
            reach,
            impressions
        ]))

        print(ad_insights)
