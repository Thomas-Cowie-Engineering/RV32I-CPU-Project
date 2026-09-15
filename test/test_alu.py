

# Work in progress, very much incomplete !
import cocotb
from random import randint
from cocotb.triggers import Timer

@cocotb.test()
async def test_ALU_combinational(uut):
  # set random input values
  uut.rs1.value = randint(0,2147483647)
  uut._log.info(f"Setting rs1 to {uut.rs1.value}")

  uut.rs2.value = randint(0,2147483647)
  uut._log.info(f"Setting rs2 to {uut.rs2.value}")

  uut.alu_control.value = randint(0,7)
  uut._log.info(f"Setting alu_control to {uut.alu_control.value}")

  await Timer(randint(1,10), unit="ns")
  
  # TODO - add checks for expected output values

  uut._log.info("Test Complete!")