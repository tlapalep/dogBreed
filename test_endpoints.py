import urllib.request
import json

total = 0
counter = 0

# IDs reales
sample_breed_id = "036feed0-da8a-42c9-ab9a-57449b530b13"
sample_group_id = "f56dc4b1-ba1a-4454-8ce2-bd5d41404a0c"

basic_endpoints = [
    "http://127.0.0.1:5000/breeds",
    f"http://127.0.0.1:5000/breeds/{sample_breed_id}",
    "http://127.0.0.1:5000/facts",
    "http://127.0.0.1:5000/groups",
    f"http://127.0.0.1:5000/groups/{sample_group_id}"
]

complex_endpoints = [
    f"http://127.0.0.1:5000/group-details/{sample_group_id}",
    f"http://127.0.0.1:5000/group-details/{sample_group_id}/breed/{sample_breed_id}"
]

def eval_resp(task_done=False, fct=1):
    global total, counter
    total += fct
    if task_done:
        counter += fct

def test_endpoints(endpoints, title):
    f = 1 if title.lower().startswith("basic") else 2
    print(f"\n{title}")
    for url in endpoints:
        try:
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            with urllib.request.urlopen(req) as response:
                status = response.getcode()
                content = response.read().decode()
                try:
                    json.loads(content)
                    is_json = True
                except:
                    is_json = False
                eval_resp(is_json, f)
                if status == 200:
                    print(f"200 OK - {url}")
                else:
                    print(f"WRONG {status} - {url}")
                eval_resp(status == 200, f)
        except Exception as e:
            print(f"ERROR - {url} - {e}")
            eval_resp(False, f)

if __name__ == "__main__":
    test_endpoints(basic_endpoints, "Basic Endpoints")
    test_endpoints(complex_endpoints, "Complex/Structured Endpoints")
    print(f"\n # Result: {100 * counter / total:.1f} %")
