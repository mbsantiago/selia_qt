import sys

from fbs_runtime.application_context import ApplicationContext
from app import Selia


class AppContext(ApplicationContext):
    def run(self):
        self.main_app = Selia()
        return self.app.exec_()


if __name__ == '__main__':
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)
