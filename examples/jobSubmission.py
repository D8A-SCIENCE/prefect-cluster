from prefect import flow
from prefect.deployments import Deployment
from prefect.infrastructure import KubernetesJob
from prefect.orion.schemas.schedules import IntervalSchedule
from datetime import timedelta

#Import the job to distribute
testFlow = flow.from_source(
    source="https://github.com/D8A-SCIENCE/prefect-cluster.git",
    entrypoint="examples/simpleJob.py:testFlow"
)

# Define Kubernetes Job with resource specifications
k8s_job = KubernetesJob(
    cpu="2",  # 2 CPUs
    memory="4Gi",  # 4GB of memory
    image="ghcr.io/d8a-science/prefect-kubectl:latest"  # specify your container image
)

# Create the deployment
deployment = Deployment.build_from_flow(
    flow=testFlow,
    name="exampleDeployment",
    work_queue_name="k8s-dynamic",
    tags=["k8s", "example"],
    infrastructure=k8s_job
)