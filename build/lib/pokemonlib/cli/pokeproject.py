import click


@click.group()
def pokeproject():
    pass


@pokeproject.group()
def manage():
    pass


@pokeproject.group()
def build():
    pass


@pokeproject.command()
def run():
    pass


@pokeproject.command()
@click.option('--projectname', '-n', 'projectname', prompt=True)
@click.option('--path', '-o', 'path', prompt=True)
def create(projectname, path):
    click.echo("%s and %s" % (projectname, path))


@manage.command()
def initdb():
    click.echo('Initialized the database')


@manage.command()
def dropdb():
    click.echo('Dropped the database')
