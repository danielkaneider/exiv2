# -*- coding: utf-8 -*-

import system_tests


class InfiniteLoopInPrintIFD(metaclass=system_tests.CaseMeta):

    url = "https://github.com/Exiv2/exiv2/issues/156"

    filename = system_tests.path(
        "$data_path/exiv2_0-26_exiv2_infinite_loop_printIFDStructure.jpg"
    )
    commands = ["$exiv2 -pt $filename"]
    stdout = [""]
    stderr = [
        """Error: Directory Image: Next pointer is out of bounds; ignored.
"""
    ]
    retval = [0]
