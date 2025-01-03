import click
from cfcli.lazy_group import LazyGroup
from cfcli import CFCLI
##
from cfcli.clis import *
def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f'version {CFCLI.VERSION}')
    ctx.exit()


@click.version_option(CFCLI.VERSION, '--version', '-v', callback=print_version)
@click.option('--output', '-o', default='yaml', help='Output format', type=click.Choice(['table', 'yaml'], case_sensitive=False))
@click.group(cls=LazyGroup,
             lazy_subcommands={
                #  "accounts": "cfcli.clis.accounts.accounts",
                #  "acm": "cfcli.clis.acm.acm",
                #  "addressing": "cfcli.clis.addressing.addressing",
                #  "ai_gateway": "cfcli.clis.ai_gateway.ai_gateway",
                #  "alerting": "cfcli.clis.alerting.alerting",
                #  "api_gateway": "cfcli.clis.api_gateway.api_gateway",
                #  "argo": "cfcli.clis.argo.argo",
                #  "billing": "cfcli.clis.billing.billing",
                #  "cache": "cfcli.clis.cache.cache",
                #  "calls": "cfcli.clis.calls.calls",
                #  "certificate_authorities": "cfcli.clis.certificate_authorities.certificate_authorities",
                #  "challenges": "cfcli.clis.challenges.challenges",
                #  "cloud_connector": "cfcli.clis.cloud_connector.cloud_connector",
                #  "cloudforce_one": "cfcli.clis.cloudforce_one.cloudforce_one",
                #  "custom_certificates": "cfcli.clis.custom_certificates.custom_certificates",
                #  "custom_hostnames": "cfcli.clis.custom_hostnames.custom_hostnames",
                #  "client_certificates": "cfcli.clis.client_certificates.client_certificates",
                #  "d1": "cfcli.clis.d1.d1",
                #  "diagnostics": "cfcli.clis.diagnostics.diagnostics",
                #  "dns": "cfcli.clis.dns.dns",
                #  "durable_objects": "cfcli.clis.durable_objects.durable_objects",
                #  "email_routing": "cfcli.clis.email_routing.email_routing",
                #  "event_notifications": "cfcli.clis.event_notifications.event_notifications",
                #  "firewall": "cfcli.clis.firewall.firewall",
                #  "healthchecks": "cfcli.clis.healthchecks.healthchecks",
                #  "hostnames": "cfcli.clis.hostnames.hostnames",
                #  "hyperdrive": "cfcli.clis.hyperdrive.hyperdrive",
                #  "iam": "cfcli.clis.iam.iam",
                #  "images": "cfcli.clis.images.images",
                #  "intel": "cfcli.clis.intel.intel",
                "ips": "cfcli.clis.ips.ips",
                #  "kv": "cfcli.clis.kv.kv",
                #  "load_balancers": "cfcli.clis.load_balancers.load_balancers",
                #  "logpush": "cfcli.clis.logpush.logpush",
                #  "logs": "cfcli.clis.logs.logs",
                #  "magic_network_monitoring": "cfcli.clis.magic_network_monitoring.magic_network_monitoring",
                #  "magic_transit": "cfcli.clis.magic_transit.magic_transit",
                #  "mtls_certificates": "cfcli.clis.mtls_certificates.mtls_certificates",
                #  "origin_tls_client_auth": "cfcli.clis.origin_tls_client_auth.origin_tls_client_auth",
                #  "plan": "cfcli.clis.plan.plan",
                #  "rules": "cfcli.clis.rules.rules",
                #  "ssl": "cfcli.clis.ssl.ssl",
                #  "user": "cfcli.clis.user.user",
                #  "waf": "cfcli.clis.waf.waf",
                "zones": "cfcli.clis.zones.zones",
                 },
             help="A CLI for interacting with Cloudflare.")
def cli(output: str):
    pass