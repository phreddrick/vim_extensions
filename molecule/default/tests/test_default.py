import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/home/tester')

    assert f.exists
    assert f.user == 'tester'


@pytest.mark.parametrize("name", [
    (".vimrc"),
    (".vim/filetype.vim"),
])
def test_vim_files(host, name):
    print("Checking '"+name+"'")
    f = host.file('/home/tester/'+name)
    assert f.is_file
    assert f.user == 'tester'
