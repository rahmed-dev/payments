# Copyright (c) 2024, Frappe Technologies and contributors
# License: MIT. See LICENSE

from erpnext.accounts.doctype.payment_request.payment_request import (
	PaymentRequest as ERPNextPaymentRequest,
)


class PaymentRequest(ERPNextPaymentRequest):
	def on_payment_authorized(self, status=None):
		"""Called by payment gateways after successful payment.

		Restores v14 behaviour: marks Payment Request as Paid and creates
		the Payment Entry linked to the reference document (Sales Invoice, etc.).
		"""
		if status not in ("Authorized", "Completed"):
			return

		self.set_as_paid()
