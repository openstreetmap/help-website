+++
type = "question"
title = "Mate filter for MySQL"
description = '''Hi guys I&#x27;m having a little trouble with my mate filter for MySQL I&#x27;m trying to write the start and stop conditions, but can&#x27;t seem to work out how we find the last packet - it&#x27;s quite clear in the packet list, but I can&#x27;t build the Gop or the Gog from it. Gop mysql_req On mysql_pdu Match (mysql_add...'''
date = "2013-04-25T16:04:00Z"
lastmod = "2015-09-15T07:33:00Z"
weight = 20812
keywords = [ "mate", "gop" ]
aliases = [ "/questions/20812" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Mate filter for MySQL](/questions/20812/mate-filter-for-mysql)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20812-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys I'm having a little trouble with my mate filter for MySQL I'm trying to write the start and stop conditions, but can't seem to work out how we find the last packet - it's quite clear in the packet list, but I can't build the Gop or the Gog from it.</p><pre><code>Gop mysql_req On mysql_pdu Match (mysql_addr, mysql_addr, mysql_port, mysql_port,mysql_command, mysql_eof) {
        Start (mysql_command = 3);
        Stop (mysql_eof = 254);
};</code></pre><p>I would have thought the start would be the query (mysql_command = 3) and the stop would be mysql_eof = 254, but I never get a completed gop</p><p>I'm really trying to find a way to pull out the long queries and find out what's causing them - in particular when we are unable to get a table lock within a reasonable timeframe. I've got the mysql slow logs, where I can see the issues occurring, but it would be really nice to be able to build the complete extractor.</p></div><div id="question-tags" class="tags-container tags">mate gop</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '13, 16:04</strong></p><img src="https://secure.gravatar.com/avatar/c4a59238ef906285e110fa429a9a94b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott%20Harman&#39;s gravatar image" /><p>Scott Harman<br />
<span class="score" title="46 reputation points">46</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott Harman has one accepted answer">50%</span></p></div></div><div id="comments-container-20812" class="comments-container"></div><div id="comment-tools-20812" class="comment-tools"></div><div class="clear"></div><div id="comment-20812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45855"></span>

<div id="answer-container-45855" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45855-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just came across this while looking for another question...</p><p>I'm guessing your GoP never completes because the PDUs in the GoP must all have the same <code>mysql_command</code> and <code>mysql_eof</code> (in the Match parameters). The responses aren't going to have the command number and the queries aren't going to have the eof indicator.</p><p>At least the first step in getting this working will be to remove the command and eof fields from the Match line.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '15, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-45855" class="comments-container"></div><div id="comment-tools-45855" class="comment-tools"></div><div class="clear"></div><div id="comment-45855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

