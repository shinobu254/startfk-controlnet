import unittest
import numpy as np

import importlib
utils = importlib.import_module('extensions.sd-startfk-controlnet.tests.utils', 'utils')
utils.setup_test_env()

from annotator.openpose import encode_poses_as_json, PoseResult, Keypoint
from annotator.openpose.body import BodyResult

class TestEncodePosesAsJson(unittest.TestCase):
    def test_empty_list(self):
        poses = []
        canvas_height = 1080
        canvas_width = 1920
        result = encode_poses_as_json(poses, canvas_height, canvas_width)
        expected = {
            'people': [],
            'canvas_height': canvas_height,
            'canvas_width': canvas_width,
        }
        self.assertDictEqual(result, expected)

    def test_single_pose_no_keypoints(self):
        poses = [PoseResult(BodyResult(None, 0, 0), None, None, None)]
        canvas_height = 1080
        canvas_width = 1920
        result = encode_poses_as_json(poses, canvas_height, canvas_width)
        expected = {
            'people': [
                {
                    'pose_keypoints_2d': None,
                    'face_keypoints_2d': None,
                    'hand_left_keypoints_2d': None,
                    'hand_right_keypoints_2d': None,
                },
            ],
            'canvas_height': canvas_height,
            'canvas_width': canvas_width,
        }
        self.assertDictEqual(result, expected)

    def test_single_pose_with_keypoints(self):
        keypoints = [Keypoint(np.float32(0.5), np.float32(0.5)), None, Keypoint(0.6, 0.6)]
        poses = [PoseResult(BodyResult(keypoints, 0, 0), keypoints, keypoints, keypoints)]
        canvas_height = 1080
        canvas_width = 1920
        result = encode_poses_as_json(poses, canvas_height, canvas_width)
        expected = {
            'people': [
                {
                    'pose_keypoints_2d': [
                        0.5, 0.5, 1.0,
                        0.0, 0.0, 0.0,
                        0.6, 0.6, 1.0,
                    ],
                    'face_keypoints_2d': [
                        0.5, 0.5, 1.0,
                        0.0, 0.0, 0.0,
                        0.6, 0.6, 1.0,
                    ],
                    'hand_left_keypoints_2d': [
                        0.5, 0.5, 1.0,
                        0.0, 0.0, 0.0,
                        0.6, 0.6, 1.0,
                    ],
                    'hand_right_keypoints_2d': [
                        0.5, 0.5, 1.0,
                        0.0, 0.0, 0.0,
                        0.6, 0.6, 1.0,
                    ],
                },
            ],
            'canvas_height': canvas_height,
            'canvas_width': canvas_width,
        }
        self.assertDictEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
