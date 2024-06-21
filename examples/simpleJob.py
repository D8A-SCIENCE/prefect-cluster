#The below code will be loaded (from github) on to all workers assigned
#to your task(s). It's up to you to ensure that the image you are loading
#into your workers has all of the relevant packages you need.

from prefect import flow, serve, task, deploy
from datetime import datetime
import time
import os

@flow(name="testFlow",
      description="A test flow for Prefect",
      log_prints=True)
def testFlow(testParameter):
    env_cluster_uid = os.environ.get("PREFECT_KUBERNETES_CLUSTER_UID")
    print(env_cluster_uid)
    print("------")
    start_time = time.time()
    TIMESTAMP = str(datetime.now())
    print("This is a test flow, executed at time " + TIMESTAMP)
    n = 10**7
    primes = [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
    print(f"Computed {len(primes)} primes in {time.time() - start_time:.2f} seconds")
    print("Incoming parameter was: " + str(testParameter))
    return(primes)