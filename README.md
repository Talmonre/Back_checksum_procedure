# Back_checksum_procedure
The code needed to compare the files between two backups to ensure they are the same, using low-tech methods native to most Linux distros. 

# Moshi
Moshi install code for setting up the Conda environments needed.
Install files required for automatic system setup. The script is a modified version of the one provided by the Biostar's team. Check out their work https://www.biostarhandbook.com/.

# Run the code for the first file :
```
find /path/to/first/directory -type f -exec openssl dgst -md5 {} \; > checksums_directory1.txt
```

# The run the code for the second file :
```
find /path/to/second/directory -type f -exec openssl dgst -md5 {} \; > checksums_directory2.txt
```

# Move the output files to the same place and run the last line to compare.
```
iff checksums_directory1.txt checksums_directory2.txt
```

# Moving the output files or copying them is bad practice. The best method would be to path to the original files and compare those.

