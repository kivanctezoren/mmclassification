* FIXME: A new model class is not recognized by the registry

```
Traceback (most recent call last):
  File "/home/kiwo/miniconda3/envs/open-mmlab/lib/python3.8/site-packages/mmcv/utils/registry.py", line 52, in build_from_cfg
    return obj_cls(**args)
  File "/home/kiwo/miniconda3/envs/open-mmlab/lib/python3.8/site-packages/mmcls/models/classifiers/image.py", line 30, in __init__
    self.backbone = build_backbone(backbone)
  File "/home/kiwo/miniconda3/envs/open-mmlab/lib/python3.8/site-packages/mmcls/models/builder.py", line 19, in build_backbone
    return BACKBONES.build(cfg)
  File "/home/kiwo/miniconda3/envs/open-mmlab/lib/python3.8/site-packages/mmcv/utils/registry.py", line 212, in build
    return self.build_func(*args, **kwargs, registry=self)
  File "/home/kiwo/miniconda3/envs/open-mmlab/lib/python3.8/site-packages/mmcv/cnn/builder.py", line 27, in build_model_from_cfg
    return build_from_cfg(cfg, registry, default_args)
  File "/home/kiwo/miniconda3/envs/open-mmlab/lib/python3.8/site-packages/mmcv/utils/registry.py", line 44, in build_from_cfg
    raise KeyError(
KeyError: 'ResNet32_Custom is not in the models registry'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "tools/train.py", line 181, in <module>
    main()
  File "tools/train.py", line 153, in main
    model = build_classifier(cfg.model)
  File "/home/kiwo/miniconda3/envs/open-mmlab/lib/python3.8/site-packages/mmcls/models/builder.py", line 38, in build_classifier
    return CLASSIFIERS.build(cfg)
  File "/home/kiwo/miniconda3/envs/open-mmlab/lib/python3.8/site-packages/mmcv/utils/registry.py", line 212, in build
    return self.build_func(*args, **kwargs, registry=self)
  File "/home/kiwo/miniconda3/envs/open-mmlab/lib/python3.8/site-packages/mmcv/cnn/builder.py", line 27, in build_model_from_cfg
    return build_from_cfg(cfg, registry, default_args)
  File "/home/kiwo/miniconda3/envs/open-mmlab/lib/python3.8/site-packages/mmcv/utils/registry.py", line 55, in build_from_cfg
    raise type(e)(f'{obj_cls.__name__}: {e}')
KeyError: "ImageClassifier: 'ResNet32_Custom is not in the models registry'"

```
