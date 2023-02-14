import os
# f  = open("2022-11-11", "x")
# f = open("2023-12-17","x")
# os.remove("FPW0AD_B-000A_20221111_032132_41005_PU_FPW0AD_772901_0000530001_EAR_ECCN_EAR99.DAT")
from datetime import datetime,timedelta
current_date = datetime.now()
file_name = ["FPW0AD_B-000A_20221111_032132_41005_PU_FPW0AD_772901_0000530001_EAR_ECCN_EAR99.DAT",
             "FPW0AD_B-000A_20231217_032132_41005_PU_FPW0AD_772901_0000530001_EAR_ECCN_EAR97.DAT"]
for x in file_name:
 file_date = datetime.strptime(x.split("_")[2], "%Y%m%d")
 difference = (current_date - file_date).days
 if difference >= 60:
  print(f"{file_date.strftime('%Y-%m-%d')}")
  os.remove(file_date.strftime('%Y-%m-%d'))
  
  
  
#   AWS CLI Command :- aws s3 rm s3://<bucket_name>/<file_name>







