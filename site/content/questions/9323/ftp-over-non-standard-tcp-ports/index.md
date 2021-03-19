+++
type = "question"
title = "FTP over non-standard TCP ports"
description = '''is it possible to build a capture filter to capture FTP traffic using non-standard TCP port 20 or 21?'''
date = "2012-03-02T23:26:00Z"
lastmod = "2012-03-03T08:26:00Z"
weight = 9323
keywords = [ "ftp" ]
aliases = [ "/questions/9323" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [FTP over non-standard TCP ports](/questions/9323/ftp-over-non-standard-tcp-ports)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9323-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>is it possible to build a capture filter to capture FTP traffic using non-standard TCP port 20 or 21?</p></div><div id="question-tags" class="tags-container tags">ftp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '12, 23:26</strong></p><img src="https://secure.gravatar.com/avatar/aff55c3506ef4f245350fb1191a40d78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wsitu&#39;s gravatar image" /><p>wsitu<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wsitu has no accepted answers">0%</span></p></div></div><div id="comments-container-9323" class="comments-container"></div><div id="comment-tools-9323" class="comment-tools"></div><div class="clear"></div><div id="comment-9323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9325"></span>

<div id="answer-container-9325" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9325-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are using Active FTP, you can use the alternative TCP ports for the command and the data channel to build a capture filter. If you use 10021 for the command channel and 10020 for the data channel, you can use the capture filter <code>"tcp port 10021 or 10020"</code>.</p><p>If you are using passive FTP, then you can only filter on the command channel, as the data channel uses ephemeral ports for which you would have to do deep inspection of the FTP traffic to extract the port numbers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '12, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9325" class="comments-container"></div><div id="comment-tools-9325" class="comment-tools"></div><div class="clear"></div><div id="comment-9325-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

