## 11.3 Test design rules
1. Each test has a clear name, an arrange-act-assert structure, and a **single reason to fail**.
2. Tests are deterministic. Time, randomness, and network are controlled.
3. The test data is synthetic. Production data is never used (NN-09).
4. Tests are independent and can run in any order and in parallel.
5. A bug fix begins with a failing test (regression).
6. Tests of the security controls include *negative* cases (the forbidden action must fail).
7. Test code is production-quality code and is reviewed.
