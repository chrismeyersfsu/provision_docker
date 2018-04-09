[![Build Status](https://travis-ci.org/mongrelion/ansible-role-docker.svg?branch=master)](https://travis-ci.org/mongrelion/ansible-role-docker)

# docker

Install and configure Docker.

## Role Variables

### `docker_config`

A dict of options that are written into docker's `daemon.json` config file. See [the docs for dockerd](https://docs.docker.com/engine/reference/commandline/dockerd/) for a full list of available options.

Default values: (set them in your `docker_config` to overwrite)

    storage-driver: devicemapper
    log-level: info

### `docker_version`

Specify the version of Docker to install, e.g. `1.12.6`, `17.05`. It allows to upgrade to latest version by specifying `latest`.

Default value: `17.06`

### `docker_proxy`, `docker_http_proxy`, `docker_https_proxy`, `docker_no_proxy`

`docker_proxy` specifies if proxy need to be applied. Default value of `docker_proxy` is no. If you need proxy set it to yes and updated other three variables as needed.

## Dependencies

None

## Example Playbook

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

## Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v1.25). You will have to install Docker on your system. See Get started for a Docker package suitable to for your system.
All packages you need to can be specified in one line:
```sh
pip install ansible 'ansible-lint>=3.4.15' 'molecule==1.25.0' docker 'testinfra>=1.7.0,<=1.10.1'
```
This should be similar to one listed in `.travis.yml` file in `install` section. 
After installing test suit you can run test by running
```sh
molecule test
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/stable-1.25/).

## License

MIT

## Author Information

You can find me on Twitter: [@mongrelion](https://twitter.com/mongrelion)
