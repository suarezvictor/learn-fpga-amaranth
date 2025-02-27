## learn-fpga (Amaranth HDL version)

This repository contains code to follow the excellent learn-fpga tutorial by Bruno Levy [from blinker to RISC-V](https://github.com/BrunoLevy/learn-fpga/blob/master/FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV/README.md) using [Amaranth HDL](https://github.com/amaranth-lang/amaranth) instead of Verilog.

The tutorial starts from a very simple 'blink' example and will end with a fully functional RISC-V CPU core.

This code repository is only meant as a supplement to Bruno Levy's main repository. There are very few explanations in this repository that go beyond explaining certain aspects of Amaranth HDL. Please refer to the main tutorial for detailed information of every step of the implementation.

Using Amaranth HDL the code can certainly be simplified / restructured, but the aim of this project is to keep close to the original.


### Board support

Support for the following boards is included:

* Digilent Arty A7
* Digilent CMOD A7
* Digilent CMOD S7 (untested)

If you don't have a board, you can still run the code in the Amaranth Python simulator.


### Toolchain

Amaranth HDL supports the following toolchains for the boards:

* AMD/Xilinx Vivado, proprietary
* F4PGA (former Symbiflow), using FLOSS tools (Yosys, Nextpnr)


### Running the simulation

Each directory contains a `bench.py` file. This contains a test bench for the simulator. Run it like so:

```
source env.sh        # Add directories to Python library path
cd 01_blink
python bench.py
```


### Building a firmware bitfile

The platform specific code is in the `boards` directory. To build e.g. step 5 for the Arty A7 board:

```
source env.sh        # Add directories to Python library path
python boards/digilent_arty_a7.py 5
```


### RISC-V assembler

This repository also contains a (minimal) RISC-V assembler written in Python in the `tools` directory.


### UART connection

Due to deviation of the internal oscillator frequency from the nominal value it is possible that the UART baudrate is not exactly the same as what is set in the code (by default 1 MBaud). In this case it helps to vary the receiver baudrate by +- 20% and check if reception works. If an oscilloscope is available, you can also measure the clock frequency by patching out the clock signal to one of the pins and measuring the signal period.


### Licensing

See the LICENSE file in the repository.


### Author

* *Bastian Löher (bl0x)*
