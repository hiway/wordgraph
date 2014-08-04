# Copyright 2014 Tennessee Leeuwenburg

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from wordgraph.points import Point

EPOCH_START = 1407109280

def time_values(values, start=EPOCH_START, increment=1):
    datapoints = []
    for index, value in enumerate(values):
        datapoints.append(Point(x=value, y=start + (increment * index)))
    return datapoints
