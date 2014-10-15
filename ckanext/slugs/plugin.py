import logging

from routes.mapper import SubMapper
from ckan.lib.plugins import DefaultGroupForm

import ckan.plugins as p

log = logging.getLogger(__name__)


class OrganizationSlug(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IRoutes, inherit=True)


    def update_config(self, config):
        pass

    def before_map(self, map):
        map.redirect('/group/{url:.*}', '/institucion/{url}', _redirect_code='301 Moved Permanently')
        map.redirect('/group', '/institucion', _redirect_code='301 Moved Permanently')
        map.redirect('/organization/{url:.*}', '/institucion/{url}', _redirect_code='301 Moved Permanently')
        map.redirect('/organization', '/institucion', _redirect_code='301 Moved Permanently')
        map.redirect('/instituciones', '/institucion')
        map.redirect('/instituciones/{url:.*}', '/institucion/{url}')

        org_controller = 'ckan.controllers.organization:OrganizationController'
        with SubMapper(map, controller=org_controller) as m:
            m.connect('instituciones_index', '/institucion', action='index')
            m.connect('/institucion/list', action='list')
            m.connect('/institucion/new', action='new')
            m.connect('/institucion/{action}/{id}',
                      requirements=dict(action='|'.join([
                          'delete',
                          'admins',
                          'member_new',
                          'member_delete',
                          'history'
                      ])))
            m.connect('institucion_activity', '/institucion/activity/{id}', action='activity', ckan_icon='time')
            m.connect('institucion_read', '/institucion/{id}', action='read')
            m.connect('institucion_about', '/institucion/about/{id}', action='about', ckan_icon='info-sign')
            m.connect('institucion_read', '/institucion/{id}', action='read', ckan_icon='sitemap')
            m.connect('institucion_edit', '/institucion/edit/{id}', action='edit', ckan_icon='edit')
            m.connect('institucion_members', '/institucion/edit_members/{id}', action='members', ckan_icon='group')
            m.connect('institucion_bulk_process', '/institucion/bulk_process/{id}', action='bulk_process', ckan_icon='sitemap')
        map.redirect('/api/{ver:1|2|3}/rest/institucion', '/api/{ver}/rest/group')
        map.redirect('/api/rest/institucion', '/api/rest/group')
        map.redirect('/api/{ver:1|2|3}/rest/institucion/{url:.*}', '/api/{ver}/rest/group/{url:.*}')
        map.redirect('/api/rest/institucion/{url:.*}', '/api/rest/group/{url:.*}')
        map.connect('institucion_members_read', '/institucion/members/{id}', controller='ckanext.slugs.controllers.customslug:SlugController', 
                    action='members_read', ckan_icon='group')
        return map

