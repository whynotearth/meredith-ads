from facebook_business.api import FacebookAdsApi

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.ad import Ad

import json
import sys

from lib import File

File = File()

def arrayToTSVLine(array):
    line = ""
    for elem in array:
        line += "\"" + elem + "\"" + "\t"
    return line[:-1]

FORMAT_TEXT = '''

The format must be the following:
{
    "app_id" : "<YOUR APP_ID HERE>",
    "app_secret" : "<YOUR APP_SECRET HERE>",
    "access_token" : "<YOUR ACCESS_TOKEN HERE>",
    "ad_account" : "<YOUR_AD_ACCOUNT_HERE>"
}
'''


secret_filename = raw_input('''
Enter the path of your secret json key file.
Example : /Users/Desktop/credentials.json
''' + FORMAT_TEXT + '''
$: ''')

json_file = File.read(secret_filename)
json_data = json.loads(json_file)

app_id = json_data["app_id"]
app_secret = json_data["app_secret"]
access_token = json_data["access_token"]
ad_account = json_data["ad_account"]

if app_id == '' or app_secret == '' or access_token == '' or ad_account == '':
    print(FORMAT_TEXT)
    sys.exit(1)

output_filename = raw_input("Enter the name of your output (example: meredith.tsv)\n$: ")

if output_filename == '':
    print("Invalid file name")
    sys.exit(1)

json_file = '[]'

# Facebook ADS Api Initialization
FacebookAdsApi.init(app_id, app_secret, access_token)

# Ad Accounts Initialization ( with all the campaigns )
account = AdAccount(ad_account)

fields = [
    'name',
    'account_id',
]

params = {
    'date_presets': 'lifetime'
}

# TODO: Clean up this part and create methods / class with verification

File.write("../data/" + output_filename, arrayToTSVLine([
    "Cost Per Click",
    "Spend",
    "Ad (friendly name)",
    "Ad ID",
    "Source",
    "Clicks",
]))

for ad in account.get_ads(fields, params=params):

    # Ad Initialization
    current_ad = Ad(ad["id"])

    fields = [
        'spend',
        'clicks',
        'ad_id',
        'cpc',
        'ad_name',
    ]

    params = {
        'date_presets': 'lifetime'
    }

    # Get all insights above from current AD
    ad_insights = current_ad.get_insights(fields, params)

    if ad_insights:
        data = ad_insights[0]

        ad_id = data["ad_id"]
        ad_name = data["ad_name"]

        cpc = data["cpc"]
        clicks = data["clicks"]

        spend = data["spend"]

        File.append("../data/" + output_filename, arrayToTSVLine([
            cpc,
            spend,
            ad_name,
            ad_id,
            "facebook",
            clicks
        ]))

        json_line = {}

        json_line["AD_NAME"] = ad_name
        json_line["AD_ID"] = ad_id

        json_line["CLICKS"] = clicks
        json_line["CPC"] = cpc

        json_line["SPEND"] = spend
        json_line["SOURCE"] = "facebook"

        # TODO: Clean up this part and make it better

        json_data = json.dumps(json_line)

        json_file = json_file[:-1] + json_data + ","

        File.write("../data/" + "ads_export.json", json_file[:-1].replace("}{", "},{") + "]")

        print(ad_insights)
