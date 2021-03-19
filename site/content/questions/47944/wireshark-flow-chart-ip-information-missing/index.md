+++
type = "question"
title = "Wireshark Flow Chart / IP information missing"
description = '''Hi folks, I downloaded Wireshark (today), watched youtube tutorials, captured traffic and tried to generate a flow chart. But... there are no ip addresses/hostnames above the flow chart, as there are in screenshots or videos of previous versions. Is there a bug/change? Should not a flow chart contai...'''
date = "2015-11-24T16:36:00Z"
lastmod = "2015-11-24T16:54:00Z"
weight = 47944
keywords = [ "flow", "chart" ]
aliases = [ "/questions/47944" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Flow Chart / IP information missing](/questions/47944/wireshark-flow-chart-ip-information-missing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47944-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi folks,</p><p>I downloaded Wireshark (today), watched youtube tutorials, captured traffic and tried to generate a flow chart.</p><p>But... there are no ip addresses/hostnames above the flow chart, as there are in screenshots or videos of previous versions. Is there a bug/change?</p><p>Should not a flow chart contain the information which ip addresses were involved during communication?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2015-11-25_01-42-32_819noHh.png" alt="missing ip addresses" /></p><p>I tried with Windows and Mac version - no difference. Please advice.</p><p>With best regards dm7</p></div><div id="question-tags" class="tags-container tags">flow chart</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '15, 16:36</strong></p><img src="https://secure.gravatar.com/avatar/8f81b83d4a6c79d78206482590b919d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dm7&#39;s gravatar image" /><p>dm7<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dm7 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 24 Nov '15, 16:45</p></div></div><div id="comments-container-47944" class="comments-container"></div><div id="comment-tools-47944" class="comment-tools"></div><div class="clear"></div><div id="comment-47944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47947"></span>

<div id="answer-container-47947" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47947-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You have tried the latest stable build 2.0.x and apparently it's either not implemented or there is still a bug.</p><p>Please try 1.12.8 (old stable) and you'll see the IP addresses.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '15, 16:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-47947" class="comments-container"><span id="47949"></span><div id="comment-47949" class="comment"><div id="post-47949-score" class="comment-score"></div><div class="comment-text"><p>Seems to be a bug in wireshark QT. wireshark V2 'legacy' still shows the IP addresses</p></div><div id="comment-47949-info" class="comment-info"><span class="comment-age">(24 Nov '15, 21:54)</span> mrEEde</div></div><span id="47950"></span><div id="comment-47950" class="comment"><div id="post-47950-score" class="comment-score"></div><div class="comment-text"><p>This is a known missing feature tracked by <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11710">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11710</a></p></div><div id="comment-47950-info" class="comment-info"><span class="comment-age">(24 Nov '15, 22:51)</span> Pascal Quantin</div></div></div><div id="comment-tools-47947" class="comment-tools"></div><div class="clear"></div><div id="comment-47947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

