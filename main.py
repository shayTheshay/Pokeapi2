from deploy.ec2_setup import ec2_deploy
from deploy.dynamoDB_setup import deploy_dynamoDB

def main() -> None:
    ec2_deploy()
    deploy_dynamoDB()

if __name__ == "__main__":
    main()