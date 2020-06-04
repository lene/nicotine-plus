import os
import signal
from pathlib import Path
from subprocess import Popen, PIPE
from time import sleep


# noinspection PyInterpreter
class nicotine_library:  # noqa
    def __init__(self):
        self._result = None

    def running_nicotine_starts_a_process(self, command, timeout):
        if not isinstance(command, list):
            command = [command]
        proc = Popen(command)
        sleep(int(timeout))
        self._result = bool(proc.pid)
        os.kill(proc.pid, signal.SIGTERM)
        sleep(1)

    def nicotine_exit_code_ok(self, command, timeout):
        if not isinstance(command, list):
            command = [command, '&']

        with open(Path(os.environ['HOME']) / '.xinitrc', 'w') as xinitrc:
            print(*command, file=xinitrc)

        twm = Popen(['twm'])
        nicotine = Popen(['nicotine'])
        sleep(1)
        cancel = Popen([
            'xdotool',
            'search', '--class', 'nicotine+',
            'windowactivate', '--sync', '%1',
            'key', 'ctrl+q'
        ])
        cancel_out = cancel.communicate()
        sleep(1)
        nicotine_out = nicotine.communicate()
        sleep(1)
        self._result = [nicotine.returncode] + nicotine_out + cancel_out
        sleep(1)
        twm.kill()

    def nicotine_exit_code_ok_bak(self, command, timeout):
        if not isinstance(command, list):
            command = [command]

        proc = Popen(command)
        sleep(int(timeout))
        cancel = Popen([
            'xdotool',
            'key', 'ctrl+q'
        ])
        cancel_out = cancel.communicate()
        # os.kill(proc.pid, signal.SIGTERM)
        proc_out = proc.communicate()
        # self._result = proc.returncode
        self._result = proc_out + cancel_out + (proc.returncode,)
        sleep(1)

    def result_should_be(self, expected):
        with open('/tmp/robot.log', 'a+') as file:
            print(f"Expected: {expected}, actual: {self._result}", file=file)
        actual = self._result
        self._result = None
        assert actual == expected
