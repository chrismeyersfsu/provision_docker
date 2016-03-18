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

## Testing w/ Travis-CI
Take a look at [.travis.yml](https://github.com/chrismeyersfsu/provision_docker/blob/master/.travis.yml) to see how to test your role using travis-ci.

## Similar Work

* https://github.com/metacloud/molecule 
