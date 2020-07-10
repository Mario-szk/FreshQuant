import click
import shutil
import os


class AppGroup(click.Group):
    pass


cli = AppGroup()


# 提供创建示例strategy的命令
@click.command('create_strategy', short_help="Create a example strategy !")
@click.argument('name', default='example')
def create_project(name):
    click.echo(f'create strategy {name} !')
    import quant
    example_path = quant.__example__
    if os.path.exists(name):
        click.echo(f'{name} already exists !')
    else:
        shutil.copytree(example_path, name)
        click.echo(f'stategy {name} created !')


cli.add_command(create_project)