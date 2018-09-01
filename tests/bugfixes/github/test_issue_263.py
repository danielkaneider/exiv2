# -*- coding: utf-8 -*-

import system_tests


class OutOfBoundsReadInPrintIFD(metaclass=system_tests.CaseMeta):

    url = "https://github.com/Exiv2/exiv2/issues/263"

    encodings = [bytes]

    files = [
        system_tests.path("$data_path/" + fname) for fname in
        (
            "10-printStructure-outbound-read-2",
            "9-printStructure-outbound-read-1"
        )
    ]
    commands = ["$exiv2 -pv " + f for f in files]
    stdout = [
        bytes(
            """0x0100 Image        ImageWidth                  Short       0
0x0100 Image        ImageWidth                  Short       1  0
0x0102 Image        BitsPerSample               Short       1  1
0x0103 Image        Compression                 Short       1  3
0x0106 Image        PhotometricInterpretation   Short       1  0
0x83bb Image        IPTCNAA                     Ascii     244  I*
0x0103 Image        Compression                 Short       1  3
0x0106 Image        PhotometricInterpretation   Short       1  246
0x014a Image        SubIFDs                     Short      19  8 0 19 256 3 97 0 1728 1024 256 3 1 0 0 0 258 3 1 0
0x0101 Image        ImageLength                 0x0301      0
""",
            encoding='utf-8'
        ),
        bytes("""0x0100 Image        ImageWidth                  Short       0
0x0100 Image        ImageWidth                  Short       0
0x0102 Image        BitsPerSample               Short       1  1
0x0103 Image        Compression                 Short       1  3
0x0106 Image        PhotometricInterpretation   Short       1  0
0x0100 Image        ImageWidth                  Short       1  2
0x83bb Image        IPTCNAA                     Ascii       2  """,
              encoding='utf-8'
        ) + bytes([1]) + bytes("""
0x0103 Image        Compression                 Short       1  3
0x0106 Image        PhotometricInterpretation   Short       1  246
0x014a Image        SubIFDs                     Short      19  42 8 0 19 256 3 97 0 1728 1024 256 3 65 0 0 0 258 3 1
0x0101 Image        ImageLength                 0x4003      0
0x0106 Image        PhotometricInterpretation   Short       0
0x0101 Image        ImageLength                 0xfc03      0
""", encoding='utf-8')
    ]

    compare_stderr = system_tests.check_no_ASAN_UBSAN_errors
