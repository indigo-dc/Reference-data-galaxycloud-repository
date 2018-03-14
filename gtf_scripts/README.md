Clean gtf files
===============

Clean method for .gtf file in order to build the rsem indexes

1. Run the script chr_list.py to have the list of chromosome of the .gtf
   ```
   python chr_list.py file.gtf
   ```

2. Delete the extra-chromosome lines using sed (from terminal
   ```
   sed -i ‘/’extra-chromosome’/d’ file.gtf)
   ```

3. Run he rewrite_gtf.py redirecting the output to a file.gtf
   ```
   python rewrite_gtf.py file.gtf>new_file.gtf
   ```

Author
------

Pietro Mandreoli
