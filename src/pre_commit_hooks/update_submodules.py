import git


def main() -> int:
    # Open the Git repository
    repo = git.Repo('.', search_parent_directories=True)

    # Update submodules recursively
    update_res = repo.git.submodule('update', '--init', '--recursive')

    # Check if there were any updates
    if update_res != '':
        # Print the result
        print(update_res)
        print("Submodules were updated successfully. Please commit the changes.")
        return 1

    return 0


if __name__ == "__main__":
    main()
