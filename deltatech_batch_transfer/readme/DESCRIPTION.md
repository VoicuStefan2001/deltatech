- Improves functionality of the batch picking module by managing the "empty" pickings (pickings which have all qty's
  done=zero). Odoo standard will process all quantities for those pickings, if in batch. There are two options:

  - If system parameter "deltatech_batch_keep_pickings" is not present, the empty pickings are removed from the batch
    when the \<Validate\> button is pressed. Only non-empty pickings will be processed. You can manually add the empty
    pickings to another batch (recommended). If all pickings in the batch are empty, the batch will become empty
  - If system parameter "deltatech_batch_keep_pickings" is present, the empty picking will not be processed, but it will
    remain in the batch to be processed later (not recommended, it doesn't behave well in the barcode interface).
  - Added fields direction, reference, note