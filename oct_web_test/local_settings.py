import os
from pathlib import Path
import dj_database_url

#settings.pyからそのままコピー
BASE_DIR = Path(__file__).resolve().parent.parent 

SECRET_KEY = '*swf$xt(zg2vfuqsz)d8j6s6&=*c$vogvl^p==vww8+x#9ug6m'

#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True #ローカルでDebugできるようになります