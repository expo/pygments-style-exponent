# -*- coding: utf-8 -*-
"""
Exponent color scheme
"""

from pygments.style import Style
from pygments.token import Comment, Error, Keyword, Name, Number, Operator, \
                           Punctuation, String, Text, Generic

BACKGROUND   = "#ffffff"
CURRENT_LINE = "#efefef"
SELECTION    = "#d6d6d6"
FOREGROUND   = "#4d4d4c"
COMMENT      = "#8e908c"
RED          = "#c82829"
ORANGE       = "#f5871f"
YELLOW       = "#eab700"
GREEN        = "#718c00"
AQUA         = "#3e999f"
BLUE         = "#4271ae"
PURPLE       = "#8959a8"


class ExponentStyle(Style):

    """
    Exponent color scheme, based on the Tomorrow theme.
    """

    default_style = ''

    background_color = BACKGROUND
    highlight_color = SELECTION

    styles = {

        Comment:                COMMENT,
        Text:                   FOREGROUND,

        Keyword:                BLUE,
        Keyword.Type:           YELLOW,
        Operator.Word:          '',

        String:                 GREEN,
        String.Char:            FOREGROUND,

        Name.Builtin:           RED,
        Name.Variable:          '',
        Name.Variable.Instance: RED,
        Name.Constant:          GREEN,
        Name.Class:             YELLOW,
        Name.Function:          BLUE,
        Name.Namespace:         YELLOW,
        Name.Exception:         RED,
        Name.Tag:               PURPLE,
        Name.Other:             FOREGROUND,
        # Name.Attribute:        '',
        Name.Decorator:         AQUA,

        Generic.Deleted:        RED,
        Generic.Inserted:       GREEN,
        Generic.Heading:        "bold " + FOREGROUND,
        Generic.Subheading:     "bold " + AQUA,
        Generic.Prompt:         "bold " + COMMENT

}
