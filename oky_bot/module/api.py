"""This module is the file used for fastapi test in the backend system.

The module contains three data types including Perm for the permission,
User for the user message and Group for the group message information.
"""

from typing import Union
import json
from fastapi import FastAPI
from pydantic import BaseModel
import os
app = FastAPI()


class Perm(BaseModel):
    perm_id:int
    module_id: int
    module_name: str
    module_permit: int
# This data type is used to record every permission,
# including the id (should be unique),
# module_id(for identifying the permission module)
# module_name(to name this permission) and permit level(0-3)

class User(BaseModel):
    user_id: int
    user_name: str
    user_permit: int
    user_info: str
# This data type is used to record every user,
# including the id (should be unique),
# user_name(string for user name)
# user_permit(permit level(0-3)) and user_info (user description)

class Group(BaseModel):
    group_id: int
    group_name: str
    group_permit: int
    group_default_permit: int
    group_info: str
# This data type is used to record every group,
# including the group_id (should be unique),
# group_name(string for group name)
# group_permit(permit level(0-3))
# group_default_permit(default permit level(0-3))
# and group_info (group description)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/permission/get/{perm_id}")
def read_perm(perm_id: int, q: Union[int, None] = None):
    if(os.path.isfile("../permit.json")):
        f = open("../permit.json", "r")
        json_data = json.load(f)
        f.close()
    else:
        json_data={}
    # print(json_data)
    if str(perm_id) in json_data:
        return json_data[str(perm_id)]
    return {"error message": "permission not found"}
    """Fetches permit information from the stored json.

    Retrieves permit information created before. The information is a dictionary 
    stored in json and represented by perm_id.  String keys will be UTF-8 encoded.

    Args:
        perm_id: A unique integer for the permission.
        q: A parameter used for query the permission, currently not used.

    Returns:
        A dict mapping keys to the corresponding permission data
        fetched.  For example:

        { "perm_id": perm_id,
         "perm_name": perm.module_name,
         "module_id":perm.module_id,
         "perm_level": perm.module_permit}

        If a key from the keys argument is missing from the dictionary, 
        then that row was not found in the dict and will return an error message.

    Raises:
        KeyError:If the key was not found in the dict, it'll return an error.
    """

@app.put("/permission/set/{perm_id}")
def update_perm(perm_id: int, perm: Perm):
    if os.path.isfile("../permit.json"):
        f = open("../permit.json", "r")
        json_data = json.load(f)
        f.close()
    else:
        json_data={}
    # Change here if you want to change the permit information
    perm_data = { "perm_id": perm_id, "perm_name": perm.module_name,"module_id":perm.module_id,"perm_level": perm.module_permit}
    json_data[perm_id] = perm_data
    # print(json_data)
    with open("../permit.json", "w") as f:
        json.dump(json_data,f)
    # print(perm.name,perm.price)
    # Change here if you want to change the permit information
    return { "perm_id": perm_id, "perm_name": perm.module_name,"module_id":perm.module_id,"perm_level": perm.module_permit}
    """Update permit information from the stored json.

    Retrieves permit information created before. The information is a dictionary 
    stored in json and represented by perm_id. Then update the information for the input permit_id.
    String keys will be UTF-8 encoded.

    Args:
        perm_id: A unique integer for the permission.
        perm: The permission information to be updated.

    Returns:
        A dict mapping keys to the corresponding permission data
        updated.  For example:

        { "perm_id": perm_id,
         "perm_name": perm.module_name,
         "module_id":perm.module_id,
         "perm_level": perm.module_permit}


    """

@app.get("/user/get/{user_id}")
def read_user(user_id: int, q: Union[str, None] = None):
    if(os.path.isfile("../user.json")):
        f = open("../user.json", "r")
        json_data = json.load(f)
        f.close()
    else:
        json_data={}
    # print(json_data)
    if str(user_id) in json_data:
        return json_data[str(user_id)]
    return {"error message": "permission not found"}
    """Fetches user information from the stored json.

    Retrieves user information created before. The information is a dictionary 
    stored in json and represented by user_id.  String keys will be UTF-8 encoded.

    Args:
        user_id: A unique integer for the user account.
        q: A parameter used for query the user account, currently not used.

    Returns:
        A dict mapping keys to the corresponding user account data
        fetched.  For example:

        {"user_name": user.user_name,
         "user_id": user_id,
         "user_permit":user.user_permit,
         "user_info":user.user_info}

        If a key from the keys argument is missing from the dictionary, 
        then that row was not found in the dict and will return an error message.

    Raises:
        KeyError:If the key was not found in the dict, it'll return an error.
    """

@app.put("/user/set/{user_id}")
def update_user(user_id: int, user: User):
    if os.path.isfile("../user.json"):
        f = open("../user.json", "r")
        json_data = json.load(f)
        f.close()
    else:
        json_data={}
    # Change here if you want to change the user information
    user_data = {"user_name": user.user_name, "user_id": user_id,"user_permit":user.user_permit,"user_info":user.user_info}
    json_data[user_id] = user_data
    print(json_data)
    with open("../user.json", "w") as f:
        json.dump(json_data,f)
    # print(perm.name,perm.price)
    # Change here if you want to change the user information
    return {"user_name": user.user_name, "user_id": user_id,"user_permit":user.user_permit,"user_info":user.user_info}
    """Update user account information from the stored json.

    Retrieves user account information created before. The information is a dictionary 
    stored in json and represented by user_id. Then update the information for the input user_id.
    String keys will be UTF-8 encoded.

    Args:
        user_id: A unique integer for the user account.
        user: The user account information to be updated.

    Returns:
        A dict mapping keys to the corresponding user account data
        updated.  For example:

        {"user_name": user.user_name,
         "user_id": user_id,
         "user_permit":user.user_permit,
         "user_info":user.user_info}


    """

@app.get("/group/get/{group_id}")
def read_group(group_id: int, q: Union[str, None] = None):
    if(os.path.isfile("../group.json")):
        f = open("../group.json", "r")
        json_data = json.load(f)
        f.close()
    else:
        json_data={}
    # print(json_data)
    if str(group_id) in json_data:
        return json_data[str(group_id)]
    return {"error message": "permission not found"}
    """Fetches group information from the stored json.

    Retrieves group information created before. The information is a dictionary 
    stored in json and represented by group_id.  String keys will be UTF-8 encoded.

    Args:
        group_id: A unique integer for the group.
        q: A parameter used for query the group, currently not used.

    Returns:
        A dict mapping keys to the corresponding group data
        fetched.  For example:

        {"group_name": group.group_name,
         "group_id": group_id,
          "group_permit":group.group_permit,
          "group_default_permit":group.group_default_permit,
          "group_info":group.group_info}

        If a key from the keys argument is missing from the dictionary, 
        then that row was not found in the dict and will return an error message.

    Raises:
        KeyError:If the key was not found in the dict, it'll return an error.
    """

@app.put("/group/set/{module}")
def update_group(group_id: int, group: Group):
    if os.path.isfile("../group.json"):
        f = open("../group.json", "r")
        json_data = json.load(f)
        f.close()
    else:
        json_data={}
    # Change here if you want to change the group information
    group_data = {"group_name": group.group_name, "group_id": group_id, "group_permit":group.group_permit,"group_default_permit":group.group_default_permit,"group_info":group.group_info}
    json_data[group_id] = group_data
    # print(json_data)
    with open("../group.json", "w") as f:
        json.dump(json_data,f)
    # Change here if you want to change the group information
    return {"group_name": group.group_name, "group_id": group_id, "group_permit":group.group_permit,"group_default_permit":group.group_default_permit,"group_info":group.group_info}
    """Update group information from the stored json.

    Retrieves group information created before. The information is a dictionary 
    stored in json and represented by group_id. Then update the information for the input group_id.
    String keys will be UTF-8 encoded.

    Args:
        group_id: A unique integer for the group.
        group: The group information to be updated.

    Returns:
        A dict mapping keys to the corresponding group data
        updated.  For example:

        {"group_name": group.group_name,
         "group_id": group_id,
          "group_permit":group.group_permit,
          "group_default_permit":group.group_default_permit,
          "group_info":group.group_info}


    """