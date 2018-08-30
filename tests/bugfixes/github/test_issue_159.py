# -*- coding: utf-8 -*-

import system_tests


class TestPoCs(metaclass=system_tests.CaseMeta):
    """
    Regression test for the bugs described in:
    https://github.com/Exiv2/exiv2/issues/159
    """
    url = "https://github.com/Exiv2/exiv2/issues/159"

    files = [
        system_tests.path("$data_path/printStructure" + c) for c in ('', '2')
    ]
    commands = ["$exiv2 " + fname for fname in files]
    stdout = [
        """File name       : """ + files[0] + """
File size       : 12357 Bytes
MIME type       : image/tiff
Image size      : 0 x 0
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

""",
        """File name       : """ + files[1] + """
File size       : 12357 Bytes
MIME type       : image/tiff
Image size      : 0 x 0
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
    stderr = [""] * 2
    retval = [0] * 2

    compare_stderr = system_tests.check_no_ASAN_UBSAN_errors
