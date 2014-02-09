# -*- coding: utf-8 -*-

'''
Created on Dec 26, 2013
@author: Karolis Ramanauskas
@copyright: 2013 Karolis Ramanauskas. All rights reserved.
@license: GPLv3
'''

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

__all__ = []
__version__ = 0.1
__updated__ = '2013-12-28'

import os
import tempfile
import zipfile
import shutil

import krpy

# def parse_directory(path, file_name_sep, sort='forward'):
#
#     '''
#     Will parse a directory at a given path and return a list of dictionary
#     objects with keys:
#         name: name of a file without extension
#         ext: file extension
#         full: file name with extension
#         path: full file path, relative to the input path
#         split: file name split using file_name_sep input variable
#     '''
#
#     import os
#
#     ps = os.path.sep
#     path = path.rstrip(ps) + ps
#     file_list = os.listdir(path)
#     file_list.sort(reverse=False)
#     if sort == 'reverse':
#         file_list.sort(reverse=True)
#     return_list = list()
#
#     for f in file_list:
#         # Mac hack
#         if f == '.DS_Store':
#             continue
#         file_name = os.path.splitext(f)[0]
#         file_ext = None
#         if os.path.splitext(f)[1] != '':
#             file_ext = os.path.splitext(f)[1].split('.')[1]
#         isdir = os.path.isdir(path + f)
#         file_name_split = file_name.split(file_name_sep)
#
#         file_dict = dict()
#         file_dict['name'] = file_name
#         file_dict['ext'] = file_ext
#         file_dict['full'] = f
#         file_dict['path'] = path + f
#         file_dict['basepath'] = path
#         file_dict['split'] = file_name_split
#         file_dict['isdir'] = isdir
#         return_list.append(file_dict)
#
#     return return_list


# def prepare_directory(path):
#
#     '''
#     Checks if directory at path exists and, if not, creates full path.
#     '''
#
#     import os
#     path_sep = os.path.sep
#     if not os.path.exists(path):
#         os.makedirs(path)
#     path = path.rstrip(path_sep) + path_sep
#     return path
#
#
# def num_lines_in_file(file_path):
#     '''
#         Count the number of lines in a file.
#     '''
#     num_lines = 0
#     with open(file_path) as f:
#         for i, l in enumerate(f):
#             num_lines = i
#     return num_lines + 1


# The commented file reading class from:
# http://www.mfasold.net/blog/2010/02/
#   python-recipe-read-csvtsv-textfiles-and-ignore-comment-lines
class CommentedFile:
    '''
    Provide an open file handle with comments removed.
    '''
    def __init__(self, f, commentstring="#"):
        self.f = f
        self.commentstring = commentstring

    def next(self):
        line = self.f.next()
        while line.startswith(self.commentstring) or not line.strip():
            line = self.f.next()
        return line

    def __iter__(self):
        return self

    def close(self):
        self.f.close()


def read_table_file(handle=None, path=None, has_headers=False, headers=None,
                    delimiter=',', quotechar='"', stripchar='',
                    commentchar="#", rettype='dict'  # dict, list, set
                    ):

    '''
    Reads a delimited text file.
    Returns:
        A list of dictionaries, one dictionary per row. Header names as keys.
    '''

    if not handle:
        handle = CommentedFile(open(path, 'rb'), commentstring=commentchar)
    else:
        handle = CommentedFile(handle, commentstring=commentchar)
    if headers is not None:
        has_headers = False
    if has_headers:
        headers = handle.next()
        headers = krpy.other.parse_line(headers, delimiter, quotechar,
                                        stripchar)

    return_value = list()

    if rettype.startswith('dict'):
        for l in handle:

            l_spl = krpy.other.parse_line(l, delimiter, quotechar, stripchar)

            row_dict = dict()
            for i, h in enumerate(headers):
                row_dict[h] = l_spl[i]
            return_value.append(row_dict)

    if rettype.startswith('list') or rettype.startswith('set'):
        for l in handle:

            l_spl = krpy.other.parse_line(l, delimiter, quotechar, stripchar)

            if rettype.startswith('set') and len(l_spl) == 1:
                l_spl = l_spl[0]

            return_value.append(l_spl)

    if rettype.startswith('set'):
        return_value = set(return_value)

    handle.close()

    return return_value


def remove_file_from_zip(zipfname, *filenames):
    '''
    Removes file(s) frome a zip file.
    '''
    tempdir = tempfile.mkdtemp()
    try:
        tempname = os.path.join(tempdir, 'new.zip')
        with zipfile.ZipFile(zipfname, 'r') as zipread:
            with zipfile.ZipFile(tempname, 'w') as zipwrite:
                for item in zipread.infolist():
                    if item.filename not in filenames:
                        data = zipread.read(item.filename)
                        zipwrite.writestr(item, data)
        shutil.move(tempname, zipfname)
    finally:
        shutil.rmtree(tempdir)

if __name__ == '__main__':
    pass

#     # Tests
#
#     import os
#
#     ps = os.path.sep
#
#     # CommentedFile
#    handle = CommentedFile(open('testdata' + ps + 'commented_file.csv', 'rb'))
#     for i, line in enumerate(handle):
#         print(i, repr(line))
#     handle.close()
#
#     # read_table_file
#     table = read_table_file(path='testdata' + ps + 'commented_file.csv',
#                             has_headers=True, headers=None, delimiter=',')
#     for i, line in enumerate(table):
#         print(i, repr(line))