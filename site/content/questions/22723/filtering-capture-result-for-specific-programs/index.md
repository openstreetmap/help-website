+++
type = "question"
title = "filtering capture result for specific programs"
description = '''Is it possible to filter the capture result for specific programs so that it only shows the packets which that program has sent/recieved ?'''
date = "2013-07-08T05:46:00Z"
lastmod = "2013-07-08T05:48:00Z"
weight = 22723
keywords = [ "capture", "program", "filtering" ]
aliases = [ "/questions/22723" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [filtering capture result for specific programs](/questions/22723/filtering-capture-result-for-specific-programs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22723-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to filter the capture result for specific programs so that it only shows the packets which that program has sent/recieved ?</p></div><div id="question-tags" class="tags-container tags">capture program filtering</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '13, 05:46</strong></p><img src="https://secure.gravatar.com/avatar/1206ef65764ee2e1944067f02209107d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Milad%20Rad&#39;s gravatar image" /><p>Milad Rad<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Milad Rad has no accepted answers">0%</span></p></div></div><div id="comments-container-22723" class="comments-container"></div><div id="comment-tools-22723" class="comment-tools"></div><div class="clear"></div><div id="comment-22723-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22724"></span>

<div id="answer-container-22724" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22724-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, you can't unless each program uses specific ports that you can associate to the program, e.g. port 80 being an apache web server process. This means that you need to know for certain that there is that program running on the originating host, and no other program "hijacked" that port. There is no program executable name or other identification of the originating process in a trace file, unless using capture programs that can provide this (like Microsoft NetMon etc.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '13, 05:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jul '13, 05:50</p></div></div><div id="comments-container-22724" class="comments-container"></div><div id="comment-tools-22724" class="comment-tools"></div><div class="clear"></div><div id="comment-22724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

