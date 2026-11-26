### 19. Cryptography and Identity Management

| Skill | Description and knowledge | Practical competencies | Tools | Applied in | Level | Validation |
|---|---|---|---|---|---|---|
| Applied cryptography | Symmetric and asymmetric primitives, AEAD, hashing, KDF and password hashing, signatures, TLS, and key lifecycle. **Never design custom primitives or protocols.** | Select and configure the vetted libraries correctly. Spot the misuse (nonce reuse, ECB, weak RNG, unauthenticated encryption, and hard-coded keys). | Crypto libraries, KMS, openssl | P02, P04 | M, L3. Security L4 | SEED, CR |
| Key and secrets management | Generation, storage, rotation, escrow, and revocation | Operate a KMS and a secrets manager with rotation | KMS, vaults | P04, P08 | M, L3. DevOps L4 | DRILL |
| Identity and access protocols | OAuth 2.x, OIDC, SAML, SCIM, WebAuthn, and JWT/JWS/JWE | Integrate and attack-test a flow | IdPs, protocol debuggers | P02, P04 | R: Backend L3. Security L4 | LAB |
| PKI and certificate management | CAs, chains, revocation, and automation | Automate renewal and detect expiry | ACME tooling | P08 | R: DevOps L3 | LAB |
