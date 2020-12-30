import os


class WalkAndFind(object):
    def __init__(self: object) -> None:
        pass

    def find_files_with_suffix(self: object, suffix: str, base_path: str) -> list:
        """
        Find all files beneath path with file names with a suffix.

        Note that a path may contain further subdirectories
        and those subdirectories may also contain further subdirectories.

        There are no limit to the depth of the subdirectories can be.

        Parameters
        ----------
        suffix: str, required 
            Suffix if the file name to be found.

        path: str, required 
            Path of the file system.

        Returns
        ----------
        list
            List of full paths for files with the suffix.
        """

        all_paths: list = []

        def get_paths(path: str) -> None:
            if os.path.exists(path):
                paths: list = [f"{path}\{p}" for p in os.listdir(path)]
                for p in paths:
                    if os.path.isfile(p) and p.endswith(suffix):
                        all_paths.append(p)
                    else:
                        if os.path.isdir(p):
                            get_paths(p)
            else:
                #print("Path does not exist...")
                pass

        get_paths(base_path)

        return all_paths
