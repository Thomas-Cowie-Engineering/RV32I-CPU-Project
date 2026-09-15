// Auto-generated Verilog Testbench Wrapper - Coraltb 
 
`timescale 1ns/1ns 


module alu_wtb;

  // ALU instantation signals
  reg  [31:0] A;
  reg  [31:0] B;
  reg  [3:0] ALUControl;
  wire [31:0] ALUResult;
  wire  Zero;
  wire  blt_flg;
  wire  bltu_flg;

ALU dut (
      .A(A),
      .B(B),
      .ALUControl(ALUControl),
      .ALUResult(ALUResult),
      .Zero(Zero),
      .blt_flg(blt_flg),
      .bltu_flg(bltu_flg)
  );

endmodule 
 