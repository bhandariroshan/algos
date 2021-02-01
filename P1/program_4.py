class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    return user in group.users or any(is_user_in_group(user, sub_group) for sub_group in group.get_groups())

def test():
    # Test Cases
    codes = {}

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    parent.add_user("P1")
    child.add_user("C1")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    # sub_child_user is in the parent
    print ("Pass" if (True == is_user_in_group("sub_child_user", parent)) else "Fail")
    
    # sub_child_user is in the child
    print ("Pass" if (True == is_user_in_group("sub_child_user", child)) else "Fail")
    
    # P1 is in the parent
    print ("Pass" if (True == is_user_in_group("P1", parent)) else "Fail")
    
    # P1 cannot be in the sub child
    print ("Pass" if (False == is_user_in_group("P1", sub_child)) else "Fail")
    
    # P1 cannot be in the child
    print ("Pass" if (False == is_user_in_group("P1", child)) else "Fail")

    # C1 should be in the child
    print ("Pass" if (True == is_user_in_group("C1", parent)) else "Fail")

if __name__ == "__main__":
    test()