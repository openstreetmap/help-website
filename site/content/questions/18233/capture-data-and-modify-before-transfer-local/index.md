+++
type = "question"
title = "Capture data and modify before transfer (local)"
description = '''Capture data and modify before transfer (local), I have a PC running a software that transfer data to one PLC, that application had some bugs that I would like to filter and avoid transfer wrong data to the PLC, here is an example:  ^XA ^A@N,80,20,B:CYRI_UB.FNT^FO90,80^FDManufacturing Plant^FS ^FO20...'''
date = "2013-02-01T10:29:00Z"
lastmod = "2013-02-01T11:20:00Z"
weight = 18233
keywords = [ "filter" ]
aliases = [ "/questions/18233" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture data and modify before transfer (local)](/questions/18233/capture-data-and-modify-before-transfer-local)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18233-score" class="post-score" title="current number of votes">0</div><span id="post-18233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Capture data and modify before transfer (local), I have a PC running a software that transfer data to one PLC, that application had some bugs that I would like to filter and avoid transfer wrong data to the PLC, here is an example: ^XA ^<span class="__cf_email__" data-cfemail="2061606e">[email protected]</span>,80,20,B:CYRI_UB.FNT^FO90,80^FDManufacturing Plant^FS ^FO200,400^BY3^BCN,100,Y,N,N^FDDANIEL^FS ^FO350,190^BXN,10,200^FDDANIEL^FS ^FO50,35^GB800,540,4^FS ^XZ</p><p>I wanto to filter and transfer as follow</p><p>^XA ^FO200,400^BY3^BCN,100,Y,N,N^FDARTURO^FS ^FO350,190^BXN,10,200^FDJUAN^FS ^FO50,35^GB800,540,4^FS ^XZ</p><p>Wireshark can do it? is like a data filter</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '13, 10:29</strong></p><img src="https://secure.gravatar.com/avatar/e71f13d49476020301b6ec647e9fa44f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ing_israel&#39;s gravatar image" /><p><span>ing_israel</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ing_israel has no accepted answers">0%</span></p></div></div><div id="comments-container-18233" class="comments-container"><span id="18235"></span><div id="comment-18235" class="comment"><div id="post-18235-score" class="comment-score"></div><div class="comment-text"><p>how do you 'transfer' the data to the PLC?</p></div><div id="comment-18235-info" class="comment-info"><span class="comment-age">(01 Feb '13, 11:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-18233" class="comment-tools"></div><div class="clear"></div><div id="comment-18233-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18234"></span>

<div id="answer-container-18234" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18234-score" class="post-score" title="current number of votes">1</div><span id="post-18234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No. Wireshark can record network packets, but not modify them or any part of the content transported inside of them. What you need is some sort of filtering proxy mechanism, not a network analysis tool.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '13, 10:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-18234" class="comments-container"></div><div id="comment-tools-18234" class="comment-tools"></div><div class="clear"></div><div id="comment-18234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

