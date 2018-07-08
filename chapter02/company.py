class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(['yang', 'deng', 'hahahaha'])
company1 = company[:2]
# employee = company.employee
# for em in employee:
#     print(em)

for item in company:
    print(item)

print('-' * 50)
for item in company1:
    print(item)

print(len(company))
