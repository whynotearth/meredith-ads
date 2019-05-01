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
access_token = 'EAAeN4kERtWcBAEDMkq53cocQtSDk1XCokU6tOYovTkRwkJc9MLryzH9hbDQZBGXnBFN9vcOajuy7R8n66st58VFSz4ETv4XS25ZArC92pX2iNVy3Ac5MxYHUWToJkaiArtX5PVpJXtvL8KwMdzABZC1SG0vGMzy5enezsVhQjiUljVjMSuomVIWnjiRXAdLORe7Mh0HogZDZD'

# Facebook ADS Api Initialization
FacebookAdsApi.init(app_id, app_secret, access_token)

# Ad Accounts Initialization ( with all the campaigns )
account = AdAccount('act_495346300520002')

fields = [
    'name',
    'status',
    'account_id',
    'campaign_id',
    'created_time'
]

params = {
    'date_presets': 'lifetime'
}

File.write(output_filename, arrayToTSVLine([
    "ad_name".upper(),
    "ad_id".upper(),
    "campaign_id".upper(),
    "account_id".upper(),
    "adset_id".upper(),
    "status".upper(),
    "clicks".upper(),
    "cpc".upper(),
    "cpm".upper(),
    "cpp".upper(),
    "ctr".upper(),
    "spend".upper(),
    "relevance_score".upper(),
    "date_start".upper(),
    "date_end".upper()
]))

for ad in account.get_ads(fields, params=params):

    # Ad Initialization
    current_ad = Ad(ad["id"])
    status = ad["status"]

    fields = [
        'spend',
        'relevance_score',
        'clicks',
        'ad_id',
        'adset_id',
        'account_id',
        'campaign_id',
        'cost_per_unique_click',
        'cpc',
        'cpp',
        'cpc',
        'cpm',
        'ctr',
        'date_start',
        'date_stop',
        'reach',
        'frequency',
        'impressions',
        'social_spend',
        'unique_ctr',
        'unique_clicks',
        'ad_name'
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

        # TEXT
        ad_name = data["ad_name"]

        # DATE
        date_start = data["date_start"]
        date_stop = data["date_stop"]

        # METRICS
        impressions = data["impressions"]
        reach = data["reach"]
        clicks = data["clicks"]
        unique_clicks = data["unique_clicks"]

        relevance_score = data["relevance_score"]["score"]

        # COST
        spend = data["spend"]
        social_spend = data["social_spend"]

        cpc = data["cpc"]
        cpm = data["cpm"]
        cpp = data["cpp"]
        ctr = data["ctr"]

        cost_per_unique_click = data["cost_per_unique_click"]

        File.append(output_filename, arrayToTSVLine([
            ad_name,
            ad_id,
            campaign_id,
            account_id,
            adset_id,
            status,
            clicks,
            cpc,
            cpm,
            cpp,
            ctr,
            spend,
            relevance_score,
            date_start,
            date_stop
        ]))

        print(ad_insights)
