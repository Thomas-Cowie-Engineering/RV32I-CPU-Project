

// Module for a RV32I ALU
module ALU (
    input  wire [31:0] rs1, 
    input  wire [31:0] rs2,
    input  wire [3:0]  alu_control, // Control signal from Control Unit that decides what operation the ALU will perform
    output reg  [31:0] rd,  // Result of the ALU operation
    output wire        zero_flg,       // 1 if ALUResult is zero, 0 otherwise ( For A==B and A!=B comparison)
    output wire        blt_flg,    // 1 if A < B (signed comparison), 0 otherwise
    output wire        bltu_flg    // 1 if A < B (unsigned comparison), 0 otherwise
);
    assign zero_flg = (rd == 32'b0);
    assign blt_flg  = ($signed(rs1) < $signed(rs2));
    assign bltu_flg = (rs1 < rs2);


    always @(*) begin
        case (alu_control)
            4'b0000: rd = rs1 + rs2; // ADD
            4'b0001: rd = rs1 - rs2; // SUB
            4'b0010: rd =  rs1 ^ rs2; // XOR
            4'b0011: rd = rs1 | rs2; // OR
            4'b0100: rd = rs1 & rs2; // AND
            4'b0101: rd = rs1 << rs2[4:0]; // SLL
            4'b0110: rd = rs1 >> rs2[4:0]; // SRL
            4'b0111: rd = $signed(rs1) >>> rs2[4:0]; // SRA
            4'b1000: rd = ($signed(rs1) < $signed(rs2)) ? 32'b1 : 32'b0; // SLT
            4'b1001: rd = (rs1 < rs2) ? 32'b1 : 32'b0; // SLTU
            default: rd = 32'b0; 
        endcase
    end

endmodule