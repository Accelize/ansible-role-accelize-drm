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

Installation:
Accelize DRM installation.
* **accelize_drm_python**: If `true`, install the Python library and systemd service. Default to `true`.
* **accelize_drm_devel**: If `true`, install the development C/C++ headers. Default to `false`.
* **accelize_repository_channel**: Accelize Repository channel to use: `stable` or `prerelease`. Default to `stable`.
* **accelize_drm_from_source**: If `true`, install from sources instead of from package. Default to `false`.

DRM Service:
Accelize DRM systemd service configuration.
* **accelize_drm_service_started**: If `true`, start the DRM service and enable it at boot (Require *accelize_drm_python* to `true`). Default to `true`.
* **accelize_drm_disabled**: If `true`, do not license the FPGA, only program FPGA at service start. Default to `false`.
* **fpga_slots**: List of FPGA slots to manage. Default to `[0]`.
* **fpga_image**: List of image to program on FPGA slots. Default to `[]`.
* **accelize_drm_driver_name**: FPGA driver name to use with the Accelize DRM service. Default to `aws_f1`.

DRM Configuration:
Accelize DRM configuration files.
* **accelize_drm_cred_src**: Path to the local `cred.json` file to transfer to the host. Default to `cred.json`.
* **accelize_drm_cred_dst**: Destination path of the `cred.json` file on the target host. Default to `/root/.accelize_drm/cred.json`.
* **accelize_drm_conf_src**: Path to the local `conf.json` file to transfer to the host. Default to `conf.json`.
* **accelize_drm_conf_dst**: Destination path of the `conf.json` file on the target host. Default to `/etc/accelize_drm/conf.json`.

Source installation, test & build requirements:
Installation of Accelize DRM build and testing dependencies. Mainly intended to DRM library developers.
* **accelize_drm_git_clone**: If specified, Git clone Accelize DRM to the specified path. Default to `''`.
* **accelize_drm_git_ref**: branch, tag or commit ID to use for source installation and git clone. Default to `master`.
* **accelize_drm_test**: If `true`, install tests dependencies. Default to `false`.
* **accelize_drm_coverage**: If `true`, install coverage dependencies. Default to `false`.
* **accelize_drm_abi_check**: If `true`, install ABI check dependencies. Default to `false`.
* **accelize_drm_build**: If `true`, install build dependencies. Default to `false`.
* **accelize_drm_build_doc**: If `true`, install documentation build dependencies. Default to `false`.
* **accelize_drm_build_package**: If `true`, install packages build & signature dependencies. Default to `false`.
* **accelize_drm_no_install**: If `true`, does not install Accelize DRM, only prepare the environment. Default to `false`.

Example Playbook
----------------

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
