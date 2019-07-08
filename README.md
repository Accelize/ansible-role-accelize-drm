[![Build Status](https://travis-ci.org/Accelize/ansible-role-accelize-drm.svg?branch=master)](https://travis-ci.org/Accelize/ansible-role-ansible-drm)

Accelize DRM Ansible Role
=========================

This Ansible role install the Accelize DRM.

See [documentation](http://accelize.com/docs) for more information.

Requirements
------------

The role requires to be run as root on the target host.

Role Variables
--------------

* **fpga_slots**: List of FPGA slots to manage. Default to `[0]`.
* **fpga_image**: List of image to program on FPGA slots. Default to `[]`.
* **accelize_drm_service_started**: If `true`, start the DRM service and enable it at boot. Default to `true`.
* **accelize_drm_disabled**: If `true`, do not license the FPGA, only program FPGA at service start. Default to `false`.
* **accelize_drm_driver_name**: FPGA driver name to use with the Accelize DRM service. Default to `aws_f1`.
* **accelize_drm_cred_src**: Path to the local `cred.json` file to transfer to the host. Default to `cred.json`.
* **accelize_drm_cred_dst**: Destination path og the `cred.json` file on the target host. Default to `/root/.accelize_drm/cred.json`.
* **accelize_drm_conf_src**: Path to the local `conf.json` file to transfer to the host. Default to `conf.json`.
* **accelize_drm_conf_dst**: Destination path og the `conf.json` file on the target host. Default to `/etc/accelize_drm/conf.json`.
* **accelize_repository_channel**: Accelize Repository channel to use: `stable` or `prerelease`. Default to `stable`.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  become: true  
  roles:
     - role: accelize.accelize_drm
```

Dependencies
------------

None.

License
-------

Apache 2.0

Author Information
------------------

This role is provided by [Accelize](https://www.accelize.com).
