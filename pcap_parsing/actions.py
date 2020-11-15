import tempfile
import os
from scapy.utils import rdpcap


def pcap_to_scapy(file):
    """
    Convert an uploaded PCAP file into a list of scapy packets
    :param file: UploadedFile containing the PCAP
    :return: PacketList
    """
    # Delete is false here to allow for Windows support. The file is deleted at the end of the method.
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pcap')
    file_name = tmp_file.name
    for chunk in file.chunks():
        tmp_file.write(chunk)
    # For Windows support, we must close the file before we can read it.
    tmp_file.close()
    packets = rdpcap(file_name)
    # Delete that temp file
    os.unlink(file_name)
    return packets


def packlist_to_sanity(packets):
    """
    Convert a PacketList to a list we can actually display
    :param packets:
    :return:
    """
    res = []
    for p in packets:
        res.append(p.show2(dump=True))
    return res
