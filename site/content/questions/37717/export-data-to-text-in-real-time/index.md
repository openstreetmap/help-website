+++
type = "question"
title = "Export data to text in real time?"
description = '''Hello, I am trying to export data in real time to either text or C array. Suggestions as to how?  Thanks! Ess Tee'''
date = "2014-11-09T16:33:00Z"
lastmod = "2014-11-11T14:40:00Z"
weight = 37717
keywords = [ "export", "real-time" ]
aliases = [ "/questions/37717" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Export data to text in real time?](/questions/37717/export-data-to-text-in-real-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37717-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to export data in real time to either text or C array. Suggestions as to how?</p><p>Thanks!</p><p>Ess Tee</p></div><div id="question-tags" class="tags-container tags">export real-time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '14, 16:33</strong></p><img src="https://secure.gravatar.com/avatar/f6477025d3a37749f7be652be9422937?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ess%20Tee&#39;s gravatar image" /><p>Ess Tee<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ess Tee has no accepted answers">0%</span></p></div></div><div id="comments-container-37717" class="comments-container"></div><div id="comment-tools-37717" class="comment-tools"></div><div class="clear"></div><div id="comment-37717-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37730"></span>

<div id="answer-container-37730" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37730-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>File &gt;&gt; export packet Dissections &gt;&gt; "plain text" then mark "Packet summary line" and unmark all other</p><p>update !!</p><p>Only now I noticed that in real time.</p><p>There is no way to do this in real time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '14, 08:13</strong></p><img src="https://secure.gravatar.com/avatar/1ce4fe2b91a61d892d4c9b6a373704eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shlomig&#39;s gravatar image" /><p>shlomig<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shlomig has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Nov '14, 08:23</p></div></div><div id="comments-container-37730" class="comments-container"></div><div id="comment-tools-37730" class="comment-tools"></div><div class="clear"></div><div id="comment-37730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37765"></span>

<div id="answer-container-37765" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37765-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try using <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark</a>.</p><blockquote><p>tshark -ni eth0 -xV -R "port 80"</p></blockquote><p>Then parse the output of that command with a script.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '14, 14:40</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Nov '14, 14:41</p></div></div><div id="comments-container-37765" class="comments-container"></div><div id="comment-tools-37765" class="comment-tools"></div><div class="clear"></div><div id="comment-37765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

