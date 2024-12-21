from subprocess import check_output
from pathlib import Path
import pytest

@pytest.fixture(scope="session")
def name(pytestconfig):
    return pytestconfig.getoption("name")


def test_ca_source(name):

    if name in "alma, arch":
        file_loc = "/etc/pki/ca-trust/source/anchors/brave-vesperia-ca.crt"
    else:
        file_loc = "/usr/local/share/ca-certificates/brave-vesperia-ca.crt"

    my_file = Path(file_loc)
    assert(my_file.is_file())


def test_ca_certificate_store():

    output = None

    try:
        output = check_output(["trust", "list"])
    except Exception as e:
        print(e)
    assert (str(output).find("ROOT-CA.FAUCH"))

