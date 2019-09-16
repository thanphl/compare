from filecmp import dircmp
import sys
import difflib
import os


def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print("Different file found: %s" % name)
        with open(dcmp.left + '/' + name, 'r') as left:
            with open(dcmp.right + '/' + name, 'r') as right:
                left_content = left.readlines()
                right_content = right.readlines()
                result = difflib.ndiff(left_content, right_content)
                sys.stdout.writelines(result)

    for name in dcmp.right_only:
        print("Diff folders %s found in %s" % (name, dcmp.right))
    for name in dcmp.left_only:
        print("Diff folders %s found in %s" % (name, dcmp.left))
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)


folder = 'output'
print("Remove output files in %s folder" % folder)
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
            print("  Removed %s" % the_file)
    except Exception as e:
        print(e)

dir1 = sys.argv[1]
dir2 = sys.argv[2]
dcmp = dircmp(dir1, dir2)
print_diff_files(dcmp)
