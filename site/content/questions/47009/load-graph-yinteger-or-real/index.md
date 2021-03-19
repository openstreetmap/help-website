+++
type = "question"
title = "LOAD graph : y=integer or real ?"
description = '''Hi ,  I&#x27;am trying to understand an smb load graph .. analysing a sniffer trace with wireshark 1.12.4 gives :  analysing the same trace with wireshark 1.6.2 gives :  so it seems that wireshark no more uses integer to represent the values . i.e. the two graphs give the same value which is max 0.5 IO ....'''
date = "2015-10-28T02:30:00Z"
lastmod = "2015-10-28T18:36:00Z"
weight = 47009
keywords = [ "iograph" ]
aliases = [ "/questions/47009" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [LOAD graph : y=integer or real ?](/questions/47009/load-graph-yinteger-or-real)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47009-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi , I'am trying to understand an smb load graph ..</p><p>analysing a sniffer trace with wireshark 1.12.4 gives : <img src="https://osqa-ask.wireshark.org/upfiles/W1.12.4_IW36GeQ.jpeg" alt="alt text" /></p><p>analysing the same trace with wireshark 1.6.2 gives : <img src="https://osqa-ask.wireshark.org/upfiles/W1.6.2_cuu4bna.JPG" alt="alt text" /></p><p>so it seems that wireshark no more uses integer to represent the values . i.e. the two graphs give the same value which is max 0.5 IO . ? Is that correct ?</p><p>jm</p></div><div id="question-tags" class="tags-container tags">iograph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '15, 02:30</strong></p><img src="https://secure.gravatar.com/avatar/bf3b6fb4e16ad7abad1e9c2af6ff83d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmnogues&#39;s gravatar image" /><p>jmnogues<br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmnogues has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 28 Oct '15, 21:25</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></img></div></div><div id="comments-container-47009" class="comments-container"></div><div id="comment-tools-47009" class="comment-tools"></div><div class="clear"></div><div id="comment-47009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47042"></span>

<div id="answer-container-47042" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47042-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like this was an <a href="http://anonsvn.wireshark.org/viewvc/viewvc.cgi?view=rev&amp;revision=49647">intentional change</a> between these two versions.</p><p>The commit message for that change says:</p><pre><code>IOSTAT: plot LOAD y-axis in number of I/O  not number of I/O times 1000</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '15, 18:36</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-47042" class="comments-container"></div><div id="comment-tools-47042" class="comment-tools"></div><div class="clear"></div><div id="comment-47042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

