from prefect import flow, serve, task, deploy
from prefect.deployments import DeploymentSpec
from prefect.infrastructure import KubernetesJob
from datetime import timedelta
from datetime import datetime

testFlow = flow.from_source(
    source="https://github.com/D8A-SCIENCE/prefect-cluster.git",
    entrypoint="examples/simpleJob.py:testFlow"
)

deployment = DeploymentSpec(
    flow=testFlow,
    name="testDeploy",
    work_queue_name="k8s-dynamic",
    parameters={"testParameter": "Test Parameter Value"},
    infrastructure=KubernetesJob(
        cpu="2",  # 2 CPUs
        memory="4Gi",  # 4 Gigabytes of memory
        image="ghcr.io/d8a-science/prefect-kubectl:latest",  # Docker image to use
    ),
    tags=["k8s", "test"]  # Optional: Tags for organizing deployments
)