# Fork of [pytorch-yolo2](https://github.com/ayooshkathuria/pytorch-yolo2)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.5. (🔥)
* Original pretrained models and converted ONNX models from GitHub [releases page](https://github.com/clibdev/pytorch-yolo2/releases). (🔥)
* Installation with [requirements.txt](requirements.txt) file.
* The following deprecations and errors has been fixed:
  * RuntimeError: The size of tensor a (3) must match the size of tensor b (864) at non-singleton dimension 3.
  * RuntimeError: output with shape [425, 1024, 1, 1] doesn't match the broadcast shape [425, 1024, 1, 435200].
  * TypeError: conv2d() received an invalid combination of arguments.
  * TypeError: view(): argument 'size' failed to unpack the object.
  * UserWarning: Implicit dimension choice for softmax has been deprecated.
  * UserWarning: TypedStorage is deprecated.

# Installation

```shell
pip install -r requirements.txt
```

# Pretrained models

* Download links:

| Name   | Model Size (MB) | Link                                                                                                                                                                                 | SHA-256                                                                                                                              |
|--------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| YOLOv2 | 194.5<br>194.4  | [Darknet](https://github.com/clibdev/pytorch-yolo2/releases/latest/download/yolov2.weights)<br>[ONNX](https://github.com/clibdev/pytorch-yolo2/releases/latest/download/yolov2.onnx) | d9945162ed6f54ce1a901e3ec537bdba4d572ecae7873087bd730e5a7942df3f<br>64ac7f7763f53a8293985cab833442f6b936849815114fa86ef7218c51585ffb |

# Inference

```shell
python detect.py cfg/yolo.cfg yolov2.weights data/dog.jpg
```

# Export to ONNX format

```shell
pip install onnx
```
```shell
python export.py --cfg cfg/yolo.cfg --weights yolov2.weights
```
