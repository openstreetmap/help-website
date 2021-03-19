+++
type = "question"
title = "Can Wireshark search packets for phrase found within TCP stream?"
description = '''I have a UNIX server that has two network interfaces, once for incoming traffic and one for outgoing traffic. I can a SNOOP on each interface as audio-content was sent through my server. Afterwards, I can analyze my SNOOPs and &#x27;follow TCP stream&#x27; to find the exact audio files, proving they went in a...'''
date = "2014-08-30T07:15:00Z"
lastmod = "2014-08-31T04:24:00Z"
weight = 35885
keywords = [ "follow.tcp.stream", "tcp" ]
aliases = [ "/questions/35885" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can Wireshark search packets for phrase found within TCP stream?](/questions/35885/can-wireshark-search-packets-for-phrase-found-within-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35885-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a UNIX server that has two network interfaces, once for incoming traffic and one for outgoing traffic. I can a SNOOP on each interface as audio-content was sent through my server. Afterwards, I can analyze my SNOOPs and 'follow TCP stream' to find the exact audio files, proving they went in and out of my server. However, I need to compare the size of the files to ensure that my server didn't strip the files, sending out an empty 'shell'. The only way I can think of finding the size of the packets is to look at the MAIN view in Wireshark and click packet-by-packet until I see something relating to my audio files in the lower preview window. My SNOOP has 1000+ lines - is there an easier way to locate the exact raw packet for my audio data (to determine it's size) by searching on a phrase within the packet's content?<br />
</p></div><div id="question-tags" class="tags-container tags">follow.tcp.stream tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '14, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/7d0358fe642cadc6336df41b11f08dd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="guiltyspark232&#39;s gravatar image" /><p>guiltyspark232<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="guiltyspark232 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-35885" class="comments-container"></div><div id="comment-tools-35885" class="comment-tools"></div><div class="clear"></div><div id="comment-35885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="35888"></span>

<div id="answer-container-35888" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35888-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I may have misunderstood the question but it sounds like you need to do a Find (Ctl-F) with:</p><ul><li>Find by String</li><li>Search in Packet Bytes</li></ul><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '14, 14:16</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-35888" class="comments-container"><span id="35890"></span><div id="comment-35890" class="comment"><div id="post-35890-score" class="comment-score"></div><div class="comment-text"><p>Thank you, that's the answer, I wasn't looking closely at the FIND feature. When I use this feature, it finds the first packet in the packet list with my phrase in the TCP stream; how can I move to the next packet it's found? I notice the FIND window disappears when viewing the first result.</p></div><div id="comment-35890-info" class="comment-info"><span class="comment-age">(30 Aug '14, 15:22)</span> guiltyspark232</div></div><span id="35891"></span><div id="comment-35891" class="comment"><div id="post-35891-score" class="comment-score">1</div><div class="comment-text"><p>Find Next (Ctrl + N).</p><p>There's also Find Previous (Ctrl + B)</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-35891-info" class="comment-info"><span class="comment-age">(30 Aug '14, 16:02)</span> grahamb ♦</div></div></div><div id="comment-tools-35888" class="comment-tools"></div><div class="clear"></div><div id="comment-35888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35895"></span>

<div id="answer-container-35895" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35895-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can try the following display filter</p><blockquote><p>tcp and frame contains "xxxxxxx"</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '14, 04:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-35895" class="comments-container"></div><div id="comment-tools-35895" class="comment-tools"></div><div class="clear"></div><div id="comment-35895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

