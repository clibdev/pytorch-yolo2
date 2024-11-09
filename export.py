import argparse
import os
import torch
from darknet import Darknet


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--weights', type=str, default='./yolov2.weights', help='Weights path')
    parser.add_argument('--cfg', type=str, default='./cfg/yolo.cfg', help='Model configuration path')
    parser.add_argument('--device', default='cpu', type=str, help='cuda:0 or cpu')
    args = parser.parse_args()

    if not os.path.exists(args.weights):
        print('Cannot find weights: {0}'.format(args.weights))
        exit()
    if not os.path.exists(args.cfg):
        print('Cannot find model configuration: {0}'.format(args.cfg))
        exit()

    model = Darknet(args.cfg)
    model.load_weights(args.weights)

    model_path = os.path.splitext(args.weights)[0] + '.onnx'

    dummy_input = torch.randn(1, 3, 416, 416).to(args.device)
    torch.onnx.export(
        model,
        dummy_input,
        model_path,
        verbose=False,
        input_names=['input'],
        output_names=['output'],
        opset_version=18
    )
