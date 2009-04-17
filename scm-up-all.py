#!/usr/bin/env python
import os
import sys


__author__ = 'Igor Davydenko <playpauseandstop@gmail.com>'
__version__ = '0.1'

def run():
    if len(sys.argv) == 2:
        dirname = os.path.expanduser(sys.argv[1])
    else:
        dirname = os.getcwd()

    if not os.path.isdir(dirname):
        sys.stderr.write('Directory "%s" was not exists or you have not ' \
                         'permissions to read from it.\n' % dirname)
        sys.exit(1)

    dirdata = os.listdir(dirname)

    not_scms = []
    scms = (
        ('bzr', []),
        ('darcs', []),
        ('git', []),
        ('git-svn', []),
        ('hg', []),
        ('svn', []),
    )

    dirs_len = len(dirdata)
    scms_len = 0

    for name in dirdata:
        subdirname = os.path.join(dirname, name)

        if not os.path.isdir(subdirname):
            continue

        scms_len += 1
        subdirdata = os.listdir(subdirname)

        if '.bzr' in subdirdata:
            scms[0][1].append(subdirname)
        elif '_darcs' in subdirdata:
            scms[1][1].append(subdirname)
        elif '.git' in subdirdata:
            f = open(os.path.join(subdirname, '.git/config'), 'r')
            if not 'svn-remote' in f.read():
                scms[2][1].append(subdirname)
            else:
                scms[3][1].append(subdirname)
            f.close()
        elif '.hg' in subdirdata:
            scms[4][1].append(subdirname)
        elif '.svn' in subdirdata:
            scms[5][1].append(subdirname)
        else:
            scms_len -= 1
            not_scms.append(subdirname)

    print 'Work directory:', dirname
    print 'Number of found subdirs:', dirs_len
    print 'Number of found SCM dirs:', scms_len

    if dirs_len != scms_len:
        print 'Not SCM dirs:', not_scms

    print

    if not scms_len:
        sys.exit(0)

    for protocol, dirs in scms:
        if protocol == 'bzr':
            cmd = "cd '%s' && bzr pull"
        elif protocol == 'darcs':
            cmd = "cd '%s' && darcs pull -a"
        elif protocol == 'git':
            cmd = "cd '%s' && git pull"
        elif protocol == 'git-svn':
            cmd = "cd '%s' && git svn fetch"
        elif protocol == 'hg':
            cmd = "cd '%s' && hg pull && hg update"
        elif protocol == 'svn':
            cmd = "svn update '%s'"

        dirs.sort()

        for dirname in dirs:
            print '$', cmd % dirname
            os.system(cmd % dirname)
            print

if __name__ == '__main__':
    run()
