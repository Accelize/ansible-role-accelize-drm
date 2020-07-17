[![Build Status](https://travis-ci.org/Accelize/ansible-role-accelize-drm.svg?branch=master)](https://travis-ci.org/Accelize/ansible-role-ansible-drm)

Accelize DRM Ansible Role
=========================

This Ansible role install the Accelize DRM.

See [documentation](https://tech.accelize.com/documentation/stable/) for more information.

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

DRM Configuration:
Accelize DRM configuration files.
* **accelize_drm_cred_src**: Path to the local `cred.json` file to transfer to the host. If not specified, does not transfer file.
* **accelize_drm_cred_dst**: Destination path of the `cred.json` file on the target host. Default to `/root/.accelize_drm/cred.json`.
* **accelize_drm_conf_src**: Path to the local `conf.json` file to transfer to the host. If not specified, does not transfer file.
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

Enhancements
------------

### How to modify a role?

Some tasks might require an update, like installing a new python library.
To to so:
* Open the main.yml file in the tasks folder. This file lists all the tasks available and associates the operation to be performed.
* Look for the task that must be updated.
* Modify the appropriate section of the task and save the file.
* Commit and push the modification on git.
* Add a X.Y.Z tag to the commit in order to trigger the automatic job that will publish the new version on the ansible shared repository, Galaxy.
* The modification will be effective only when the version appears in the [Ansible Galaxy](https://galaxy.ansible.com/accelize/accelize_drm).

### How to add a new role?

* Open the main.yml file in the tasks folder. This file lists all the tasks available and associates the operation to be performed.
* Create a new role. You can copy paste an existing role that matches your wish the most and modify it appropriately.
* Save, commit and push the modification on git.
* Add a X.Y.Z tag to the commit in order to trigger the automatic job that will publish the new version on the ansible shared repository, Galaxy.
* The modification will be effective only when the version appears in the [Ansible Galaxy](https://galaxy.ansible.com/accelize/accelize_drm).

License
-------

Apache 2.0

Author Information
------------------

This role is provided by [Accelize](https://www.accelize.com).
