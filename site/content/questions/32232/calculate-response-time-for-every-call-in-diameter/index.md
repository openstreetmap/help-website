+++
type = "question"
title = "calculate response time for every call in diameter"
description = '''Hi All, I want to calculate response time of each diameter call ( response time of each CCR--&amp;gt; CCA pair ). Can anybody suggest how can I achieve this? Thanks, Vidhi.'''
date = "2014-04-28T00:05:00Z"
lastmod = "2014-04-28T08:24:00Z"
weight = 32232
keywords = [ "diameter", "response", "time" ]
aliases = [ "/questions/32232" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [calculate response time for every call in diameter](/questions/32232/calculate-response-time-for-every-call-in-diameter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32232-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I want to calculate response time of each diameter call ( response time of each CCR--&gt; CCA pair ).</p><p>Can anybody suggest how can I achieve this?</p><p>Thanks, Vidhi.</p></div><div id="question-tags" class="tags-container tags">diameter response time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '14, 00:05</strong></p><img src="https://secure.gravatar.com/avatar/b794b90289cddde7dadc03e91012c605?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vidhi&#39;s gravatar image" /><p>Vidhi<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vidhi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Apr '14, 08:16</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-32232" class="comments-container"></div><div id="comment-tools-32232" class="comment-tools"></div><div class="clear"></div><div id="comment-32232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32261"></span>

<div id="answer-container-32261" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32261-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark already calculates the response times (at least in modern versions) so it really depends on what you want to do with the information. For example, you could use <code>tshark</code> to list all the response times by themselves like this:</p><p><code>tshark -n -T fields -e diameter.resp_time -Y diameter.resp_time -r /path/to/file.pcapng</code></p><p>(The "-Y" bit tells tshark to only show those frames that have the "diameter.resp_time" field.)</p><p>(Of course you could also pull some more details of each transaction with more "-e" arguments, like <code>-e diameter.Session-Id -e diameter.endtoendid</code>.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '14, 08:24</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-32261" class="comments-container"><span id="32376"></span><div id="comment-32376" class="comment"><div id="post-32376-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much! It solved my task.</p></div><div id="comment-32376-info" class="comment-info"><span class="comment-age">(01 May '14, 21:18)</span> Vidhi</div></div></div><div id="comment-tools-32261" class="comment-tools"></div><div class="clear"></div><div id="comment-32261-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

