+++
type = "question"
title = "Can see RTP stream but couldn&#x27;t found SIP or H.323"
description = '''I am trying to analyze some voip traffic in Wireshark. But all I could see are small UDP packets; some containing RTP streams and I can see various codec information like G.711, G.723 etc. But there is no sign of SIP or any other signaling packets. Is it possible to hide SIP or H323 signalling withi...'''
date = "2013-09-25T09:38:00Z"
lastmod = "2013-09-29T09:33:00Z"
weight = 25224
keywords = [ "sip", "stun", "h323" ]
aliases = [ "/questions/25224" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can see RTP stream but couldn't found SIP or H.323](/questions/25224/can-see-rtp-stream-but-couldnt-found-sip-or-h323)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25224-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to analyze some voip traffic in Wireshark. But all I could see are small UDP packets; some containing RTP streams and I can see various codec information like G.711, G.723 etc. But there is no sign of SIP or any other signaling packets. Is it possible to hide SIP or H323 signalling within UDP packets in a way which are undetectable to Wireshark? or STUN can do some encoding to hide signalling packets?</p></div><div id="question-tags" class="tags-container tags">sip stun h323</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '13, 09:38</strong></p><img src="https://secure.gravatar.com/avatar/816daf575e97e551b970f51fb006e1a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rousseau&#39;s gravatar image" /><p>rousseau<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rousseau has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Sep '13, 10:14</p></div></div><div id="comments-container-25224" class="comments-container"></div><div id="comment-tools-25224" class="comment-tools"></div><div class="clear"></div><div id="comment-25224-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25342"></span>

<div id="answer-container-25342" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25342-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it possible to hide SIP or H323 signalling within UDP packets in a way which are undetectable to Wireshark?</p></blockquote><p>the easiest way to "hide" SIP messages from Wireshark is to use a non-standard port, as Wireshark detects SIP basically by its ports (5060 and 5061 for secure SIP).</p><p>You can change (extend) the ports</p><blockquote><p>Edit -&gt; Preferences -&gt; Protocols -&gt; SIP -&gt; SIP TCP Ports / SIP TLS Ports</p></blockquote><p>However, you will have to know the port then. One way would be to search for string typically contained in SIP messages.</p><blockquote><p>frame contains "INVITE"<br />
</p></blockquote><p>or</p><blockquote><p>frame contains "REGISTER"<br />
</p></blockquote><p>However, this will only work for unencrypted SIP. In the case of encrypted SIP, you'll have to wade through the traffic manually to figure out the port.</p><p>BTW: If there is no SIP/H.323 traffic in you capture file, it may well be missing, because it was not recorded in the first place ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '13, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-25342" class="comments-container"></div><div id="comment-tools-25342" class="comment-tools"></div><div class="clear"></div><div id="comment-25342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

