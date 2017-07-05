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
