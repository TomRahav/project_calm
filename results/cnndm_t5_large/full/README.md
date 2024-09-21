---
library_name: transformers
base_model: ./save/cnndm_t5_large
tags:
- generated_from_trainer
datasets:
- cnn_dailymail
model-index:
- name: full
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# full

This model is a fine-tuned version of [./save/cnndm_t5_large](https://huggingface.co/./save/cnndm_t5_large) on the cnn_dailymail 3.0.0 dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- num_devices: 2
- total_train_batch_size: 16
- total_eval_batch_size: 2
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.1+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1
