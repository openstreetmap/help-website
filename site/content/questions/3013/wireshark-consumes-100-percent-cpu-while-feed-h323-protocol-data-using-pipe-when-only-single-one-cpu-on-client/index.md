+++
type = "question"
title = "Wireshark consumes 100 percent CPU while feed H323 protocol data using pipe when Only single one CPU on client"
description = '''I use pipe to feed H323 protocol data into Wireshark, If only single one CPU on client side, Wireshark will consume 100 percent CPU, if 4 CPUs exists, it will consume 25 percent, it will continue occupying one CPU 100 percent.'''
date = "2011-03-22T00:07:00Z"
lastmod = "2011-03-22T18:47:00Z"
weight = 3013
keywords = [ "pipe", "consume", "h323", "cpu" ]
aliases = [ "/questions/3013" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark consumes 100 percent CPU while feed H323 protocol data using pipe when Only single one CPU on client](/questions/3013/wireshark-consumes-100-percent-cpu-while-feed-h323-protocol-data-using-pipe-when-only-single-one-cpu-on-client)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3013-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use pipe to feed H323 protocol data into Wireshark, If only single one CPU on client side, Wireshark will consume 100 percent CPU, if 4 CPUs exists, it will consume 25 percent, it will continue occupying one CPU 100 percent.</p></div><div id="question-tags" class="tags-container tags">pipe consume h323 cpu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '11, 00:07</strong></p><img src="https://secure.gravatar.com/avatar/9f94dd6c84b70b9abb80a22546d09710?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brenthuang&#39;s gravatar image" /><p>brenthuang<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brenthuang has no accepted answers">0%</span></p></div></div><div id="comments-container-3013" class="comments-container"><span id="3018"></span><div id="comment-3018" class="comment"><div id="post-3018-score" class="comment-score"></div><div class="comment-text"><p>Wireshark version? Platform version? Command line used?</p></div><div id="comment-3018-info" class="comment-info"><span class="comment-age">(22 Mar '11, 07:03)</span> Jaap ♦</div></div></div><div id="comment-tools-3013" class="comment-tools"></div><div class="clear"></div><div id="comment-3013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3029"></span>

<div id="answer-container-3029" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3029-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This sounds like bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5309">5309</a>. I'd suggest upgrading to the latest version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '11, 11:20</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-3029" class="comments-container"></div><div id="comment-tools-3029" class="comment-tools"></div><div class="clear"></div><div id="comment-3029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3035"></span>

<div id="answer-container-3035" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3035-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>wireshark version: V1.4.2 Platform version: Windows XP x86 Command line:wireshark.exe -k -i pipeName</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '11, 18:47</strong></p><img src="https://secure.gravatar.com/avatar/9f94dd6c84b70b9abb80a22546d09710?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brenthuang&#39;s gravatar image" /><p>brenthuang<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brenthuang has no accepted answers">0%</span></p></div></div><div id="comments-container-3035" class="comments-container"><span id="3042"></span><div id="comment-3042" class="comment"><div id="post-3042-score" class="comment-score"></div><div class="comment-text"><p>For the record, this was opened as bug 5777: https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5777</p></div><div id="comment-3042-info" class="comment-info"><span class="comment-age">(23 Mar '11, 07:52)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-3035" class="comment-tools"></div><div class="clear"></div><div id="comment-3035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

