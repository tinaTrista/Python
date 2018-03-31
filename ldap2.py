 1#-*- coding: UTF-8 -*-
 ldap_config = {
 2     'ldap_path': 'ldap://xx.xx.xx.xx:389',
 3     'base_dn': 'ou=users,dc=ledo,dc=com',
 4     'ldap_user': 'uid=reporttest,ou=users,dc=ledo,dc=com',
 5     'ldap_pass': '111111.0',
 6     'original_pass': '111111.0'
 7 }
 8
 9 ldap_message = {
10     0: 0, #'ok'
11     1: 1, #'用户名或密码错误'
12     2: 2, #ldap验证异常'
13 }
14
15 import ldap
16 import base64
17 import hashlib
18 from config_message import ldap_config, ldap_message
19
20
21 class LDAP_API(object):
22
23     _ldap_path = ldap_config['ldap_path']
24     _base_dn = ldap_config['base_dn']
25     _ldap_user = ldap_config['ldap_user']
26     _ldap_pass = ldap_config['ldap_pass']
27     _original_pass = ldap_config['original_pass']
28
29     # 连接ldap服务器
30     def __init__(self):
31
32         try:
33             self.ldapconn = ldap.initialize(self._ldap_path)
34             self.ldapconn.protocal_version = ldap.VERSION3
35             self.ldapconn.simple_bind(self._ldap_user, self._ldap_pass)
36
37         except ldap.LDAPError, e:
38             print e
39
40     # 验证用户登录
41     def ldap_get_vaild(self, username, password):
42
43         obj = self.ldapconn
44         searchScope = ldap.SCOPE_SUBTREE
45         # searchFilter = '(&(cn='+username+')(userPassword='+password+'))'
46         searchFilter = 'uid=' + username
47
48         try:
49             obj.search(self._base_dn, searchScope, searchFilter, None)  # id--2
50             # 将上一步计算的id在下面运算
51             result_type, result_data = obj.result(2, 0)
52             if result_type != ldap.RES_SEARCH_ENTRY:
53                 return {'status': ldap_message[1], 'data': ''}
54             dic = result_data[0][1]
55             l_realname = dic['sn'][0]
56             l_password = dic['userPassword'][0]
57             md_password = LDAP_API.hash_md5(password)
58             if l_password in (password, md_password):
59                 return {'status': ldap_message[0], 'data': l_realname}
60             else:
61                 return {'status': ldap_message[1], 'data': ''}
62         except ldap.LDAPError, e:
63             return {'status': ldap_message[2], 'data': ''}
64
65     @staticmethod
66     def hash_md5(data):
67         md = hashlib.md5()
68         md.update(str(data))
69         a = md.digest()
70         b = '{MD5}' + base64.b64encode(a)
71         return b
