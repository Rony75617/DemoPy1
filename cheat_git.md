- Initialize a git repo in local

    git init <PATH_OF_REPO>

- Adding all the files of repo to staging area

    git add <PATH_OF_REPO>

- Commit a file with a message

    git commit -m "Message for commit"

- Pushing the commit to your `master` repo on github

    git push origin master

- Checking the status of local repo

    git status

- Remove the folder from your local git tracking, but keep it on your disk.

    git rm -r --cached path_to_your_folder/

- How to git commit a single file/directory

    git commit -m 'my notes' -- path/to/my/file.ext  OR  git commit -m 'my notes' -- path/to/my/file.ext

- How to commit only modified (and not new or deleted) files?

    git commit -am "commit message"  OR  git commit -a

    > Providing the -a option to the git commit command makes Git automatically stage every file that is > > already tracked before doing the commit.
