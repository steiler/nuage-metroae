#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
import yaml

DOCUMENTATION = '''

---
module: libn_install
short_description: Returns list of hosts on which Libnetwork is to be installed
options:
   path:
     description:
         - Path to the build_var.yml file that has the VRS information.
     required: True
'''

EXAMPLES = '''
- libn_install: path=./build_vars.yml
'''


def libn_check(filepath):
    fil = open(filepath)
    config = yaml.load(fil)
    vrs_list = []
    for item in config['myvrss']:
        if item['libnetwork_install'] == "True" or item['libnetwork_install'] == "true":
            for ip in item['vrs_ip_list']:
                vrs_list.append(ip)
    return vrs_list


arg_spec = dict(
    path=dict(
        required=False,
        type='str'))
module = AnsibleModule(argument_spec=arg_spec, supports_check_mode=True)


def main():
    path = module.params['path']
    result = libn_check(path)
    module.exit_json(meta=result)


if __name__ == '__main__':
    main()
