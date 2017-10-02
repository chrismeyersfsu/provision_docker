[![Build Status](https://travis-ci.org/mongrelion/ansible-role-docker.svg?branch=master)](https://travis-ci.org/mongrelion/ansible-role-docker)

docker
=========

Install and configure Docker.

Role Variables
--------------

### `docker_config`

A dict of options that are written into docker's `daemon.json` config file. See [the docs for dockerd](https://docs.docker.com/engine/reference/commandline/dockerd/) for a full list of available options.

Default values: (set them in your `docker_config` to overwrite)

    storage-driver: devicemapper
    log-level: info

### `docker_version`

Specify the version of Docker to install, e.g. `1.12.6`, `17.05`.

Default value: `17.03`

### `setup_script_md5_sum`

Default value: md5 checksum of default `docker_version` setup script (see `defaults/main.yml` for exact default value)

**If you intend to install a version of Docker other than the default, you must provide an appropriate override value for this variable.**

Either:

1. Generate an md5 checksum for the desired version's install script
1. If you know what you are doing and are not worried about security, set this variable to "no" or "false" to disable checksum verification of the setup script.

### `setup_script_url`

URL pointing to a Docker setup script that will install the specified `docker_version`.

Default value: `https://releases.rancher.com/install-docker/{{ docker_version }}.sh`

The default URL utilizes [Rancher Labs' version-specific, OS-agnostic setup scripts](https://github.com/rancher/install-docker), which in turn just install the appropriate version of `docker-ce` or `docker-engine` from the official Docker `apt` and `yum` repositories.

### `upgrade_docker`

Per default, this role will only download and run the installation script when
Docker is not installed (or more precise: when `dockerd` is not in `$PATH`). Set
`upgrade_docker` to `True` to override this behavior and force the install
script to be run.

So in order to upgrade Docker on managed systems, take the following steps:

0. Either download a newer version of this role (with a more recent default
   version) or update `docker_version` and `setup_script_md5_sum` in your
   host/group vars.
1. Run your playbook with `-e upgrade_docker=True`


Dependencies
------------

None

Example Playbook
----------------
Install Docker
```yaml
- hosts: servers
  roles:
    - mongrelion.docker
```

Install and configure docker
```yaml
- hosts: servers
  roles:
    - role: mongrelion.docker
      docker_config:
        live-restore: true
        userland-proxy: false
```

Testing
-------
For development, we use Vagrant.
Bring the VM up with

```
$ vagrant up
```

This will automatically run the playbooks against the virtual machine once it's up.
After making changes to any playbook, you can test the provisioning with

```
$ vagrant provision
```

License
-------

MIT

Author Information
------------------

You can find me on Twitter: [@mongrelion](https://twitter.com/mongrelion)
