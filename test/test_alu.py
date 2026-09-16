

# Work in progress

import cocotb
from cocotb.triggers import Timer
import random 

# Testing the "ADD" operation of the ALU.
@cocotb.test()
async def test_add(uut):
  
  uut._log.info("Testing the 'ADD' operation of the ALU.")
  uut._log.info("Test 1: Basic test: Adding two positive numbers.")

  # Defining the input values
  uut.rs1.value = random.randint(0,(2**32)-1)
  uut.rs2.value = random.randint(0,(2**32)-1)
  uut.alu_control.value = 0b0000  

  # wait 1ns for the signals to settle
  await Timer(1, units="ns")

  uut._log.info(f"Setting rs1 to {uut.rs1.value.to_unsigned()}")
  uut._log.info(f"Setting rs2 to {uut.rs2.value.to_unsigned()}")
  uut._log.info(f"Setting alu_control to {uut.alu_control.value.to_unsigned()}")

  rs1_value = uut.rs1.value.to_unsigned()
  rs2_value = uut.rs2.value.to_unsigned()
  rd_value  = uut.rd.value.to_unsigned()

  # Applying a AND mask for overflow cases.
  expected_result = (rs1_value + rs2_value) & 0xFFFFFFFF

  assert rd_value == expected_result, f"Test failed: Expected {expected_result}, got {rd_value}"

  uut._log.info(f"Test passed: {rs1_value} + {rs2_value} = {rd_value}")

  uut._log.info("*****************************************************************")

  # I'm not going to test adding one negative and one posotive number as that's just subtraction, right ?
  uut._log.info("Test 2: Adding two negative numbers.")

  uut.rs1.value = random.randint(-(2**31),-1)
  uut.rs2.value = random.randint(-(2**31),-1)
  uut.alu_control.value = 0b0000

  await Timer(1, units="ns")

  rs1_value = uut.rs1.value.to_signed()
  rs2_value = uut.rs2.value.to_signed()
  rd_value  = uut.rd.value.to_signed()
  uut._log.info(f"Setting rs1 to {uut.rs1.value.to_signed()}")
  uut._log.info(f"Setting rs2 to {uut.rs2.value.to_signed()}")
  uut._log.info(f"Setting alu_control to {uut.alu_control.value.to_signed()}")

  # Note to self: Investigate binary masks that work with negative numbers. Cannot apply AND mask here.
  expected_result = (rs1_value + rs2_value) 
  assert rd_value == expected_result, f"Test failed: Expected {expected_result}, got {rd_value}"

  uut._log.info(f"Test passed: {rs1_value} + {rs2_value} = {rd_value}")
  
  uut._log.info("*****************************************************************")

  uut._log.info("Test 3: Testing if it adds when alu_control is not set too ADD mode.")

  uut.rs1.value = 5
  uut.rs2.value = 10
  # Randomly chooses a mode that is not ADD (0b0000) to test if the ALU still performs addition.
  # 1,10 and not 1,9 to set the default case.
  uut.alu_control.value = random.randint(1,10)

  await Timer(1, units="ns")

  rs1_value = uut.rs1.value.to_unsigned()
  rs2_value = uut.rs2.value.to_unsigned()
  rd_value  = uut.rd.value.to_unsigned()

  uut._log.info(f"Setting rs1 to {uut.rs1.value.to_unsigned()}")
  uut._log.info(f"Setting rs2 to {uut.rs2.value.to_unsigned()}")
  uut._log.info(f"Setting alu_control to {uut.alu_control.value.to_unsigned()}")

  incorrect_result = (rs1_value + rs2_value) 
  assert incorrect_result != rd_value, f"Test failed: Addition should not occur here. {rs1_value} + {rs2_value} = {incorrect_result}, rd: {rd_value}"
  uut._log.info(f"Test passed: Addition did not occur when alu_control was set to {uut.alu_control.value.to_unsigned()}.")
  







