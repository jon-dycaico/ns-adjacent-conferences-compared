# Core Protocol Track - Stage 4 Day 1 Summary
Devcon SEA 2024

## Session 1: When to Use ZK Proofs, FHE, and MPC
Speaker: Jakomo (Cryptography Engineer, PSE/Ethereum Foundation)

### Overview
A high-level introduction to the building blocks of programmable cryptography, focusing on practical applications rather than technical implementation details.

### Key Technologies Covered

1. **Zero Knowledge Proofs (ZK)**
   - Allows one party to prove a statement's truth without revealing additional information
   - Example: Proving age above threshold without revealing exact age
   - Most mature of the three technologies

2. **Secure Multi-Party Computation (MPC)**
   - Enables multiple parties to compute functions while keeping inputs private
   - Ideal for applications like private voting systems
   - Growing ecosystem of tools and frameworks

3. **Fully Homomorphic Encryption (FHE)**
   - Enables computation on encrypted data
   - Perfect for outsourcing computation while maintaining privacy
   - Most experimental of the three technologies
   - Currently limited to addition and multiplication operations

### Combinations and Synergies
- ZK + MPC: Verifiable multi-party computation
- MPC + FHE: Distributed key management
- ZK + FHE: Verifiable encrypted computation
- All three can be combined for complex privacy-preserving applications

## Session 2: MPC Tooling and Application Development
Speaker: Rosu (Software Engineer, PSE)

### Overview
Introduction to MPC development tools and frameworks for building privacy-preserving applications.

### Key Tools Presented

1. **Circom MPC**
   - Fork of the popular Circom ZK DSL
   - Compiles to Bristol fashion circuit format
   - Leverages existing Circom knowledge and circuit libraries

2. **Summon**
   - TypeScript-like DSL for collaborative computations
   - User-friendly approach to MPC development
   - Enables end-to-end TypeScript development
   - Already used by Cursive team

3. **Circom MPCSpeed**
   - Transpiler from Bristol format to MPC representation
   - Bridges gap between circuit description and execution
   - Supports both Circom MPC and Summon outputs

### Example Applications
- Privacy-preserving machine learning
- MPC Stats project
- "2 PCs for Lovers" - A privacy-preserving matching game

## Session 3: Multilateral Credit Set-off in MPC
Speaker: Enrico Batti (PSE/Ethereum Foundation)

### Overview
Presentation on applying MPC to payment networks and trade credit settlement.

### Key Points
- Focus on payment networks with multiple firms
- Handling obligations and balances privately
- Application of MPC to financial systems

## Significance
These sessions highlight the Core Protocol track's focus on advancing privacy-preserving computation in Ethereum. The presentations demonstrate the maturation of cryptographic tools and their practical applications, while also showing the ongoing work to make these technologies more accessible to developers. 