+++
type = "question"
title = "Filter Question"
description = '''Hello, I am wondering if there is a way to create a filter that would sort through a capture and pull out source IP, Destination IP and source ports used or what protocol was used in each packet? I know how to setup filters to look at source IP and destination IP but I&#x27;m not sure how to setup the po...'''
date = "2014-12-30T12:18:00Z"
lastmod = "2014-12-30T14:07:00Z"
weight = 38803
keywords = [ "filter" ]
aliases = [ "/questions/38803" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filter Question](/questions/38803/filter-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38803-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am wondering if there is a way to create a filter that would sort through a capture and pull out source IP, Destination IP and source ports used or what protocol was used in each packet? I know how to setup filters to look at source IP and destination IP but I'm not sure how to setup the ports used. I'm capturing data within our DMZ and simply want to be able to look at a filter that shows source IP, destination IP, Protocol and port number used if possible.</p><p>Thanks for any help!</p></div><div id="question-tags" class="tags-container tags">filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Dec '14, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/a6414c2ff8204ee9c4a3bc2a646c4644?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rock90&#39;s gravatar image" /><p>rock90<br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rock90 has no accepted answers">0%</span></p></div></div><div id="comments-container-38803" class="comments-container"></div><div id="comment-tools-38803" class="comment-tools"></div><div class="clear"></div><div id="comment-38803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38807"></span>

<div id="answer-container-38807" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38807-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>and simply want to be able to look at a filter that shows source IP, destination IP, Protocol <strong>and port number used</strong> if possible.</p></blockquote><p><strong>"port number used"</strong> sounds like you want a list of all conversations, because with a display filter, you need to know the port in advance to be able to filter for it !?!</p><p>So, if you need a list of conversations:</p><blockquote><p>Statistics -&gt; Conversations -&gt; TCP/UDP [Tabs]</p></blockquote><p>If you need a filter for the port, here we go:</p><blockquote><p><a href="http://wiki.wireshark.org/DisplayFilters">http://wiki.wireshark.org/DisplayFilters</a><br />
</p></blockquote><p>In detail:</p><blockquote><p>tcp.port == 1234<br />
</p></blockquote><p>or</p><blockquote><p>tcp.srcport == 1234<br />
</p></blockquote><p>or</p><blockquote><p>tcp.dstport == 1234<br />
</p></blockquote><p>same for UDP.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '14, 14:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-38807" class="comments-container"></div><div id="comment-tools-38807" class="comment-tools"></div><div class="clear"></div><div id="comment-38807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

