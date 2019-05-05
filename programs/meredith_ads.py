from facebook_business.api import FacebookAdsApi

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.ad import Ad

import json

class File:
    def write(self, filename, content):
        file = open(filename, "w")
        file.write(content + "\n")
        file.close()

    def append(self, filename, content):
        file = open(filename, "a")
        file.write(content.encode("utf-8") + "\n")
        file.close()

    def toArray(self, filename):
        array = []
        for line in self.readLines(filename):
            formattedLine = line.rstrip()
            if formattedLine != '':
                array.append(formattedLine)
        return array

File = File()

def arrayToTSVLine(array):
    line = ""
    for elem in array:
        line += "\"" + elem + "\"" + "\t"
    return line[:-1]


secret_filename = raw_input('''
Enter the path of your secret key file.
Example : /Users/Desktop/your_secret_file

The format must be the following:
app_id = <YOUR APP_ID HERE> (example : app_id = 11111111111)
app_secret = <YOUR APP_SECRET HERE> (example : app_secret = 22222222222 )
access_token = <YOUR ACCESS_TOKEN HERE> (example : access_token = abcef123456)
ad_account = <YOUR_AD_ACCOUNT_HERE> (example : ad_account = act_123456789)

$: ''')

output_filename = raw_input("Enter the name of your output (example: meredith.tsv)\n$: ")

# Meredith Marketing App ID
app_id = ''

# Meredith Marketing App Secret Key
app_secret = ''

# Meredith Marketing App Access Token

# WARNING : Don't forget to remove this line before push
access_token = ''

json_file = '[]'

# Facebook ADS Api Initialization
FacebookAdsApi.init(app_id, app_secret, access_token)

# Ad Accounts Initialization ( with all the campaigns )
account = AdAccount('')

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

# TODO: Clean up this part and create methods / class with verification

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

        # relevance_score = data["relevance_score"]["score"]

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
            date_start,
            date_stop
        ]))

        json_line = {}

        json_line["AD_NAME"] = ad_name
        json_line["AD_ID"] = ad_id
        json_line["CAMPAIGN_ID"] = campaign_id
        json_line["ACCOUNT_ID"] = account_id
        json_line["ADSET_ID"] = adset_id
        json_line["STATUS"] = status
        json_line["CLICKS"] = clicks
        json_line["CPC"] = cpc
        json_line["CPM"] = cpm
        json_line["CPP"] = cpp
        json_line["CTR"] = ctr
        json_line["SPEND"] = spend
        json_line["DATE_START"] = date_start
        json_line["DATE_STOP"] = date_stop

        # TODO: Clean up this part and make it better

        json_data = json.dumps(json_line)

        json_file = json_file[:-1] + json_data + ","

        File.write("ads_export.json", json_file[:-1].replace("}{", "},{") + "]")

        print(ad_insights)
