# WORKLOAD_TEMPLATE for custom workload of kube-burner
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export WORKLOAD_TEMPLATE=${WORKLOAD_TEMPLATE:-"${DIR}/../../kubeburner-object-templates/pause-config.yml"}
# ENVs to overwrite the kube-burner configuration file
export NAME=${NAME:-"large-network-policy"}
export NAMESPACE=${NAMESPACE:-"large-network-policy"}
export JOB_ITERATION=${JOB_ITERATION:-5000}
export QPS=${QPS:-50}
export BURST=${BURST:-50}
export SERVICE_TYPE=${SERVICE_TYPE:-"ClusterIP"}
# Other ENV needed by the test case script
export NETWORK_POLICY=${NETWORK_POLICY:-"${DIR}/../../content/allow_default_network_policy.yaml"}
