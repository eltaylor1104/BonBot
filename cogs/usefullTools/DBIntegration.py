import pymongo
from pymongo import MongoClient
import os

mongodbclient_token = os.getenv("CONNECTION_URL")

cluster = pymongo.MongoClient(mongodbclient_token)

db = cluster.BonBot
collection = db["warnings"]
warnthresh_collection = db["warnthresh"]
guilds = db["guild_channels"]
assets = db["assets"]
mod_log_channels = db["mod_log"]
join_log_channels  = db["join_log"]
leave_log_channel_collection = db["leave_log"]
message_log_channel_collection = db["message_log"]
mute_role_collection = db["mute_role"]

print("Database connection has been established\n")


# ------------------------------------------------- LOGS -------------------------------------------------
def insert_mod_log_channel(guild_id, channel_id):
    mod_channel=None
    mod_channel=mod_channel = mod_log_channels.find_one({"guild_id": int(guild_id)})

    if mod_channel is None:
        results = mod_log_channel_collection.insert_one({"guild_id": int(guild_id), "channel_id": int(channel_id)})
    else:
        results = mod_log_channel_collection.update_one({"guild_id": int(guild_id)}, {"$set": {"channel_id": int(channel_id)}})

def fetch_mod_log_channel(guild_id):

	mod_channel = None
	mod_channel = mod_log_channels.find_one({"guild_id": int(guild_id)})

	return mod_channel

def delete_mod_log_channel(guild_id):

	result = mod_log_channels.delete_one({"guild_id": int(guild_id)})


# ------------------------------------------------- KICK -------------------------------------------------

def insert_warns(guild_id, member_id, mod_id, warning):

	initial_warn = None
	initial_warn = collection.find_one({"member_id": str(member_id), "guild_id" : str(guild_id)})

	if initial_warn is None:
		results = collection.insert_one({"guild_id": str(guild_id), "member_id": str(member_id), "mod_id": str(mod_id), "warning": warning})
	else:

		get_warns = collection.find_one({"member_id": str(member_id), "guild_id": str(guild_id)})
		warns = get_warns["warning"]
		modd_id = get_warns["mod_id"]
		results = collection.update_one({"member_id": str(member_id)}, {"$set": {"warning": f"{warns}\n{warning}"}})
		results1 = collection.update_one({"member_id": str(member_id)}, {"$set":{"mod_id": f"{modd_id}\n{mod_id}"}})
