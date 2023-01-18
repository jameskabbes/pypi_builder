import pypi_builder
import kabbes_client
import datetime
import repository_generator

class Client( pypi_builder.PackageGenerator ):

    _BASE_DICT = { "year_str": str(datetime.datetime.now().year) }

    def __init__( self, dict={} ):

        d = {}
        d.update( Client._BASE_DICT )
        d.update( dict )

        self.Package = kabbes_client.Package( pypi_builder._Dir, dict=d )
        cfg_pypi = self.Package.cfg
        cfg_repo_gen = repository_generator.Client().cfg

        cfg_repo_gen.merge( cfg_pypi )
        self.cfg = cfg_repo_gen

        self.cfg.print_atts()

        pypi_builder.PackageGenerator.__init__( self )

