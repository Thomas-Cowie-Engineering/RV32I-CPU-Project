// Auto-generated Verilog Testbench Wrapper - Coraltb 
 
`timescale 1ns/1ns 

module alu_wtb;

  // ALU instantation signals
  reg  [31:0] rs1;
  reg  [31:0] rs2;
  reg  [3:0] alu_control;
  wire [31:0] rd;
  wire  zero_flg;
  wire  blt_flg;
  wire  bltu_flg;

ALU dut (
      .rs1(rs1),
      .rs2(rs2),
      .alu_control(alu_control),
      .rd(rd),
      .zero_flg(zero_flg),
      .blt_flg(blt_flg),
      .bltu_flg(bltu_flg)
  );

endmodule 
 