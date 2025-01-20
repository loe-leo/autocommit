from autocommit import autocommit
import generate_data

if __name__ == '__main__':
    generate_data.time_json("data.json")
    autocommit.commit_to_git("data.json", "Auto update file")