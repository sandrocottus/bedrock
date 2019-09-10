# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import jinja2
from django_jinja import library

from lib.l10n_utils.fluent import translate, has_all_messages


@library.global_function
@jinja2.contextfunction
def ftl(ctx, message_id, fallback=None, **args):
    """Return the translated string.

    :param ctx: the context from the template
    :param message_id: the ID of the message
    :param fallback: the ID of a message to use if message_id is not translated
    :param args: the other args are passed to the translation as variables
    """
    return jinja2.Markup(translate(message_id, ctx['ftl_files'], fallback, **args))


@library.global_function
@jinja2.contextfunction
def ftl_has_messages(ctx, *message_ids):
    """Return True if the current translation has all of the message IDs."""
    return has_all_messages(message_ids, ctx['ftl_files'])
