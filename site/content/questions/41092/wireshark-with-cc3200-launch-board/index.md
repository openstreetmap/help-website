+++
type = "question"
title = "Wireshark with CC3200 Launch Board"
description = '''Hi , I am trying to sniff the packets with airpcap that I send with the cc3200 mod launch board ( texas instruments). It seems that the packets are sent ( I can see it in the terminal where I have the successfull of operation) but I can see in wireshark only 802.11 and not udp ( i would like to see ...'''
date = "2015-04-01T05:31:00Z"
lastmod = "2015-04-01T15:51:00Z"
weight = 41092
keywords = [ "cc3200" ]
aliases = [ "/questions/41092" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark with CC3200 Launch Board](/questions/41092/wireshark-with-cc3200-launch-board)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41092-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ,</p><p>I am trying to sniff the packets with airpcap that I send with the cc3200 mod launch board ( texas instruments). It seems that the packets are sent ( I can see it in the terminal where I have the successfull of operation) but I can see in wireshark only 802.11 and not udp ( i would like to see the udp traffic from the board to a smartphone). In the smartphone , the connection is ok and the server is running without problem.. What is the problem ?</p></div><div id="question-tags" class="tags-container tags">cc3200</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '15, 05:31</strong></p><img src="https://secure.gravatar.com/avatar/785637bbb9d672f0e3290342c13aa882?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paolo%20Rossi&#39;s gravatar image" /><p>Paolo Rossi<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paolo Rossi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Apr '15, 07:34</p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-41092" class="comments-container"><span id="41218"></span><div id="comment-41218" class="comment"><div id="post-41218-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.dropbox.com/s/7jvwxnl5zkf679f/Prova_forum.pcapng?dl=0">https://www.dropbox.com/s/7jvwxnl5zkf679f/Prova_forum.pcapng?dl=0</a> <a href="https://www.dropbox.com/s/kiu1xz2hnf41j4m/Prova_forum_2.pcapng?dl=0">https://www.dropbox.com/s/kiu1xz2hnf41j4m/Prova_forum_2.pcapng?dl=0</a></p><p>I share the dropbox link for the capture in wire shark.. Transmitter address: Texans 04:03:07 (5c:31:3e:04:03:07) Destination address: 8a:30:8a:4e:a6:6c (8a:30:8a:4e:a6:6c) I can see nothing about the udp packets.. There is only the procedure to establish the connection. What Must I set in wire-shark for seeing the udp packets ?? I tried to change the channel but the result is the same..</p></div><div id="comment-41218-info" class="comment-info"><span class="comment-age">(06 Apr '15, 06:16)</span> Paolo Rossi</div></div></div><div id="comment-tools-41092" class="comment-tools"></div><div class="clear"></div><div id="comment-41092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41113"></span>

<div id="answer-container-41113" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41113-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is probably that the traffic is on a "protected" network, and therefore encrypted, and either Wireshark doesn't know the password for the network or, if it's a WPA/WPA2 network, the capture doesn't include the initial "EAPOL handshake". Either of those would mean that Wireshark can't decrypt the traffic to discover that it's UDP (or TCP or...) traffic, and can't get past the 802.11 layer.</p><p>See <a href="https://wiki.wireshark.org/HowToDecrypt802.11">the Wireshark Wiki "how to decrypt 802.11"</a> page for more information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '15, 15:51</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-41113" class="comments-container"><span id="41120"></span><div id="comment-41120" class="comment"><div id="post-41120-score" class="comment-score"></div><div class="comment-text"><p>Why protected ? I don't use a password , the network is free.. but maybe I don't know the bases of 802.11 transmission. You are saying that in each case to decrypt the packets if I use 802.11 , I need of one key... It is strange because for udp transmission I don't need the connection.. If you can explain well , I would be very happy.</p><p>Thanks for the help</p></div><div id="comment-41120-info" class="comment-info"><span class="comment-age">(02 Apr '15, 01:06)</span> Paolo Rossi</div></div><span id="41127"></span><div id="comment-41127" class="comment"><div id="post-41127-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-41127-info" class="comment-info"><span class="comment-age">(02 Apr '15, 02:31)</span> grahamb ♦</div></div><span id="41216"></span><div id="comment-41216" class="comment"><div id="post-41216-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.dropbox.com/s/7jvwxnl5zkf679f/Prova_forum.pcapng?dl=0">https://www.dropbox.com/s/7jvwxnl5zkf679f/Prova_forum.pcapng?dl=0</a><br />
<a href="https://www.dropbox.com/s/kiu1xz2hnf41j4m/Prova_forum_2.pcapng?dl=0">https://www.dropbox.com/s/kiu1xz2hnf41j4m/Prova_forum_2.pcapng?dl=0</a><br />
</p><p>I share the dropbox link for the capture in wire shark.. Transmitter address: Texans 04:03:07 (5c:31:3e:04:03:07) Destination address: 8a:30:8a:4e:a6:6c (8a:30:8a:4e:a6:6c) I can see nothing about the udp packets.. There is only the procedure to establish the connection. What Must I set in wire-shark for seeing the udp packets ?? I tried to change the channel but the result is the same..</p></div><div id="comment-41216-info" class="comment-info"><span class="comment-age">(06 Apr '15, 05:51)</span> Paolo Rossi</div></div><span id="41217"></span><div id="comment-41217" class="comment"><div id="post-41217-score" class="comment-score"></div><div class="comment-text"><p>@Paolo Rossi: I converted your answer to a comment, as that's how this Q&amp;A site works. See FAQ.</p></div><div id="comment-41217-info" class="comment-info"><span class="comment-age">(06 Apr '15, 06:10)</span> Kurt Knochner ♦</div></div><span id="41222"></span><div id="comment-41222" class="comment"><div id="post-41222-score" class="comment-score"></div><div class="comment-text"><p>FWIW (and not knowing too much about 802.11): In the first capture I see that many of the frames from 5c:31:.... have the "data is protected" flag set which I believe means that the data is encrypted.</p><p>In the second capture I don't see much of anything for 5c:31:... and 8a:30:... other than management and control frames. Correction: I don't see anything in the 2nd capture for (8a:30:8a:4e:a6:6c)</p></div><div id="comment-41222-info" class="comment-info"><span class="comment-age">(06 Apr '15, 08:24)</span> Bill Meier ♦♦</div></div><span id="41284"></span><div id="comment-41284" class="comment not_top_scorer"><div id="post-41284-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt Knochner, In the first capture you can see something from 5C:31... ?? I am looking at now but I see only Probe request.. are you sure ??</p><p>How can I see the setting for the protected data ?</p></div><div id="comment-41284-info" class="comment-info"><span class="comment-age">(08 Apr '15, 06:40)</span> Paolo Rossi</div></div><span id="41288"></span><div id="comment-41288" class="comment not_top_scorer"><div id="post-41288-score" class="comment-score"></div><div class="comment-text"><p>@Paolo Rossi: Again, your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-41288-info" class="comment-info"><span class="comment-age">(08 Apr '15, 08:03)</span> Jaap ♦</div></div><span id="41303"></span><div id="comment-41303" class="comment not_top_scorer"><div id="post-41303-score" class="comment-score"></div><div class="comment-text"><p>Yes,I'm sure. See,for example, frame 838 in the first capture.</p><p>Note that in that frame, (and some number following) that the protected flag is set under QOS Data/Frame Control Field/Flags</p><p>If you haven't done so, use a display filter for 'wlan.addr == 5c:31:3e:04:03:07' to select all the packets sent/received to that address.</p></div><div id="comment-41303-info" class="comment-info"><span class="comment-age">(08 Apr '15, 15:07)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-41113" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-41113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

