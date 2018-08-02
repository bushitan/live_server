# -*- coding: utf-8 -*-


from django.conf.urls import url
from views import *



urlpatterns = [

    url(r'^get/theme_list/$', GetThemeList.as_view()),
    url(r'^get/theme/$', GetTheme.as_view()),
    url(r'^get/token/$', GetToken.as_view()),
    url(r'^add/voice/$', AddVoice.as_view()),
    url(r'^delete/voice/$', DeleteVoice.as_view()),


    url(r'^bonus/check/$', BonusCheck.as_view()),
    url(r'^bonus/share/$', BonusShare.as_view()),
    url(r'^bonus/sign_in/$', BonusSignIn.as_view()),

    url(r'^bonus/exchange/$', BonusExchangeGift.as_view()),
    url(r'^bonus/get/record/$', BonusGetRecord.as_view()),
    url(r'^bonus/get/score/$', BonusGetScore.as_view()),

    # url(r'^register/$', WXRegister.as_view()),
    # url(r'^company/get/info/$', CompanyGetInfo.as_view()),
    # url(r'^user/set/info/$', UserSetInfo.as_view()),
    # url(r'^user/get/ppt/$', UserGetPPT.as_view()),


    # url(r'^tag/delete/$', TagAdd.as_view()),
    # url(r'^tag/get_list/$', TagAdd.as_view()),
    # url(r'^tag/update/$', TagAdd.as_view()),
]