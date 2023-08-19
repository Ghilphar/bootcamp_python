class Account(object):
    
    ID_COUNT = 1
    
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    
    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []
    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        """

        if not isinstance(new_account, Account):
            return False
        if new_account.name in [account.name for account in self.accounts]:
            return False

        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
            @origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        if not isinstance(origin, str) or not isinstance(dest, str) or not isinstance(amount, (int, float)):
            return False
        originAccount = next((account for account in self.accounts if account.name == origin), None)
        destAccount = next((account for account in self.accounts if account.name == dest), None)
        if not originAccount or not destAccount:
            return False
        if (not self.checkAccount(originAccount)) or (not self.checkAccount(destAccount)):
            return False
        if (amount < 0) or (originAccount.value < amount):
            return False
        if originAccount == destAccount:
            return True
        originAccount.value -= amount
        destAccount.value += amount
        return True

    def checkAccount(self, account):
        attributes = account.__dict__
        
        if len(attributes) % 2 == 0:
            return False
        if any(attribute.startswith("b") for attribute in attributes.keys()):
            return False
        if not any(attribute.startswith("zip") or attribute.startswith("addr") for attribute in attributes.keys()):
            return False
        if not all(hasattr(account, attribute) for attribute in ["name", "id", "value"]):
            return False
        if not isinstance(account.name, str):
            return False
        if not isinstance(account.id, int):
            return False
        if not isinstance(account.value, (int, float)):
            return False
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        recoverAccount = next((account for account in self.accounts if account.name == name), None)
        if not recoverAccount:
            return False
        recoverAccountAttributes = recoverAccount.__dict__
        for attribute in recoverAccountAttributes.keys():
            if attribute.startswith("b"):
                del recoverAccount.attribute
        if not any(attribute.startswith("zip") for attribute in recoverAccountAttributes.keys()):
            recoverAccount.zip_recover = True
        if not any(attribute.startswith("addr") for attribute in recoverAccountAttributes.keys()):
            recoverAccount.addr_recover = "newAddress"
        if not hasattr(recoverAccount, "id"):
            recoverAccount.id = 999
        if not hasattr(recoverAccount, "value"):
            recoverAccount.value = 1000
        if not isinstance(recoverAccount.id, int):
            recoverAccount.id = 888
        if not isinstance(recoverAccount.value, (int, float)):
            recoverAccount.value = 1000
        if len(recoverAccountAttributes) % 2 == 0:
            recoverAccount.fixAttribute = True
        return True
        
        