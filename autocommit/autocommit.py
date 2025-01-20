from git import Repo

def commit_to_git(file_path:str, message:str):
    """Commit changes to the Git repository."""
    repo = Repo()
    try:
        repo.git.add(file_path)
        repo.index.commit(message)
        origin = repo.remote(name='origin')
        origin.push()
        print("Changes pushed to GitHub.")
    except Exception as e:
        print(f"Error during Git operations: {e}")