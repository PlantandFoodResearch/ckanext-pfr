import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import logging


class PfrPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # SCHEMA_OPTION = 'pfr.dataset_schemas'
    # FALLBACK_OPTION = 'pfr.dataset_fallback'
    # SCHEMA_TYPE_FIELD = 'dataset_type'

    @classmethod
    def _store_instance(cls, self):
        PfrPlugin.instance = self

    # IConfigurer

    def update_config(self, config_):
        logger = logging.getLogger(__name__)
        logger.info('PfrPlugin:update_config ')
        self._store_instance(self)
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'pfr')
