+++
type = "question"
title = "How can I observe HTTP request-response latency?"
description = '''I&#x27;d like to see HTTP request/response latency. I tried using tcp.calculate_timestamps and tcp.time_delta, but the latter is empty. I&#x27;m using a Mac in case that matters. /Applications/Wireshark.app/Contents/Resources/bin/tshark -b duration:3600 -o tcp.calculate_timestamps:TRUE -i en1 -f &#x27;tcp port 80&#x27;...'''
date = "2011-03-01T10:25:00Z"
lastmod = "2011-03-01T10:26:00Z"
weight = 2613
keywords = [ "latency", "request", "response", "tcp", "http" ]
aliases = [ "/questions/2613" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I observe HTTP request-response latency?](/questions/2613/how-can-i-observe-http-request-response-latency)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2613-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like to see HTTP request/response latency. I tried using tcp.calculate_timestamps and tcp.time_delta, but the latter is empty. I'm using a Mac in case that matters.</p><p>/Applications/Wireshark.app/Contents/Resources/bin/tshark -b duration:3600 -o tcp.calculate_timestamps:TRUE -i en1 -f 'tcp port 80' -w capture.bin</p><p>I open the capture file in Wireshark and add a column for Delta time (conversation). Its value in all rows is empty.</p></div><div id="question-tags" class="tags-container tags">latency request response tcp http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '11, 10:25</strong></p><img src="https://secure.gravatar.com/avatar/7055c5f5253d54724373553372514768?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="matthewlmcclure&#39;s gravatar image" /><p>matthewlmcclure<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="matthewlmcclure has no accepted answers">0%</span></p></div></div><div id="comments-container-2613" class="comments-container"></div><div id="comment-tools-2613" class="comment-tools"></div><div class="clear"></div><div id="comment-2613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2614"></span>

<div id="answer-container-2614" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2614-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I found the answer to my own question:</p><p>When I opened the capture file in Wireshark, I had already entered a display filter. I removed the display filter, and the values appeared in the Delta time (conversation) column. Then I added the display filter again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '11, 10:26</strong></p><img src="https://secure.gravatar.com/avatar/7055c5f5253d54724373553372514768?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="matthewlmcclure&#39;s gravatar image" /><p>matthewlmcclure<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="matthewlmcclure has no accepted answers">0%</span></p></div></div><div id="comments-container-2614" class="comments-container"></div><div id="comment-tools-2614" class="comment-tools"></div><div class="clear"></div><div id="comment-2614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

