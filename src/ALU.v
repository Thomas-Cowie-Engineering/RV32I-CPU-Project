

// Module for a RV32I ALU
module ALU (
    input  wire [31:0] A, 
    input  wire [31:0] B,
    input  wire [3:0]  ALUControl, // Control signal from Control Unit that decides what operation the ALU will perform
    output reg  [31:0] ALUResult,  // Result of the ALU operation
    output wire        Zero,       // 1 if ALUResult is zero, 0 otherwise
    output wire        blt_flg,    // 1 if A < B (signed comparison), 0 otherwise
    output wire        bltu_flg    // 1 if A < B (unsigned comparison), 0 otherwise
);


    assign Zero     = (ALUResult == 32'b0);
    assign blt_flg  = ($signed(A) < $signed(B));
    assign bltu_flg = (A < B);


    always @(*) begin
        case (ALUControl)
            4'b0000: ALUResult = A + B; // ADD
            4'b0001: ALUResult = A - B; // SUB
            4'b0010: ALUResult =  A ^ B; // XOR
            4'b0011: ALUResult = A | B; // OR
            4'b0100: ALUResult = A & B; // AND
            4'b0101: ALUResult = A << B[4:0]; // SLL
            4'b0110: ALUResult = A >> B[4:0]; // SRL
            4'b0111: ALUResult = $signed(A) >>> B[4:0]; // SRA
            4'b1000: ALUResult = ($signed(A) < $signed(B)) ? 32'b1 : 32'b0; // SLT
            4'b1001: ALUResult = (A < B) ? 32'b1 : 32'b0; // SLTU
            default: ALUResult = 32'b0; 
        endcase
    end

endmodule