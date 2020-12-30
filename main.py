from tests.tests_walk_and_find import TestCasesWalkAndFind
from solution.walk_and_find import WalkAndFind

if __name__ == "__main__":
    ###################################
    # Tests
    ###################################
    test_cases: TestCasesWalkAndFind = TestCasesWalkAndFind()
    test_dictory_base_path: str = r'.\tests\test_directories'

    test_cases.execute_tests_single_file_at_root(test_dictory_base_path)
    test_cases.execute_tests_single_subdirectory(test_dictory_base_path)
    test_cases.execute_tests_single_subdirectory_nested(test_dictory_base_path)
    test_cases.execute_tests_multiple_subdirectories_nested(
        test_dictory_base_path)
    test_cases.execute_tests_multiple_subdirectories_nested_no_file_match(
        test_dictory_base_path)
    test_cases.execute_tests_no_files_or_directories(test_dictory_base_path)
    test_cases.execute_tests_path_does_not_exist(test_dictory_base_path)

    ###################################
    # Demo
    ###################################
    demo_path: str = r'.\tests\test_directories\case_03'
    suffix: str = ".c"
    walk_and_find_instance: WalkAndFind = WalkAndFind()

    file_paths: list = walk_and_find_instance.find_files_with_suffix(
        suffix, demo_path)
    for file_path in file_paths:
        print(file_path)

    """
    Output:
    .\tests\test_directories\case_03\subdir1\a.c
    .\tests\test_directories\case_03\subdir3\subsubdir1\b.c
    .\tests\test_directories\case_03\subdir5\a.c
    .\tests\test_directories\case_03\t1.c
    """
