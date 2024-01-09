Release announcement : Ansible Community Package {{ package_version }}

Hello everyone,

We're happy to announce the release of the Ansible {{ package_version }} package!

Ansible {{ package_version }} requires latest version of ansible-core a.b and includes a curated set of Ansible collections that provides a vast number of modules and plugins. This is a major release of Ansible.

ansible-core is a required dependency, not contained within the ansible packages. Pip install builds the
dependency, but it can be built and installed quite independently of the "ansible" distribution.

How to get it
-------------

This release is available on PyPI and can be installed with pip:

```
$ python3 -m pip install ansible=={{ package_version }} --user
```

The sources for this release can be found here:

Release tarball: {{ tarball_url }}

SHA256: {{ tarball_sha }}

Wheel package: {{ wheel_url }}

SHA256: {{ wheel_sha }}

On behalf of the Ansible community, thank you and happy automating!

Cheers,
Ansible Community Team