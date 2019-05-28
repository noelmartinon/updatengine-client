###############################################################################
# UpdatEngine - Software Packages Deployment and Administration tool          #
#                                                                             #
# Copyright (C) Yves Guimard - yves.guimard@gmail.com                         #
#                                                                             #
# This program is free software; you can redistribute it and/or               #
# modify it under the terms of the GNU General Public License                 #
# as published by the Free Software Foundation; either version 2              #
# of the License, or (at your option) any later version.                      #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU General Public License for more details.                                #
#                                                                             #
# You should have received a copy of the GNU General Public License           #
# along with this program; if not, write to the Free Software                 #
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,                  #
# MA  02110-1301, USA.                                                        #
###############################################################################

'''
UpdatEngine client Errors
'''


class UeImportError(Exception):
    '''Response didn't return Import ok'''
    def __init__(self, response):
        self.value = response

    def __str__(self):
        return self.value


class UeResponseError(Exception):
    '''Response isn't valid, XML return don't contain Import section'''
    def __init__(self, response):
        self.value = response

    def __str__(self):
        return self.value


class UeReadResponse(Exception):
    '''Can't read XML Response (XML return isn't valid)'''
    def __init__(self, response):
        self.value = response

    def __str__(self):
        return self.value
