+++
type = "question"
title = "Chart network traffic"
description = '''I&#x27;m brand new to wireshark. Is there a chart that will show me the volume of network activity by LAN IP address? I&#x27;d like to see which computers have the most traffic.'''
date = "2013-11-09T13:07:00Z"
lastmod = "2013-11-09T14:56:00Z"
weight = 26805
keywords = [ "chart" ]
aliases = [ "/questions/26805" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Chart network traffic](/questions/26805/chart-network-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26805-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm brand new to wireshark. Is there a chart that will show me the volume of network activity by LAN IP address? I'd like to see which computers have the most traffic.</p></div><div id="question-tags" class="tags-container tags">chart</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '13, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/b54be53683c98f7a916ee8a09604dec3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott216&#39;s gravatar image" /><p>Scott216<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott216 has no accepted answers">0%</span></p></div></div><div id="comments-container-26805" class="comments-container"></div><div id="comment-tools-26805" class="comment-tools"></div><div class="clear"></div><div id="comment-26805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26808"></span>

<div id="answer-container-26808" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26808-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are several methods.</p><blockquote><p>Statistics -&gt; Endpoints -&gt; IPv4 (sort for Bytes or Packets)<br />
Statistics -&gt; Conversations -&gt; IPv4 (or TCP)<br />
Statistics -&gt; IO Graph (<a href="http://www.youtube.com/watch?v=Z6kLoqiRZfQ">IO Graph Tutorial</a>)</p></blockquote><p>or on the CLI</p><blockquote><p>tshark -nr input.pcap -z conv,ip</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '13, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-26808" class="comments-container"></div><div id="comment-tools-26808" class="comment-tools"></div><div class="clear"></div><div id="comment-26808-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

