import coverage
import unittest
import sys


def run_tests():
    """
    Runs all unit tests and generates coverage reports.
    This function performs the following steps:
    1. Starts code coverage tracking
    2. Discovers and executes all tests in the 'Tests' directory
    3. Exits with code 1 if any tests fail
    4. Generates coverage reports in both console and HTML format
    Returns:
        None
    Raises:
        SystemExit: If any tests fail (with exit code 1)
    Notes:
        - Tests are discovered automatically from the 'Tests' directory
        - HTML coverage report is generated in 'coverage_html' directory
        - Requires the 'coverage' module to be installed
    """
    # Start coverage tracking
    cov = coverage.Coverage()
    cov.start()

    # Discover and run tests
    loader = unittest.TestLoader()
    tests = loader.discover('Tests')
    runner = unittest.TextTestRunner()
    test_result = runner.run(tests)
    if not test_result.wasSuccessful():
        sys.exit(1)

    # Stop coverage tracking
    cov.stop()
    cov.save()

    # Generate coverage report
    cov.report()
    # Generate HTML report
    cov.html_report(directory='coverage_html')


if __name__ == '__main__':
    run_tests()
