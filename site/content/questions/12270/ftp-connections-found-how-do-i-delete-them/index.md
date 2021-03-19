+++
type = "question"
title = "ftp connections found... how do I delete them?"
description = '''So, recently i&#x27;ve been downloading several high-risk and malicious programs/files/etc... At first, wireshark didnt find any ftp connections, meaning I haven&#x27;t been keylogged then. But when i started wireshark today, i found several ftp connection, meaning i am the victim of keyloggers... Can anybody...'''
date = "2012-06-28T05:47:00Z"
lastmod = "2012-06-28T08:51:00Z"
weight = 12270
keywords = [ "dissector_delete", "ftp", "keylogger", "help", "trace" ]
aliases = [ "/questions/12270" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ftp connections found... how do I delete them?](/questions/12270/ftp-connections-found-how-do-i-delete-them)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12270-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So, recently i've been downloading several high-risk and malicious programs/files/etc... At first, wireshark didnt find any ftp connections, meaning I haven't been keylogged then. But when i started wireshark today, i found several ftp connection, meaning i am the victim of keyloggers... Can anybody please help me on how to get rid of these connections?</p><p>Here are some of the ftp's found by wireshark..</p><p>No. Time Source Destination Protocol Length Info 2 30.044721000 169.254.195.50 169.254.255.255 UDP 86 Source port: 57621 Destination port: 57621</p><p>Frame 2: 86 bytes on wire (688 bits), 86 bytes captured (688 bits) on interface 0 Ethernet II, Src: CadmusCo_00:fc:d0 (08:00:27:00:fc:d0), Dst: Broadcast (ff:ff:ff:ff:ff:ff) Internet Protocol Version 4, Src: 169.254.195.50 (169.254.195.50), Dst: 169.254.255.255 (169.254.255.255) User Datagram Protocol, Src Port: 57621 (57621), Dst Port: 57621 (57621) Data (44 bytes)</p><p>0000 53 70 6f 74 55 64 70 30 2f e9 a9 b8 54 bb fc 08 SpotUdp0/...T... 0010 00 01 00 04 48 95 c2 03 a0 3e a6 fe 72 35 8d 42 ....H....&gt;..r5.B 0020 7f 9f 55 d5 34 09 46 65 07 c7 97 c3 ..U.4.Fe....</p><p>No. Time Source Destination Protocol Length Info 189 1772.533866000 169.254.195.50 169.254.255.255 UDP 86 Source port: 57621 Destination port: 57621</p><p>Frame 189: 86 bytes on wire (688 bits), 86 bytes captured (688 bits) on interface 0 Ethernet II, Src: CadmusCo_00:fc:d0 (08:00:27:00:fc:d0), Dst: Broadcast (ff:ff:ff:ff:ff:ff) Internet Protocol Version 4, Src: 169.254.195.50 (169.254.195.50), Dst: 169.254.255.255 (169.254.255.255) User Datagram Protocol, Src Port: 57621 (57621), Dst Port: 57621 (57621) Data (44 bytes)</p><p>0000 53 70 6f 74 55 64 70 30 2f e9 a9 b8 54 bb fc 08 SpotUdp0/...T... 0010 00 01 00 04 48 95 c2 03 a0 3e a6 fe 72 35 8d 42 ....H....&gt;..r5.B 0020 7f 9f 55 d5 34 09 46 65 07 c7 97 c3 ..U.4.Fe....</p><p>Most of them are being transferred to an IP 169.254.255.255 And no, this is not my own IP adress....</p><p>Can anybody please help me, I just want to get rid of these connections!</p><p>Kind regards and thanks in advance, John S.</p></div><div id="question-tags" class="tags-container tags">dissector_delete ftp keylogger help trace</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '12, 05:47</strong></p><img src="https://secure.gravatar.com/avatar/479ba4ac12834a9a5f827c39a43208eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JohnS&#39;s gravatar image" /><p>JohnS<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JohnS has no accepted answers">0%</span></p></div></div><div id="comments-container-12270" class="comments-container"></div><div id="comment-tools-12270" class="comment-tools"></div><div class="clear"></div><div id="comment-12270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12276"></span>

<div id="answer-container-12276" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12276-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This does not look like FTP. FTP normally runs over TCP; these packets are UDP. TFTP uses UDP, but there's nothing in these packets that indicates TFTP.</p><p>169.254.255.255 is not the IP address of an individual machine. This is the directed broadcast address for the 169.254.0.0/16 network. These are broadcasts.</p><p>Based on destination port 57621 and the presence of the string "SpotUDP" in the data portion of the packet, this is probably Spotify, which is a streaming music service.</p><p>How to remove unwanted software is not a Wireshark question, but this should give you enough information to Google for an answer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '12, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-12276" class="comments-container"></div><div id="comment-tools-12276" class="comment-tools"></div><div class="clear"></div><div id="comment-12276-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

