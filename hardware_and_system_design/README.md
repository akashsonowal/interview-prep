# Computer Hardware

## Computers
- A processor (CPU): execute the program we give (in addition to running the OS and many more things), typically consists of 8 or more cores.
- Memory (RAM): To store and retrieve the results from computation. (weight vectors, activations, training data)
- An Ethernet Network connection (sometimes multiples): speed 1 GB/s to 100 GB/s.
- A speed expansion bus to connect system to one or more GPUs (PCIe): servers have upto 8 accelerators (GPUs). Desktop has 2.
- Durable Storage (magnetic Hard Disk Drive, Solid State Drive) in many cases connected using PCIe bus.It provides efficient transfer of training data and storage of checkpoints.

![computer](http://d2l.ai/_images/mobo-symbol.svg)

Network, GPU, storage are connected to CPU by PCIe bus. It consists of mulitple lanes.The data transfer happens at 100 GB/s.

## Memory
DDR4 variety (20-25 GB/s per module) for CPU

GPU Memory has even more bandwidth requirements. NVIDIA RTX 2080 Ti has 352-bit wide bus.

Consumer grade NVIDIA RTX and Titan series use GDDR6 chips with over 500 GB/s aggregate bandwidth.

High end server: Nvidia Volta V100.
The key features are bandwidth and latency.

## Storage
HDD: High end 16TB with 9 platters.



