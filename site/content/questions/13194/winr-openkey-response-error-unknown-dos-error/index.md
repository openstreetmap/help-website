+++
type = "question"
title = "winr openkey response, error unknown dos error"
description = '''I am getting tons of malformed packet errors with &quot; winr openkey response, error unknown dos error&quot; in the information before and below. '''
date = "2012-07-31T12:55:00Z"
lastmod = "2012-08-01T04:03:00Z"
weight = 13194
keywords = [ "errors" ]
aliases = [ "/questions/13194" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [winr openkey response, error unknown dos error](/questions/13194/winr-openkey-response-error-unknown-dos-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13194-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am getting tons of malformed packet errors with " winr openkey response, error unknown dos error" in the information before and below.</p></div><div id="question-tags" class="tags-container tags">errors</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '12, 12:55</strong></p><img src="https://secure.gravatar.com/avatar/78f68b10839b77b651973cf979129185?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cyberseeds&#39;s gravatar image" /><p>cyberseeds<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cyberseeds has no accepted answers">0%</span></p></div></div><div id="comments-container-13194" class="comments-container"></div><div id="comment-tools-13194" class="comment-tools"></div><div class="clear"></div><div id="comment-13194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13196"></span>

<div id="answer-container-13196" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13196-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Perhaps they're not actually "Windows Registry access" protocol packets, and Wireshark is misidentifying them as such, trying to dissect them as such, and reporting errors (which would be errors if they <em>were</em> those packets, but wouldn't be if they're not). You might want to <a href="http://bugs.wireshark.org/">file a bug on that</a> and attach a capture file to the bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '12, 13:42</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Jul '12, 13:50</p></div></div><div id="comments-container-13196" class="comments-container"></div><div id="comment-tools-13196" class="comment-tools"></div><div class="clear"></div><div id="comment-13196-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13228"></span>

<div id="answer-container-13228" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13228-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can select the protocol in the packet details pane and select from the context menu the option 'Disable protocol...'. This disables the dissector (for that session) to allow possible other dissectors to pick up the traffic. Another option is to select from the context menu the option 'Decode as...', and then select the protocol you think it is.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '12, 04:03</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-13228" class="comments-container"></div><div id="comment-tools-13228" class="comment-tools"></div><div class="clear"></div><div id="comment-13228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

