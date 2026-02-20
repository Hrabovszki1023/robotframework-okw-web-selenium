"""okw_web_selenium.widgets -- Selenium-Web-Widget-Klassen.

Neue WebSe_* Architektur (Delegation):
    WebSe_Base          -- gemeinsame Selenium-Logik
    WebSe_TextField     -- input[type=text], input[type=password], ...
    WebSe_MultilineField -- textarea
    WebSe_Button        -- button, input[type=submit], ...
    WebSe_Link          -- a[href]
    WebSe_Label         -- span, div, p (read-only Text)
    WebSe_CheckBox      -- input[type=checkbox]
    WebSe_ComboBox      -- select, editierbare Combos
    WebSe_RadioList     -- input[type=radio] Gruppen
    WebSe_ListBox       -- select[multiple]
    WebSe_Table         -- table

Legacy widgets/common/ Klassen bleiben vorerst erhalten.
"""

from .webse_base import WebSe_Base
from .webse_textfield import WebSe_TextField
from .webse_multilinefield import WebSe_MultilineField
from .webse_button import WebSe_Button
from .webse_link import WebSe_Link
from .webse_label import WebSe_Label
from .webse_checkbox import WebSe_CheckBox
from .webse_combobox import WebSe_ComboBox
from .webse_radiolist import WebSe_RadioList
from .webse_listbox import WebSe_ListBox
from .webse_table import WebSe_Table

__all__ = [
    "WebSe_Base",
    "WebSe_TextField",
    "WebSe_MultilineField",
    "WebSe_Button",
    "WebSe_Link",
    "WebSe_Label",
    "WebSe_CheckBox",
    "WebSe_ComboBox",
    "WebSe_RadioList",
    "WebSe_ListBox",
    "WebSe_Table",
]
