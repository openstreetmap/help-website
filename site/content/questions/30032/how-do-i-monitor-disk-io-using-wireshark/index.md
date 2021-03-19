+++
type = "question"
title = "How do I monitor disk i/o using wireshark"
description = '''Can someone provide the exact steps to monitor disk I/o? I currently have a Server 2003 R2 Server with wireshark installed, about 8pm every day the server freezes for around 5mins, this is the period where everyone logs off in the evening.'''
date = "2014-02-19T13:30:00Z"
lastmod = "2014-02-19T13:34:00Z"
weight = 30032
keywords = [ "disk", "io" ]
aliases = [ "/questions/30032" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I monitor disk i/o using wireshark](/questions/30032/how-do-i-monitor-disk-io-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30032-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can someone provide the exact steps to monitor disk I/o?</p><p>I currently have a Server 2003 R2 Server with wireshark installed, about 8pm every day the server freezes for around 5mins, this is the period where everyone logs off in the evening.</p></div><div id="question-tags" class="tags-container tags">disk io</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '14, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/8befce2c8dd119643872975790745d83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="unrealone&#39;s gravatar image" /><p>unrealone<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="unrealone has no accepted answers">0%</span></p></div></div><div id="comments-container-30032" class="comments-container"></div><div id="comment-tools-30032" class="comment-tools"></div><div class="clear"></div><div id="comment-30032-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30033"></span>

<div id="answer-container-30033" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30033-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark monitors network traffic not disk I/O. Unless you are assuming that the network traffic is causing the high disk I/O Wireshark won't be much help, even then you may be better off just monitoring the NIC packet counters using Performance Monitor to see if there's a correlation between the disk I/O and network I/O.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '14, 13:34</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-30033" class="comments-container"></div><div id="comment-tools-30033" class="comment-tools"></div><div class="clear"></div><div id="comment-30033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

