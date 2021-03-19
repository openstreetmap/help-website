+++
type = "question"
title = "How to check if fragmentation is happening?"
description = '''Hi, How can I verify from wireshark traces if the fragmentation is happening or not when jumbo frames are configured? Any pattern or messages I need to look for? Also how do I troubleshoot the jumbo frames network performance issues? Thanks!!'''
date = "2015-04-02T09:55:00Z"
lastmod = "2015-04-02T12:22:00Z"
weight = 41152
keywords = [ "fragmentation", "jumboframes" ]
aliases = [ "/questions/41152" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to check if fragmentation is happening?](/questions/41152/how-to-check-if-fragmentation-is-happening)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41152-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, How can I verify from wireshark traces if the fragmentation is happening or not when jumbo frames are configured? Any pattern or messages I need to look for? Also how do I troubleshoot the jumbo frames network performance issues?</p><p>Thanks!!</p></div><div id="question-tags" class="tags-container tags">fragmentation jumboframes</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '15, 09:55</strong></p><img src="https://secure.gravatar.com/avatar/68b978baf280d6656178b3a96a1df45e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vondutch9&#39;s gravatar image" /><p>vondutch9<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vondutch9 has no accepted answers">0%</span></p></div></div><div id="comments-container-41152" class="comments-container"><span id="41169"></span><div id="comment-41169" class="comment"><div id="post-41169-score" class="comment-score"></div><div class="comment-text"><p>"How do I troubleshoot the jumbo frames network performance issues?" Start looking at the TCP flows, if you need help open a new thread stating this and provide a capture from both ends of the connection.</p></div><div id="comment-41169-info" class="comment-info"><span class="comment-age">(02 Apr '15, 20:48)</span> mrEEde</div></div></div><div id="comment-tools-41152" class="comment-tools"></div><div class="clear"></div><div id="comment-41152-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41162"></span>

<div id="answer-container-41162" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41162-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Fragmentation has occured when either the more fragment bit is set or the fragmentation offset is greater than zero. The filter tp display both types would look like:<br />
</p><pre><code> ip.flags.mf ==1 or ip.frag_offset gt 0</code></pre><p>I typically also want to see the packets that require fragmentation but did not allow to be fragmented. So the path MTU discovery process kicks in an reduces the MTU size. A filter on those packet would be icmp.code == 4<br />
</p><p>So the combination of both in i little more cryptic notation is<br />
</p><p>ip[6:2]&amp;3fff or icmp[1]==4</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '15, 12:22</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Apr '15, 01:35</p></div></div><div id="comments-container-41162" class="comments-container"><span id="41163"></span><div id="comment-41163" class="comment"><div id="post-41163-score" class="comment-score"></div><div class="comment-text"><p>Ok here is what my wireshark trace looks like. Source 10.14.166.13 is sending a packet of size 12426 to destination 10.5.98.29 and then the destination is sending 5 acknowledgements. Each ack packet is a naked acknowledgement and acknowledges 2920 bytes. So can I conclude the packet from 10.14.166.13 is broken down into packets of size 2920 by some router on the way and then delivered to 10.5.98.29? Full size image if gets cropped in your browser, at <a href="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2015-04-03_at_4.28.57_AM.png">https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2015-04-03_at_4.28.57_AM.png</a> if the image</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2015-04-03_at_4.28.57_AM.png" alt="alt text" /></p></div><div id="comment-41163-info" class="comment-info"><span class="comment-age">(02 Apr '15, 13:38)</span> vondutch9</div></div><span id="41165"></span><div id="comment-41165" class="comment"><div id="post-41165-score" class="comment-score">1</div><div class="comment-text"><p>TCP usually acks every 2nd packet so when you see 2920 bytes being acked this means the remote side received two segments of 1460 bytes indicating an MTU size of 1500 along the route. Sending a packet size of 12426 is not possible as even jumboframes only allows an MTU of 9000 bytes. What you see is a trace at the sender that has LArgeSend or Segmentation Offload enabled where segmentation is done by the ethernet card.</p></div><div id="comment-41165-info" class="comment-info"><span class="comment-age">(02 Apr '15, 14:08)</span> mrEEde</div></div><span id="41166"></span><div id="comment-41166" class="comment"><div id="post-41166-score" class="comment-score"></div><div class="comment-text"><p>So can we conclude that jumbo frames are not being used here at all? How can I make jumbo frames work here? Also if segmentation offload is enabled on nic card then how can wireshark know what size packets are being sent over on the wire?</p></div><div id="comment-41166-info" class="comment-info"><span class="comment-age">(02 Apr '15, 14:14)</span> vondutch9</div></div><span id="41167"></span><div id="comment-41167" class="comment"><div id="post-41167-score" class="comment-score">1</div><div class="comment-text"><p>The easiest way to determine if jumbo frames are used would be to inspect the SYN packets and look at the offered MSS. If you don't have the 3-way handshake you would need to have a trace at the receiver also and see how large the biggest inbound packet is.</p></div><div id="comment-41167-info" class="comment-info"><span class="comment-age">(02 Apr '15, 20:35)</span> mrEEde</div></div><span id="41168"></span><div id="comment-41168" class="comment"><div id="post-41168-score" class="comment-score">1</div><div class="comment-text"><p>"How can I make jumbo frames work here" - well, you need to use an MTU size of 9000 all the way along the path and your network hardware needs to enable it also. So it depends what the 'here' is. <a href="http://lmgtfy.com/?q=how+to+enable+jumbo+frames">http://lmgtfy.com/?q=how+to+enable+jumbo+frames</a> This is drifting away from the original question "how-to-check-if-fragmentation-is-happening" though ;-)</p></div><div id="comment-41168-info" class="comment-info"><span class="comment-age">(02 Apr '15, 20:46)</span> mrEEde</div></div><span id="41172"></span><div id="comment-41172" class="comment not_top_scorer"><div id="post-41172-score" class="comment-score"></div><div class="comment-text"><p>Hi meEEde! Very much appreciate it! Yup, it<code>s drifting from the original question as I know now jumbo frames are not there so I</code>m thinking on next step is how to make it work, thanks to you. :-)</p></div><div id="comment-41172-info" class="comment-info"><span class="comment-age">(02 Apr '15, 22:59)</span> vondutch9</div></div><span id="41173"></span><div id="comment-41173" class="comment not_top_scorer"><div id="post-41173-score" class="comment-score"></div><div class="comment-text"><p>Good to hear, once you consider a question answered please use the checkmark next to the answer to close it out. Thanks</p></div><div id="comment-41173-info" class="comment-info"><span class="comment-age">(02 Apr '15, 23:38)</span> mrEEde</div></div><span id="41176"></span><div id="comment-41176" class="comment not_top_scorer"><div id="post-41176-score" class="comment-score"></div><div class="comment-text"><p>Enabling jumbo frames requires <strong>three</strong> things:</p><ol><li>Enabling them on the sender (usually on driver level)</li><li>Enabling them on the receiver</li><li>Enabling processing of jumbo frames on <strong>each and every</strong> network device between sender and receiver, meaning switches and routers.</li></ol></div><div id="comment-41176-info" class="comment-info"><span class="comment-age">(03 Apr '15, 02:00)</span> Jasper ♦♦</div></div></div><div id="comment-tools-41162" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-41162-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41154"></span>

<div id="answer-container-41154" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41154-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please use the following display filter:</p><blockquote><p>ip.fragment</p></blockquote><p>You can test it with the following sample capture file</p><blockquote><p><a href="https://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=teardrop.cap">https://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=teardrop.cap</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '15, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></img></div></div><div id="comments-container-41154" class="comments-container"><span id="41159"></span><div id="comment-41159" class="comment"><div id="post-41159-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your response. I do see a message Fragmented IP Protocol but when I try to apply the above mentioned filter, it doesn<code>t show up anything. Also I am wondering the packet in this capture is just 38bytes, why is it fragmented if it</code>s not a jumbo packet at all. Also I note this is not TCP but UDP.</p></div><div id="comment-41159-info" class="comment-info"><span class="comment-age">(02 Apr '15, 10:55)</span> vondutch9</div></div><span id="41161"></span><div id="comment-41161" class="comment"><div id="post-41161-score" class="comment-score"></div><div class="comment-text"><p>TCP never fragments, unless someone cheats.</p></div><div id="comment-41161-info" class="comment-info"><span class="comment-age">(02 Apr '15, 11:51)</span> Jasper ♦♦</div></div><span id="41215"></span><div id="comment-41215" class="comment"><div id="post-41215-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Also I am wondering the packet in this capture is just 38bytes,</p></blockquote><p>It's a demonstration of an attack.</p></div><div id="comment-41215-info" class="comment-info"><span class="comment-age">(06 Apr '15, 04:04)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-41154" class="comment-tools"></div><div class="clear"></div><div id="comment-41154-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

