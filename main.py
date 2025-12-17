import cli_commands
import argparse



def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        title="Available commands",
        description="Choose one of the subcommands below",
        dest="command",
        required=True
    )    
    cli_commands.register(subparsers)
     
    args = parser.parse_args()
    args.func(args)



if __name__ == "__main__":
    main()

