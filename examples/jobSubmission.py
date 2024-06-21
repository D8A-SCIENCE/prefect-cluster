from prefect import flow, task
from prefect.deployments import Deployment
from prefect_kubernetes import KubernetesJob 

#Import the job to distribute
testFlow = flow.from_source(
    source="https://github.com/D8A-SCIENCE/prefect-cluster.git",
    entrypoint="examples/simpleJob.py:testFlow"
)

# Create the deployment
deployment = Deployment.build_from_flow(
    flow=testFlow,
    name="exampleDeployment",
    work_queue_name="k8s-dynamic",
    tags=["k8s", "example"]
)