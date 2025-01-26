#!/usr/bin/env python3
import speedtest
from rich.console import Console
from rich.progress import Progress
import time

console = Console()

def test_speed():
    console.print("[bold blue]Starting Network Speed Test...[/bold blue]")
    
    try:
        st = speedtest.Speedtest()
        
        with Progress() as progress:
            # Select best server
            task1 = progress.add_task("[cyan]Selecting best server...", total=1)
            st.get_best_server()
            progress.update(task1, completed=1)
            
            # Test download speed
            task2 = progress.add_task("[green]Testing download speed...", total=1)
            download_speed = st.download() / 1_000_000  # Convert to Mbps
            progress.update(task2, completed=1)
            
            # Test upload speed
            task3 = progress.add_task("[yellow]Testing upload speed...", total=1)
            upload_speed = st.upload() / 1_000_000  # Convert to Mbps
            progress.update(task3, completed=1)
            
            # Test ping
            task4 = progress.add_task("[magenta]Testing ping...", total=1)
            ping = st.results.ping
            progress.update(task4, completed=1)
        
        # Display results
        console.print("\n[bold green]== Speed Test Results ==[/bold green]")
        console.print(f"[cyan]Download Speed:[/cyan] {download_speed:.2f} Mbps")
        console.print(f"[yellow]Upload Speed:[/yellow] {upload_speed:.2f} Mbps")
        console.print(f"[magenta]Ping:[/magenta] {ping:.2f} ms")
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")

if __name__ == "__main__":
    test_speed()
