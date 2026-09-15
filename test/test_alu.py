# Work in progress
import cocotb
from random import randint
from cocotb.triggers import Timer



# Testing the "ADD" operation of the ALU.
@cocotb.test()
async def test_add(uut):
  
  uut._log.info("Testing the 'ADD' operation of the ALU.")
  uut._log.info("Test 1: Basic test: Adding two positive numbers.")

  # Defining the input values
  uut.rs1.value = 100
  uut.rs2.value = 200
  uut.alu_control.value = 0b0000  

  # wait 1ns for the signals to settle
  await Timer(1, unit="ns")

  uut._log.info(f"Setting rs1 to {uut.rs1.value.to_unsigned()}")
  uut._log.info(f"Setting rs2 to {uut.rs2.value.to_unsigned()}")
  uut._log.info(f"Setting alu_control to {uut.alu_control.value.to_unsigned()}")


  rs1_value = uut.rs1.value.to_unsigned()
  rs2_value = uut.rs2.value.to_unsigned()
  rd_value  = uut.rd.value.to_unsigned()

  expected_result = rs1_value + rs2_value
  assert rd_value == expected_result, f"Test failed: Expected {expected_result}, got {rd_value}"

  uut._log.info(f"Test passed: {rs1_value} + {rs2_value} = {rd_value}")

