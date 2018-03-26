from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


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
    if host.system_info.distribution == 'ol':
        DOCKER = 'docker-engine'
    else:
        DOCKER = 'docker-ce'

    assert host.package(DOCKER).is_installed
