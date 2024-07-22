# Backup_checksum_procedure
The code needed to compare the files between two backups to ensure they are identical, using low-tech methods native to most Linux distros. 

# Run the code for the first file :
```
find /path/to/first/directory -type f -exec openssl dgst -md5 {} \; > checksums_directory1.txt
```

# The run the code for the second file :
```
find /path/to/second/directory -type f -exec openssl dgst -md5 {} \; > checksums_directory2.txt
```
# This script edits the checksums created above to remove the pathing information and additional characters, then sorts the output for comparison. The output file name can be anything. The output from this script will be used for the digital comparison in during the next step. 

```
python edit.py -h
usage: edit.py [-h] input_file output_file

Sort lines in a text file with respect to lines containing an '='.

positional arguments:
  input_file   Input text file
  output_file  Output text file

optional arguments:
  -h, --help   show this help message and exit
```
# Move the output files to the same place and run the last line to compare.
```
diff checksums_edit1.txt checksums_edit2.txt > comparison.txt
```

# Moving the files to the same directory will make it easier to run the Python script. The final result will be a text file containing checksum values that do not correspond between the files. If the file is empty, the checks are good, and the values have no differences. The copy was successful.  

