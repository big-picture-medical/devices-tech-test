from pydicom import dcmread
from pynetdicom import AE, build_context
from pynetdicom.sop_class import OphthalmicPhotography8BitImageStorage
import sys
import os.path


if __name__ == '__main__':
    pathname = os.path.dirname(sys.argv[0])
    ds = dcmread(os.path.join(pathname, "test_dicom.dcm"))

    ae = AE()
    context = build_context(OphthalmicPhotography8BitImageStorage, transfer_syntax="1.2.840.10008.1.2.4.70")
    assoc = ae.associate('127.0.0.1', 11112, contexts=[context])
    if assoc.is_established:
        assoc.send_c_store(ds)
        assoc.release()

    else:
        print("Association rejected. Ensure the DICOM SCP is running.")


