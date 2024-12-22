ansible-cert-distribution
=========

Ansible role to copy certitificates from the Ansible controller to the target hosts and add them to the OS trust store.
Works on __Debian-derivates__, __RHEL__ and __derivates__, __Alpine__ and __Archlinux__.


Requirements
------------

None

Role Variables
--------------

<table>
<thead><tr><th>Key</th><th>Value</th></tr></thead>
<tbody>
<tr>
<td>source_glob</td>
<td>location of ca-certificates</td>
</tr>
</table>

Dependencies
------------


None

Example Playbook
----------------

Below is an example playbook. The values under ```source_glob``` 
are simply a number of globs where the role will search for your certificates.

```
---
- hosts: centos-hosts
  become: true
  remote_user: root
  roles:
    - ca-certificates
  vars:
    source_glob:
      - /opt/admin/ca-certificates/*.crt

```

License
-------

BSD

Author Information
------------------

Martin Schmid, [mscbiz@akaritech.com](mailto:mscbiz@akaritech.com)
