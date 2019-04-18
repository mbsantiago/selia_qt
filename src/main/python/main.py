"""
Main application container
"""
import sys

from fbs_runtime.application_context import ApplicationContext
from fbs_runtime.application_context import cached_property
from app import Selia
from app.settings import Settings


ORGANIZATION_NAME = 'CONABIO'
ORGANIZATION_DOMAIN = 'https://www.gob.mx/conabio'
APPLICATION_NAME = 'Selia'


class AppContext(ApplicationContext):
    """Main applicacion container"""
    @cached_property
    def main_app(self):  # pylint: disable=no-self-use
        """Aplication object"""
        return Selia()

    def run(self):
        self.config_app()

        main_app = self.main_app  # pylint: disable=unused-variable
        return self.app.exec_()

    def config_app(self):
        """Configure app at startup"""
        self.app.setOrganizationName(ORGANIZATION_NAME)
        self.app.setOrganizationDomain(ORGANIZATION_DOMAIN)
        self.app.setApplicationName(APPLICATION_NAME)

        config_file = self.get_resource('settings.ini')
        settings = Settings()
        settings.initialize(config_file)


if __name__ == '__main__':
    APP_CTXT = AppContext()
    EXIT_CODE = APP_CTXT.run()
    sys.exit(EXIT_CODE)
