# Copyright (c) OpenMMLab. All rights reserved.
from .alexnet import AlexNet
from .lenet import LeNet5
from .mobilenet_v2 import MobileNetV2
from .mobilenet_v3 import MobileNetV3
from .regnet import RegNet
from .repvgg import RepVGG
from .res2net import Res2Net
from .resnet32_custom import ResNet32_Custom
from .resnest import ResNeSt
from .resnet import ResNet, ResNetV1d
from .resnet_cifar import ResNet_CIFAR
from .resnext import ResNeXt
from .seresnet import SEResNet
from .seresnext import SEResNeXt
from .shufflenet_v1 import ShuffleNetV1
from .shufflenet_v2 import ShuffleNetV2
from .swin_transformer import SwinTransformer
from .t2t_vit import T2T_ViT
from .timm_backbone import TIMMBackbone
from .tnt import TNT
from .vgg import VGG
from .vision_transformer import VisionTransformer

__all__ = [
    'LeNet5', 'AlexNet', 'VGG', 'RegNet', 'ResNet', 'ResNet32_Custom',
    'ResNeXt', 'ResNetV1d', 'ResNeSt', 'ResNet_CIFAR', 'SEResNet',
    'SEResNeXt', 'ShuffleNetV1', 'ShuffleNetV2', 'MobileNetV2',
    'MobileNetV3', 'VisionTransformer', 'SwinTransformer', 'TNT',
    'TIMMBackbone', 'T2T_ViT', 'Res2Net', 'RepVGG'
]
