from git import Repo
from datetime import datetime

FILE_TO_COMMIT = 'data.json'
COMMIT_MESSAGE = 'Auto-update data'

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
commit_message = f"{COMMIT_MESSAGE} ({timestamp})"

def commit_to_git(file_path, message):
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

commit_to_git(FILE_TO_COMMIT, commit_message)