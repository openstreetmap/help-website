+++
type = "question"
title = "Monitoring FTP on a different port number"
description = '''Greetings - I was wondering if it possible to monitor FTP traffic to a different port number. I mean, I know it is and I can see it but just cannot see the usual FTP communications i.e. user logs in, password posting. All I see is TCP protocol no FTP at all. Data is initiated from outside to our ser...'''
date = "2016-05-23T05:25:00Z"
lastmod = "2016-05-23T05:34:00Z"
weight = 52833
keywords = [ "ftp" ]
aliases = [ "/questions/52833" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Monitoring FTP on a different port number](/questions/52833/monitoring-ftp-on-a-different-port-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52833-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings - I was wondering if it possible to monitor FTP traffic to a different port number. I mean, I know it is and I can see it but just cannot see the usual FTP communications i.e. user logs in, password posting. All I see is TCP protocol no FTP at all. Data is initiated from outside to our server. Thank you for your feedback. Mike</p></div><div id="question-tags" class="tags-container tags">ftp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '16, 05:25</strong></p><img src="https://secure.gravatar.com/avatar/dca8e78ae723e7283bf88a5154bc3993?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adrianvas12&#39;s gravatar image" /><p>adrianvas12<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adrianvas12 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 May '16, 06:34</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-52833" class="comments-container"></div><div id="comment-tools-52833" class="comment-tools"></div><div class="clear"></div><div id="comment-52833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52834"></span>

<div id="answer-container-52834" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52834-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Right-click a packet you know to belong to the "ftp to different port" control session in the packet-list, choose <code>Decode as...</code> from the context menu, and select FTP in the last column (named <code>Current</code>), and press the <code>OK</code> button. That should do the trick, including automatic detection of the data transmission sessions initiated by that control session.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '16, 05:34</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 May '16, 05:34</p></div></div><div id="comments-container-52834" class="comments-container"></div><div id="comment-tools-52834" class="comment-tools"></div><div class="clear"></div><div id="comment-52834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

