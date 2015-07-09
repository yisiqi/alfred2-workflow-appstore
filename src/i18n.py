# -*- coding: utf-8 -*-

import os

_dics = {
  
  'en_US': {
    'FREE'      : u'Free',
    'VERSION'   : u'\tVer',
    'RATINGS'   : u'Ratings',
    'RAT_COUNT' : u'from',
    'RAT_TAIL'  : u'users',
    'BY'        : u'By',
    'COUNTRY'   : u'us',
    'USD'       : u'$',
    'UNIVERSAL' : u'Universal',
    'FOR_IPHONE': u'for iPhone',
    'FOR_IPAD'  : u'for iPad',
    'NULL_TITLE': u'Noting found',
    'NULL_SUBTITLE': u'Try to search with Google',
  },

  'zh_CN': {
    'FREE'      : u'免费',
    'VERSION'   : u'版本',
    'RATINGS'   : u'评分',
    'RAT_COUNT' : u'共计',
    'RAT_TAIL'  : u'人打分',
    'BY'        : u'开发者',
    'COUNTRY'   : u'cn',
    'CNY'       : u'￥',
    'UNIVERSAL' : u'通用型应用\t',
    'FOR_IPHONE': u'iPhone应用\t',
    'FOR_IPAD'  : u'iPad应用\t',
    'NULL_TITLE': u'未找到任何符合条件的应用',
    'NULL_SUBTITLE': u'不如去Google上搜搜看',
  }

}

local = os.popen('defaults read -g AppleLocale').read().rstrip()

try:
  dic = _dics[local]
except KeyError as e:
  dic = _dics['en_US']


  