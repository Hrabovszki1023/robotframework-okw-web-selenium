"""WebSe_Table -- Selenium-Implementierung fuer HTML-Tabellen.

Navigiert die DOM-Struktur (thead/tbody/tr/td/th) fuer Zeilen-/Spalten-Zugriff.
"""

from .webse_base import WebSe_Base


class WebSe_Table(WebSe_Base):

    def _root(self):
        return self.sl.get_webelement(self.adapter._resolve(self.locator))

    def _header_cells(self):
        tbl = self._root()
        heads = tbl.find_elements("css selector", "thead tr th")
        if heads:
            return heads
        heads = tbl.find_elements("css selector", "tr th")
        if heads:
            return heads
        row = tbl.find_elements("css selector", "tr")
        if row:
            return row[0].find_elements("css selector", "td")
        return []

    def _data_rows(self):
        tbl = self._root()
        rows = tbl.find_elements("css selector", "tbody tr")
        if rows:
            return rows
        return tbl.find_elements("css selector", "tr")

    def _row_cells(self, row_el):
        cells = row_el.find_elements("css selector", "td")
        if cells:
            return cells
        return row_el.find_elements("css selector", "th")

    # ------------------------------------------------------------------
    # Tabellen-Methoden (OkwWidget-Interface)
    # ------------------------------------------------------------------
    def get_row_texts(self, row_index: int) -> list[str]:
        if row_index == 0:
            return [c.text or "" for c in self._header_cells()]
        rows = self._data_rows()
        if 1 <= row_index <= len(rows):
            cells = self._row_cells(rows[row_index - 1])
            return [c.text or "" for c in cells]
        return []

    def get_column_texts(self, col_index: int) -> list[str]:
        out = []
        rows = self._data_rows()
        for r in rows:
            cells = self._row_cells(r)
            if 1 <= col_index <= len(cells):
                out.append(cells[col_index - 1].text or "")
            else:
                out.append("")
        return out

    def get_cell_text(self, row_index: int, col_index: int) -> str:
        if row_index == 0:
            heads = self._header_cells()
            if 1 <= col_index <= len(heads):
                return heads[col_index - 1].text or ""
            return ""
        rows = self._data_rows()
        if 1 <= row_index <= len(rows):
            cells = self._row_cells(rows[row_index - 1])
            if 1 <= col_index <= len(cells):
                return cells[col_index - 1].text or ""
        return ""

    def get_row_count(self) -> int:
        return len(self._data_rows())

    def get_column_count(self) -> int:
        heads = self._header_cells()
        if heads:
            return len(heads)
        rows = self._data_rows()
        mx = 0
        for r in rows:
            mx = max(mx, len(self._row_cells(r)))
        return mx

    def get_header_names(self) -> list[str]:
        return [c.text or "" for c in self._header_cells()]
