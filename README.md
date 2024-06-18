This repository is designed to help you kickstart your project using Prefect.

Prefect is an ETL and observability tool that:
1) Gives you a user interface through which you can observe your logs for job runs.
2) Will automatically launch jobs (submit them to kubernetes) when certain criteria are met (i.e., ETL pipelines).
3) Allows you to dynamically launch jobs on different types of infrastructure if needed.
4) Is fully pythonic in implementation.

Please note that this guide presumes that you already have a working Prefect Server (you need the IP address).  The HPC team can configure this for you if you do not already have one.

This repository is structured as follows:
1) In the /prefect/ folder are the files required to stand up a prefect worker, workpools, and check everything is working.
2) In the /examples/ folder are a few short examples you can use to test the system, and jumpstart your own project.

