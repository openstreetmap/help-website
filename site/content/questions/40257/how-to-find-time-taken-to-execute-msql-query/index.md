+++
type = "question"
title = "How to find time taken to execute msql query"
description = '''Hi I have captured mysql traffic with wireshark. I would like to know how long it took to execute the query. what type of filter can i use to get this information. thanks'''
date = "2015-03-04T05:29:00Z"
lastmod = "2015-03-04T05:40:00Z"
weight = 40257
keywords = [ "mysql" ]
aliases = [ "/questions/40257" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to find time taken to execute msql query](/questions/40257/how-to-find-time-taken-to-execute-msql-query)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40257-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have captured mysql traffic with wireshark. I would like to know how long it took to execute the query.</p><p>what type of filter can i use to get this information.</p><p>thanks</p></div><div id="question-tags" class="tags-container tags">mysql</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '15, 05:29</strong></p><img src="https://secure.gravatar.com/avatar/be8a9b2e9d87b13606c3b9e75d26e71d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scara&#39;s gravatar image" /><p>scara<br />
<span class="score" title="31 reputation points">31</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scara has no accepted answers">0%</span></p></div></div><div id="comments-container-40257" class="comments-container"></div><div id="comment-tools-40257" class="comment-tools"></div><div class="clear"></div><div id="comment-40257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40259"></span>

<div id="answer-container-40259" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40259-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Usually, find the request and find the last packet of the response. Then use a time reference point on the relative time column to determine how long it took between those two (set your time column to "seconds since beginning of the capture" and use the popup menu on the request packet to set a time reference).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '15, 05:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-40259" class="comments-container"></div><div id="comment-tools-40259" class="comment-tools"></div><div class="clear"></div><div id="comment-40259-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

