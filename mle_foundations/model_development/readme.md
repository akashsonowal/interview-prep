## Experiment Tracking and Versioning

## Distributed Training

1. Data Parallelsim

    - Synchronous
    - Asynchonous
   
   Model fits into one gpu but data can't. PyTorch DataParallel and Horovord are good libraries.
  
2. Model Parallelism

   Pipeline parallelsim is more clever technique of model parallelism that utilies the concept of micro-batch. 
   
Note:

If model is too big and can't fit into a single node. We can shard the model. There are three techniques: FSDP (Fully Sharded Data Parallel). Libraries: PyTorch FSDP, Facebook Fairscale, Microsoft DeepSpeed. The other is pipelined model parallelsim. The third is tensor parallelsim (distribute matrix over multiple GPUs: Nvidia Megatron LM).

RPC is a communcation framework that makes distributed training fast.
  
## AutoML
