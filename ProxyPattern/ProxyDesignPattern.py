from abc import ABC, abstractmethod

# interface
class EmployeeDAO(ABC):
    @abstractmethod
    def get_employee_info(self, emp_id: int):
        pass

    @abstractmethod
    def create_employee(self, obj):
        pass


# real implementation
class ImplEmployeeDAO(EmployeeDAO):
    def get_employee_info(self, emp_id: int):
        print(f"fetching employee info for ID -> {emp_id}")

    def create_employee(self, obj):
        print(f"creating employee -> {obj}")


# proxy
class ProxyEmployeeDAO(EmployeeDAO):
    def __init__(self, client_role: str):
        self.emp_dao_obj = ImplEmployeeDAO()
        self.client_role = client_role

    def get_employee_info(self, emp_id: int):
        if self.client_role in ("ADMIN", "USER"):
            self.emp_dao_obj.get_employee_info(emp_id)
        else:
            raise Exception("acess denied")

    def create_employee(self, obj):
        if self.client_role == "ADMIN":
            self.emp_dao_obj.create_employee(obj)
        else:
            raise Exception("access denied")

# data object
class EmployeeDo:
    def __repr__(self):
        return "EmployeeDo()"



if __name__ == "__main__":
    print("=====proxy design pattern=====")

    user_proxy = ProxyEmployeeDAO("USER")
    user_proxy.get_employee_info(1)

    try:
        user_proxy.create_employee(EmployeeDo())
    except Exception as e:
        print(e)