
import click

@click.group()
def cli():
    """A CLI for Differentiable Modeling."""
    pass

@click.command()
@click.argument('name')
def greet(name):
    """Greet someone by NAME."""
    click.echo(f"Hello, {name}! Welcome to Differentiable Modeling.")

cli.add_command(greet)

if __name__ == '__main__':
    cli()

