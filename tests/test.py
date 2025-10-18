import csv
import sys
from os import path
current_dir = path.dirname( path.abspath(__file__) )
sys.path.append( path.dirname( current_dir ) )
from dist.python.phonemizer import Phonemizer

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

if __name__ == "__main__":
    test_case_filepath = "test_cases.csv"

    phonemizer = Phonemizer()

    total_tests = 0
    passed_tests = 0
    failed_tests = []

    print(f"{Colors.YELLOW}--- Running tests using {test_case_filepath} ---{Colors.RESET}")

    with open(path.join(current_dir, test_case_filepath), 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            total_tests += 1

            input_str = row['input']
            expected_output = row['expected_output']

            # --- Run the function under test ---
            try:
                actual_output = phonemizer.phonemize(input_str)
            except Exception as e:
                # Catch internal errors in the function
                print(f"{Colors.RED}Error processing input{Colors.RESET} '{input_str}': {e}", file=sys.stderr)
                failed_tests.append({
                    'input': input_str,
                    'reason': 'Function raised an exception'
                })
                continue

            filler = ' ' * (18 - len(input_str))

            # --- Compare results ---
            if actual_output == expected_output:
                passed_tests += 1
                print(f"{Colors.GREEN}[PASS]{Colors.RESET} '{input_str}' {filler} {Colors.YELLOW}=>{Colors.RESET} '{Colors.GREEN}{actual_output}{Colors.RESET}'")
            else:
                failed_tests.append({
                    'input': input_str,
                    'expected': expected_output,
                    'actual': actual_output
                })
                print(f"{Colors.RED}[FAIL]{Colors.RESET} '{input_str}' {filler} {Colors.YELLOW}=>{Colors.RESET} '{Colors.RED}{actual_output}{Colors.RESET}', expected '{Colors.YELLOW}{expected_output}{Colors.RESET}'")

    # --- Summary Report ---
    print(f"\n{Colors.YELLOW}--- Test Summary ---{Colors.RESET}")
    print(f"Total Tests Run: {total_tests}")
    print(f"{Colors.GREEN}Passed:{Colors.RESET} {passed_tests}")
    print(f"{Colors.RED}Failed:{Colors.RESET} {len(failed_tests)}")

    if failed_tests:
        print(f"\n{Colors.YELLOW}Failures:{Colors.RESET}")
        for failure in failed_tests:
            print("-" * 30)
            print(f"  Input: {Colors.YELLOW}{repr(failure['input'])}{Colors.RESET}")
            if 'reason' in failure:
                 print(f"  Reason: {failure['reason']}")
            else:
                print(f"  Expected: {Colors.GREEN}{repr(failure['expected'])}{Colors.RESET}")
                print(f"  Actual:   {Colors.RED}{repr(failure['actual'])}{Colors.RESET}")

        # Exit with a non-zero code to indicate test failure
        sys.exit(1)
    else:
        print(f"\n{Colors.GREEN}All tests passed successfully!{Colors.RESET}")
