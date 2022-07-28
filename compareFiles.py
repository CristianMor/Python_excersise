import difflib
import sys

# git-styled output

with open('../../Downloads/app-katana-local-v1.1/UpdateRutinaGuardadas.php', 'r') as file0:
    with open('../../Downloads/app-testing/UpdateRutinaGuardadas.php', 'r') as file1:
        diff = difflib.unified_diff(
            file0.readlines(),
            file1.readlines(),
            fromfile='file0',
            tofile='file1',
        )
        for line in diff:
            sys.stdout.write(line)
