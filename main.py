#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
import webapp2
import random
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

fortunes = [
"A beautiful, smart, and loving person will be coming into your life.",
"A dubious friend may be an enemy in camouflage.",
"A feather in the hand is better than a bird in the air.",
"A fresh start will put you on your way."
]
users_fav_num = 3
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('This is my main handler!')


class CountHandler(webapp2.RequestHandler):
        #count_welcome ={"user_num" : users_fav_num}
    def get(self):
        count_welcome = JINJA_ENVIRONMENT.get_template("/templates/number-start.html")
        self.response.write(count_welcome.render())

    def post(self):
        count_template = JINJA_ENVIRONMENT.get_template("/templates/number.html")
        users_fav_num = self.request.get ('my_num')
        self.response.write(count_template.render({'user_num' : users_fav_num}))

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        fortune_page = JINJA_ENVIRONMENT.get_template("templates/fortune-start.html")
        self.response.write(fortune_page.render({"user_name":"Kristie" ,"user_location":"Atlanta"}))

    def post(self):
        name=self.request.get('name')
        location=self.request.get('location')
        template= JINJA_ENVIRONMENT.get_template("/templates/fortune.html")
        self.response.write(template.render({'name' : name, 'location' : location}))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/count', CountHandler),
    ('/fortune',FortuneHandler)





], debug=True)
