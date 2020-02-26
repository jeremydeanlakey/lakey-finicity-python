# python -m unittest discover -s tightership.tests -p "*.py"
coverage run -m unittest discover
coverage html --omit="**/tests*"
# python -m unittest tightership.tests.processes.test_plaid_processes.TestPlaidProcesses

