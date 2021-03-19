+++
type = "question"
title = "what is (RA) &amp; (TA) means?"
description = '''Hi There, I have some questions:   In my wireshare result, the source column sometimes showing (TA) and destination (RA). are these means Transmission Address and Recipient Address?   I did a tcpdump with limit -s 60, and the source column come out blank. But when I did not set any limit the some so...'''
date = "2013-10-20T12:25:00Z"
lastmod = "2013-10-21T03:38:00Z"
weight = 26225
keywords = [ "and", "source", "traffic", "ta" ]
aliases = [ "/questions/26225" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [what is (RA) & (TA) means?](/questions/26225/what-is-ra-ta-means)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26225-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi There,</p><p>I have some questions:</p><ol><li><p>In my wireshare result, the source column sometimes showing (TA) and destination (RA). are these means Transmission Address and Recipient Address?</p></li><li><p>I did a tcpdump with limit -s 60, and the source column come out blank. But when I did not set any limit the some source line showed MAC address (TA) and some line are showing blank. Can anyone help me explain to me why?</p></li></ol></div><div id="question-tags" class="tags-container tags">and source traffic ta</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '13, 12:25</strong></p><img src="https://secure.gravatar.com/avatar/40bddd06be8d51c9c2dc9d7591fa5c85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Billy&#39;s gravatar image" /><p>Billy<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Billy has no accepted answers">0%</span></p></div></div><div id="comments-container-26225" class="comments-container"></div><div id="comment-tools-26225" class="comment-tools"></div><div class="clear"></div><div id="comment-26225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26232"></span>

<div id="answer-container-26232" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26232-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The only source file where I found those two strings is <a href="http://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-ieee80211.c">packet-ieee80211.c</a>.</p><p>If you search that file for "RA" and "TA" you'll see that those stings are added to the source and destination address if it is a wlan/wifi control frame.</p><p>You can see that in the following capture files as well:</p><blockquote><p><a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=Http.cap">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=Http.cap</a> (Frames: 2,6,10,etc.)<br />
<a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=mesh.pcap">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=mesh.pcap</a> (Frames: 129,132,136)</p><p>are these means Transmission Address and Recipient Address?</p></blockquote><p>yes.</p><blockquote><p>I did a tcpdump with limit -s 60, and the source column come out blank.</p></blockquote><p>As you did not give any information about the interface you were capturing on (and how - monitor mode:yes/no), I can only speculate. I guess you simply did not capture enough bytes of the frame to show the src/dst addresses.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '13, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-26232" class="comments-container"></div><div id="comment-tools-26232" class="comment-tools"></div><div class="clear"></div><div id="comment-26232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

