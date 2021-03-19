+++
type = "question"
title = "Can not open HTTP port 80 internal web page"
description = '''I have a phone PDX 192.168.132.10 that has a management interface on http port 80. I can not access it and have tried all 3 of the top Internet browsers. I can access the switch management interface on port 80 that is connected to this PBX. Just for clarity the PC 192.168.110.111 is behind a firewal...'''
date = "2017-06-29T08:15:00Z"
lastmod = "2017-07-03T14:34:00Z"
weight = 62411
keywords = [ "tcp_retransmission" ]
aliases = [ "/questions/62411" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can not open HTTP port 80 internal web page](/questions/62411/can-not-open-http-port-80-internal-web-page)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62411-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a phone PDX 192.168.132.10 that has a management interface on http port 80. I can not access it and have tried all 3 of the top Internet browsers. I can access the switch management interface on port 80 that is connected to this PBX. Just for clarity the PC 192.168.110.111 is behind a firewall connected to a MPLS circuit and the PBX is behind a firewall connected to a MPLS circuit. I can see the TCP 3-way handshake then I get TCP Retransmission. Any insight would be helpful.</p><p>This is the screen shot of the PCAP. I can not find a way to link the PCAP file. <img src="https://osqa-ask.wireshark.org/upfiles/Capture_bunUtOu.JPG" alt="link text" /></p></div><div id="question-tags" class="tags-container tags">tcp_retransmission</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '17, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/9777d7e6df68dc43653b2ba9cc7c035f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vonkloha&#39;s gravatar image" /><p>vonkloha<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vonkloha has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jul '17, 08:43</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-62411" class="comments-container"><span id="62412"></span><div id="comment-62412" class="comment"><div id="post-62412-score" class="comment-score"></div><div class="comment-text"><p>Telling us IPs etc. is nice, but doesn't help without a pcap...</p></div><div id="comment-62412-info" class="comment-info"><span class="comment-age">(29 Jun '17, 08:26)</span> Jasper ♦♦</div></div><span id="62413"></span><div id="comment-62413" class="comment"><div id="post-62413-score" class="comment-score"></div><div class="comment-text"><p>I'm trying to get PCAP uploaded</p></div><div id="comment-62413-info" class="comment-info"><span class="comment-age">(29 Jun '17, 08:28)</span> vonkloha</div></div><span id="62415"></span><div id="comment-62415" class="comment"><div id="post-62415-score" class="comment-score"></div><div class="comment-text"><p>Looks like a MTU problem to me, but it's only a guess. There's probably something between the two IPs running with a lower MTU.</p></div><div id="comment-62415-info" class="comment-info"><span class="comment-age">(29 Jun '17, 08:43)</span> Jasper ♦♦</div></div><span id="62420"></span><div id="comment-62420" class="comment"><div id="post-62420-score" class="comment-score"></div><div class="comment-text"><p>The engine of this site doesn't support direct upload of pcap files. You have to post the file at Cloudshark or at any generic file sharing service and edit your question with a link to it.</p></div><div id="comment-62420-info" class="comment-info"><span class="comment-age">(29 Jun '17, 12:25)</span> sindy</div></div><span id="62426"></span><div id="comment-62426" class="comment"><div id="post-62426-score" class="comment-score"></div><div class="comment-text"><p>I have put the file at CloudShark. You can use this filter to see the problem. tcp.stream eq 4</p><p><a href="https://www.cloudshark.org/captures/c89d6f894c80">https://www.cloudshark.org/captures/c89d6f894c80</a></p></div><div id="comment-62426-info" class="comment-info"><span class="comment-age">(29 Jun '17, 13:25)</span> vonkloha</div></div><span id="62427"></span><div id="comment-62427" class="comment not_top_scorer"><div id="post-62427-score" class="comment-score"></div><div class="comment-text"><p>Yes, I agree with <a href="https://ask.wireshark.org/users/145/jasper">@Jasper</a> that it seems that something between the PC and the PBX doesn't let the 1514 bytes packet through. The first packet of the http response got through and has been responded, the second which makes full use of the MTU value of 1514 bytes hasn't got through.</p></div><div id="comment-62427-info" class="comment-info"><span class="comment-age">(29 Jun '17, 13:33)</span> sindy</div></div></div><div id="comment-tools-62411" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-62411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62482"></span>

<div id="answer-container-62482" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62482-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you look at tcp.stream==1 you will all is good until frame 9 when the first 1448 byte TCP segment is sent. Inside the IP header this has the don't fragment bit set, also, you will see this is the segment that is continually re-transmitted. Some device along the path is likely not supporting MTU that can fit the size frame in frame 9, and is hence dropping the packet as the don't fragment bit is set.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '17, 14:34</strong></p><img src="https://secure.gravatar.com/avatar/8234281d80d46cc33dc8ba9dbdd33aa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sneak2k2&#39;s gravatar image" /><p>Sneak2k2<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sneak2k2 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jul '17, 14:34</p></div></div><div id="comments-container-62482" class="comments-container"></div><div id="comment-tools-62482" class="comment-tools"></div><div class="clear"></div><div id="comment-62482-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

