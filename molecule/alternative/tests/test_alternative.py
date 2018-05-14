import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_directories(host):
    present = [
        "/etc/docker",
    ]
    absent = []
    if present:
        for directory in present:
            d = host.file(directory)
            assert d.is_directory
            assert d.exists
    if absent:
        for directory in absent:
            d = host.file(directory)
            assert not d.exists


def test_files(host):
    present = [
        "/etc/docker/daemon.json",
    ]
    if present:
        for file in present:
            f = host.file(file)
            assert f.exists
            assert f.is_file


# def test_socket(host):
#     assert host.socket("unix:///var/run/docker.sock").is_listening


def test_service(host):
    present = [
        "docker"
    ]
    if present:
        for service in present:
            s = host.service(service)
            assert s.is_running
            assert s.is_enabled


def test_packages(host):
    assert host.package('docker-ce').is_installed
    # host.package doesn't support checking if package doesn't exist
    # assert not host.package('python-pip').is_installed
    assert not host.file('/usr/bin/pip').exists


def test_user(host):
    assert 'docker' in host.user("test").groups
