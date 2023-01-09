import pypi_builder
import repository_generator
import kabbes_user_client
import py_starter as ps
import datetime

class Client( pypi_builder.PackageGenerator, repository_generator.Client ):

    BASE_CONFIG_DICT = {
        "_Dir": pypi_builder._Dir,
        "year_str": str(datetime.datetime.now().year)
    }

    def __init__( self, dict={}, **kwargs ):

        repository_generator.Client.__init__( self )
        dict = ps.merge_dicts( Client.BASE_CONFIG_DICT, dict )
        overwrite_cfg = kabbes_user_client.Client( dict=dict, **kwargs ).cfg
        self.cfg.merge(overwrite_cfg)

        pypi_builder.PackageGenerator.__init__( self )

