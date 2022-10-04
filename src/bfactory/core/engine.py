#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
from bfactory.core import tasks 
from bfactory.inputs.manifest import Manifest
from bfactory.config.settings import TITLE_BANNER
from bfactory.utils.render import render_to_file
from bfactory.utils.paths import Paths

fpaths = Paths()


class Engine():
    """
        Se encarga de crear el esqueleto del codigo fuente de la API
        Necesita conocer un manifiesto ya verificado.
    """

    def __init__(self,  manifest: Manifest, force: bool = False ):
        """
            El objeto Manifiesto se encuentra validado
            el path es donde el engine va a trabajar.
        """
        self.manifest = manifest
    
    def create_api(self) -> bool:

        self._clonar_proyecto()

        os.chdir(fpaths.base_path)

        self._create_readme()

        self._configurar_proyecto()
        
        self._create_models()

        self._create_admin()

        self._create_selectors()
        
        self._create_services()
        
        self._create_views()

        self._create_urls()
        
        return True 



    def __str__(self) -> str:
        return "bfactory Engine"


    def _create_admin(self) -> None:
        values = {
            'models':self.manifest.get_models(),
        } 

        path_models = fpaths.path_file_from_app_api('admin.py')

        render_to_file(template='admin.py', file_name=path_models, values=values)
 

    def _clonar_proyecto(self) -> None:
        
        fpaths.mk_and_ch_dir(fpaths.base_path)

        tasks.get_zip_base_project(slug=self.manifest.app_slug, path=fpaths.base_path)


    def _create_services(self) -> None:
        values = {
            'models':self.manifest.get_models(),
        } 

        path_services = fpaths.path_file_from_app_api('services.py')

        render_to_file(template='services.py', file_name=path_services, values=values)


    def _create_models(self) -> None:
        values = {
            'models':self.manifest.get_models(),
        } 

        path_models = fpaths.path_file_from_app_api('models.py')

        render_to_file(template='models.py', file_name=path_models, values=values)



    def _create_selectors(self) -> None:
        values = {
            'models':self.manifest.get_models(),
        } 

        path_models = fpaths.path_file_from_app_api('selectors.py')

        render_to_file(template='selectors.py', file_name=path_models, values=values)




    def _create_views(self) -> None:
        values = {
            'models':self.manifest.get_models(),
        } 

        path_models = fpaths.path_file_from_app_api('views.py')

        render_to_file(template='views.py', file_name=path_models, values=values)



    def _create_urls(self) -> None:
        values = {
            'models':self.manifest.get_models(),
        } 

        path_models = fpaths.path_file_from_app_api('urls.py')

        render_to_file(template='urls.py', file_name=path_models, values=values)



    def _create_readme(self) -> None:
        values = {
            'banner':TITLE_BANNER,
            'app_name':self.manifest.app_name,
            'app_version':self.manifest.app_version
        }

        path_readme =  fpaths.path_file_from_project('READ.ME')

        render_to_file(template='READ.ME', file_name=path_readme, values=values)


    def _configurar_proyecto(self) -> None:
        """
            Crea el archivo myconf.py
        """
        tasks.crear_configuracion_del_proyecto(manifest = self.manifest)


