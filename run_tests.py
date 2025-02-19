import coverage
import unittest
import sys

def run_tests():
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
