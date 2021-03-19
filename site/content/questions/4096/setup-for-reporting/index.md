+++
type = "question"
title = "Setup for reporting"
description = '''I have just downloaded wireshark - do I need to set up things to get the reports that I need on normal internet usage??'''
date = "2011-05-16T07:49:00Z"
lastmod = "2011-05-16T22:08:00Z"
weight = 4096
keywords = [ "setup", "reports" ]
aliases = [ "/questions/4096" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Setup for reporting](/questions/4096/setup-for-reporting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4096-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have just downloaded wireshark - do I need to set up things to get the reports that I need on normal internet usage??</p></div><div id="question-tags" class="tags-container tags">setup reports</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '11, 07:49</strong></p><img src="https://secure.gravatar.com/avatar/8447cd5dc702739c4bb617f185044d78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jax&#39;s gravatar image" /><p>Jax<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jax has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 16 May '11, 21:41</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4096" class="comments-container"></div><div id="comment-tools-4096" class="comment-tools"></div><div class="clear"></div><div id="comment-4096-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4098"></span>

<div id="answer-container-4098" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4098-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First, verify your capture privileges (read the <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">Wireshark Wiki</a> on this).</p><p>By "reports", I assume you mean statistics. Wireshark has several <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChUseStatisticsMenuSection.html">Statistics</a> you can look at while packets are being captured (or after the fact). If you're looking for a specific type of traffic, then you need to setup the display filter. For example, you could use a display filter of "http" in IO Graphs (shown below). The black line (Graph 1) is all traffic, and the red line (Graph 2) is the HTTP traffic.</p><p><img src="http://www.wireshark.org/docs/wsug_html_chunked/wsug_graphics/ws-stats-iographs.png" alt="IO Graphs" />.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '11, 22:08</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 20 May '11, 20:46</p></div></div><div id="comments-container-4098" class="comments-container"></div><div id="comment-tools-4098" class="comment-tools"></div><div class="clear"></div><div id="comment-4098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

