+++
type = "question"
title = "Can Python show if a PcapNG trace file came from 802.11n or 802.11ac?"
description = '''I&#x27;m trying to determine the 802.11 protocol variant - from PcapNG trace files created by wiretap (see relevant question on StackOverflow, and another relevant question on StackOverflow). The link-layer header type for the interface on which the packet was captured is LINKTYPE_IEEE802_11_RADIOTAP (12...'''
date = "2015-03-31T08:52:00Z"
lastmod = "2015-03-31T08:52:00Z"
weight = 41062
keywords = [ "python", "wifi", "802.11", "pcap-ng", "802.11n" ]
aliases = [ "/questions/41062" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can Python show if a PcapNG trace file came from 802.11n or 802.11ac?](/questions/41062/can-python-show-if-a-pcapng-trace-file-came-from-80211n-or-80211ac)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41062-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41062-score" class="post-score" title="current number of votes">0</div><span id="post-41062-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to determine the 802.11 protocol variant - from PcapNG trace files created by wiretap (see <a href="http://stackoverflow.com/questions/29339864/is-there-a-way-to-extract-the-wifi-protocol-type-from-a-pcapng-trace-file/29354788#29354788">relevant question on StackOverflow</a>, and <a href="http://stackoverflow.com/questions/29351577/cannot-understand-802-11-data-frame-format-in-pcapng-file?noredirect=1#comment46892264_29351577">another relevant question on StackOverflow</a>).</p><p>The link-layer header type for the interface on which the packet was captured is <code>LINKTYPE_IEEE802_11_RADIOTAP</code> (127), so I can use <a href="https://code.google.com/p/python-radiotap/source/browse/trunk/radiotap.py?r=3">radiotap.py</a> to extract the <a href="http://www.radiotap.org/defined-fields/Channel">Channel</a> field and thus ascertain if the 802.11 protocol variant is a, b, or g.</p><p>However, to ascertain if I have 802.11n or 802.11ac, I need to access the <a href="http://www.radiotap.org/suggested-fields/XChannel">XChannel</a>/<a href="http://www.radiotap.org/defined-fields/MCS">MCS</a> or the <a href="http://www.radiotap.org/defined-fields/VHT">VHT</a> fields. These fields are not defined in <a href="https://code.google.com/p/python-radiotap/source/browse/trunk/radiotap.py?r=3">radiotap.py</a>, which means I need to extend <a href="https://code.google.com/p/python-radiotap/source/browse/trunk/radiotap.py?r=3">radiotap.py</a>'s <code>parse</code> function.</p><p><em>I tried and failed:</em> I suspect I'm setting the alignment/structures wrong (or some other obscure bug) and the existing <a href="https://code.google.com/p/python-radiotap/source/browse/trunk/radiotap.py?r=3">radiotap.py</a> code isn't helping me much.</p><h2 id="can-anyone-suggest-which-changes-should-i-make-in-radiotap.py-so-itll-recognise-the-xchannel-mcs-and-vht-fields">Can anyone suggest which changes should I make in <a href="https://code.google.com/p/python-radiotap/source/browse/trunk/radiotap.py?r=3">radiotap.py</a> so it'll recognise the <a href="http://www.radiotap.org/suggested-fields/XChannel">XChannel</a>, <a href="http://www.radiotap.org/defined-fields/MCS">MCS</a>, and <a href="http://www.radiotap.org/defined-fields/VHT">VHT</a> fields?</h2><p><br />
</p><p>A sample PcapNG trace file is <a href="https://drive.google.com/folderview?id=0Bw5McUt95YdefnZUaGFDTUQ3TVVWLWtIZjBONTlRdFJnOEpwTzBTSEM5T19RYmdJcm1kS0U&amp;usp=sharing">here</a>.</p><p>My Python code is:</p><pre><code>#!/usr/bin/env python

from pcapng import FileScanner
import radiotap

def hex_str_to_num(hex_str,out_format=&#39;X&#39;):
    if out_format.upper() == &#39;B&#39;:
        return &#39; &#39;.join(format(ord(x), out_format).zfill(8) for x in hex_str)
    else:
        return &#39; &#39;.join(format(ord(x), out_format).zfill(2) for x in hex_str)

def get_protocol_variant(channel):
    &quot;&quot;&quot;
    0x0010  Turbo Channel
    0x0020  CCK channel
    0x0040  OFDM channel
    0x0080  2 GHz spectrum channel
    0x0100  5 GHz spectrum channel
    0x0200  Only passive scan allowed
    0x0400  Dynamic CCK-OFDM channel
    0x0800  GFSK channel (FHSS PHY)

    If link-layer header type for the interface is LINKTYPE_IEEE802_11, protocol variant
    cannot be ascertained.

    If link-layer header type for the interface is LINKTYPE_IEEE802_11_RADIOTAP, then 
    the packet begins with a radiotap header giving various meta-data about the packet.

    If the radiotap header includes the Channel field, then, from the information there,
    the protocol variant may be ascertained as following:

        &quot;5 GHz spectrum channel&quot; + &quot;OFDM channel&quot; = 802.11a;
        &quot;2 GHz spectrum channel&quot; + &quot;CCK channel&quot; = 802.11b;
        &quot;2 GHz spectrum channel&quot; + &quot;OFDM channel&quot; = 802.11g;
        &quot;2 GHz spectrum channel&quot; + &quot;Dynamic CCK-OFDM channel&quot; = 802.11g;
        (the difference between the two flavors of 802.11g indicates whether there 
         might also be 802.11b traffic on the same channel - that&#39;s what the 
         &quot;Dynamic CCK-OFDM channel&quot; indicates).

        However, if the MCS field is present, it&#39;s 802.11n, not any of those other types,
        and if the VHT field is present, it&#39;s 802.11ac.

        There might also be an XChannel field, which can be interpreted similarly to the 
        Channel field, although it also contains some information for 802.11n.
    &quot;&quot;&quot;

    def check(_name, _const):
        _bit = None
        if (channel &amp; _const):
            _bit = True
            print _name,_bit
        return _bit

    TURBO = 0x0010
    CCK   = 0x0020
    OFDM  = 0x0040
    GHz_2 = 0x0080
    GHz_5 = 0x0100
    PASSI = 0x0200
    DYNAM = 0x0400
    GFSK  = 0x0800

    variant = None

    turbo = check(&quot;turbo&quot;, TURBO)
    cck = check(&quot;cck&quot;, CCK)
    ofdm = check(&quot;ofdm&quot;, OFDM)
    ghz_2 = check(&quot;ghz_2&quot;, GHz_2)
    ghz_5 = check(&quot;ghz_5&quot;, GHz_5)
    passi = check(&quot;passi&quot;, PASSI)
    dynam = check(&quot;dynam&quot;, DYNAM)
    gfsk = check(&quot;gfsk&quot;, GFSK)

    if ghz_5 and ofdm:
        variant = &quot;802.11a&quot;
    elif ghz_2 and cck:
        variant = &quot;802.11b&quot;
    elif ghz_2 and ofdm:
        variant = &quot;802.11g&quot;
    elif ghz_2 and dynam:
        variant = &quot;802.11g&quot;

    print &quot;variant&quot;,variant    
    return variant

PCAPNG = &quot;/cygdrive/c/tmp/trace3.pcapng&quot;
MAX = 5
INTERFACEDESCRIPTION = 1
ENHANCEDPACKET = 6
LINKTYPE_IEEE802_11_RADIOTAP = 127

with open(PCAPNG, &quot;r&quot;) as pcapng_file:
    scanner = FileScanner(pcapng_file)
    counter = MAX
    link_type = None
    for block in scanner:
        print
        print &quot;magic_number&quot;,hex(block.magic_number)
        print block

        if block.magic_number == ENHANCEDPACKET:
            if link_type == LINKTYPE_IEEE802_11_RADIOTAP:
                payload_data = block.packet_payload_info[2]
                print &quot;packet_payload_data (hex):&quot;,hex_str_to_num(payload_data,&quot;X&quot;)
                radiotap_dict = radiotap.parse(payload_data)
                radiotap_hedear_len = radiotap.get_length(payload_data)
                print &quot;radiotap_dict&quot;,radiotap_dict
                channel = radiotap_dict[radiotap.RTAP_CHANNEL]
                protocol_variant = get_protocol_variant(channel)
                print &quot;protocol_variant&quot;,protocol_variant
                &quot;&quot;&quot;
                print &quot;channel&quot;,channel,hex(channel),bin(channel)
                print &quot;radiotap_hedear_len&quot;,radiotap_hedear_len
                payload_802_11 = payload_data[radiotap_hedear_len+1:]
                print &quot;payload_802_11 (hex)&quot;,hex_str_to_num(payload_802_11,&quot;X&quot;)
                &quot;&quot;&quot;
        elif block.magic_number == INTERFACEDESCRIPTION:
            link_type = block.link_type

        counter -= 1
        if not counter:
            break</code></pre><p>and its output is:</p><pre><code>magic_number 0xa0d0d0a
SectionHeader(version_major=1, version_minor=0, section_length=-1, options=Options({&#39;shb_userappl&#39;: [u&#39;Dumpcap 1.12.4 (v1.12.4-0-gb4861da from master-1.12)&#39;], &#39;shb_os&#39;: [u&#39;Mac OS X 10.10.2, build 14C109 (Darwin 14.1.0)&#39;]}))

magic_number 0x1
InterfaceDescription(link_type=127, reserved=&#39;\x00\x00&#39;, snaplen=262144, options=Options({&#39;if_os&#39;: [u&#39;Mac OS X 10.10.2, build 14C109 (Darwin 14.1.0)&#39;], &#39;if_tsresol&#39;: [6], &#39;if_name&#39;: [u&#39;en1&#39;]}))

magic_number 0x6
EnhancedPacket(interface_id=0, timestamp_high=332139, timestamp_low=2801116064L, packet_payload_info=(45, 45, &#39;\x00\x00\x19\x00o\x08\x00\x00`I\xb2&amp;\x00\x00\x00\x00\x12\x18q\[email protected]\x01\xb1\xaa\x00\xb4\x00\x90\x00\xf4\x0f\x1b\xb8sL`\x92\x175\x00\x01\xe3\xcf\x00\x12&#39;), options=Options({}))
packet_payload_data (hex): 00 00 19 00 6F 08 00 00 60 49 B2 26 00 00 00 00 12 18 71 16 40 01 B1 AA 00 B4 00 90 00 F4 0F 1B B8 73 4C 60 92 17 35 00 01 E3 CF 00 12
radiotap_dict {0: 649218400, 1: 18, 2: 24, 3: 20977265, 5: -79, 6: -86, 11: 0}
turbo True
cck True
ofdm True
passi True
dynam True
variant None
protocol_variant None

magic_number 0x6
EnhancedPacket(interface_id=0, timestamp_high=332139, timestamp_low=2801116070L, packet_payload_info=(39, 39, &#39;\x00\x00\x19\x00o\x08\x00\x00\x92I\xb2&amp;\x00\x00\x00\x00\x12\x18q\[email protected]\x01\xcd\xaa\x00\xc4\x00`\x00`\x92\x175\x00\x01\xf7eny&#39;), options=Options({}))
packet_payload_data (hex): 00 00 19 00 6F 08 00 00 92 49 B2 26 00 00 00 00 12 18 71 16 40 01 CD AA 00 C4 00 60 00 60 92 17 35 00 01 F7 65 6E 79
radiotap_dict {0: 649218450, 1: 18, 2: 24, 3: 20977265, 5: -51, 6: -86, 11: 0}
turbo True
cck True
ofdm True
passi True
dynam True
variant None
protocol_variant None

magic_number 0x6
EnhancedPacket(interface_id=0, timestamp_high=332139, timestamp_low=2801116213L, packet_payload_info=(57, 57, &#39;\x00\x00\x19\x00o\x08\x00\x00\tJ\xb2&amp;\x00\x00\x00\x00\x12\x18q\[email protected]\x01\xca\xaa\x00\x94\x00\x00\x00`\x92\x175\x00\x01\xf4\x0f\x1b\xb8sL\x04\x00\xc0#\xff\xff\xff\xff\xff\xff\xff\xffX\xd0Y\\&#39;), options=Options({}))
packet_payload_data (hex): 00 00 19 00 6F 08 00 00 09 4A B2 26 00 00 00 00 12 18 71 16 40 01 CA AA 00 94 00 00 00 60 92 17 35 00 01 F4 0F 1B B8 73 4C 04 00 C0 23 FF FF FF FF FF FF FF FF 58 D0 59 5C
radiotap_dict {0: 649218569, 1: 18, 2: 24, 3: 20977265, 5: -54, 6: -86, 11: 0}
turbo True
cck True
ofdm True
passi True</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-pcap-ng" rel="tag" title="see questions tagged &#39;pcap-ng&#39;">pcap-ng</span> <span class="post-tag tag-link-802.11n" rel="tag" title="see questions tagged &#39;802.11n&#39;">802.11n</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Mar '15, 08:52</strong></p><img src="https://secure.gravatar.com/avatar/49126502d466d76912a86cec6cbcf0e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ronbarak&#39;s gravatar image" /><p><span>ronbarak</span><br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ronbarak has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Mar '15, 15:15</strong> </span></p></div></div><div id="comments-container-41062" class="comments-container"></div><div id="comment-tools-41062" class="comment-tools"></div><div class="clear"></div><div id="comment-41062-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

