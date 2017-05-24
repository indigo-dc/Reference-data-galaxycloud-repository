Reference-data-galaxycloud-repository
=====================================

Reference Data repository for Galaxy.
Related ansible roles:

- https://github.com/indigo-dc/ansible-role-cvmfs-client
- https://github.com/indigo-dc/ansible-role-galaxycloud-refdata

Create CernVM-FS Repository
---------------------------

The CernVM-FS (cvmfs) relies on OverlayFS or AUFS as default storage driver.
Ubuntu 16.04 natively supports OverlayFS, therefore it is used as default, to create and populate the cvmfs server.

Directories
-----------

- cvmfs_server_keys/
   Public key to mount cvmfs server containing Galaxy Reference Data are located in  cvmfs_server_keys/ directory.

- heat_template/
  Openstack Heat recipes to automatically deploy ad CernVM-FS server.

- scripts/
  Scripts to populate cvmfs server.

- lists/
  list files (yaml format) to automatically download reference data


Populate a CernVM-FS Repository (with reference data)
----------------------------------------------------

Content Publishing
```
  - cvmfs_server transaction <repository name>
  - Install content into /cvmfs/<repository name>
  - cvmfs_server publish <repository name>
```
cvmfs_server publish command will take time to move your contents from /cvmfs/<repository name> to /srv/cvmfs/. Enough space should be
Once installed on /cvmfs/<repository_name> 


### Reference data download



1. install pycurl



lists/
------
