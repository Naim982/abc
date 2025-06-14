# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from ultralytics.models.yolo import detect

from .model import YOLO, YOLOE, YOLOWorld

__all__ = "detect", "YOLO", "YOLOWorld", "YOLOE"
