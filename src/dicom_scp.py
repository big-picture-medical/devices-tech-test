from pynetdicom import AE, evt, AllStoragePresentationContexts
from pynetdicom.sop_class import OphthalmicPhotography8BitImageStorage
import logging
import sys


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)


SYNTAX_UIDS = ["1.2.840.10008.1.2", "1.2.840.10008.1.2.1", "1.2.840.10008.1.2.4.50",
               "1.2.840.10008.1.2.4.51", "1.2.840.10008.1.2.4.57", "1.2.840.10008.1.2.4.70",
               "1.2.840.10008.1.2.4.90", "1.2.840.10008.1.2.4.91"]

class DicomSCP:
    def __init__(self):
        self.ae = AE()
        self.ae.ae_title = "BPPACS"
        self.ae.add_supported_context(OphthalmicPhotography8BitImageStorage, SYNTAX_UIDS)

    def start(self):
        self.ae.start_server(('', 11112), evt_handlers=[(evt.EVT_C_ECHO, self.handle_echo), (evt.EVT_C_STORE, self.handle_store)])

    def handle_echo(self, event):
        log.info("Echo called")
        return 0x0000

    def handle_store(self, event):
        log.info("Store received for patient %s" % event.dataset.PatientID)
        return 0x0000


if __name__ == '__main__':
    scp = DicomSCP()
    scp.start()
