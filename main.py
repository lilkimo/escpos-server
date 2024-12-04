from typing import Any, Literal
from contextlib import contextmanager
from socket import gethostname
from subprocess import call

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from escpos.escpos import Escpos
from escpos.printer import File, Network
from pydantic import BaseModel


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@contextmanager
def Printer(printerType: Escpos, *args):
    printer = printerType(*args)
    try:
        yield printer
    finally:
        printer.close()


class Command(BaseModel):
    command: Literal['image', 'qr', 'barcode', 'text', 'textln', 'ln', 'block_text', 'software_columns', 'cut', 'buzzer']
    args: list[Any] = []
    kwargs: dict[str, Any] = {}


def escposPrint(commands: list[Command], *printerArgs):
    with Printer(*printerArgs) as printer:
        for command in commands:
            method = getattr(printer, command.command)
            method(*command.args, **command.kwargs)


@app.post('/print/driver')
def driver(shareName: str, commands: list[Command]):
    call(r'net use lpt1 /delete')
    call(rf'net use lpt1 \\{gethostname()}\{shareName}')
    escposPrint(commands, File, 'lpt1')

@app.post('/print/network')
def network(ip: str, port: int | None, commands: list[Command]):
    if port is None:
        port = 9100
    escposPrint(commands, Network, ip, port)
