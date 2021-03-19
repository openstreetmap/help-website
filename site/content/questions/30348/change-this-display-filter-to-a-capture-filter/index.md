+++
type = "question"
title = "Change this display filter to a capture filter."
description = '''Hey there,  I found in an earlier post, the display filter (http.request.method == &quot;GET&quot; and http.request.uri == &quot;/&quot;), which filter out ip address and visited url in a very good way. This filter also &quot;removes&quot; ads and other crap which is really nice. I&#x27;m trying to solve this display filter as an cap...'''
date = "2014-03-03T08:50:00Z"
lastmod = "2014-03-03T10:30:00Z"
weight = 30348
keywords = [ "wireshark" ]
aliases = [ "/questions/30348" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Change this display filter to a capture filter.](/questions/30348/change-this-display-filter-to-a-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30348-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey there,</p><p>I found in an earlier post, the display filter (http.request.method == "GET" and http.request.uri == "/"), which filter out ip address and visited url in a very good way. This filter also "removes" ads and other crap which is really nice. I'm trying to solve this display filter as an capture filter, but I'm having problems.</p><p>I found this capture filter at Wireshark Wiki: port 80 and tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x4745542, but this gives me too much information, ads and other crap. Do anyone of you know how I can expand the mentioned filter or create a new filter that filters out only the visited websites without ads as the display filter does?</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '14, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/229e875798c96fc4b63fda5eeb1e3024?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="svante&#39;s gravatar image" /><p>svante<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="svante has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Mar '14, 08:51</p></div></div><div id="comments-container-30348" class="comments-container"></div><div id="comment-tools-30348" class="comment-tools"></div><div class="clear"></div><div id="comment-30348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30350"></span>

<div id="answer-container-30350" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30350-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Go to</p><blockquote><p><a href="http://www.wireshark.org/tools/string-cf.html">http://www.wireshark.org/tools/string-cf.html</a></p></blockquote><p>Then enter your string, like "GET /" and you'll get a matching capture filter, that looks weird, but works ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '14, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-30350" class="comments-container"><span id="30354"></span><div id="comment-30354" class="comment"><div id="post-30354-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much! That was what I was looking for.</p></div><div id="comment-30354-info" class="comment-info"><span class="comment-age">(03 Mar '14, 12:35)</span> svante</div></div></div><div id="comment-tools-30350" class="comment-tools"></div><div class="clear"></div><div id="comment-30350-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

