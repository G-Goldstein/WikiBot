

businessAnalysis = 'Business Analysis'
clientManagement = 'Client Management'
product = 'Product'
solutionsDesign = 'Solutions Design'
solutionsDevelopment = 'Solutions Development'
testing = 'Testing'
rnSI = 'Releases & Software Installation'
lnUA = 'Learning & User Assistance'
hRFinance = 'HR & Finance'
office = 'Office'
technology = 'Technology'
fst = 'Solutions Support'
projectsDelivery = 'Projects Delivery'
salesMarketing = 'Sales & Marketing'
techSupport = 'Tech Support'

templateToAdd = 'Page ownership'


def templateTextToAdd(area):
	return '{{' + templateToAdd + '|' + propertyValueString('area',area) + '|' + propertyValueString('review','yes') + '}}'

def propertyValueString(prop, value):
	return prop + '=' + value

