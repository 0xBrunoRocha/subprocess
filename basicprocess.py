import errno
import subprocess


class BasicProcess:
    def __init__(self, command):
        self._command = command
        self._arguments = []
        self.process = None

    def run(self, stdout=None, stderr=None):

        try:
            self.process = subprocess.Popen(
                self._command,
                stdin=subprocess.PIPE,
                stdout=stdout,
                stderr=stderr
            )
        except OSError as e:
            if e.errno == errno.ENOENT:
                raise ProcessNotFoundError("Process called does not exist.")
            else:
                raise
        out = self.process.communicate()
        return out;

class ProcessNotFoundError(Exception):
    """When returns non-zero exit code.
    """
