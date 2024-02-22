def get_pay_ref_no(doc, method=None):
    if doc.references:
        if doc.mode_of_payment in ['Unified Payment Interface (UPI)', 'Mooflow Credit']:
            mooretail_order_uuid = doc.doc.mooretail_order_uuid  
            related_docs = frappe.get_all(doc.doctype, filters={'mooretail_order_uuid': mooretail_order_uuid})
            for related_doc in related_docs:
                for reference in doc.referinces:
                    reference_name = reference.reference_name
                    reference_type = reference.reference_doctype
                    ref_doc = frappe.get_doc(reference_type, reference_name)
                    if ref_doc:
                        ref_doc.reference_no = doc.reference_no
                        ref_doc.save()
                    else:
                        frappe.throw(f"Document not found for reference name: {reference_name}")
        else:
            frappe.throw("Mode of payment is not supported.")
    else:
        frappe.throw("References list is empty.")
