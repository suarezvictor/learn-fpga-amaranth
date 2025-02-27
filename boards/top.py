from amaranth import *

import sys

class Top(Elaboratable):
    def __init__(self, leds, uart):
        if len(sys.argv) == 1:
            print("Usage: {} step_number".format(sys.argv[0]))
            exit(1)
        step = int(sys.argv[1])
        print("step = {}".format(step))
        self.leds = leds
        self.uart = uart

        # TODO: this is messy and should be done with iterating over dirs
        if step == 1:
            path = "01_blink"
        elif step == 2:
            path = "02_slower_blinky"
        elif step == 3:
            path = "03_blink_from_rom"
        elif step == 4:
            path = "04_instruction_decoder"
        elif step == 5:
            path = "05_register_bank"
        elif step == 6:
            path = "06_alu"
        elif step == 7:
            path = "07_assembler"
        elif step == 8:
            path = "08_jumps"
        elif step == 9:
            path = "09_branches"
        elif step == 10:
            path = "10_lui_auipc"
        elif step == 11:
            path = "11_modules"
        elif step == 12:
            path = "12_size_optimisation"
        elif step == 13:
            path = "13_subroutines"
        elif step == 14:
            path = "14_subroutines_v2"
        elif step == 15:
            path = "15_load"
        elif step == 16:
            path = "16_store"
        elif step == 17:
            path = "17_memory_map"
        elif step == 18:
            path = "18_mandelbrot"
        else:
            print("Invalid step_number {}.".format(step))
            exit(1)
        sys.path = [path] + sys.path #give priority to projects, to avoid global "soc" packages
        from soc import SOC
        self.soc = SOC()

    def elaborate(self, platform):
        m = Module()
        soc = self.soc
        leds = self.leds
        uart = self.uart
        m.submodules.soc = soc

        # We connect the SOC leds signal to the various LEDs on the board.
        m.d.comb += [
            leds[0].o.eq(soc.leds[0]),
            leds[1].o.eq(soc.leds[1]),
            leds[2].o.eq(soc.leds[2]),
            leds[3].o.eq(soc.leds[3]),
            leds[4].o.eq(soc.leds[4]),
        ]

        # The TX port is added only later to the SOC
        if hasattr(soc, "tx"):
            m.d.comb += [
                uart.tx.eq(soc.tx)
            ]

        return m
