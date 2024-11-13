import subprocess

# List of scripts to run in sequence
scripts = ["GetUserDetails.py", "GetFinancialYearFilter.py","GetHeadCodeByUserID.py","GET_TechnicalSactionNumberInbox.py","GETTechnicalSactionNumberInboxMasslip.py"
,"GetWorkDetailsbyIDForPhysicalProgress.py","GetHeadCodeByUserID-3054.py","GetPhysicalPercentage.py","CheckPhysicalLinkToDemand.py" ,"CheckPhysicalLinkToDemand.py",
"CheckExistPhysicalProgressPercentage.py","SetPhysicalProgress.py"]

for script in scripts:
    subprocess.run(["python", script])