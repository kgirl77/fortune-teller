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
fortunes = [
"A beautiful, smart, and loving person will be coming into your life.",
"A dubious friend may be an enemy in camouflage.",
"A feather in the hand is better than a bird in the air.",
"A fresh start will put you on your way."
]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('This is my main handler!')

class CountHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('This is my count handler!')

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(random.choice(fortunes))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/count', CountHandler),
    ('/fortune',FortuneHandler)




], debug=True)
