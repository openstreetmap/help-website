+++
type = "question"
title = "Wireshark for HTTP packets"
description = '''Hi guys, In wireshark I am facing another issues. I am sending HTTP requests for same url, so I am getting HTTP responses. But In Some HTTP responses Info field as &quot;HTTP/1.1 403 Forbidden (text/html)&quot; and Some Http responses Info field as &quot;Continuation or non-HTTP traffic&quot;. But data is seeing as TCP...'''
date = "2016-02-05T01:32:00Z"
lastmod = "2016-02-05T02:50:00Z"
weight = 49888
keywords = [ "about_wireshark" ]
aliases = [ "/questions/49888" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark for HTTP packets](/questions/49888/wireshark-for-http-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49888-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>In wireshark I am facing another issues.</p><p>I am sending HTTP requests for same url, so I am getting HTTP responses. But In Some HTTP responses Info field as "HTTP/1.1 403 Forbidden (text/html)" and Some Http responses Info field as "Continuation or non-HTTP traffic". But data is seeing as TCP segments. Can u guys tell me the reason and solution about this issue.</p><p>Regards, Swathi.</p></div><div id="question-tags" class="tags-container tags">about_wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '16, 01:32</strong></p><img src="https://secure.gravatar.com/avatar/a34282ab2b31d84bc63d5ea83c15d775?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swathi%20jakkam&#39;s gravatar image" /><p>swathi jakkam<br />
<span class="score" title="6 reputation points">6</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swathi jakkam has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Feb '16, 02:43</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-49888" class="comments-container"></div><div id="comment-tools-49888" class="comment-tools"></div><div class="clear"></div><div id="comment-49888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49891"></span>

<div id="answer-container-49891" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49891-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What Wireshark is telling you is most likely true, so your requests to the same URL may look the same but differ in some bits, causing the server to treat them in a different way. In that case, the solution would be to fix the contents of the http requests. Or the server may treat the requests in a different way due to its own dynamic condition (overload, access to user authentication database broken, ...) - in that case, the solution would be to fix something at server side.</p><p>If you want to get more detailed information, please publish the capture somewhere for public access (not requesting any login) and provide a link to it here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '16, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-49891" class="comments-container"></div><div id="comment-tools-49891" class="comment-tools"></div><div class="clear"></div><div id="comment-49891-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

