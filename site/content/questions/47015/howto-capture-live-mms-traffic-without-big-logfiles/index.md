+++
type = "question"
title = "Howto capture live MMS traffic without BIG logfiles?"
description = '''How to combine 2 filters to get HTTP GET and POST in the same command? I have tried but result have been only the first filter part. HTTP GET Capture filter sudo tshark -i p2p3 &#x27;port 80 and (tcp[((tcp[12:1] &amp;amp; 0xf0) &amp;gt;&amp;gt; 2):4] = 0x47455420)&#x27; HTTP POST Capture filter sudo tshark -i p2p3 &#x27;tcp p...'''
date = "2015-10-28T07:36:00Z"
lastmod = "2015-11-09T08:10:00Z"
weight = 47015
keywords = [ "post", "http", "tshark", "get" ]
aliases = [ "/questions/47015" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Howto capture live MMS traffic without BIG logfiles?](/questions/47015/howto-capture-live-mms-traffic-without-big-logfiles)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47015-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to combine 2 filters to get HTTP GET and POST in the same command? I have tried but result have been only the first filter part.</p><p>HTTP GET Capture filter sudo tshark -i p2p3 'port 80 and (tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x47455420)'</p><p>HTTP POST Capture filter sudo tshark -i p2p3 'tcp port 80 and (tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x504f5354)'</p><p>Or is there a way to filter out picture and video content since this is the source of the problem?</p></div><div id="question-tags" class="tags-container tags">post http tshark get</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '15, 07:36</strong></p><img src="https://secure.gravatar.com/avatar/8137fe6ef9a31e720b8be0ed865c3a73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmh64swe&#39;s gravatar image" /><p>jmh64swe<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmh64swe has no accepted answers">0%</span></p></div></div><div id="comments-container-47015" class="comments-container"><span id="47018"></span><div id="comment-47018" class="comment"><div id="post-47018-score" class="comment-score"></div><div class="comment-text"><p>What was the combined filter that you tried? If the two filters each worked separately, you should be able to combine them with a logical 'or'.</p></div><div id="comment-47018-info" class="comment-info"><span class="comment-age">(28 Oct '15, 08:26)</span> Jim Aragon</div></div><span id="47144"></span><div id="comment-47144" class="comment"><div id="post-47144-score" class="comment-score"></div><div class="comment-text"><p>Now I tested tshark -i p2p3 'tcp port 80 and (tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x504f5354)' or 'tcp port 80 and (tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x504f5354)' but this only gives the last filter in the output.</p></div><div id="comment-47144-info" class="comment-info"><span class="comment-age">(02 Nov '15, 03:54)</span> jmh64swe</div></div><span id="47278"></span><div id="comment-47278" class="comment"><div id="post-47278-score" class="comment-score"></div><div class="comment-text"><p>Any comment?</p></div><div id="comment-47278-info" class="comment-info"><span class="comment-age">(05 Nov '15, 01:05)</span> jmh64swe</div></div><span id="47432"></span><div id="comment-47432" class="comment"><div id="post-47432-score" class="comment-score"></div><div class="comment-text"><p>Is there other ways to discard the actual picture/video content?</p></div><div id="comment-47432-info" class="comment-info"><span class="comment-age">(09 Nov '15, 07:19)</span> jmh64swe</div></div></div><div id="comment-tools-47015" class="comment-tools"></div><div class="clear"></div><div id="comment-47015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47433"></span>

<div id="answer-container-47433" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47433-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can set the <code>-s</code> snaplen parameter to cut the contents of each packet at a particular length. Have a look at the Wiki page for <a href="https://wiki.wireshark.org/SnapLen">SnapLen</a> for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '15, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-47433" class="comments-container"></div><div id="comment-tools-47433" class="comment-tools"></div><div class="clear"></div><div id="comment-47433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

