+++
type = "question"
title = "TCP packet length was much greater than MTU"
description = '''I am a newbie with TCP, MTU (which I have to play around with) and Wireshark. I sent some data that was over 100k over tcp and used Wireshark to view and confirm the data that I sent. I assume each Wireshark frame corresponds to a TCP segment, am I correct? I noticed the length of some of the frames...'''
date = "2013-09-14T19:23:00Z"
lastmod = "2013-09-14T21:52:00Z"
weight = 24699
keywords = [ "tcp", "mtu" ]
aliases = [ "/questions/24699" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TCP packet length was much greater than MTU](/questions/24699/tcp-packet-length-was-much-greater-than-mtu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24699-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am a newbie with TCP, MTU (which I have to play around with) and Wireshark. I sent some data that was over 100k over tcp and used Wireshark to view and confirm the data that I sent. I assume each Wireshark frame corresponds to a TCP segment, am I correct? I noticed the length of some of the frames were 1514, which looked correct, because MTU was 1500 plus some bytes for headers. However, some of the frame lengths were much higher, such as 5xxx, 1xxxx. Why was that the case..? I thought all the frames (the ones about data sent from my machine to the remote server) would be 1514.</p><p>I also added the column "Packet Length" and thought maybe that column would report TCP segment size and I noticed the numbers in that column were the same as the numbers in the column "Length". What's the difference between "Packet Length" and "Length"?</p></div><div id="question-tags" class="tags-container tags">tcp mtu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '13, 19:23</strong></p><img src="https://secure.gravatar.com/avatar/3a53e4ad3861136b4e080af57353bf12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiresharknewbie&#39;s gravatar image" /><p>wiresharknewbie<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiresharknewbie has no accepted answers">0%</span></p></div></div><div id="comments-container-24699" class="comments-container"></div><div id="comment-tools-24699" class="comment-tools"></div><div class="clear"></div><div id="comment-24699-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24702"></span>

<div id="answer-container-24702" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24702-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>Probably you captured on the host that transmitted the oversized packet, and TCP Large Segment Offload is enabled. (Sometimes abbreviated TSO and sometimes LSO.) The operating system is passing packets larger than MTU to the network adapter, and the network adapter driver is breaking them up so that they fit within the MTU. If you capture from the wire, instead of from an endpoint involved in the communication, you will see that the packets are correctly sized when they are transmitted. This is one reason of several to capture from the wire, instead of on an endpoint.</p><p>TSO is a performance enhancement, but you can turn it off, in which case, the OS will no longer generate oversized frames.</p><p>To show the size of the TCP segment, add a custom column using the field "tcp.len".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '13, 21:52</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-24702" class="comments-container"><span id="24708"></span><div id="comment-24708" class="comment"><div id="post-24708-score" class="comment-score"></div><div class="comment-text"><p>Thanks a bunch! Follow-up questions - how can I capture from the wire?</p><p>I tried to add a custom column using the field "tcp.len" but I don't see the field "tcp.len" in the menu. I am using 1.6.7 on Ubuntu. Maybe the older version doesn't have that field?</p></div><div id="comment-24708-info" class="comment-info"><span class="comment-age">(15 Sep '13, 01:08)</span> wiresharknewbie</div></div><span id="24714"></span><div id="comment-24714" class="comment"><div id="post-24714-score" class="comment-score"></div><div class="comment-text"><p>It's a custom field, which means there is no hard-coded column setting for it. You need to create a custom column. The easiest way to do this is to find a packet with that field, right-click on it and select "Apply as Column".</p><p>Capture on the Wire means using an additional capture device on a TAP or SPAN port. See <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></div><div id="comment-24714-info" class="comment-info"><span class="comment-age">(15 Sep '13, 06:28)</span> Jasper ♦♦</div></div><span id="24726"></span><div id="comment-24726" class="comment"><div id="post-24726-score" class="comment-score"></div><div class="comment-text"><p>Thank you for pointing out the document! TAP or SPAN won't be my option so I will try disabling offload to see if that solves the problem. I tried to get tcp.len to show as column, but I was only able to get frame.len, ip.len, data.len to show. I was not able to find a field under the "Transmission Control Protocol" section about length even though the heading of that section included "Len" (Transmission Control Protocol, Src Port: 123 (123), Dst Port: 456 (456), Seq: 789, Ack: 1, Len: 1448)</p></div><div id="comment-24726-info" class="comment-info"><span class="comment-age">(15 Sep '13, 15:18)</span> wiresharknewbie</div></div><span id="24727"></span><div id="comment-24727" class="comment"><div id="post-24727-score" class="comment-score"></div><div class="comment-text"><p><code>tcp.len</code> is a hidden field, so it won't appear in the packet details pane unless you enable hidden fields to be displayed. So you can either:</p><ol><li>Enable hidden fields via: <code>Edit -&gt; Preferences -&gt; Protocols -&gt; Display hidden protocol items</code>, and then do the <code>right-click -&gt; Apply as column</code> trick that Jasper pointed out, or</li><li>Manually add the <code>tcp.len</code> field via: <code>Edit -&gt; Preferences -&gt; Columns -&gt; Add -&gt; Field type: Custom, Field name: tcp.len -&gt; [click title and rename from Custom to something else like TCP Len] -&gt; [drag &amp; drop new column to desired location] -&gt; OK</code></li></ol></div><div id="comment-24727-info" class="comment-info"><span class="comment-age">(15 Sep '13, 16:46)</span> cmaynard ♦♦</div></div><span id="24735"></span><div id="comment-24735" class="comment"><div id="post-24735-score" class="comment-score"></div><div class="comment-text"><p>Awesome - thanks so much for pointing out TCP Segment length is a hidden field! I followed 1 and now I have TCP Segment length as a column.</p></div><div id="comment-24735-info" class="comment-info"><span class="comment-age">(15 Sep '13, 23:56)</span> wiresharknewbie</div></div><span id="38136"></span><div id="comment-38136" class="comment not_top_scorer"><div id="post-38136-score" class="comment-score"></div><div class="comment-text"><p>Sounds great...EXCEPT, I set a column for frame.len &gt; 1500 and saw lengths of 4540B, 5094b and even 22734. And, I am using a span port in a 3750x. Is the span doing something goofy??</p></div><div id="comment-38136-info" class="comment-info"><span class="comment-age">(25 Nov '14, 10:47)</span> dribniff</div></div></div><div id="comment-tools-24702" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-24702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

