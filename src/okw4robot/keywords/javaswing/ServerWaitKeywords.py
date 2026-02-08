from robot.api.deco import keyword
from ...runtime.context import context
from requests.exceptions import RequestException

class ServerWaitKeywords:
    # @keyword("Warte Bis JavaRPC-Server Bereit Ist")
    @keyword("Wait Until JavaRPC Server Is Ready")
    def wait_until_ready(self, timeout=10, interval=1):
        """
        Wartet, bis der aktive Java-RPC-Adapter erfolgreich auf `get_object_tree` antwortet.
        """
        import time
        start_time = time.time()
        while True:
            try:
                adapter = context.get_adapter()
                adapter.get_object_tree()
                return  # Erfolg → wir sind fertig
            except Exception as e:
                if time.time() - start_time > timeout:
                    raise RuntimeError(f"Server war nach {timeout}s nicht bereit: {e}")
                time.sleep(interval)
