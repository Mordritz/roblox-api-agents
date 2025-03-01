from .tools import Executor
from agentsjson.integrations.types import ExecutorType

map_type = ExecutorType.SDK

map = {
    "Cloud_ListGroupJoinRequests": Executor.roblox_get_group_join_requests,
    "Cloud_AcceptGroupJoinRequest": Executor.roblox_post_accept_group_join_request
}