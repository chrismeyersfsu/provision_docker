[![Build Status](https://travis-ci.org/mongrelion/ansible-role-docker.svg?branch=master)](https://travis-ci.org/mongrelion/ansible-role-docker)

docker
=========

Install Docker

Requirements
------------

None

Role Variables
--------------

None

Dependencies
------------

None

Example Playbook
----------------
Install Docker
```
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
