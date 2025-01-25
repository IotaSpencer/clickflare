import click
from clickflare import ClickFlare
from clickflare.lazy_group import LazyGroup
##
# import clis.*
def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f'Version {ClickFlare.VERSION}')
    ctx.exit()


@click.version_option(ClickFlare.VERSION, '--version', '-v', callback=print_version)
@click.option('--output', '-o', default='yaml', help='Output format', type=click.Choice(['table', 'yaml'], case_sensitive=False))
@click.group(cls=LazyGroup,
             lazy_subcommands={
                "accounts": "clickflare.clis.accounts.accounts",
                #  "acm": "clickflare.clis.acm.acm",
                #  "addressing": "clickflare.clis.addressing.addressing",
                #  "ai_gateway": "clickflare.clis.ai_gateway.ai_gateway",
                #  "alerting": "clickflare.clis.alerting.alerting",
                #  "api_gateway": "clickflare.clis.api_gateway.api_gateway",
                #  "argo": "clickflare.clis.argo.argo",
                #  "billing": "clickflare.clis.billing.billing",
                #  "cache": "clickflare.clis.cache.cache",
                #  "calls": "clickflare.clis.calls.calls",
                #  "certificate_authorities": "clickflare.clis.certificate_authorities.certificate_authorities",
                #  "challenges": "clickflare.clis.challenges.challenges",
                #  "cloud_connector": "clickflare.clis.cloud_connector.cloud_connector",
                #  "cloudforce_one": "clickflare.clis.cloudforce_one.cloudforce_one",
                #  "custom_certificates": "clickflare.clis.custom_certificates.custom_certificates",
                #  "custom_hostnames": "clickflare.clis.custom_hostnames.custom_hostnames",

                #  "client_certificates": "clickflare.clis.client_certificates.client_certificates",
                                #  "d1": "clickflare.clis.d1.d1",
                #  "diagnostics": "clickflare.clis.diagnostics.diagnostics",
                #  "dns": "clickflare.clis.dns.dns",
                #  "durable_objects": "clickflare.clis.durable_objects.durable_objects",
                #  "email_routing": "clickflare.clis.email_routing.email_routing",
                #  "event_notifications": "clickflare.clis.event_notifications.event_notifications",
                #  "firewall": "clickflare.clis.firewall.firewall",
                #  "healthchecks": "clickflare.clis.healthchecks.healthchecks",
                #  "hostnames": "clickflare.clis.hostnames.hostnames",
                #  "hyperdrive": "clickflare.clis.hyperdrive.hyperdrive",
                #  "iam": "clickflare.clis.iam.iam",
                #  "images": "clickflare.clis.images.images",
                #  "intel": "clickflare.clis.intel.intel",
                 "ips": "clickflare.clis.ips.ips",
                #  "kv": "clickflare.clis.kv.kv",
                #  "load_balancers": "clickflare.clis.load_balancers.load_balancers",
                #  "logpush": "clickflare.clis.logpush.logpush",
                #  "logs": "clickflare.clis.logs.logs",
                #  "magic_network_monitoring": "clickflare.clis.magic_network_monitoring.magic_network_monitoring",
                #  "magic_transit": "clickflare.clis.magic_transit.magic_transit",
                #  "mtls_certificates": "clickflare.clis.mtls_certificates.mtls_certificates",
                #  "origin_tls_client_auth": "clickflare.clis.origin_tls_client_auth.origin_tls_client_auth",
                #  "plan": "clickflare.clis.plan.plan",
                #  "rules": "clickflare.clis.rules.rules",
                #  "ssl": "clickflare.clis.ssl.ssl",
                #  "user": "clickflare.clis.user.user",
                #  "waf": "clickflare.clis.waf.waf",
                "zones": "clickflare.clis.zones.zones",
                 },
             help="A CLI for interacting with Cloudflare.")
def cli(output):
    pass