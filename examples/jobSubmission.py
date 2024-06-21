from prefect import flow, task
from prefect.deployments import Deployment
from prefect_kubernetes import KubernetesJob 

#Import the job to distribute
testFlow = flow.from_source(
    source="https://github.com/D8A-SCIENCE/prefect-cluster.git",
    entrypoint="examples/simpleJob.py:testFlow"
)

# Define Kubernetes Job with resource specifications
# Define Kubernetes Job with resource specifications using the new package
k8s_job = KubernetesJob(
    job={
        "metadata": {
            "labels": {
                "example": "kubernetes-job"
            }
        },
        "spec": {
            "template": {
                "spec": {
                    "containers": [{
                        "name": "flow-container",
                        "image": "ghcr.io/d8a-science/prefect-kubectl:latest",
                        "resources": {
                            "limits": {
                                "cpu": "2",
                                "memory": "4Gi"
                            }
                        }
                    }]
                }
            }
        }
    }
)

# Create the deployment
deployment = Deployment.build_from_flow(
    flow=testFlow,
    name="exampleDeployment",
    work_queue_name="k8s-dynamic",
    tags=["k8s", "example"],
    infrastructure=k8s_job
)