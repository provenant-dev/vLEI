# -*- encoding: utf-8 -*-
"""
server module

"""
import argparse

import falcon
from hio.base import doing
from hio.core import http

from vlei.app import serving

parser = argparse.ArgumentParser(description="Runs vLEI schema server")
parser.add_argument('-p', '--http',
                    action='store',
                    default=7723,
                    help="Port on which to serve vLEI schema SADs.  Defaults to 7723")
parser.add_argument('-s', '--schema-dir',
                    action='store', dest="schemaDir",
                    required=True,
                    help="Directory of schema to serve")
parser.add_argument('-c', '--cred-dir',
                    action='store', dest="credDir",
                    required=True,
                    help="Directory of credentials to serve")
parser.add_argument('-o', '--oobi-dir',
                    action='store', dest="oobiDir",
                    required=True,
                    help="Directory of OOBIs to serve")


def launch(args):
    app = falcon.App()
    server = http.Server(port=int(args.http), app=app)
    if not server.reopen():
        raise RuntimeError(f"cannot create http server on port {int(args.http)}")
    httpServerDoer = http.ServerDoer(server=server)

    serving.loadEnds(app, schemaDir=args.schemaDir, credDir=args.credDir, oobiDir=args.oobiDir)

    doers = [httpServerDoer]

    tock = 0.03125
    doist = doing.Doist(limit=0.0, tock=tock, real=True)
    doist.do(doers=doers)


def main():
    args = parser.parse_args()
    launch(args)


if __name__ == "__main__":
    main()