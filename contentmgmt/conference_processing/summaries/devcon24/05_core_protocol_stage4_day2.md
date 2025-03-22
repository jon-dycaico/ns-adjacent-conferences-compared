# Core Protocol Track - Stage 4 Day 2 Summary
Devcon SEA 2024

## Session 1: Rethinking Ethereum Account Model
Speaker: Dan (Former CEV, Author of Account Abstraction)

### Overview
A discussion on reimagining Ethereum's account model and L2 account models to improve scalability and security through deterministic state access.

### Key Points

1. **State Access Lists**
   - Deterministic state addresses and access patterns
   - Enables concurrent execution of transactions
   - Improves scaling, indexing, and security
   - Potential for multiple concurrent proposers

2. **Current Challenges**
   - ERC20 represents a "global state lock" problem
   - Non-deterministic transaction patterns
   - Limited ability to predict state access

3. **Proposed Improvements**
   - Account-centric model
   - Programmatic ownership patterns
   - Fast pre-processing for security analysis
   - Better wallet transaction analysis capabilities

4. **Implementation Considerations**
   - Need for stronger consensus rules around access lists
   - Balance between current account model benefits and new features
   - Potential for hybrid approaches

## Session 2: Universal Encrypted MEV - Path to Ethereum L1
Speaker: Mark (Ethereum Core Developer, Nethermind)

### Overview
Exploration of encrypted Maximal Extractable Value (MEV) solutions and their potential implementation on Ethereum L1.

### Key Problems Addressed
1. Front-running
2. Sandwich attacks
3. Transaction censorship

### Proposed Solution Components

1. **Encrypted Mempool Design**
   - Encrypted transaction submission
   - Public constraint system
   - Predefined transaction ordering
   - Mandatory inclusion rules

2. **Keeper System**
   - Spectrum from trusted to trustless designs
   - Options:
     - Trusted party
     - Secure enclave (e.g., Intel SGX)
     - Threshold encryption (e.g., Shutter)
     - Delay encryption

3. **Public Constraint Implementation**
   - Calldata-based approach
   - Proposer-constructed constraints in blobs
   - Validator subset construction

4. **Enforcement Mechanisms**
   - Protocol-level enforcement
   - Smart contract-based verification
   - EIP changes for out-of-protocol MEV solutions

### Future Considerations
- Homomorphic encryption for advanced block building
- Transaction metadata privacy
- Progressive removal of trust assumptions
- L1 enshrinement path

## Significance
These sessions demonstrate the Core Protocol track's focus on fundamental improvements to Ethereum's architecture. The discussions around account models and MEV protection show a clear path toward more scalable, secure, and fair transaction processing systems. 