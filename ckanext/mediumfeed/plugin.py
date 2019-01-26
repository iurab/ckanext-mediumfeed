import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class MediumfeedPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)


    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'mediumfeed')

    # ITemplateHelpers
    def get_helpers(self):
        '''
        TODO:
            Request Route: GET https://api.medium.com/v1/users/{{userId}}/publications
            Python Client: https://github.com/Medium/medium-sdk-python
        '''
        publications =  {
            "data": [
                {
                    "id": "b969ac62a46b",
                    "name": "About Medium",
                    "description": "What is this thing and how does it work?",
                    "url": "https://medium.com/about",
                    "imageUrl": "https://cdn-images-1.medium.com/fit/c/200/200/0*ae1jbP_od0W6EulE.jpeg"
                },
                {
                    "id": "b45573563f5a",
                    "name": "Developers",
                    "description": "Mediums Developer resources",
                    "url": "https://medium.com/developers",
                    "imageUrl": "https://cdn-images-1.medium.com/fit/c/200/200/1*ccokMT4VXmDDO1EoQQHkzg@2x.png"
                }
            ]
        }
        return {
            'medium_publications': publications['data']
        }