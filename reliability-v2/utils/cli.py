from integrations.SlackIntegration import slackIntegration
import subprocess
import logging

def shell(cmd,ignore_log=False,ignore_slack=False):
    logger = logging.getLogger('reliability')
    rc = 0
    result = ""
    # mask password to avoid output in log file or slack channel
    if " -p " in cmd:
        pwd = cmd.partition(" -p ")[2].partition(" ")[0]
        cmd_output = cmd.replace(pwd, "xxxx")
    else:
        cmd_output = cmd
    if not ignore_log:
        logger.info(f"=> {cmd_output}")
    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
        string_result = result.decode("utf-8")
        if not ignore_log:
            logger.info(f"{cmd_output} \n {str(rc)} : {string_result}")
    except subprocess.CalledProcessError as cpe:
        rc = cpe.returncode
        result = cpe.output
        string_result = result.decode("utf-8")
        if not ignore_log:
            logger.error(f"{cmd_output} \n {str(rc)} : {string_result}")
        # send slack message if oc command failed
        if not ignore_slack:
            slackIntegration.error(f"cmd: {cmd_output}  failed. Result: {string_result}")
    return string_result, rc

def oc(cmd, config="",ignore_log=False,ignore_slack=False):
    rc = 0
    result = ""
    if config:
        cmd = "oc --kubeconfig " + config + ' ' + cmd
    else:
        cmd = "oc " + cmd
    result,rc = shell(cmd,ignore_log=ignore_log,ignore_slack=ignore_slack)
    return result,rc

def kubectl(cmd, config="",ignore_log=False,ignore_slack=False):
    rc = 0
    result = ""
    if config:
        cmd = "kubectl --kubeconfig " + config + ' ' + cmd
    else:
        cmd = "kubectl " + cmd
    result,rc = shell(cmd,ignore_log=ignore_log,ignore_slack=ignore_slack)
    return result,rc

if __name__ == "__main__":
    (result, rc) = oc("get projects")
    print(rc)
