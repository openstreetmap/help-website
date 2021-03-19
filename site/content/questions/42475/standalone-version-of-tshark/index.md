+++
type = "question"
title = "Standalone version of tshark"
description = '''I am using ubuntu 14.10 and doing some post-processing on output from tshark tshark -r pcapFile -V -P -x. The problem is, the format of info line looks different between versions. On TShark 1.10.6 6 0.000569 10.10.11.37 46145 10.10.10.161 80 HTTP 152 GET / HTTP/1.0  On TShark 1.12.1 6 0.000569 10.10...'''
date = "2015-05-17T20:30:00Z"
lastmod = "2015-05-18T16:21:00Z"
weight = 42475
keywords = [ "tshark" ]
aliases = [ "/questions/42475" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Standalone version of tshark](/questions/42475/standalone-version-of-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42475-score" class="post-score" title="current number of votes">0</div><span id="post-42475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using ubuntu 14.10 and doing some post-processing on output from tshark <code>tshark -r pcapFile -V -P -x</code>. The problem is, the format of info line looks different between versions.</p><p>On TShark 1.10.6</p><pre><code>6   0.000569  10.10.11.37 46145 10.10.10.161 80 HTTP 152 GET / HTTP/1.0</code></pre><p>On TShark 1.12.1</p><pre><code>6   0.000569  10.10.11.37 -&gt; 10.10.10.161 HTTP 152 GET / HTTP/1.0</code></pre><p>On the version 1.12.1, I don't see the port numbers (src, dst) as on version 1.10.6.</p><p>I am thinking of using a standalone tshark executable (say for 1.10.6), but the current tshark has lots of dependencies. Wonder where to get one or how to create one. Thanks.</p><p><strong>Edit 1</strong> I need the output to be like the following. The problem is, if I use "-T" options for tshark to influence the output of "info" line (the first line), I will not be able to have the rest of the output lines.</p><pre><code>  4   0.000342 10.10.10.161 -&gt; 10.10.11.37  TCP 62 80→46145 [SYN, ACK] Seq=0 Ack=1 Win=5840 Len=0 MSS=1460 SACK_PERM=1
Frame 4: 62 bytes on wire (496 bits), 62 bytes captured (496 bits)
    Encapsulation type: Ethernet (1)
    Arrival Time: Sep 18, 2009 10:53:55.465815000 CDT
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1253289235.465815000 seconds
    [Time delta from previous captured frame: 0.000178000 seconds]
    [Time delta from previous displayed frame: 0.000178000 seconds]
    [Time since reference or first frame: 0.000342000 seconds]
    Frame Number: 4
    Frame Length: 62 bytes (496 bits)
    Capture Length: 62 bytes (496 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:ip:tcp]
Ethernet II, Src: Dell_8c:d7:8c (00:13:72:8c:d7:8c), Dst: Dell_32:44:cb (00:1e:c9:32:44:cb)
    Destination: Dell_32:44:cb (00:1e:c9:32:44:cb)
        Address: Dell_32:44:cb (00:1e:c9:32:44:cb)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Source: Dell_8c:d7:8c (00:13:72:8c:d7:8c)
        Address: Dell_8c:d7:8c (00:13:72:8c:d7:8c)
        .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
        .... ...0 .... .... .... .... = IG bit: Individual address (unicast)
    Type: IP (0x0800)
Internet Protocol Version 4, Src: 10.10.10.161 (10.10.10.161), Dst: 10.10.11.37 (10.10.11.37)
    Version: 4
    Header Length: 20 bytes
    Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
        0000 00.. = Differentiated Services Codepoint: Default (0x00)
        .... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
    Total Length: 48
    Identification: 0x0000 (0)
    Flags: 0x02 (Don&#39;t Fragment)
        0... .... = Reserved bit: Not set
        .1.. .... = Don&#39;t fragment: Set
        ..0. .... = More fragments: Not set
    Fragment offset: 0
    Time to live: 64
    Protocol: TCP (6)
    Header checksum: 0x10ef [validation disabled]
        [Good: False]
        [Bad: False]
    Source: 10.10.10.161 (10.10.10.161)
    Destination: 10.10.11.37 (10.10.11.37)
    [Source GeoIP: Unknown]
    [Destination GeoIP: Unknown]
Transmission Control Protocol, Src Port: 80 (80), Dst Port: 46145 (46145), Seq: 0, Ack: 1, Len: 0
    Source Port: 80 (80)
    Destination Port: 46145 (46145)
    [Stream index: 0]
    [TCP Segment Len: 0]
    Sequence number: 0    (relative sequence number)
    Acknowledgment number: 1    (relative ack number)
    Header Length: 28 bytes
    .... 0000 0001 0010 = Flags: 0x012 (SYN, ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Nonce: Not set
        .... 0... .... = Congestion Window Reduced (CWR): Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 0... = Push: Not set
        .... .... .0.. = Reset: Not set
        .... .... ..1. = Syn: Set
            [Expert Info (Chat/Sequence): Connection establish acknowledge (SYN+ACK): server port 80]
                [Connection establish acknowledge (SYN+ACK): server port 80]
                [Severity level: Chat]
                [Group: Sequence]
        .... .... ...0 = Fin: Not set
    Window size value: 5840
    [Calculated window size: 5840]
    Checksum: 0x3044 [validation disabled]
        [Good Checksum: False]
        [Bad Checksum: False]
    Urgent pointer: 0
    Options: (8 bytes), Maximum segment size, No-Operation (NOP), No-Operation (NOP), SACK permitted
        Maximum segment size: 1460 bytes
            Kind: Maximum Segment Size (2)
            Length: 4
            MSS Value: 1460
        No-Operation (NOP)
            Type: 1
                0... .... = Copy on fragmentation: No
                .00. .... = Class: Control (0)
                ...0 0001 = Number: No-Operation (NOP) (1)
        No-Operation (NOP)
            Type: 1
                0... .... = Copy on fragmentation: No
                .00. .... = Class: Control (0)
                ...0 0001 = Number: No-Operation (NOP) (1)
        TCP SACK Permitted Option: True
            Kind: SACK Permitted (4)
            Length: 2
    [SEQ/ACK analysis]
        [This is an ACK to the segment in frame: 3]
        [The RTT to ACK the segment was: 0.000178000 seconds]

0000  00 1e c9 32 44 cb 00 13 72 8c d7 8c 08 00 45 00   ...2D...r.....E.
0010  00 30 00 00 40 00 40 06 10 ef 0a 0a 0a a1 0a 0a   [email protected]@.........
0020  0b 25 00 50 b4 41 3e 1b 68 16 f0 9d c6 c0 70 12   .%.P.A&gt;.h.....p.
0030  16 d0 30 44 00 00 02 04 05 b4 01 01 04 02         ..0D..........</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '15, 20:30</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 May '15, 07:00</strong> </span></p></div></div><div id="comments-container-42475" class="comments-container"></div><div id="comment-tools-42475" class="comment-tools"></div><div class="clear"></div><div id="comment-42475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42476"></span>

<div id="answer-container-42476" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42476-score" class="post-score" title="current number of votes">0</div><span id="post-42476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You don't need a separate (old) tshark version. Instead you should use the capabilities built into tshark, like printing fields</p><blockquote><p>tshark -ni eth0 -T fields -e frame.number -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e frame.len -e tcp.len -e _ws.col.Info</p></blockquote><p>Alternatively, you can print the whole frame in verbose mode and parse that.</p><blockquote><p>tshark -ni eth0 -V<br />
tshark -ni eth0 -T pdml<br />
</p></blockquote><p>Alternatively, you can adjust the "gui.column.format". Please read the man page of tshark for further details (Option <strong>-G column-formats</strong>).</p><blockquote><p><a href="https://www.wireshark.org/docs/man-pages/tshark.html">https://www.wireshark.org/docs/man-pages/tshark.html</a></p></blockquote><p><strong>++ UPDATE ++</strong></p><p>Based on your update in the question, here is my suggestion:</p><blockquote><p>tshark.exe -nr http.pcap.pcapng -V -P -x -o "gui.column.format:\"No.\",\"%m\",\"Time\",\"%t\",\"Source\",\"%s\",\"Sport\",\"%S\",\"Destination\",\"%d\",\"Dport\",\"%rD\",\"Protocol\",\"%p\",\"Length\",\"%L\",\"Info\",\"%i\""</p></blockquote><p>Output:</p><pre><code>  1 0.000000000 192.168.90.55 49456 80.190.158.9 80 TCP 66 49456ΓåÆ80 [SYN] Seq=
3750447103 Win=8192 Len=0 MSS=1460 WS=4 SACK_PERM=1
Frame 1: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) on interface
0
    Interface id: 0 (\Device\NPF_{7D3191DB-949D-45D5-B11E-0F415B9C9DD2})
    Encapsulation type: Ethernet (1)
    Arrival Time: May 18, 2015 05:33:32.496687000 W. Europe Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1431920012.496687000 seconds
    [Time delta from previous captured frame: 0.000000000 seconds]
    [Time delta from previous displayed frame: 0.000000000 seconds]
    [Time since reference or first frame: 0.000000000 seconds]
    Frame Number: 1
    Frame Length: 66 bytes (528 bits)</code></pre><p>This is the closest you can get, without using -T fields.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '15, 20:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 May '15, 07:32</strong> </span></p></div></div><div id="comments-container-42476" class="comments-container"><span id="42478"></span><div id="comment-42478" class="comment"><div id="post-42478-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@Kurt</span> for the quick response at this time. I need both the info line (the first line) to be in the right format (like by tshark v 1.10.6) and also the other outputs from <code>tshark -r pcapFile -V -P -x</code>.</p></div><div id="comment-42478-info" class="comment-info"><span class="comment-age">(17 May '15, 21:39)</span> <span class="comment-user userinfo">pktUser1001</span></div></div><span id="42480"></span><div id="comment-42480" class="comment"><div id="post-42480-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I need both the info line (the first line) to be in the right format</p></blockquote><p>as I've written: You can either use <strong>-T fields</strong> to craft your own output version and modify your parser script (this would be the most flexibel option), or you can modify the <strong>column-formats</strong> to get it as close as possible to the old 1.10.x style. It won't be the same, but "somehow" close.</p></div><div id="comment-42480-info" class="comment-info"><span class="comment-age">(17 May '15, 21:49)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="42486"></span><div id="comment-42486" class="comment"><div id="post-42486-score" class="comment-score"></div><div class="comment-text"><p>Post processing output should always be done on machine readable output (produced by set rules as defined by -T fields options), i.s.o. human readable output as produced by Tshark without these options.</p><p>When machine readable output is unavailable human readable output can be used, but, as you've noticed, may vary from version to version, which can make scripting/post processing a bit of a pain.</p></div><div id="comment-42486-info" class="comment-info"><span class="comment-age">(17 May '15, 23:01)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="42499"></span><div id="comment-42499" class="comment"><div id="post-42499-score" class="comment-score"></div><div class="comment-text"><p>Thanks again, I updated the question on why using "-T fields" is not enough for my case.</p></div><div id="comment-42499-info" class="comment-info"><span class="comment-age">(18 May '15, 07:01)</span> <span class="comment-user userinfo">pktUser1001</span></div></div><span id="42500"></span><div id="comment-42500" class="comment"><div id="post-42500-score" class="comment-score"></div><div class="comment-text"><p>see the <strong>++ Update ++</strong> in my answer.</p></div><div id="comment-42500-info" class="comment-info"><span class="comment-age">(18 May '15, 07:32)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="42519"></span><div id="comment-42519" class="comment not_top_scorer"><div id="post-42519-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@Kurt</span> for the updated answer. It works great!</p></div><div id="comment-42519-info" class="comment-info"><span class="comment-age">(18 May '15, 16:21)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-42476" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-42476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

