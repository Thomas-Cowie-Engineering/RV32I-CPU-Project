

# Work in progress

# Testing the ALU using cocotb as cocotb enables more rigorous testing than conventional test benches.

import cocotb
from cocotb.triggers import Timer
from cocotb.types import LogicArray   
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


# Errors with rd that I need to investigate.
# Perhaps an overflow/underflow error.
"""
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
"""

  # Need to figure out a new way of how to test this.
  # 5+10 = 15. This arithmetic result can be achieved by other operations as well.
  # Therefore, my current way of testing this does not work for every case.
  # will revist at a later date.
"""
  uut._log.info("Test 3: Testing if it adds when alu_control is not set too ADD mode.")

  uut.rs1.value = 5
  uut.rs2.value = 10
  # Randomly chooses a mode that is not ADD (0b0000) to test if the ALU still performs addition.
  # 1,15 and not 1,9 to test the default case.
  uut.alu_control.value = random.randint(1,15)
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
  """



# Testing the "SUB" operation of the ALU.
@cocotb.test()
async def test_sub(uut):



    uut._log.info("Testing the 'SUB' operation of the ALU.")
    uut._log.info("Test 1: Subtracting one number from another.")

    # Defining the input values
    uut.rs1.value = random.randint(0, (2**32)-1)
    uut.rs2.value = random.randint(0, (2**32)-1)
    uut.alu_control.value = 0b0001  #Activate sub mode

    # wait 1ns for the signals to settle
    await Timer(1, units="ns")

    uut._log.info(f"Setting rs1 to {uut.rs1.value.to_unsigned()}")
    uut._log.info(f"Setting rs2 to {uut.rs2.value.to_unsigned()}")
    uut._log.info(f"Setting alu_control to {uut.alu_control.value.to_unsigned()}")

    rs1_value = uut.rs1.value.to_unsigned()
    rs2_value = uut.rs2.value.to_unsigned()
    rd_value  = uut.rd.value.to_unsigned()

    # Applying an AND mask for overflow/underflow cases.
    expected_result = (rs1_value - rs2_value) & 0xFFFFFFFF

    assert rd_value == expected_result, f"Test failed: Expected {expected_result}, got {rd_value}"

    uut._log.info(f"Test passed: {rs1_value} - {rs2_value} = {rd_value}")

    uut._log.info("*****************************************************************")




# Testing the "XOR" operation of the ALU.
@cocotb.test()
async def test_XOR(uut):

    uut._log.info("Testing the 'XOR' operation of the ALU.")
    uut._log.info("Test 1: Performing XOR operation on two positive numbers.")

    # Defining the input values
    uut.rs1.value = random.randint(0, (2**32)-1)
    uut.rs2.value = random.randint(0, (2**32)-1)
    uut.alu_control.value = 0b0010  #Activate XOR mode

    # wait 1ns for the signals to settle
    await Timer(1, units="ns")

    uut._log.info(f"Setting rs1 to {uut.rs1.value.to_unsigned()}")
    uut._log.info(f"Setting rs2 to {uut.rs2.value.to_unsigned()}")
    uut._log.info(f"Setting alu_control to {uut.alu_control.value.to_unsigned()}")

    rs1_value = uut.rs1.value.to_unsigned()
    rs2_value = uut.rs2.value.to_unsigned()
    rd_value  = uut.rd.value.to_unsigned()

    expected_result = (rs1_value ^ rs2_value)
    assert rd_value == expected_result, f"Test failed: Expected {expected_result}, got {rd_value}"

    uut._log.info(f"Test passed: {rs1_value} ^ {rs2_value} = {rd_value}")
    uut._log.info(f"Test passed: {rs1_value:032b} ^ {rs2_value:032b} = {rd_value:032b}")

    uut._log.info("*****************************************************************")

    uut._log.info("Test 2: Performing XOR operation on two negative numbers.")

    # Defining the input values
    uut.rs1.value = random.randint(-(2**31),-1)
    uut.rs2.value = random.randint(-(2**31),-1)
    uut.alu_control.value = 0b0010  #Activate XOR mode

    # wait 1ns for the signals to settle
    await Timer(1, units="ns")

    uut._log.info(f"Setting rs1 to {uut.rs1.value.to_signed()}")
    uut._log.info(f"Setting rs2 to {uut.rs2.value.to_signed()}")
    uut._log.info(f"Setting alu_control to {uut.alu_control.value.to_unsigned()}")

    rs1_value = uut.rs1.value.to_signed()
    rs2_value = uut.rs2.value.to_signed()
    rd_value  = uut.rd.value.to_signed()

    expected_result = (rs1_value ^ rs2_value)
    assert rd_value == expected_result, f"Test failed: Expected {expected_result}, got {rd_value}"  

    uut._log.info(f"Test passed: {rs1_value} ^ {rs2_value} = {rd_value}")





# Testing the "OR" operation of the ALU.
@cocotb.test()
async def test_OR(uut):

    uut._log.info("Testing the 'OR' operation of the ALU.")
    uut._log.info("Test 1: Performing OR operation on two positive numbers.")

    # Defining the input values
    uut.rs1.value = random.randint(0, (2**32)-1)
    uut.rs2.value = random.randint(0, (2**32)-1)
    uut.alu_control.value = 0b0011  #Activate OR mode

    # wait 1ns for the signals to settle
    await Timer(1, units="ns")

    uut._log.info(f"Setting rs1 to {uut.rs1.value.to_unsigned()}")
    uut._log.info(f"Setting rs2 to {uut.rs2.value.to_unsigned()}")
    uut._log.info(f"Setting alu_control to {uut.alu_control.value.to_unsigned()}")

    rs1_value = uut.rs1.value.to_unsigned()
    rs2_value = uut.rs2.value.to_unsigned()
    rd_value  = uut.rd.value.to_unsigned()

    expected_result = (rs1_value | rs2_value)
    assert rd_value == expected_result, f"Test failed: Expected {expected_result}, got {rd_value}"

    uut._log.info(f"Test passed: {rs1_value} | {rs2_value} = {rd_value}")
    uut._log.info(f"Test passed: {rs1_value:032b} | {rs2_value:032b} = {rd_value:032b}")

    uut._log.info("*****************************************************************")

    uut._log.info("Test 2: Performing OR operation on two negative numbers.")

    # Defining the input values
    uut.rs1.value = random.randint(-(2**31),-1)
    uut.rs2.value = random.randint(-(2**31),-1)
    uut.alu_control.value = 0b0011  #Activate OR mode

    # wait 1ns for the signals to settle
    await Timer(1, units="ns")

    uut._log.info(f"Setting rs1 to {uut.rs1.value.to_signed()}")
    uut._log.info(f"Setting rs2 to {uut.rs2.value.to_signed()}")
    uut._log.info(f"Setting alu_control to {uut.alu_control.value.to_unsigned()}")

    rs1_value = uut.rs1.value.to_signed()
    rs2_value = uut.rs2.value.to_signed()
    rd_value  = uut.rd.value.to_signed()

    expected_result = (rs1_value | rs2_value)
    assert rd_value == expected_result, f"Test failed: Expected {expected_result}, got {rd_value}"  

    uut._log.info(f"Test passed: {rs1_value} | {rs2_value} = {rd_value}")




# Testing the "AND" operation of the ALU.
@cocotb.test()
async def test_AND(uut):

    uut._log.info("Testing the 'AND' operation of the ALU.")
    uut._log.info("Test 1: Performing AND operation on two positive numbers.")

    # Defining the input values
    uut.rs1.value = random.randint(0, (2**32)-1)
    uut.rs2.value = random.randint(0, (2**32)-1)
    uut.alu_control.value = 0b0100 #Activate AND mode

    # wait 1ns for the signals to settle
    await Timer(1, units="ns")

    uut._log.info(f"Setting rs1 to {uut.rs1.value.to_unsigned()}")
    uut._log.info(f"Setting rs2 to {uut.rs2.value.to_unsigned()}")
    uut._log.info(f"Setting alu_control to {uut.alu_control.value.to_unsigned()}")

    rs1_value = uut.rs1.value.to_unsigned()
    rs2_value = uut.rs2.value.to_unsigned()
    rd_value  = uut.rd.value.to_unsigned()

    expected_result = (rs1_value & rs2_value)
    assert rd_value == expected_result, f"Test failed: Expected {expected_result}, got {rd_value}"

    uut._log.info(f"Test passed: {rs1_value} & {rs2_value} = {rd_value}")
    uut._log.info(f"Test passed: {rs1_value:032b} & {rs2_value:032b} = {rd_value:032b}")

    uut._log.info("*****************************************************************")

    uut._log.info("Test 2: Performing AND operation on two negative numbers.")

    # Defining the input values
    uut.rs1.value = random.randint(-(2**31),-1)
    uut.rs2.value = random.randint(-(2**31),-1)
    uut.alu_control.value = 0b0100 #Activate AND mode

    # wait 1ns for the signals to settle
    await Timer(1, units="ns")

    uut._log.info(f"Setting rs1 to {uut.rs1.value.to_signed()}")
    uut._log.info(f"Setting rs2 to {uut.rs2.value.to_signed()}")
    uut._log.info(f"Setting alu_control to {uut.alu_control.value.to_unsigned()}")

    rs1_value = uut.rs1.value.to_signed()
    rs2_value = uut.rs2.value.to_signed()
    rd_value  = uut.rd.value.to_signed()

    expected_result = (rs1_value & rs2_value)
    assert rd_value == expected_result, f"Test failed: Expected {expected_result}, got {rd_value}"  

    uut._log.info(f"Test passed: {rs1_value} & {rs2_value} = {rd_value}")



# Testing the "SLL" operation of the ALU.
@cocotb.test()
async def test_SLL(uut):

    uut._log.info("Testing the 'SLL' operation of the ALU.")
    uut._log.info("Test 1: Performing SLL operation on two positive numbers.")

    # Defining the input values
    uut.rs1.value = random.randint(0, (2**32)-1)
    uut.rs2.value = random.randint(0, (2**32)-1)
    uut.alu_control.value = 0b0101 #Activate SLL mode

    # wait 1ns for the signals to settle
    await Timer(1, units="ns")

    rs1_value = uut.rs1.value.to_unsigned()
    rs2_value = uut.rs2.value.to_unsigned()
    rs2_lower_5_bits = int(LogicArray(uut.rs2.value)[4:0])  # rs2[4:0]
    uut._log.info(f"Setting rs1 to {uut.rs1.value.to_unsigned()}")
    uut._log.info(f"Setting rs2 to {uut.rs2.value.to_unsigned()}")
    uut._log.info(f"Setting alu_control to {uut.alu_control.value.to_unsigned()}")
    uut._log.info(f"Setting rs2 lower 5 bits are to {rs2_lower_5_bits}")
    rd_value  = uut.rd.value.to_unsigned()

    expected_result = (rs1_value << rs2_lower_5_bits) & 0xFFFFFFFF
    assert rd_value == expected_result, f"Test failed: Expected {expected_result}, got {rd_value}"

    uut._log.info(f"Test passed: {rs1_value} << {rs2_lower_5_bits} = {rd_value}")

    uut._log.info("*****************************************************************")

# Testing the "SRL" operation of the ALU.
@cocotb.test()
async def test_SRL(uut):

    uut._log.info("Testing the 'SRL' operation of the ALU.")
    uut._log.info("Test 1: Performing SRL operation on two positive numbers.")

    # Defining the input values
    uut.rs1.value = random.randint(0, (2**32)-1)
    uut.rs2.value = random.randint(0, (2**32)-1)
    uut.alu_control.value = 0b0110 #Activate SRL mode

    # wait 1ns for the signals to settle
    await Timer(1, units="ns")

    rs1_value = uut.rs1.value.to_unsigned()
    rs2_value = uut.rs2.value.to_unsigned()
    rs2_lower_5_bits = int(LogicArray(uut.rs2.value)[4:0])  # rs2[4:0]
    uut._log.info(f"Setting rs1 to {uut.rs1.value.to_unsigned()}")
    uut._log.info(f"Setting rs2 to {uut.rs2.value.to_unsigned()}")
    uut._log.info(f"Setting alu_control to {uut.alu_control.value.to_unsigned()}")
    uut._log.info(f"Setting rs2 lower 5 bits are to {rs2_lower_5_bits}")
    rd_value  = uut.rd.value.to_unsigned()

    expected_result = (rs1_value >> rs2_lower_5_bits) & 0xFFFFFFFF
    assert rd_value == expected_result, f"Test failed: Expected {expected_result}, got {rd_value}"

    uut._log.info(f"Test passed: {rs1_value} >> {rs2_lower_5_bits} = {rd_value}")

    uut._log.info("*****************************************************************")



# Testing the "SRA" operation of the ALU.
@cocotb.test()
async def test_SRA(uut):

    uut._log.info("Testing the 'SRA' operation of the ALU.")
    uut._log.info("Test 1: Performing SRA operation")

    # Defining the input values
    uut.rs1.value = random.randint(-(2**31), -1)
    uut.rs2.value = random.randint(0, (2**32)-1)
    uut.alu_control.value = 0b0111  # Activate SRA mode

    # wait 1ns for the signals to settle
    await Timer(1, units="ns")

    rs1_value = uut.rs1.value.to_signed()
    rs2_value = uut.rs2.value.to_unsigned()
    rs2_lower_5_bits = int(LogicArray(uut.rs2.value)[4:0])  # rs2[4:0]

    uut._log.info(f"Setting rs1 to {rs1_value}")
    uut._log.info(f"Setting rs2 to {rs2_value}")
    uut._log.info(f"Setting alu_control to {uut.alu_control.value.to_unsigned()}")
    uut._log.info(f"Setting rs2 lower 5 bits are to {rs2_lower_5_bits}")

    rd_value = uut.rd.value.to_signed()

    expected_result = rs1_value >> rs2_lower_5_bits
    assert rd_value == expected_result, f"Test failed: Expected {expected_result}, got {rd_value}"

    uut._log.info(f"Test passed: {rs1_value} >> {rs2_lower_5_bits} = {rd_value}")

    uut._log.info("*****************************************************************")

    


    




























    











    























