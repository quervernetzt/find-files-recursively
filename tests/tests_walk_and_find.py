import unittest
from solution.walk_and_find import WalkAndFind


class TestCasesWalkAndFind(unittest.TestCase):
    def execute_tests_single_file_at_root(self, test_dictory_base_path: str) -> None:
        # Arrange
        base_path: str = f"{test_dictory_base_path}\\case_00"
        suffix: str = ".c"
        walk_and_find_instance: WalkAndFind = WalkAndFind()

        # Act
        all_paths: list = walk_and_find_instance.find_files_with_suffix(
            suffix, base_path)

        # Assert
        result_list: list = [f"{base_path}\\t1.c"]
        self.assertListEqual(all_paths, result_list)

    def execute_tests_single_subdirectory(self, test_dictory_base_path: str) -> None:
        # Arrange
        base_path: str = f"{test_dictory_base_path}\\case_01"
        suffix: str = ".c"
        walk_and_find_instance: WalkAndFind = WalkAndFind()

        # Act
        all_paths: list = walk_and_find_instance.find_files_with_suffix(
            suffix, base_path)

        # Assert
        result_list: list = [f"{base_path}\\subdir1\\t1.c"]
        self.assertListEqual(all_paths, result_list)

    def execute_tests_single_subdirectory_nested(self, test_dictory_base_path: str) -> None:
        # Arrange
        base_path: str = f"{test_dictory_base_path}\\case_02"
        suffix: str = ".c"
        walk_and_find_instance: WalkAndFind = WalkAndFind()

        # Act
        all_paths: list = walk_and_find_instance.find_files_with_suffix(
            suffix, base_path)

        # Assert
        result_list: list = [
            f"{base_path}\\subdir1\\subsubdir1\\t2.c", f"{base_path}\\subdir1\\t1.c"]
        self.assertListEqual(all_paths, result_list)

    def execute_tests_multiple_subdirectories_nested(self, test_dictory_base_path: str) -> None:
        # Arrange
        base_path: str = f"{test_dictory_base_path}\\case_03"
        suffix: str = ".c"
        walk_and_find_instance: WalkAndFind = WalkAndFind()

        # Act
        all_paths: list = walk_and_find_instance.find_files_with_suffix(
            suffix, base_path)

        # Assert
        result_list: list = [
            f"{base_path}\\subdir1\\a.c",
            f"{base_path}\\subdir3\\subsubdir1\\b.c",
            f"{base_path}\\subdir5\\a.c",
            f"{base_path}\\t1.c"
        ]
        self.assertListEqual(all_paths, result_list)

    def execute_tests_multiple_subdirectories_nested_no_file_match(self, test_dictory_base_path: str) -> None:
        # Arrange
        base_path: str = f"{test_dictory_base_path}\\case_04"
        suffix: str = ".c"
        walk_and_find_instance: WalkAndFind = WalkAndFind()

        # Act
        all_paths: list = walk_and_find_instance.find_files_with_suffix(
            suffix, base_path)

        # Assert
        result_list: list = []
        self.assertListEqual(all_paths, result_list)

    def execute_tests_no_files_or_directories(self, test_dictory_base_path: str) -> None:
        # Arrange
        base_path: str = f"{test_dictory_base_path}\\case_05"
        suffix: str = ".c"
        walk_and_find_instance: WalkAndFind = WalkAndFind()

        # Act
        all_paths: list = walk_and_find_instance.find_files_with_suffix(
            suffix, base_path)

        # Assert
        result_list: list = []
        self.assertListEqual(all_paths, result_list)

    def execute_tests_path_does_not_exist(self, test_dictory_base_path: str) -> None:
        # Arrange
        base_path: str = f"{test_dictory_base_path}\\case_500"
        suffix: str = ".c"
        walk_and_find_instance: WalkAndFind = WalkAndFind()

        # Act
        all_paths: list = walk_and_find_instance.find_files_with_suffix(
            suffix, base_path)

        # Assert
        result_list: list = []
        self.assertListEqual(all_paths, result_list)
