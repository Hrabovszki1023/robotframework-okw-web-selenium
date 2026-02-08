from ..common.button import Button as CommonButton


class MyProjectButton(CommonButton):
    """Project-specific Button with pre-click wait for a busy/progress overlay.

    Adjust the locator below to match the project's busy indicator.
    """

    # Example: data-testid selector for a global progress bar/overlay
    BUSY_OVERLAY_LOCATOR = {"css": '[data-testid="progress-bar"]'}

    def okw_click(self):
        try:
            # Wait a short moment until the overlay disappears (if present)
            self.adapter.wait_until_not_visible(self.BUSY_OVERLAY_LOCATOR, timeout="5 s")
        except Exception:
            # If overlay not found/timeouts, proceed to click anyway
            pass
        super().okw_click()

