+++
type = "question"
title = "Bandwidth measurement and display for each tcp connection in wireshark."
description = '''Hi All,  I am new to wireshark , recently started . I am trying to measure the bandwidth between two hosts which uses tcp connection. I want it to be displayed graphically and it should be dynamic( display contiously throught the connection).  Is there any option for this to get it done ? . Best Reg...'''
date = "2012-05-30T04:18:00Z"
lastmod = "2012-05-30T04:33:00Z"
weight = 11469
keywords = [ "bandwidthutilization" ]
aliases = [ "/questions/11469" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Bandwidth measurement and display for each tcp connection in wireshark.](/questions/11469/bandwidth-measurement-and-display-for-each-tcp-connection-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11469-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am new to wireshark , recently started . I am trying to measure the bandwidth between two hosts which uses tcp connection. I want it to be displayed graphically and it should be dynamic( display contiously throught the connection).</p><p>Is there any option for this to get it done ? .</p><p>Best Regards, yash</p></div><div id="question-tags" class="tags-container tags">bandwidthutilization</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '12, 04:18</strong></p><img src="https://secure.gravatar.com/avatar/5dc8192968061e7ff0475f55dc94802f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yash&#39;s gravatar image" /><p>yash<br />
<span class="score" title="2 reputation points">2</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yash has no accepted answers">0%</span></p></div></div><div id="comments-container-11469" class="comments-container"></div><div id="comment-tools-11469" class="comment-tools"></div><div class="clear"></div><div id="comment-11469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11470"></span>

<div id="answer-container-11470" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11470-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could just use the I/O Graph (statistics menu). If you put in a filter for the according tcp session in one of the filter edit boxes you can have it track just that one session, even while it is still being captured. A filter for a tcp session is usually either created by filtering on IPs and ports of both nodes, or by using the tcp stream index.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '12, 04:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-11470" class="comments-container"></div><div id="comment-tools-11470" class="comment-tools"></div><div class="clear"></div><div id="comment-11470-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

