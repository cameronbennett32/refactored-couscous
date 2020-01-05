#!/usr/bin/env python3
# *-* coding: utf-8 *-*
"""Script should upload the same file to two different Git repositories.
It will update an existing file, or create a new file, in a 'PyUploads' branch.

Resources:
https://pygithub.readthedocs.io/en/latest/examples/Repository.html
https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html
https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
"""

# Import libraries
from github import Github


def uploadFileToBranch(git, repo, branch, filename):
    """ This function should either update or create a file in a git repo.

    Inputs: GitHub object, repo address, branch name, and a file
    Outputs: None

    # Step 1: Search repo for files of the same name
    # Step 2: If one exist, update the file else create a new file (in 'Test' branch)
    # Step 3: Commit
    """

    # Fetch contents of repo
    contents = repo.get_contents("")
    
    # attempt to read in local file
    file = readFile(filename)
    if not file:
        pass
    
    else:
        for i in range(len(contents)):
            if contents[i].name == filename:
                print(contents[i].path)
                print(contents[i].sha)
                repo.update_file(contents[i].path,'New commit','test','1ba9162fa82db84ece8b1e8553ad3e0761716b2b',branch='PyUploads')
                print(contents[i].path)
                print(contents[i].sha)
                # Don't need to continue checking repo for files, so exit
                break
                
            #else:
            #    continue
            
            # If the file doesn't exist, create a new copy of the file
            #createFile(contents[i].path,'New commit',file,branch)

    """    
    # Iterate through all files in the directory
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:    
            print(file_content)
    """

def readFile(filename):
    """ This function should attempt to open a local file and handle/print exceptions

    Inputs: The file name
    Outputs: A file stream
    """
    
    try:
        f = open(filename,'r')
        with f:
            file = f.read()
            f.close()
        return file
    
    except IOError as e:
        print('Error: ' + str(e))
        return False

def createFile(path, message, content, branch_):
    """ This function should create a new file in a Git repo

    Inputs: Git file path, commit message, file contents, Git branch
    Outputs: Success or fail reponse
    """
    
    response = repo.create_file(path,
                     message,
                     content,
                     branch=branch_)
    return response

def updateFile(repo, path, message, content, sha, branch_):
    """ This function should update an existing file in a Git repo

    Inputs: Git repo, Git file path, commit message, file contents, sha, and Git branch
    Outputs: Success or fail reponse
    """
    response = repo.update_file(path,
                     message,
                     content,
                     sha,
                     branch=branch_)
    return True

# Personal repo
GitCam = Github("")
RepoCam = GitCam.get_repo("")

# Upload to personal Repo
uploadFileToBranch(GitCam, RepoCam, 'PyUploads', "FizzBuzz.py")



