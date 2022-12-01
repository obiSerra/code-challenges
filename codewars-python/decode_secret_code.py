

"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
"bdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqHabdhpF,82QsLir"

"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
"dhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqHabdhp"


"abcdefghijklmnopqrstuvwxyz"
"bdfhjlnprtvxzBDFHJLNPRTVXZ"

"" "bdfhjlnprtvxzBDFHJLNPRTVXZ"
"_" "dhlptxBFJNRVZ37,aeimquyCGK"
"__" "hpxFNV3,emuCKS08bjrzHPX5 g"


def encode(s):

    res = ""
    for i, l in enumerate(s):
        st = ord(l) + i + 1
        v = chr(st % 123) if st < 123 else chr((st % 123) + 65)
        res += v
        

    return res


def decode(s):

    return s


if __name__ == "__main__":
    print(encode("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    # decode("atC5kcOuKAr")
    # for l in "bdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqHabdhpF,82QsLir":
    #     print(l, ord(l))
