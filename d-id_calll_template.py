import os, time, base64, requests

API_KEY = "c2liYW5lei5taXRAZ21haWwuY29t:zAAbpJJgK8szv0wOPZ1WC"  # "username:password"
auth_header = "Basic " + base64.b64encode(API_KEY.encode()).decode()

create_payload = {
    "script": {
        "type": "text",
        "input": "Hello from D-ID Clips!"  # Or add a voice provider, see below
    },
    "presenter_id": "amy-Aq6OmGZnMt",
    "driver_id": "Vcq0R4a8F0",
    # Optional: "webhook": "https://your.server/clip-callback"
}

r = requests.post(
    "https://api.d-id.com/clips",
    headers={"Authorization": auth_header, "Accept":"application/json", "Content-Type":"application/json"},
    json=create_payload,
)
r.raise_for_status()
clip_id = r.json()["id"]

# Poll until ready
while True:
    s = requests.get(f"https://api.d-id.com/clips/{clip_id}",
                     headers={"Authorization": auth_header, "Accept":"application/json"})
    s.raise_for_status()
    data = s.json()
    if data.get("status") == "done":
        print("Video:", data["result_url"])
        break
    elif data.get("status") in {"error", "failed"}:
        raise RuntimeError(f"Clip failed: {data}")
    time.sleep(2)

