import git
import argparse
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    """Source: https://stackoverflow.com/a/21195182"""
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    parser.add_argument(
        '--fail-on-change',
        help="causes the hook to fail when a submodule was updated and the those "
             "working directory changes were staged.",
        action="store_true"
    )
    args = parser.parse_args(argv)
    update_retval = 0
    if args.fail_on_change:
        update_retval = 1

    # Open the Git repository
    repo = git.Repo('.', search_parent_directories=True)

    # Get the list of changed files before submodule update
    pre_update_files = repo.git.diff('--name-only')

    # Update submodules with most recent commit at the remote tracking branch
    update_res = repo.git.submodule('update', '--remote', '--merge')

    # Check if there were any updates
    if update_res != '':
        # Print the result
        print(update_res)
        print('Submodules were updated successfully. Please commit the changes.')
        # Get the list of changed files after submodule update
        post_update_files = repo.git.diff('--name-only')

        # Get the list of all changed files
        all_changed_files = repo.git.diff('--name-only', '--diff-filter=d')

        # Find the files changed during submodule update
        changed_files = set(post_update_files.splitlines()) - set(
            pre_update_files.splitlines())

        # Include files changed before the submodule update
        changed_files.update(set(all_changed_files.splitlines()))
        changed_files_string = '\n'.join(changed_files)
        print(f'The following files were staged for you:\n{changed_files_string}')
        repo.git.add(list(changed_files), update=True)

        # If there were any updates, add the changes to the index
        return update_retval

    # No updates
    return 0


if __name__ == '__main__':
    main()
