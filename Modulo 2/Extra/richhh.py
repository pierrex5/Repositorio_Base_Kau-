from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Líderes da Cultura Negra")

table.add_column("Nome", style="cyan", no_wrap=True)
table.add_column("Contribuição", style="green")
table.add_column("País", justify="center", style="yellow")

table.add_row("Zumbi dos Palmares", "Resistência e Quilombos", "Brasil")
table.add_row("Angela Davis", "Direitos Civis e feminismo negro", "EUA")
table.add_row("Nelson Mandela", "Fim do apartheid", "África do Sul")

console.print(table)
