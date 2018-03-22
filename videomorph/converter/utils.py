# -*- coding: utf-8 -*-
#
# File name: utils.py
#
#   VideoMorph - A PyQt5 frontend to ffmpeg.
#   Copyright 2016-2017 VideoMorph Development Team

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""This module contains some utilities and functions."""

import os
from os.path import pathsep
from locale import getdefaultlocale


def get_locale():
    """Return the default locale string."""
    return ('es_ES' if getdefaultlocale()[0] == 'es_CU' else
            getdefaultlocale()[0])
    # return 'es_ES'


def which(app):
    """Detect if an app is installed in your system."""
    if app == '':
        raise ValueError('Invalid app name')

    path = os.environ.get('PATH', os.defpath)
    for directory in path.split(pathsep):
        app_path = os.path.join(directory, app)
        if os.path.exists(app_path) and os.access(app_path, os.X_OK):
            return app_path


def write_time(time_in_secs):
    """Return time in 00h:00m:00s format."""
    try:
        time = int(round(float(time_in_secs)))
    except (TypeError, ValueError):
        raise ValueError('Invalid time measure.')

    if time < 0:
        raise ValueError('Time must be positive.')

    def fix(string):
        """Fix a number so it always contains two characters."""
        string = str(string)
        if len(string) == 1:
            return '0' + string

        return string

    hours = int(time / 3600)
    minutes = int(time / 60) - hours * 60
    secs = time - minutes * 60 - hours * 3600

    if hours:  # @return the time in 00h:00m:00s format
        return ':'.join(['{0}h'.format(fix(hours)),
                         '{0}m'.format(fix(minutes)),
                         '{0}s'.format(fix(secs))])
    elif minutes:  # @return the time in 00m:00s format
        return ':'.join(['{0}m'.format(fix(minutes)),
                         '{0}s'.format(fix(secs))])

    # @return the time in 00s format
    return '{0}s'.format(fix(str(secs)))
