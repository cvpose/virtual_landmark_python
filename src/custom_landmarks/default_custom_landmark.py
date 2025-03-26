# Copyright 2024 cvpose
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
import numpy as np

from custom_landmarks.custom_landmark import CustomLandmark
from custom_landmarks.decorator import point



class DefaultCustomLandmark(CustomLandmark):
    @point("LEFT_RIB")
    def calc_left_rib(self):
        return self._middle(
            self._landmarks[self._plm.LEFT_HIP.value],
            self._landmarks[self._plm.LEFT_SHOULDER.value],
        )

    def _middle(self, p1, p2):
        p1 = np.array([p1.x, p1.y, p1.z])
        p2 = np.array([p2.x, p2.y, p2.z])
        return tuple((p1 + p2) / 2)