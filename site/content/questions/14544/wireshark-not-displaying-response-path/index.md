+++
type = "question"
title = "Wireshark not displaying response path"
description = '''Hi Guyz, I am a new bie in this world of wireshark.  I have a set up where I need to sniff the communication between two devices.. Say A and B I have my laptop connected to a HUB with A and B and UPlink to this Hub is from a router. A , B and my laptop has got ips. So far so good. Now I start commun...'''
date = "2012-09-26T07:28:00Z"
lastmod = "2012-09-28T12:46:00Z"
weight = 14544
keywords = [ "size", "packet", "missing", "wireshark" ]
aliases = [ "/questions/14544" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not displaying response path](/questions/14544/wireshark-not-displaying-response-path)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14544-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guyz,</p><p>I am a new bie in this world of wireshark.</p><p>I have a set up where I need to sniff the communication between two devices.. Say A and B I have my laptop connected to a HUB with A and B and UPlink to this Hub is from a router. A , B and my laptop has got ips. So far so good. Now I start communication between A and B and start wireshark and listen to my ethernet interface connected to the hub( I have promiscus mode ON, and I am listening to the only ethernet interface I have) The communication sequence is</p><blockquote><ol><li>A asks B something -&gt;my wireshark logs it</li><li>B responds to A -&gt; my wireshark logs it</li><li>A asks something else to B -&gt; my wireshark logs it</li><li>B respons to A -&gt; <strong>MY WIRESHARK DOES NOT LOG IT :(</strong> This is my problem</li></ol></blockquote><p>But I can see from the status of my device A that B has infact responded and B has got the result. But somehow my wireshark missed it. The only chance I see is B is sending a response of large size so that wireshark skips it. is that possible? My response at step 4 infact is large and is an xml file. So this is what I am assuming.</p><p>can you provide any pointers on how to approach this issue?please?</p></div><div id="question-tags" class="tags-container tags">size packet missing wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '12, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/a3d773a42960f5627bbbe47e460a4ac6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sree_ec&#39;s gravatar image" /><p>sree_ec<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sree_ec has no accepted answers">0%</span></p></div></div><div id="comments-container-14544" class="comments-container"></div><div id="comment-tools-14544" class="comment-tools"></div><div class="clear"></div><div id="comment-14544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14608"></span>

<div id="answer-container-14608" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14608-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, Wireshark is not skipping the response because the file is too large. Wireshark does not know or care how large the file is. When B sends the XML file to A, B splits the file into individual data segments each small enough to be transmitted across the network, and sends each data segment in its own packet. This is what Wireshark will see--the individual packets, not the file. The individual data segments are then reassembled into the XML file by A. The difference between a large file and a small file is the <em>number</em> of packets that are required to transfer the file, not the <em>size</em> of the packets.</p><p>Were there any capture or display filters in place when Wireshark was capturing the traffic?</p><p>Is it possible for you to post a trace file that illustrates the problem at <a href="http://www.cloudshark.org"></a><a href="http://www.cloudshark.org">www.cloudshark.org</a>? (But be careful about posting files that contain sensitive or confidential information.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '12, 12:46</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-14608" class="comments-container"></div><div id="comment-tools-14608" class="comment-tools"></div><div class="clear"></div><div id="comment-14608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

