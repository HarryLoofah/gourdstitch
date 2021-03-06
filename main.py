#!/usr/bin/env python
#
# Copyright 2014 Greg Aitkenhead.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import webapp2

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    """Renders the root of the web-app using base.html as the template."""
    def get(self):
        """Create main web page."""
        template = env.get_template('base.html')
        self.response.write(template.render())

# class HomePage(webapp2.RequestHandler):
#     """Renders home page content."""
#     def get(self):
#         """Create home page."""
#         template = env.get_template('home.html')
#         self.response.write(template.render())

# class BlogPosts(webapp2.RequestHandler):
#     """Renders blog page."""
#     def get(self):
#         """Create blog page."""
#         template = env.get_template('blog.html')
#         self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
    # ('/home', HomePage),
    # ('/blog', BlogPosts),
], debug=False)
