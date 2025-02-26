from pydantic import BaseModel

class Executor(BaseModel): 
    @staticmethod
    def roblox_get_group_join_requests(api_key: str, **kwargs):
        from rblxopencloud import Group
        group = Group(kwargs.group_id, api_key)
        return group.list_join_requests()
    
    def roblox_post_accept_group_join_request(api_key: str, **kwargs):
        from rblxopencloud import Group
        group = Group(kwargs.group_id)
        return group.accept_join_request(kwargs.user_id)