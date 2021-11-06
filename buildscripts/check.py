import os
import yaml
import argparse
import subprocess
from collections import defaultdict


class Runner:
    def suppors(self, code):
        return False

    def run(self, code, test):
        print(f'No matching runners found for "{code["lang"]}"')
        return False


class PythonRunner:
    def __init__(self, source_prefix):
        self.source_prefix = source_prefix

    def supports(self, code):
        return code['lang'] == 'python'

    def run(self, code, tests):
        print(f'Running {code["filename"]}')

        a = []

        for i, t in enumerate(tests):
            result = subprocess.run(['python3', os.path.join(self.source_prefix, code['filename'])],
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, input=t['stdin'].encode('utf-8'))
            stdout = result.stdout.decode('utf-8') 
            exitcode = result.returncode
            passing = stdout == t['stdout'] and exitcode == t['exitcode']

            print(f'\tTest {i + 1} {"passing" if passing else "failing"}')
            if not passing:
                print(f'\t\tTest:', t,
                      f'stdout: {stdout}', f'exitcode: {exitcode}', sep='\n\t\t')

            a.append(passing)

        return all(a)


DEFAULT_RUNNER = Runner()


def get_test_data(m: dict):
    s = m.get('stdout', 'BLOCK')
    return {'stdin': m.get('stdin', ''), 'stdout': m.get('code', '') if s == 'BLOCK' else s, 'exitcode': m.get('exitcode', 0)}


def run_tests(tests: list, runners: list):

    def find_matching_runner(code, runners: list):
        return next(filter(lambda r: r.supports(code), runners), DEFAULT_RUNNER)

    return map(lambda t: find_matching_runner(t[0], runners).run(*t), tests)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Cheks code extracted by sources.py')
    parser.add_argument('metadata', metavar='SOURCES_METADATA',
                        type=str, nargs=1, help='Path to source-metadata.yaml')
    parser.add_argument('-p', metavar='PREFIX', dest='prefix',
                        type=str, default='', help='Sources path prefix')

    args = parser.parse_args()

    runners = [PythonRunner(args.prefix)]

    with open(args.metadata[0], 'r') as f:
        metadata = yaml.safe_load(f)

    if metadata == None:
        print('No tests were runned')
        exit(0)

    tests = defaultdict(list)
    code = dict()

    for m in metadata:
        if 'runs' in m:
            tests[m['runs']].append(get_test_data(m))
        if 'filename' in m:
            code[m['filename']] = m

    results = list(run_tests([(code[k], v)
                   for k, v in tests.items()], runners))

    if len(results) == 0:
        print('No tests were runned')
        exit(0)

    if all(results):
        exit(0)

    exit(1)
