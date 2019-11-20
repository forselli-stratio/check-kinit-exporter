# Check-kinit-exporter

This exporter executes a python scripts that basically executes three bash commands:
- kdestroy to destroy current ticket.
- kinit to obtain and cache Kerberos ticket-granting ticket, using the keytab you specify in the deployment json.
- klist -s to check if kinit worked.

You need to have a working keytab uploaded to vault.
| Variable | Definition |
|-------------------|:--------------|
| VAULT_KEYTAB_KEY    | Key specified in vault for the keytab        |
| KERBEROS_PRINCIPAL    | Keytab principal       |
| VAULT_KEYTAB_NAME    | Keytab name in vault         |
| VAULT_KEYTAB_PRINCIPAL_KEY    | NKey specified in vault for the principal        |

Example:
We have the following keytab stored in vault:
/userland/kerberos/example
with values:
example.mesos_keytab:XXXXXX
example.mesos_principal:example@example.com

Fill your vars like this:

| Variable | Value |
|-------------------|:--------------|
| VAULT_KEYTAB_KEY    | example.mesos        |
| KERBEROS_PRINCIPAL    | example@example.com       |
| VAULT_KEYTAB_NAME    | example         |
| VAULT_KEYTAB_PRINCIPAL_KEY    | example.mesos        |