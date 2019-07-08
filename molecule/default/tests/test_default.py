import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages_installed(host):
    """
    Test that packages are installed
    """
    assert host.package("libaccelize-drm").is_installed
    assert (host.package("python3-accelize-drm").is_installed or
            host.package("python36-accelize-drm").is_installed)


def test_service_configuration_installed(host):
    """
    Test that service configuration file is installed
    """
    conf = host.file(
        '/etc/systemd/system/accelize_drm.service.d/accelize_drm.conf')
    assert conf.exists
    assert conf.contains('Environment=ACCELIZE_DRM_DRIVER_0=aws_f1')
    assert conf.contains(
        'Environment=ACCELIZE_DRM_CRED_0=/root/.accelize_drm/cred.json')
    assert conf.contains(
        'Environment=ACCELIZE_DRM_CONF_0=/etc/accelize_drm/conf.json')
    assert not conf.contains('Environment=ACCELIZE_DRM_DISABLED_0=true')
    assert not conf.contains('Environment=ACCELIZE_DRM_IMAGE_')


def test_library_configuration_installed(host):
    """
    Test that library configuration files are installed
    """
    assert host.file('/root/.accelize_drm/cred.json').exists
    assert host.file('/etc/accelize_drm/conf.json').exists
