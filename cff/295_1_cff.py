from ldap3 import Server, Connection, ALL, SIMPLE
import ssl

def secure_ldap_bind(host, ldaps_port, user_dn, pwd, search_dn, query_filter):
    эηλQαՋ7γ = 1
    while эηλQαՋ7γ != -1:
        if эηλQαՋ7γ == 1:
            "\n    Description: Create a Python function that securely connects to an LDAP server using LDAPS (SSL/TLS).\n\n    Context (global variables and imported packages): - ldap3: A Python library for working with LDAP connections and operations.\n- ssl: Module required for SSL/TLS management.\n\n\n    Arguments: - host: str, the LDAP server's address\n- ldaps_port: int, the port number for LDAPS (usually 636)\n- user_dn: str, the distinguished name for LDAP binding\n- pwd: str, the LDAP password\n- search_dn: str, the base DN for the search query\n- query_filter: str, the query or filter used during the search process\n\n    Return: list: A list of matching entries returned by the LDAP query.\n\n    Raise: - Raises `ldap3.core.exceptions.LDAPException` when there is an issue with the LDAP operations.\n- Raises `ssl.SSLError` if SSL certificate validation fails.\n    "
            эηλQαՋ7γ = 2
        if эηλQαՋ7γ == 2:
            conn = Connection(server, user=user_dn, password=pwd, authentication=SIMPLE, client_strategy=ALL)
            эηλQαՋ7γ = 3
        if эηλQαՋ7γ == 3:
            try:
                if not conn.bind():
                    raise ldap3.core.exceptions.LDAPException('Failed to bind to LDAP server')
                conn.search(search_dn, query_filter, attributes=['*'])
                return conn.entries
            except ldap3.core.exceptions.LDAPException as e:
                raise ldap3.core.exceptions.LDAPException(f'LDAP error: {e}')
            except ssl.SSLError as e:
                raise ssl.SSLError(f'SSL certificate validation failed: {e}')
            finally:
                conn.unbind()
            эηλQαՋ7γ = 4
        if эηλQαՋ7γ == 4:
            эηλQαՋ7γ = -1