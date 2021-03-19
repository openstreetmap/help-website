+++
type = "question"
title = "Wireshark Jitter problem"
description = '''Today I install the new version of Wiredshark. Before that when I was in the RTP player I could change the jitter and decode with the new jitter setting and see the voice impacted by the jitter. Now with the new version if I change the jitter nothing happen...  How can I see the influence of jitter ...'''
date = "2016-02-08T12:53:00Z"
lastmod = "2016-02-10T06:06:00Z"
weight = 49984
keywords = [ "player", "jitter", "rtp" ]
aliases = [ "/questions/49984" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Jitter problem](/questions/49984/wireshark-jitter-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49984-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Today I install the new version of Wiredshark. Before that when I was in the RTP player I could change the jitter and decode with the new jitter setting and see the voice impacted by the jitter. Now with the new version if I change the jitter nothing happen...</p><p>How can I see the influence of jitter with the new version?</p></div><div id="question-tags" class="tags-container tags">player jitter rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '16, 12:53</strong></p><img src="https://secure.gravatar.com/avatar/30f569e01b90ee12a5cc63ec5dc127d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mariposa%20Blue&#39;s gravatar image" /><p>Mariposa Blue<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mariposa Blue has no accepted answers">0%</span></p></div></div><div id="comments-container-49984" class="comments-container"></div><div id="comment-tools-49984" class="comment-tools"></div><div class="clear"></div><div id="comment-49984-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50051"></span>

<div id="answer-container-50051" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50051-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks for the report: indeed jitter buffer management is buggy in Qt GUI (GTK GUI is working fine). I just pushed a fix that should hopefully resolve the issue here: <a href="https://code.wireshark.org/review/#/c/13885/1">https://code.wireshark.org/review/#/c/13885/1</a></p><p>I will try to have it land before Wireshark 2.0.2 is out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '16, 06:06</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-50051" class="comments-container"><span id="50052"></span><div id="comment-50052" class="comment"><div id="post-50052-score" class="comment-score"></div><div class="comment-text"><p>Thanks!!!!</p></div><div id="comment-50052-info" class="comment-info"><span class="comment-age">(10 Feb '16, 06:10)</span> Mariposa Blue</div></div></div><div id="comment-tools-50051" class="comment-tools"></div><div class="clear"></div><div id="comment-50051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50012"></span>

<div id="answer-container-50012" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50012-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I installed the old version, because I didn't had time to wait for a answer...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '16, 06:20</strong></p><img src="https://secure.gravatar.com/avatar/30f569e01b90ee12a5cc63ec5dc127d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mariposa%20Blue&#39;s gravatar image" /><p>Mariposa Blue<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mariposa Blue has no accepted answers">0%</span></p></div></div><div id="comments-container-50012" class="comments-container"><span id="50014"></span><div id="comment-50014" class="comment"><div id="post-50014-score" class="comment-score"></div><div class="comment-text"><p>Are you aware that the Windows install includes the legacy version, i.e. all the other improvements of 2.x, but still with the old UI and UI tools?</p></div><div id="comment-50014-info" class="comment-info"><span class="comment-age">(09 Feb '16, 07:19)</span> grahamb ♦</div></div><span id="50016"></span><div id="comment-50016" class="comment"><div id="post-50016-score" class="comment-score"></div><div class="comment-text"><p>No I dont, but since i'm working on a problem I didn't had time to search further.</p></div><div id="comment-50016-info" class="comment-info"><span class="comment-age">(09 Feb '16, 07:33)</span> Mariposa Blue</div></div></div><div id="comment-tools-50012" class="comment-tools"></div><div class="clear"></div><div id="comment-50012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

