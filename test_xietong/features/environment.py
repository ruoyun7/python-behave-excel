from lib.dbutils import invoke_sql_file
def before_all(context):
    print("behave test is starting!")


def after_all(context):
    print("\nbehave test is over!")