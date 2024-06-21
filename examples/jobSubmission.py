from prefect import flow
from prefect.deployments import Deployment
from prefect.infrastructure import KubernetesJob
from prefect.orion.schemas.schedules import IntervalSchedule
from datetime import timedelta

# Define your flow
@flow
def testFlow(testParameter):
    print(f"Parameter: {testParameter}")

# Create a deployment using the correct API
deployment = Deployment.build_from_flow(
    flow=testFlow,
    name="testDeploy",
    work_queue_name="k8s-dynamic",
    parameters={"testParameter": "Test Parameter Value"},
    tags=["k8s", "test"],  # Optional: Tags for organizing deployments
    schedule=IntervalSchedule(interval=timedelta(minutes=10)),  # Optional: Scheduling
    infrastructure=KubernetesJob(
        cpu="2",  # 2 CPUs
        memory="4Gi",  # 4 Gigabytes of memory
        image="ghcr.io/d8a-science/prefect-kubectl:latest"  # Docker image to use
    )
)

# Apply the deployment to register it with your Orion server
deployment.apply()