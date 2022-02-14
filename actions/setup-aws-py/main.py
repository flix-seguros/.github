import os
import sys

def main(aws_profile, root_path):
    rootDir = os.path.expanduser('~')
    print(root_path)

    try:
        os.mkdir(f"{root_path}.aws")
    except OSError:
        print (f"Creation of the directory {root_path}.aws failed")
    else:
        print (f"Successfully created the directory {root_path}.aws")

    if os.getenv("DEV_TF_AWS_KEY_ID") is not None:
        DEV_TF_AWS_KEY_ID = os.environ["DEV_TF_AWS_KEY_ID"]
        DEV_TF_AWS_SECRET_KEY = os.environ["DEV_TF_AWS_SECRET_KEY"]

    if os.getenv("HML_TF_AWS_KEY_ID") is not None:
        HML_TF_AWS_KEY_ID = os.environ["HML_TF_AWS_KEY_ID"]
        HML_TF_AWS_SECRET_KEY = os.environ["HML_TF_AWS_SECRET_KEY"]    
        
    if os.getenv("PRD_TF_AWS_KEY_ID") is not None:
        PRD_TF_AWS_KEY_ID = os.environ["PRD_TF_AWS_KEY_ID"]
        PRD_TF_AWS_SECRET_KEY = os.environ["PRD_TF_AWS_SECRET_KEY"]    

    if os.getenv("SANDBOX_TF_AWS_KEY_ID") is not None:
        SANDBOX_TF_AWS_KEY_ID = os.environ["SANDBOX_TF_AWS_KEY_ID"]
        SANDBOX_TF_AWS_SECRET_KEY = os.environ["SANDBOX_TF_AWS_SECRET_KEY"]    

    fileAws = open(f"{root_path}.aws/credentials","w")

    fileAws.write("[org]\n")
    
    
    if os.getenv("DEV_TF_AWS_KEY_ID") is not None:
        fileAws.write("[dev]\n")
        fileAws.write(f"aws_access_key_id={ DEV_TF_AWS_KEY_ID }\n")
        fileAws.write(f"aws_secret_access_key={ DEV_TF_AWS_SECRET_KEY }\n\n")
    

    if os.getenv("HML_TF_AWS_KEY_ID") is not None:
        fileAws.write("[hml]\n")
        fileAws.write(f"aws_access_key_id={ HML_TF_AWS_KEY_ID }\n")
        fileAws.write(f"aws_secret_access_key={ HML_TF_AWS_SECRET_KEY }\n\n")

    if os.getenv("PRD_TF_AWS_KEY_ID") is not None:
        fileAws.write("[prd]\n")
        fileAws.write(f"aws_access_key_id={ PRD_TF_AWS_KEY_ID }\n")
        fileAws.write(f"aws_secret_access_key={ PRD_TF_AWS_SECRET_KEY }\n\n")

    if os.getenv("SANDBOX_TF_AWS_KEY_ID") is not None:
        fileAws.write("[sandbox]\n")
        fileAws.write(f"aws_access_key_id={ SANDBOX_TF_AWS_KEY_ID }\n")
        fileAws.write(f"aws_secret_access_key={ SANDBOX_TF_AWS_SECRET_KEY }\n\n")

    fileAws.close()

    os.environ["AWS_PROFILE"] = aws_profile.lower()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
