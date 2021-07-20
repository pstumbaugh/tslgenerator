# Length
    Length:
        0.      [error]
        less15.   [single]
        15.     [property 15Start]
        16.     [property 16Start]
        more16.   [single]

#CheckDigit
    CheckDigit:
        valid.      [property valid]
        notValid.   [property invalid]

# Prefix
    Prefix:
        4.      [if !15Start]
        4.      [if 16Start && valid]
        51.     [if 16Start]
        52.     [if 16Start]
        53.     [if 16Start]
        54.     [if 16Start]
        55.     [if 16Start]
        2221.   [if 16Start]
        23.     [if 16Start]
        24.     [if 16Start]
        25.     [if 16Start]
        26.     [if 16Start]
        2720.   [if 16Start]
        2720.   [if 15Start && valid]
        34.     [if 15Start]
        37.     [if 15Start]
        37.     [if 16Start && valid]
        other.

