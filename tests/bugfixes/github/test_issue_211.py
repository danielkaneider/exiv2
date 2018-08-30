# -*- coding: utf-8 -*-

import system_tests


class TestFuzzedPoC(metaclass=system_tests.CaseMeta):

    url = "https://github.com/Exiv2/exiv2/issues/211"

    filename = system_tests.path("$data_path/2018-01-09-exiv2-crash-003.tiff")
    commands = ["$exiv2 $filename"]
    stdout = [
        """File name       : $filename
File size       : 892 Bytes
MIME type       : image/tiff
Image size      : 1728 x 0
Camera make     : 
Camera model    : 
Image timestamp : 
Image number    : 
Exposure time   : 
Aperture        : 
Exposure bias   : 
Flash           : 
Flash bias      : 
Focal length    : 
Subject distance: 
ISO speed       : 
Exposure mode   : 
Metering mode   : 
Macro mode      : 
Image quality   : 
Exif Resolution : 
White balance   : 
Thumbnail       : None
Copyright       : 
Exif comment    : 

"""
    ]

    compare_stderr = system_tests.check_no_ASAN_UBSAN_errors
