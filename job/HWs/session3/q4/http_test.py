from zeep import Client
client = Client('http://my-endpoint.com/production.svc?wsdl')
node = client.create_message(client.service, 'myOperation', user='hi')
