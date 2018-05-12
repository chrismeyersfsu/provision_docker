<p><img src="http://1000logos.net/wp-content/uploads/2017/07/Logo-Docker-500x394.jpg" alt="docker logo" title="docker" align="right" height="60" /></p>

# Ansible role: docker

[![Build Status](https://travis-ci.org/mongrelion/ansible-role-docker.svg?branch=master)](https://travis-ci.org/mongrelion/ansible-role-docker)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-mongrelion.docker-blue.svg)](https://galaxy.ansible.com/mongrelion/docker/)

## Description

Install and configure [docker](https://www.docker.com) containerization platform.

## Requirements

- Ansible >= 2.3

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `docker_compose` | yes | Install docker-compose package |
| `docker_proxy` | no | Enable HTTP proxy setup |
| `docker_http_proxy` | "" | HTTP proxy server address |
| `docker_https_proxy` | "" | HTTPS proxy server address |
| `docker_no_proxy` | "" | Comma-separated list of hosts which won't use HTTP proxy |
| `docker_version` | "17.06" | docker version which should be installed on target server. Can use `latest` for updates |
| `docker_default_config` | [ storage-driver: devicemapper, log-level: info ] | Docker daemon configuration |
| `docker_users` | [] | Add users to docker group. Users must exist before adding. Construct like `- {{ ansible_env['SUDO_USER'] \| default(ansible_user_id) }}` could be used to specify user which is used for ansible connection to host. |

## Example

### Playbooks

Just install Docker with default config
```yaml
- hosts: servers
  roles:
    - mongrelion.docker
```

Install and configure docker daemon
```yaml
- hosts: servers
  roles:
    - role: mongrelion.docker
      docker_config:
        live-restore: true
        userland-proxy: false
```

## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v2.x). You will have to install Docker on your system. See Get started for a Docker package suitable to for your system.
All packages you need to can be specified in one line:
```sh
pip install ansible 'ansible-lint>=3.4.15' 'molecule>2.12.0' docker 'testinfra>=1.7.0'
```
This should be similar to one listed in `.travis.yml` file in `install` section.
After installing test suit you can run test by running
```sh
molecule test
```
For more information about molecule go to their [docs](https://molecule.readthedocs.io/en/latest/).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.

## Author Information

You can find me on Twitter: [@mongrelion](https://twitter.com/mongrelion)

## Contributors

- Carlos Leon ([@mongrelion](https://github.com/mongrelion))
- Paweł Krupa ([@paulfantom](https://github.com/paulfantom))
- Marcus Levine ([@marcusianlevine](https://github.com/marcusianlevine))
- Manuel Hutter ([@mhutter](https://github.com/mhutter))
- Dmitri Bichko ([@dbichko](https://github.com/dbichko))
- Zane Westover ([@zanewestover](https://github.com/zanewestover))
- Bruce Becker ([@brucellino](https://github.com/brucellino))
- David Wahlstrom ([@drwahl](https://github.com/drwahl))
- Max Oreshnikov ([@maxim0r](https://github.com/maxim0r))
- Nicholas E. Rabenau ([@nerab](https://github.com/nerab))
- Petr Balogh ([@petr-balogh](https://github.com/petr-balogh))
- ramz ([@ageekymonk](https://github.com/ageekymonk))
