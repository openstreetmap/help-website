+++
type = "question"
title = "Open Sound Control OSC, how to filter"
description = '''I am trying to filter so that I can view only OSC (open sound control, http://opensoundcontrol.org/spec-1_0). I don&#x27;t know where to start. I searched the Internet for hours to find a simple utility to do this, but found nothing. I know Wireshark must be capable, but need help.'''
date = "2011-09-08T13:03:00Z"
lastmod = "2011-09-08T14:23:00Z"
weight = 6217
keywords = [ "opensoundcontrol", "osc", "filtering", "display-filter" ]
aliases = [ "/questions/6217" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Open Sound Control OSC, how to filter](/questions/6217/open-sound-control-osc-how-to-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6217-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to filter so that I can view only OSC (open sound control, <a href="http://opensoundcontrol.org/spec-1_0">http://opensoundcontrol.org/spec-1_0</a>). I don't know where to start. I searched the Internet for hours to find a simple utility to do this, but found nothing. I know Wireshark must be capable, but need help.</p></div><div id="question-tags" class="tags-container tags">opensoundcontrol osc filtering display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Sep '11, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/794e2a1bd73b672e9c4d403e5e0b21b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ryan%20Webber&#39;s gravatar image" /><p>Ryan Webber<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ryan Webber has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Sep '11, 16:01</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6217" class="comments-container"><span id="6223"></span><div id="comment-6223" class="comment"><div id="post-6223-score" class="comment-score"></div><div class="comment-text"><p>So eg. my OSC is sent on port 1234 I can then filter based on this port #?</p></div><div id="comment-6223-info" class="comment-info"><span class="comment-age">(08 Sep '11, 15:39)</span> Ryan Webber</div></div></div><div id="comment-tools-6217" class="comment-tools"></div><div class="clear"></div><div id="comment-6217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6219"></span>

<div id="answer-container-6219" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6219-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's difficult to determine heuristically if a packet stream contains OSC. It's a protocol without ties to a transport protocol, so you'll have to know something about the used transport protocol in order to define a filter.</p><p>eg. using the following command:</p><p><code>$ sendOSC -h rodet 7009</code></p><p>produces a UDP stream to host rodet, port 7009, so <em>udp.port==7009</em> should work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '11, 14:23</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6219" class="comments-container"></div><div id="comment-tools-6219" class="comment-tools"></div><div class="clear"></div><div id="comment-6219-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

