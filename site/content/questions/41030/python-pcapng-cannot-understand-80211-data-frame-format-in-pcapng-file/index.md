+++
type = "question"
title = "python-pcapng: cannot understand 802.11 Data Frame format in PcapNG file"
description = '''I have PcapNG files created by Wireshark, which I try to parse with python-pcapng. However, I cannot figure out how to reconcile the output I receive from FileScanner&#x27;s packet_payload_info with the 802.11 Data frame format:  This is the output I get (my code is at the bottom): magic_number 0xa0d0d0a...'''
date = "2015-03-30T11:06:00Z"
lastmod = "2015-03-30T13:10:00Z"
weight = 41030
keywords = [ "python", "pcapng", "802.11", "wireshark", "wifi" ]
aliases = [ "/questions/41030" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [python-pcapng: cannot understand 802.11 Data Frame format in PcapNG file](/questions/41030/python-pcapng-cannot-understand-80211-data-frame-format-in-pcapng-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41030-score" class="post-score" title="current number of votes">0</div><span id="post-41030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have <em>PcapNG</em> files created by Wireshark, which I try to parse with <code>python-pcapng</code>.</p><p>However, I cannot figure out how to reconcile the output I receive from <code>FileScanner</code>'s <code>packet_payload_info</code> with the <em>802.11 Data frame format</em>:</p><p><img src="http://i.stack.imgur.com/4E5DQ.png" alt="802.11 Data frame format" /></p><p>This is the output I get (my code is at the bottom):</p><pre><code>magic_number 0xa0d0d0a
SectionHeader(version_major=1, version_minor=0, section_length=-1, options=Options({&#39;shb_userappl&#39;: [u&#39;Dumpcap 1.12.4 (v1.12.4-0-gb4861da from master-1.12)&#39;], &#39;shb_os&#39;: [u&#39;Mac OS X 10.10.2, build 14C109 (Darwin 14.1.0)&#39;]}))

magic_number 0x1
InterfaceDescription(link_type=127, reserved=&#39;\x00\x00&#39;, snaplen=262144, options=Options({&#39;if_os&#39;: [u&#39;Mac OS X 10.10.2, build 14C109 (Darwin 14.1.0)&#39;], &#39;if_tsresol&#39;: [6], &#39;if_name&#39;: [u&#39;en1&#39;]}))

magic_number 0x6
EnhancedPacket(interface_id=0, timestamp_high=332139, timestamp_low=2801116064L, packet_payload_info=(45, 45, &#39;\x00\x00\x19\x00o\x08\x00\x00`I\xb2&amp;\x00\x00\x00\x00\x12\x18q\[email protected]\x01\xb1\xaa\x00\xb4\x00\x90\x00\xf4\x0f\x1b\xb8sL`\x92\x175\x00\x01\xe3\xcf\x00\x12&#39;), options=Options({}))

packet_payload_info      : (45, 45, &#39;\x00\x00\x19\x00o\x08\x00\x00`I\xb2&amp;\x00\x00\x00\x00\x12\x18q\[email protected]\x01\xb1\xaa\x00\xb4\x00\x90\x00\xf4\x0f\x1b\xb8sL`\x92\x175\x00\x01\xe3\xcf\x00\x12&#39;)

packet_payload_data (hex): 00 00 19 00 6F 08 00 00 60 49 B2 26 00 00 00 00 12 18 71 16 40 01 B1 AA 00 B4 00 90 00 F4 0F 1B B8 73 4C 60 92 17 35 00 01 E3 CF 00 12

packet_payload_data (bin): 00000000 00000000 00011001 00000000 01101111 00001000 00000000 00000000 01100000 01001001 10110010 00100110 00000000 00000000 00000000 00000000 00010010 00011000 01110001 00010110 01000000 00000001 10110001 10101010 00000000 10110100 00000000 10010000 00000000 11110100 00001111 00011011 10111000 01110011 01001100 01100000 10010010 00010111 00110101 00000000 00000001 11100011 11001111 00000000 00010010</code></pre><p><strong>Could you tell me where does the <code>packet_payload_data</code> fit in the 802.11 Data frame?</strong>*</p><p>*i.e., where does its first byte fit in the frame<br />
<br />
</p><p><strong><em>Python code:</em></strong></p><pre><code>#!/usr/bin/env python

from pcapng import FileScanner

def hex_str_to_num(hex_str,out_format=&#39;X&#39;):
    if out_format.upper() == &#39;B&#39;:
        return &#39; &#39;.join(format(ord(x), out_format).zfill(8) for x in hex_str)
    else:
        return &#39; &#39;.join(format(ord(x), out_format).zfill(2) for x in hex_str)

PCAPNG = &quot;/cygdrive/c/tmp/LivePerson/lana/trace3.pcapng&quot;
MAX = 3
ENHANCEDPACKET_ID = 6

with open(PCAPNG, &quot;r&quot;) as pcapng_file:
    scanner = FileScanner(pcapng_file)
    counter = MAX
    for block in scanner:
        print
        print &quot;magic_number&quot;,hex(block.magic_number)
        print block

        if block.magic_number == ENHANCEDPACKET_ID:
            print
            payload_data = block.packet_payload_info[2]
            print &quot;packet_payload_info      :&quot;,block.packet_payload_info,&quot;\n&quot;
            print &quot;packet_payload_data (hex):&quot;,hex_str_to_num(payload_data,&quot;X&quot;),&quot;\n&quot;
            print &quot;packet_payload_data (bin):&quot;,hex_str_to_num(payload_data,&quot;b&quot;)

        counter -= 1
        if not counter:
            break</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-pcapng" rel="tag" title="see questions tagged &#39;pcapng&#39;">pcapng</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '15, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/49126502d466d76912a86cec6cbcf0e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ronbarak&#39;s gravatar image" /><p><span>ronbarak</span><br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ronbarak has no accepted answers">0%</span> </br></br></p></img></div></div><div id="comments-container-41030" class="comments-container"></div><div id="comment-tools-41030" class="comment-tools"></div><div class="clear"></div><div id="comment-41030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41036"></span>

<div id="answer-container-41036" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41036-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41036-score" class="post-score" title="current number of votes">0</div><span id="post-41036-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ronbarak has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As indicated by your python library, the link type used for this capture is 127, which means LINKTYPE_IEEE802_11_RADIOTAP (as listed on tcpdump link-layer header type values <a href="http://www.tcpdump.org/linktypes.html">page</a>). The radiotap format (the one found in your payload data) is specified <a href="http://www.radiotap.org/">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '15, 13:10</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-41036" class="comments-container"></div><div id="comment-tools-41036" class="comment-tools"></div><div class="clear"></div><div id="comment-41036-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

