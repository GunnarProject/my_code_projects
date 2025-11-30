## Git Setup and Instructions.

1. Initialize a new Git repository (if not already initialized) - `git init`.
2. Configure your Git user information # (Only need to run these once per environment) `git config --global user.name "Your Name" git config --global user.email "youremail@example.com"`
3. Add the remote repository (replace name and url) `git remote add origin https://github.com/yourusername/your-repo.git`
4. Add files to staging area `git add .`
5. Commit your changes `git commit -m "Initial commit"`
6. Push your changes to the remote repository `git push -u origin master` - where master is the branch name. You should choose the relevant branch.

## Your Turn

1. Create and move to a new branch called `develop`
2. Add some new git commands to the `README.md`
3. Add, commit, and push the branch with changes to the remote repository.
4. Look at the pull request to identify the difference between the branch and master.
5. Merge the pull request and delete the branch.
6. Change back to your main branch locally, pull the results from the remote to your local, and delete the local `develop` branch.
7. Check the branch is truly removed.
