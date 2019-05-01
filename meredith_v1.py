from facebook_business.api import FacebookAdsApi
from facebook_business import adobjects
from facebook_business.adobjects.adaccountuser import AdAccountUser
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.adobjects.adreportrun import AdReportRun

import requests

def FBK_init():
    app_id = '2126327730779495'
    app_secret = '821717cc16a74b138af2c9070d8c2ff7'
    access_token = 'EAAeN4kERtWcBAEDMkq53cocQtSDk1XCokU6tOYovTkRwkJc9MLryzH9hbDQZBGXnBFN9vcOajuy7R8n66st58VFSz4ETv4XS25ZArC92pX2iNVy3Ac5MxYHUWToJkaiArtX5PVpJXtvL8KwMdzABZC1SG0vGMzy5enezsVhQjiUljVjMSuomVIWnjiRXAdLORe7Mh0HogZDZD'

    FacebookAdsApi.init(app_id, app_secret, access_token)

    print("Facebook ADS API initialized !")

def FBK_ad_account():

    # GET ALL AD ACCOUNTS

    # me = AdAccountUser(fbid='me')
    # adAccounts = me.get_ad_accounts()

    return AdAccount('act_495346300520002')

def FBK_get_ads(account):
    fields = [
        'status',
        'created_time',
        'name',
        'conversion_specs',
        'bid_amount',
        'bid_type',
        'bid_info',
        'account_id',
        'tracking_specs',
        'campaign',
        'campaign_id',
    ]

    return account.get_ads(fields=fields)

def FBK_get_ads_insights(account):
    fields = [
        'spend',
        'cpc',
        'cpm',
        'cpp',
        'reach'
    ]

    return account.get_insights(fields=fields)


def arrayToTSVLine(array):
    line = ""
    for elem in array:
        line += "\"" + elem.encode('utf-8') + "\"" + "\t"
    return line[:-1] + '\n'



FBK_init()

account = FBK_ad_account()
# print(account)
#

print(arrayToTSVLine(["campaign_id", "adset_id", "ad_id", "impressions", "cpm", "reach", "frequency", "clicks", "unique_clicks", "ctr", "cpc", "unique_ctr", "cost_per_unique_click"]))
for ad in FBK_get_ads(account):
    # print("============")
    # print(ad["id"])
    # print("===")
    targeted_ad = Ad(ad["id"])

    fields = [
        'campaign_id',
        'adset_id',
        'adset_name',
        'ad_id',
        'ad_name',
        'impressions',
        'cpm',
        'reach',
        'frequency',
        'clicks',
        'unique_clicks',
        'ctr',
        'cpc',
        'unique_ctr',
        'cost_per_unique_click'
    ]

    params = {
        'date_preset': 'lifetime',
    }

    result = targeted_ad.get_insights(fields=fields, params=params)

    # print(result)


    if result:
        e = result[0]

        print(e["ad_name"])

    # print(arrayToTSVLine([e["campaign_id"], e["adset_id"], e["ad_id"], e["impressions"], e["cpm"], e["reach"], e["frequency"], e["clicks"], e["unique_clicks"], e["ctr"], e["cpc"], e["unique_ctr"], e["cost_per_unique_click"]]))

    # print(result)
    # print("===")
    # print("============")



# campaign = Ad('6108940864443')

# insights = campaign.get_insights(params=params)
# print insights

# print(FBK_get_insights(account))


# fields = [
#     'account_currency',
#     'account_id',
#     'account_name',
#     'ad_name',
#     'spend',
#     'unique_clicks',
#     'adset_name'
#     'cpc',
#     'cpm'
# ]



    # 'cpc',
    # 'cpm',
    # 'ad_id'

#
# ads = account.get_ads(fields=fields)



# for ad in ads:
#     print("==========")
#     print(ad)
#     print("==========")

#
# fields = [
#     'campaign_name',
#     'campaign_id',
#     'impressions',
#     'clicks',
#     'spend',
#     'reach',
#     'actions',
#     'action_values'
# ]

#
# ad_insights = account.get_insights(fields=fields)
# print(ad_insights)


#
# campaigns = account.get_campaigns()
# print(campaigns)

# from facebookads.objects import AdAccount, Ad
#
# fields = [
#     'adset_id',
#     'cost'
# ]
#
# ad_iter = account.get_ads(fields=fields)
# for ad in ad_iter:
#     # print ad['adset_id']
#     print(ad)



# insights = account.get_insights(params={})
# print(insights)



# campaigns = account.get_insights()
#
# print("ADS = ")
#
# for campaign in campaigns:
#     print(campaign)



#
# print(account)
#
# fields = {
#         AdsInsights.Field.campaign_id,
#         AdsInsights.Field.campaign_name,
#         AdsInsights.Field.adset_name,
#         AdsInsights.Field.ad_name,
#         AdsInsights.Field.spend,
#         AdsInsights.Field.impressions,
#         AdsInsights.Field.clicks,
#         AdsInsights.Field.buying_type,
#         AdsInsights.Field.objective,
#         AdsInsights.Field.actions
# }
#
# params = {
# }
#
#
# insights = account.get_insights(fields=fields, params=params)
# for insight in insights:
#     print(insight)
