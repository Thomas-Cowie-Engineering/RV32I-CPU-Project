
# This is a work in progress and is not complete.

import cocotb
from random import randint
from cocotb.triggers import Timer


@cocotb.test()
async def test_ALU_combinational(uut):
  # set random input values
  uut.A.value = randint(0,2147483647)
  uut._log.info(f"Setting A to {uut.A.value}")

  uut.B.value = randint(0,2147483647)
  uut._log.info(f"Setting B to {uut.B.value}")

  uut.ALUControl.value = randint(0,7)
  uut._log.info(f"Setting ALUControl to {uut.ALUControl.value}")

  await Timer(randint(1,10), unit="ns")
  
  # TODO - add checks for expected output values

  uut._log.info("Test Complete!")