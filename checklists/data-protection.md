# Data Protection and Privacy Checklist

Use when handling personal, sensitive, Confidential, or Restricted data, and
before any external model/tool egress.

- [ ] Data classification confirmed for each data set and flow.
- [ ] Purpose and lawful basis/need-to-know documented where applicable.
- [ ] Non-production data is anonymized/masked or approved by Data Owner.
- [ ] Retention and deletion rules defined and enforced.
- [ ] Encryption in transit and at rest verified for the data class.
- [ ] Access is least-privilege, just-in-time where required, and logged.
- [ ] External egress approved for Confidential/Restricted data; secrets never sent.
- [ ] Logs, evidence, and agent memory exclude secrets and unnecessary personal data.
- [ ] DPIA/assessment flagged for humans where regulatory applicability is possible.
- [ ] Data Owner approval recorded for Restricted access or egress.
