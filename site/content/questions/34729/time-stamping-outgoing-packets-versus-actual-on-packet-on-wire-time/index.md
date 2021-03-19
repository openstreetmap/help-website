+++
type = "question"
title = "Time-stamping outgoing packets versus actual on packet-on-wire time."
description = '''We have a stange issue which is likely related to a NIC or TCP stack. A better understanding of where exactly wireshark captures an outgoing packet (and what PC related fucntions may still remain) would be very helpful in isolating this issue. In our case we have a host PC connected through a nTAP a...'''
date = "2014-07-17T09:46:00Z"
lastmod = "2014-07-17T14:36:00Z"
weight = 34729
keywords = [ "delay", "timestamp", "udp", "interpacket", "time" ]
aliases = [ "/questions/34729" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Time-stamping outgoing packets versus actual on packet-on-wire time.](/questions/34729/time-stamping-outgoing-packets-versus-actual-on-packet-on-wire-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34729-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a stange issue which is likely related to a NIC or TCP stack. A better understanding of where exactly wireshark captures an outgoing packet (and what PC related fucntions may still remain) would be very helpful in isolating this issue.</p><p>In our case we have a host PC connected through a nTAP aggregator to our product (a load) Wireshark is running on both the host PC and Wireshark is connected to a sniffer PC connected to the aggregator.</p><p>We send the following sequence of UDP packets between the host and load.</p><p>Packet 1: UDP (82 bytes) Host -&gt; Load</p><p>Packet 2: UDP (79 bytes) Load -&gt; Host</p><p>Packet 3: UDP (87 bytes) Host -&gt; Load</p><p>Packet 4: UDP (78 bytes) Load -&gt; Host</p><p>Repeat starting with Packet 1 until the sequence takes &gt; 90mS.</p><p>Typically the sequence completes in ~2ms however when it is delayed it can see interpacket delays of ~10 - 110mS. As described above, When this sequence fails, the inter-packet delay is generally 95~105mS delayed.</p><p>We see on the Host PC wireshark that the delay is between packet 1 and 2 whereas we see on the sniffer PC that the delay is between packet 4 and 1 (next sequence)</p><p>Any suggestions as to where the outgoing packet may have been generated, seen by wireshark, but not actually transmitted on the wire would be very helpful.</p><p>Host PC is a Lenovo T420i with a gigabit (wired) lan connection.</p><p>Thanks</p><p><strong><em>_ Update</em></strong> _</p><p>I used Python to emulate this same behaviour with the following sequence.</p><p>def beat(j,k): for i in range(0,k): d = 1 a = time.clock() foo = s.sendto(mes, (ip,po) ) b = time.clock()</p><pre><code>    try:
        foo = s.recv(1024)
    except:
        time.sleep(.1)
        foo = s.recv(1024)
        d = 0
    c = time.clock()
    if ( (d == 1) and ((c-a) &gt;= (j/1000.0)) ):
        print &quot;oops:&quot;
        print a
        print b
        print c
        print (c-a)
        print datetime.datetime.now()
print &quot;done&quot;</code></pre><p>beat(10,100000) oops: 164.827757197 164.900906969 164.900928408 0.0731712110398 2014-07-17 13:37:12.552000 oops: 174.882007838 174.896305127 174.896343092 0.0143352542291 2014-07-17 13:37:22.498000 oops: 218.296230804 218.38277295 218.38279439 0.0865635856404 2014-07-17 13:38:05.997000 oops: 259.240381154 259.340393392 259.340411258 0.100030104257 2014-07-17 13:38:46.997000</p><p>this shows that the output packet message is often prevented from finishing. with as much as 100mS in the call to send the packet ... Wireshark receives the packet in its capture immediately.</p><p>It is not clear why the call is taking very long or why wireshark is able to see this packet before the command finishes executing.</p><p>This has been verified in LabVIEW, C#, and Python at this point.</p><p>Any suggestions?</p></div><div id="question-tags" class="tags-container tags">delay timestamp udp interpacket time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '14, 09:46</strong></p><img src="https://secure.gravatar.com/avatar/9631e59e78b9ee4ae06de814b7a949b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MartinW&#39;s gravatar image" /><p>MartinW<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MartinW has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jul '14, 13:48</p></div></div><div id="comments-container-34729" class="comments-container"></div><div id="comment-tools-34729" class="comment-tools"></div><div class="clear"></div><div id="comment-34729-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34735"></span>

<div id="answer-container-34735" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34735-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark doesn't timestamp packets; it relies on libpcap/WinPcap to provide timestamped packets.</p><p>In most cases, libpcap relies on the OS's native packet capture mechanism to timestamp packets (HP-UX is the only exception), and WinPcap's in-kernel driver does the timestamping on Windows.</p><p>For <em>outgoing</em> packets, the packets are timestamped by the capture mechanism (for most UN*Xes - the code that reads the packets timestamps them on HP-UX) or by the in-kernel driver (on Windows). That code usually timestamps the packets, and hands a copy up to its client (libpcap/userland WinPcap), <em>before</em> the packet is transmitted, and possibly even before it's handed to the network device driver.</p><p>So the packet timestamp for outgoing packets will probably be a time <em>before</em> the packet is put onto the wire (and the packet might not even make it onto the wire if, for example, you're sending on half-duplex Ethernet and you keep getting blocked by carrier being up or keep getting collisions).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '14, 14:36</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-34735" class="comments-container"></div><div id="comment-tools-34735" class="comment-tools"></div><div class="clear"></div><div id="comment-34735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

