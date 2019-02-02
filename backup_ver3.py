import os
import time


source = ['C:\\code1']
# Example on Mac OS X and Linux: source = ['/Users/swa/notes']
# # Notice we had to use double quotes inside the string
# # for names with spaces in it.

# # 2. The backup must be stored in a
# # main backup directory
# # Example on Windows:
target_dir = 'C:\\backup'


# Example on Mac OS X and Linux:
# target_dir = '/Users/swa/backup'
# # Remember to change this to which folder you will be using

# Create target directory if it is not present

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
# 3. The files are backed up into a zip file.

# 4. The current day is the name of the subdirectory in the main direct
today = target_dir + os.sep + time.strftime('%Y%m%d')
#print('today is', today)

# The current time is the name of the zip archive.
now = time.strftime('%H%M%S')

# Take a comment from the user to # create the name of the zip file

comment = input('Enter a comment-->')
#check if a comment was entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +
             comment.replace('', '_') + '.zip'

#Creat the subdirectory if it isnt already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 5. We use the zip command to put the files in a zip archive
zip_command = 'zip -r {0} {1}'.format(target, ''.join(source))

# Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')

if os.system(zip_command) == 0:
        print('Successful backup to', target)
else:
    print('Backup FAILED')
