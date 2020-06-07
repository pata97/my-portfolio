import boto3
import StringIO
import zipfile
import mimetypes

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:024223368277:deployPortfolioTopic')

    try:
        s3 = boto3.resource('s3', 'us-east-1', config=Config(s3={'addressing_style': 'path'}))

        portfolio_bucket = s3.Bucket('portfolio.patriciaalexander.net')
        build_bucket = s3.Bucket('portfoliobuild.patriciaalexander.net')

        portfolio_zip = StringIO.StringIO()
        build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm)
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

        print "Job done!"
        topic.publish(Subject="Portfolio Deployed", Message="Portfolio deployed successfully!")

    except:
        topic.publish(Subject="Portfolio Deploy Failed", Message="The Portfolio was not deployed successfully!")
        raise

    return 'Hello from Lambda'
