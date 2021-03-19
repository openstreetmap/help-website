+++
type = "question"
title = "Packet detail tree missing items in TShark but not WireShark"
description = '''I really hope someone can help me figure this one out. I am trying to output the SNMP data in a single packet right now(only one for testing right now). The packet was a part of a wireshark capture.  When I load the capture file with the single packet in it and it has the -V parameter, it loads the ...'''
date = "2014-03-25T23:48:00Z"
lastmod = "2014-03-26T08:38:00Z"
weight = 31162
keywords = [ "snmp", "decoding", "protocol", "tshark", "wireshark" ]
aliases = [ "/questions/31162" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Packet detail tree missing items in TShark but not WireShark](/questions/31162/packet-detail-tree-missing-items-in-tshark-but-not-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31162-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I really hope someone can help me figure this one out. I am trying to output the SNMP data in a single packet right now(only one for testing right now). The packet was a part of a wireshark capture.</p><p>When I load the capture file with the single packet in it and it has the -V parameter, it loads the tree, although it is missing layers, and at the bottom it is showing a hex dump in the tree. The strange part is that Wireshark shows them all. I will add that this packet is a received SNMP response, and when I try and load the sent request packet it shows the OIDS and the SNMP info!</p><p>I have no idea why this is happening. To add insult to injury, when I try and show only the SNMP Value OCTET fields(Which is what I need, and I am glad I found this feature) I get no output. <code>-T fields -e snmp.value.octets</code>.</p><p>If you look at this image from wireshark you will see the SNMP fields. That is the layer I need. As you can see Wireshark is perfectly capable of decoding it. (This is actually a different packet from the same capture, but I can assure you wireshark decoded the other packet just fine)</p><p><img src="https://osqa-ask.wireshark.org/upfiles/stackoverflowsnmp.png" alt="alt text" /></p><p>If you look at this output you will notice that it doesn't even include the SNMP layer and it includes hex in it(im guessing instead).</p><pre><code>Frame 1: 506 bytes on wire (4048 bits), 506 bytes captured (4048 bits)
    Arrival Time: Mar 25, 2014 02:27:30.983837000 Eastern Daylight Time
    Epoch Time: 1395728850.983837000 seconds
    [Time delta from previous captured frame: 0.000000000 seconds]
    [Time delta from previous displayed frame: 0.000000000 seconds]
    [Time since reference or first frame: 0.000000000 seconds]
    Frame Number: 1
    Frame Length: 506 bytes (4048 bits)
    Capture Length: 506 bytes (4048 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ip:data]
Ethernet II, Src: CiscoSpv_8a:40:b7 (xxxxxxxxxxx), Dst: xxxxxxxx:5e:0d (xxxxxxxxxxxxxxx)
    Destination: SgmTechn_b6:5e:0d (00:22:95:b6:5e:0d)
        Address: SgmTechn_b6:5e:0d (00:22:95:b6:5e:0d)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
    Source: CiscoSpv_8a:40:b7 (54:d4:6f:8a:40:b7)
        Address: CiscoSpv_8a:40:b7 (54:d4:6f:8a:40:b7)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
    Type: IP (0x0800)
Internet Protocol Version 4, Src: 192.168.100.1 (192.168.100.1), Dst: 192.168.100.11 (192.168.100.11)
    Version: 4
    Header length: 20 bytes
    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
        0000 00.. = Differentiated Services Codepoint: Default (0x00)
        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
    Total Length: 492
    Identification: 0x4b36 (19254)
    Flags: 0x00
        0... .... = Reserved bit: Not set
        .0.. .... = Don&#39;t fragment: Not set
        ..0. .... = More fragments: Not set
    Fragment offset: 2960
    Time to live: 64
    Protocol: UDP (17)
    Header checksum: 0xe2fb [correct]
        [Good: True]
        [Bad: False]
    Source: 192.168.100.1 (192.168.100.1)
    Destination: 192.168.100.11 (192.168.100.11)
Data (472 bytes)

0000  c6 1d 93 ad d8 17 e2 be 9c 79 19 37 42 19 8a c2   .........y.7B...
0010  ea 21 ac fb e4 4f 9e c0 79 c9 00 00 00 00 00 00   .!...O..y.......
0020  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0030  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0040  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0050  00 00 00 00 00 00 00 00 00 00 00 00 00 00 30 82   ..............0.
0060  01 76 06 0c 2b 06 01 04 01 89 0e 01 13 04 36 00   .v..+.........6.
0070  04 82 01 64 01 0e 30 82 01 0a 02 82 01 01 00 c0   ...d..0.........
0080  ef 36 9d 7b da b0 a9 38 e6 ed 29 c3 8d 3a 88 9f   .6.{...8..)..:..
0090  82 48 a7 b7 c5 1e 63 55 f6 53 6f 5b da 39 8b f6   .H....cU.So[.9..
00a0  19 a1 1b 3c 0f 64 91 2d 13 3c ff b6 05 06 4e a8   ...&lt;.d.-.&lt;....N.
00b0  4a 65 c9 90 a9 fc a5 17 56 e6 6c 2e ff ad 6c e0   Je......V.l...l.
00c0  15 90 ab f5 a1 a0 f5 0a c0 52 21 f2 36 4d f3 c4   .........R!.6M..
00d0  d4 37 13 a1 cf 68 1d fa c4 79 69 0b 73 50 4b ca   .7...h...yi.sPK.
00e0  82 78 d4 1c ad 50 d9 84 9b 56 55 2d e2 d2 e0 48   .x...P...VU-...H
00f0  07 28 32 8c 36 e1 05 30 51 51 3e 14 05 f4 65 5f   .(2.6..0QQ&gt;...e_
0100  29 81 e0 31 eb 76 c9 0f 9b 31 00 d1 a4 ae cd 55   )..1.v...1.....U
0110  96 6d 60 71 ab f4 02 f7 65 64 b1 f4 f4 cb 0b f4   .m`q....ed......
0120  a1 3e a9 51 2f de 4a 2a 21 9c 27 e9 25 3f 41 f8   .&gt;.Q/.J*!.&#39;.%?A.
0130  58 53 fc 52 e0 fc a5 98 e5 c9 d8 bb d4 7b cb b5   XS.R.........{..
0140  49 4e 99 36 d5 1c b0 eb 66 ef 0b 0a 4f 0c dd 08   IN.6....f...O...
0150  e8 ca d1 14 8f 4c 37 d9 02 c0 83 cf 8e b1 96 42   .....L7........B
0160  31 70 b2 66 84 bf 67 30 c0 99 d2 71 7c 8f 1a e5   1p.f..g0...q|...
0170  3e af 67 3c 8e c8 e5 bf 7b a4 a4 1e df 8f e3 02   &gt;.g&lt;....{.......
0180  03 01 00 01 00 00 00 00 00 00 00 00 00 00 00 00   ................
0190  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
01a0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
01b0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
01c0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
01d0  00 00 00 00 00 00 00 00                           ........
    Data: c61d93add817e2be9c79193742198ac2ea21acfbe44f9ec0...
    [Length: 472]</code></pre><p><strong>Could this have something to do with it being fragmented and reassembled or maybe to long? I tried messing around with almost all the options and couldn't figure it out. All I want to do is output the Octet String value as seen in the image under Variable bindings but I can't do that until I can get the correct data. I really hope someone can help.</strong></p><p>I know this is getting very long but I figure I should show you the request packet that I sent out. Here is the output from that- done with Tshark aswell. As you can see it shows the SNMP layer just fine. The values are null because this is a request packet. The response values are the ones I am looking to get.</p><pre><code>Frame 1: 200 bytes on wire (1600 bits), 200 bytes captured (1600 bits)
    Arrival Time: Mar 24, 2014 02:46:56.639005000 Eastern Daylight Time
    Epoch Time: 1395643616.639005000 seconds
    [Time delta from previous captured frame: 0.000000000 seconds]
    [Time delta from previous displayed frame: 0.000000000 seconds]
    [Time since reference or first frame: 0.000000000 seconds]
    Frame Number: 1
    Frame Length: 200 bytes (1600 bits)
    Capture Length: 200 bytes (1600 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ip:udp:snmp]
Ethernet II, Src: Applicon_c5:c1:a1 (xxxxxxxxxxxxx), Dst: CiscoSpv_8a:40:b7 (xxxxxxxxxxxxx)
    Destination: CiscoSpv_8a:40:b7 (xxxxxxxxxxxxxx)
        Address: CiscoSpv_8a:40:b7 (xxxxxxxxxxxxxx)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
    Source: Applicon_c5:c1:a1 (xxxxxxxxxxxxxx)
        Address: Applicon_c5:c1:a1 (xxxxxxxxxxxxxx)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
    Type: IP (0x0800)
Internet Protocol Version 4, Src: 192.168.100.11 (192.168.100.11), Dst: 192.168.100.1 (192.168.100.1)
    Version: 4
    Header length: 20 bytes
    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
        0000 00.. = Differentiated Services Codepoint: Default (0x00)
        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
    Total Length: 186
    Identification: 0x051c (1308)
    Flags: 0x00
        0... .... = Reserved bit: Not set
        .0.. .... = Don&#39;t fragment: Not set
        ..0. .... = More fragments: Not set
    Fragment offset: 0
    Time to live: 64
    Protocol: UDP (17)
    Header checksum: 0x2bba [correct]
        [Good: True]
        [Bad: False]
    Source: 192.168.100.11 (192.168.100.11)
    Destination: 192.168.100.1 (192.168.100.1)
User Datagram Protocol, Src Port: 60856 (60856), Dst Port: snmp (161)
    Source port: 60856 (60856)
    Destination port: snmp (161)
    Length: 166
    Checksum: 0x870f [validation disabled]
        [Good Checksum: False]
        [Bad Checksum: False]
Simple Network Management Protocol
    version: v2c (1)
    community: xxxxxxx
    data: get-request (0)
        get-request
            request-id: 597494732
            error-status: noError (0)
            error-index: 0
            variable-bindings: 7 items
                1.3.6.1.4.1.1166.1.19.4.4.0: Value (Null)
                    Object Name: 1.3.6.1.4.1.1166.1.19.4.4.0 (iso.3.6.1.4.1.1166.1.19.4.4.0)
                    Value (Null)
                1.3.6.1.4.1.1166.1.19.4.6.0: Value (Null)
                    Object Name: 1.3.6.1.4.1.1166.1.19.4.6.0 (iso.3.6.1.4.1.1166.1.19.4.6.0)
                    Value (Null)
                1.3.6.1.4.1.1166.1.19.4.50.0: Value (Null)
                    Object Name: 1.3.6.1.4.1.1166.1.19.4.50.0 (iso.3.6.1.4.1.1166.1.19.4.50.0)
                    Value (Null)
                1.3.6.1.4.1.1166.1.19.4.51.0: Value (Null)
                    Object Name: 1.3.6.1.4.1.1166.1.19.4.51.0 (iso.3.6.1.4.1.1166.1.19.4.51.0)
                    Value (Null)
                1.3.6.1.4.1.1166.1.19.4.52.0: Value (Null)
                    Object Name: 1.3.6.1.4.1.1166.1.19.4.52.0 (iso.3.6.1.4.1.1166.1.19.4.52.0)
                    Value (Null)
                1.3.6.1.4.1.1166.1.19.4.53.0: Value (Null)
                    Object Name: 1.3.6.1.4.1.1166.1.19.4.53.0 (iso.3.6.1.4.1.1166.1.19.4.53.0)
                    Value (Null)
                1.3.6.1.4.1.1166.1.19.4.54.0: Value (Null)
                    Object Name: 1.3.6.1.4.1.1166.1.19.4.54.0 (iso.3.6.1.4.1.1166.1.19.4.54.0)
                    Value (Null)</code></pre><p>Any help would be greatly appreciated. Thank you.</p></div><div id="question-tags" class="tags-container tags">snmp decoding protocol tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '14, 23:48</strong></p><img src="https://secure.gravatar.com/avatar/6438826b56b89f1ac63250ed5f455095?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joe%20Page&#39;s gravatar image" /><p>Joe Page<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joe Page has no accepted answers">0%</span></p></img></div></div><div id="comments-container-31162" class="comments-container"><span id="31168"></span><div id="comment-31168" class="comment"><div id="post-31168-score" class="comment-score"></div><div class="comment-text"><p>Odd that the "broken" packet indicates that the frame doesn't contain udp <code>[Protocols in frame: eth:ip:data]</code>.</p><p>What sort of output do you get if you use Wireshark to "Export Packet Dissections" as a "Plain Text" file?</p><p>It would also be helpful if you could post a pcap containing the offending frame somewhere publicly accessible, i.e. <a href="http://cloudshark.org">CloudShark</a>.</p></div><div id="comment-31168-info" class="comment-info"><span class="comment-age">(26 Mar '14, 03:28)</span> grahamb ♦</div></div><span id="31173"></span><div id="comment-31173" class="comment"><div id="post-31173-score" class="comment-score"></div><div class="comment-text"><p>Thanks for replying. After you mentioned that I found something interesting. When I export from Wireshark as text I get exactly what I am looking for. The packet detail tree comes out in full but when I select the packet and export it as a pcap and re-open it in wireshark, the packets protocol is IPVR and the info is "Fragmented Ip Protocol". I believe this is a bug in Wireshark/TShark. When I ran some tests with unfragmented packets I had no issues. Although with three or more fragments, it will only decode the first two. So this obviously has something to do with Tshark having an issue with saving the reconstructed SNMP packet after capture after it is over a certain size. In the broken packet above, the part with the hex byte array is actually my third fragment. So Tshark just isn't decoding my third fragment. When running a pcap with a smaller packet, it decodes it just fine. Do you know of any settings that could help me, or should I put in a bug report for this issue? It makes sense why the UDP didn't show, it is because it is now a "fragmented ip protocol" packet instead of a UDP/SNMP packet.</p></div><div id="comment-31173-info" class="comment-info"><span class="comment-age">(26 Mar '14, 08:05)</span> Joe Page</div></div><span id="31176"></span><div id="comment-31176" class="comment"><div id="post-31176-score" class="comment-score"></div><div class="comment-text"><p>Earlier you said that wireshark did show the details correctly, but now you're saying it doesn't? I'm confused. When you open up your new pcap file in wireshark, how many frames are displayed?</p><p>You can't save a single fragmented IP packet as a single frame and expect it to be decoded correctly again when you load the file with just the one packet. The whole SNMP "packet" (and UDP packet for that matter) is really made up of multiple IP fragments, each in a separate frame, each frame being an IP fragment packet. When you export to a new file, if you only save the last frame, it only has the last IP fragment. Since every fragment but the first one only has a IP header and no UDP header, the last fragment won't be decoded by SNMP dissector... and even it were it would be malformed since it's missing the previous frames.</p><p>Wireshark was changed back in version ~1.7 or so to export all the fragment packets/frames to the new pcap file, to prevent this problem. Tshark's exporting is trickier, but it sounds like you created the new pcap file using Wireshark so I'll ignore Tshark.</p><p>Once you have a new pcap file, so long as it has all the IP fragments of the single UDP/SNMP packet, both Wireshark and Tshark should be able to dissect it properly.</p></div><div id="comment-31176-info" class="comment-info"><span class="comment-age">(26 Mar '14, 08:28)</span> Hadriel</div></div><span id="31302"></span><div id="comment-31302" class="comment"><div id="post-31302-score" class="comment-score"></div><div class="comment-text"><p>@Hadriel Thanks for the help. I meant that Wireshark decoded the packet properly. You are right, this issue was because I only included the reassembled frame. I did not know that the Ipv4 fragment frames had to be saved with the assembled SNMP frame. Thanks again for your help.</p></div><div id="comment-31302-info" class="comment-info"><span class="comment-age">(30 Mar '14, 18:16)</span> Joe Page</div></div></div><div id="comment-tools-31162" class="comment-tools"></div><div class="clear"></div><div id="comment-31162-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31178"></span>

<div id="answer-container-31178" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31178-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, I now see in the broken frame that the IP fragment offset isn't zero, i.e. it's part of an IP fragmented message.</p><p>Tshark isn't going to be able to dissect the snmp message unless you provide all the data, so you'll have to export all the frames that have parts of the IP fragments so tshark can reassemble them and then dissect the snmp data.</p><p>One part of your question bothers me though, are you saying that after exporting the single frame from Wireshark, you can then open that single frame pcap again in Wireshark and it does dissect the snmp data? Does it do this if you stop and restart Wireshark before opening the single frame pcap?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '14, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-31178" class="comments-container"><span id="31303"></span><div id="comment-31303" class="comment"><div id="post-31303-score" class="comment-score"></div><div class="comment-text"><p>Hi Graham. Thanks for your informative answer. The problem was exactly that, I was missing the Ipv4 fragments/frames to go along with the SNMP frame. I did not realize that the fragments had to be exported with the re-assembled packet. I made the assumption that once the packet was reassembled, it did not require the fragments any more as long as I exported the reassembled packet. Thank you though, this solved my issue.</p></div><div id="comment-31303-info" class="comment-info"><span class="comment-age">(30 Mar '14, 18:22)</span> Joe Page</div></div></div><div id="comment-tools-31178" class="comment-tools"></div><div class="clear"></div><div id="comment-31178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

