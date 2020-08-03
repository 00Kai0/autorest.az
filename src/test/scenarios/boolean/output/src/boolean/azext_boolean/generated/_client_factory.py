# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_boolean_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.boolean import AutoRestTestService
    from azure.core.pipeline.policies import SansIOHTTPPolicy
    return get_mgmt_service_client(cli_ctx,
                                   AutoRestTestService,
                                   subscription_bound=False,
                                   base_url_bound=False,
                                   authentication_policy=SansIOHTTPPolicy())


def cf_bool(cli_ctx, *_):
    return cf_boolean_cl(cli_ctx).bool