import sys

from fbs_runtime.application_context import ApplicationContext
from fbs_runtime.application_context import cached_property
from app import Selia


ORGANIZATION_NAME = 'CONABIO'
ORGANIZATION_DOMAIN = 'https://www.gob.mx/conabio'
APPLICATION_NAME = 'Selia'


class AppContext(ApplicationContext):
    @cached_property
    def main_app(self):  # pylint: disable=no-self-use
        return Selia()

    def run(self):
        main_app = self.main_app  # pylint: disable=unused-variable
        return self.app.exec_()

    def config_app(self):
        self.app.setOrganizationName(ORGANIZATION_NAME)
        self.app.setOrganizationDomain(ORGANIZATION_DOMAIN)
        self.app.setApplicationName(APPLICATION_NAME)


if __name__ == '__main__':
    APP_CTXT = AppContext()
    EXIT_CODE = APP_CTXT.run()
    sys.exit(EXIT_CODE)
