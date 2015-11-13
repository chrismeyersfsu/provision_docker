[![Build Status](https://travis-ci.org/chrismeyersfsu/provision_docker.svg?branch=master)](https://travis-ci.org/chrismeyersfsu/provision_docker)


# provision_docker 
An Ansible role used to create and start docker containers for each inventory host used in a play. Useful for testing.

Recomended docker images.
```
chrismeyers/centos6
chrismeyers/centos7
chrismeyers/ubuntu12.04
ubuntu-upstart:14.04
```
**Note:** The above listed images [Dockerfiles](https://github.com/chrismeyersfsu/provision_docker/blob/master/files/) are designed to run an init systems and openssh.

## Example Playbook

* [main.yml](https://github.com/chrismeyersfsu/provision_docker/blob/master/test/main.yml)
* [role-install_mongod](https://github.com/chrismeyersfsu/role-install_mongod)
* [role-ansible_deps](https://github.com/chrismeyersfsu/role-ansible_deps)
* [role-iptables](https://github.com/chrismeyersfsu/role-iptables)


## Role Variables
[main.yml](https://github.com/chrismeyersfsu/provision_docker/blob/master/defaults/main.yml)

* Plays well with osx docker-machine. 
* http://bobmaerten.github.io/blog/2015/passage-de-boot2docker-a-docker-machine/
```
-e "provision_docker_use_tls=encrypt"
```

## Recommended Role + Testing Directory Structure
**Note:** This is not the structure of this project. It's an example of how to structure your role (i.e. `ansible-galaxy init . --force`) w/ tests added.
```
├── .travis.yml          # <-- example role testing in travis-ci
├── README.md
├── defaults
│   └── main.yml
├── files
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── tasks
│   └── main.yml
├── templates
├── test
│   ├── inventory         # <-- default test inventory
│   ├── main.yml          # <-- default test playbook
│   ├── requirements.yml  # <-- dependent roles during test (see below)
│   └── roles
│       └── role_example -> ../../../role_example  # <-- allows invoking { role: role_example } in main.yml
└── vars
    └── main.yml
```

[requirements.yml](https://github.com/chrismeyersfsu/provision_docker/blob/master/test/requirements.yml) allows you to specify test-dependent roles that can be pulled down at runtime.
```
cd test/
ansible-galaxy install -r requirements.yml -p roles/
ansible-playbook -i inventory main.yml
```

## Testing w/ Travis-CI
Take a look at [.travis.yml](https://github.com/chrismeyersfsu/provision_docker/blob/master/.travis.yml) to see how to test your role using travis-ci.
