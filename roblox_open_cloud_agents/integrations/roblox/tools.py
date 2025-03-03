from pydantic import BaseModel

class Executor(BaseModel): 
    @staticmethod
    def roblox_get_group_join_requests(api_key: str, **kwargs):
        from rblxopencloud import Group
        from rblxopencloud.http import iterate_request
        group = Group(kwargs["group_id"], api_key)

        def to_dict(join_request: object):
            return {
                "id": join_request.id
            }
        
        return {"join_requests": [to_dict(req) for req in group.list_join_requests()]}
    
    def roblox_post_accept_group_join_request(api_key: str, **kwargs):
        from rblxopencloud import Group
        from rblxopencloud.http import send_request
        group = Group(kwargs["group_id"], api_key)
        
        #group.accept_join_request() is broken, so I need to manually call send_request with arguments
        #this will be fixed in the next version of rblxopencloud, currently tracked as issue #23
        return send_request(
            "POST",
            f"/groups/{group.id}/join-requests/{kwargs["user_id"]}:accept",
            authorization=api_key,
            expected_status=[200],
            json = {}
        )