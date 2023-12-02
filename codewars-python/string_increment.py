import re


def increment_string(strng):
    nm = re.search(r"\d+$", strng)
    if nm is None:
        return strng + "1"

    nv_v = nm.group(0)
    st = re.sub(r"\d+$", "", strng)
    lv_0 = len(nv_v)
    nv_v = str(int(nv_v) + 1)
    lv_1 = len(nv_v)

    nv_v = "".join(["0" for _ in range(lv_0 - lv_1)]) + nv_v

    return st + nv_v


if __name__ == "__main__":

    assert increment_string("foo") == "foo1"
    assert increment_string("foo099") == "foo100"
    assert increment_string("foo99") == "foo100"
    assert increment_string("foo001") == "foo002"
    assert increment_string("fo99obar99") == "fo99obar100"
    assert increment_string("0%=t$%1L83ylGA07037736%u0<S:J65244875749") == "0%=t$%1L83ylGA07037736%u0<S:J65244875750"

    # : '0%=t$%1L83ylGA07037736%u65244875750' should equal '0%=t$%1L83ylGA07037736%u0<S:J65244875750'
