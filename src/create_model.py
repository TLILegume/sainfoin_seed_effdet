from effdet.config.model_config import efficientdet_model_param_dict
from effdet import get_efficientdet_config, EfficientDet, DetBenchTrain
from effdet.efficientdet import HeadNet

def create_model(num_classes, image_size: int, architecture: str="tf_efficientnetv2_l"):
    efficientdet_model_param_dict[architecture] = dict(
        name=architecture,
        backbone_name=architecture,
        backbone_args=dict(drop_path_rate=0.2),
        num_classes=num_classes,
        url='',
    )

    config = get_efficientdet_config(architecture)
    config.update(
        {
            'num_classes': num_classes,
            'image_size': (image_size, image_size)
        }
    )

    net = EfficientDet(config, pretrained_backbone=True)
    net.class_net = HeadNet(
        config,
        num_outputs=config.num_classes
    )

    return DetBenchTrain(net, config)

x = create_model(num_classes=3, image_size=1024)
print(x)
