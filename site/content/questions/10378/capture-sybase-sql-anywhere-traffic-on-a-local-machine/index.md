+++
type = "question"
title = "capture sybase sql anywhere traffic on a local machine"
description = '''Hi. I just installed WireShark. I would like to capture all traffic between a sybase sql anywhere client and server, both operating on the same machine. The database communicates on port 2638. How do I setup WireShark to capture only sybase client/server traffic? Thanks.'''
date = "2012-04-21T09:56:00Z"
lastmod = "2012-04-21T11:56:00Z"
weight = 10378
keywords = [ "local" ]
aliases = [ "/questions/10378" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture sybase sql anywhere traffic on a local machine](/questions/10378/capture-sybase-sql-anywhere-traffic-on-a-local-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10378-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I just installed WireShark. I would like to capture all traffic between a sybase sql anywhere client and server, both operating on the same machine. The database communicates on port 2638. How do I setup WireShark to capture only sybase client/server traffic? Thanks.</p></div><div id="question-tags" class="tags-container tags">local</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '12, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/fc1b93ab936f907277a47ef41a736bbb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="snowtracks&#39;s gravatar image" /><p>snowtracks<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="snowtracks has no accepted answers">0%</span></p></div></div><div id="comments-container-10378" class="comments-container"></div><div id="comment-tools-10378" class="comment-tools"></div><div class="clear"></div><div id="comment-10378-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10379"></span>

<div id="answer-container-10379" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10379-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If your OS is Windows then you may have difficulties. Local machine traffic moves around the networking stack at a level where WinPCap (the actual capturing mechanism used by Wireshark) can't get hold of it.</p><p>If you can arrange to run the client on another machine then capturing the traffic may be much easier. See the Wiki page on <a href="http://wiki.wireshark.org/CaptureSetup/Loopback">Loopback Capture</a> for more info</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '12, 11:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-10379" class="comments-container"></div><div id="comment-tools-10379" class="comment-tools"></div><div class="clear"></div><div id="comment-10379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

