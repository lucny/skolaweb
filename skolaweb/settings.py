import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for skolaweb project.

Generated by 'django-admin startproject' using Django 1.8.14.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6z22d_=6+^0b98^iq*d#rah@k=q9yc&zh7o8-&1m%c#sf-!@#w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition


ROOT_URLCONF = 'skolaweb.urls'



WSGI_APPLICATION = 'skolaweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases




# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'cs'

TIME_ZONE = 'Europe/Prague'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_FORMAT = 'j. E Y'
SHORT_DATE_FORMAT = 'j. n. Y'

ALDRYN_BOILERPLATE_NAME = 'bootstrap3'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'skolaweb', 'static'),
)

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'aldryn_boilerplates.staticfile_finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'skolaweb', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.i18n',
        'django.core.context_processors.debug',
        'django.core.context_processors.request',
        'django.core.context_processors.media',
        'django.core.context_processors.csrf',
        'django.core.context_processors.tz',
        'sekizai.context_processors.sekizai',
        'django.core.context_processors.static',
        'cms.context_processors.cms_settings',
        'aldryn_boilerplates.context_processors.boilerplate',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.eggs.Loader',
        'aldryn_boilerplates.template_loaders.AppDirectoriesLoader',
            ],
        },
    },
]


MIDDLEWARE_CLASSES = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
]

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'djangocms_column',
    'djangocms_file',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'reversion',
    'appconf',
    'django_tablib',
    'bootstrap3',
    'future',
    'tablib',

    # aldryn blog
    'aldryn_apphooks_config',
    'aldryn_boilerplates',
    'aldryn_categories',
    'aldryn_common',
    'aldryn_newsblog',
    'aldryn_people',
    'aldryn_reversion',
    #'aldryn_events',
    'aldryn_translation_tools',
    'parler',
    'sortedm2m',
    'taggit',
    #'haystack',
    #'aldryn_search',
    #'spurl',

    'aldryn_style',
    'easy_thumbnails',
    'extended_choices',
    'mptt',
    'filer',
    'aldryn_bootstrap3',
    'standard_form',

    'sorl.thumbnail',
    'djangocms_unitegallery',
    #'image_gallery',
    'skolaweb'
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


LANGUAGES = (
    ## Customize this
     ('cs', gettext('cs')),
     ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'code': 'cs',
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'cs',
            'hide_untranslated': False,
            'name': gettext('cs'),
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('home.html', 'Home'),
    ('obory.html', 'Obory'),
    ('info.html', 'Info'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
    'newsblog_article_content': {
        #'plugins': ['TextPlugin', 'PicturePlugin', 'Bootstrap3IconCMSPlugin', 'Bootstrap3LabelCMSPlugin', 'Bootstrap3ImageCMSPlugin', 'Bootstrap3ButtonCMSPlugin',
        #            'Bootstrap3FileCMSPlugin'],
        'text_only_plugins': ['LinkPlugin'],
        'extra_context': {"width": 640},
        'name': gettext("Content"),
        'language_fallback': True,
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body': '<p>Zde bude text</p>',
                },
            },
        ],
        'child_classes': {
            'TextPlugin': ['PicturePlugin', 'LinkPlugin', 'Bootstrap3IconCMSPlugin', 'Bootstrap3LabelCMSPlugin'],
        },
        'parent_classes': {
            'LinkPlugin': ['TextPlugin'],
        },
    },
}


#DATABASES = {
#    'default': {
#        'CONN_MAX_AGE': 0,
#        'ENGINE': 'django.db.backends.sqlite3',
#        'HOST': 'localhost',
#        'NAME': 'project.db',
#        'PASSWORD': '',
#        'PORT': '',
#        'USER': ''
#    }
#}

DATABASES = {
    'default':
        {
            'ENGINE': 'django.db.backends.mysql', #.sqlite3
            'NAME': 'skola',
            'HOST': 'localhost',
            'USER': 'root',
            'PASSWORD': 'admin',
            'PORT': ''
        }
}

MIGRATION_MODULES = {
    
}

# Thumnail processors for the filer from Aldryn
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

CKEDITOR_SETTINGS = {
    # 'language': '{{ language }}',
    #  'toolbar': 'CMS',
    #  'skin': 'moono',
    #  'toolbar_CMS': [
        #  ['Undo', 'Redo'],
        #  ['cmsplugins', '-', 'ShowBlocks'],
        #  ['Format', 'Styles'],
        #  ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        #  ['Maximize', ''],
        #  '/',
        #  ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        #  ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        #  ['Link', 'Unlink', 'Anchor'],
        #  ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
        #  ['Source']
    #  ],
    #  See: https://github.com/yakupadakli/django_blog/blob/master/ckeditor/ckeditor/styles.js
    #  for default style definitions.

    'basicEntities': False,
    'entities': False,
    'stylesSet': [
        {
            'name': 'Page Header H1',
            'element': 'h1',
            'attributes': {
                'class': 'page-header',
            }
        },
        {
            'name': 'Page Header H2',
            'element': 'h2',
            'attributes': {
                'class': 'page-header',
            }
        },
        {
            'name': 'Page Header H3',
            'element': 'h3',
            'attributes': {
                'class': 'page-header',
            }
        },
        {
            'name': 'Code',
            'element': 'code',
        },
        {
            'name': 'Code Block',
            'element': 'pre',
            'attributes': {
                'class': 'code',
            }
        },
    ]}

TEXT_HTML_SANITIZE = False
CMS_PLACEHOLDER_CACHE = False
CMS_PAGE_CACHE = False
CMS_PLUGIN_CACHE = False

ALDRYN_BOOTSTRAP3_CAROUSEL_STYLES = "full"

ALDRYN_NEWSBLOG_UPDATE_SEARCH_DATA_ON_SAVE = True

ALDRYN_NEWSBLOG_SEARCH = True

#HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
#        'URL': 'http://127.0.0.1:8000/solr/cs/'
#    },
#    'en': {
#        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
#        'URL': 'http://127.0.0.1:8000/solr/en/'
#    },
#    'cs': {
#        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
#        'URL': 'http://127.0.0.1:8000/solr/cs/'
#    },
#}
