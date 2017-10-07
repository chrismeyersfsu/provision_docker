from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
import requests
import sys

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):

        self._supports_check_mode = False

        result = super(ActionModule, self).run(tmp, task_vars)

        params = dict()
        _tmp_args = self._task.args.copy()

        inventory_hostname = task_vars.get('inventory_hostname')
        defaults = {
            'name': inventory_hostname,
            'image': 'chrismeyers/centos6',
            'privileged': True,
            'state': "started",
            'restart': True,
            'tls': True,
            'stop_timeout': 1,
            'tty': True,
            'expose': "['1-65535']",
        }
        # TODO: Remove host_vars keys from task_vars
        for k, v in defaults.iteritems():
            _tmp_args.setdefault(k, v)

        result.update(self._execute_module('docker_container', module_args=_tmp_args, task_vars=task_vars))

        host_vars = {
            'ansible_connection': 'docker',
        }
        result['add_host'] = dict(host_name=defaults['name'], groups=task_vars['group_names'], host_vars=host_vars)

        result['changed'] = True
        return result
