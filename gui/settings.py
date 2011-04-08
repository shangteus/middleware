#+
# Copyright 2010 iXsystems
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
#####################################################################

# Django settings for FreeNAS project.

import os
    
HERE = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

TEMPLATE_DEBUG = DEBUG
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/account/login/'
LOGOUT_URL = '/account/logout/'

ADMINS = (
     ('iXsystems, Inc.', 'freenas@ixsystems.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'          # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = '/data/freenas-v1.db' # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(HERE, 'media')
MEDIA_URL = '/media/'

#This is required for django development server work (BUG fixed in django 1.3)
ADMIN_MEDIA_PREFIX = '/admin-media'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'freenasUI.freeadmin.middleware.RequireLoginMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'dojango.middleware.DojoCollector',
)

DOJANGO_DATAGRID_ACCESS = (
    'account',
    'system',
    'network',
    'storage',
    'sharing',
    'services',
)

#DOJANGO_DOJO_PROFILE = 'local'
#DOJANGO_DOJO_VERSION = '1.6.0b1'
#DOJANGO_DOJO_BUILD_VERSION = '1.6.0b1'
DOJANGO_DOJO_DEBUG = False

ROOT_URLCONF = 'freenasUI.urls'

TEMPLATE_DIRS = (
    os.path.join(HERE, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
        'django.core.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'dojango.context_processors.config',
        )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'freeadmin',
    'south',
    'dojango',
    'account',
    'system',
    'network',
    'storage',
    'sharing',
    'services',
)

BLACKLIST_NAV = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django_nav',
    'south',
    'dojango',
    'freeadmin',
)

FORCE_SCRIPT_NAME = ''

FILE_UPLOAD_MAX_MEMORY_SIZE = 268435456
FILE_UPLOAD_TEMP_DIR = "/var/tmp/firmware/"

try:
    from local_settings import *
except:
    pass
