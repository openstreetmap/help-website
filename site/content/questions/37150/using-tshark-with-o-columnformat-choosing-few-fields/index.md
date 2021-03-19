+++
type = "question"
title = "Using tshark with -o &quot;column.format: choosing few fields"
description = '''Hello Group, I would like to produce output based on few fields i choose to pick, I found out searching the internet that -o &quot;column.format:&#92;&quot;Info&#92;&quot;,&#92;&quot;%i&#92;&quot;&quot; for info column my question is how or is it possible to chain few more fields like  Time , source, destination,info ,protocol , Ack Rtt etc... ...'''
date = "2014-10-18T05:41:00Z"
lastmod = "2014-10-18T07:01:00Z"
weight = 37150
keywords = [ "-o", "tshark" ]
aliases = [ "/questions/37150" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Using tshark with -o "column.format: choosing few fields](/questions/37150/using-tshark-with-o-columnformat-choosing-few-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37150-score" class="post-score" title="current number of votes">0</div><span id="post-37150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Group,</p><p>I would like to produce output based on few fields i choose to pick, I found out searching the internet that <code>-o "column.format:\"Info\",\"%i\""</code> for info column my question is how or is it possible to chain few more fields like Time , source, destination,info ,protocol , Ack Rtt etc... just to a quick notice i currently working under Windows</p><p>Please advice</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link--o" rel="tag" title="see questions tagged &#39;-o&#39;">-o</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '14, 05:41</strong></p><img src="https://secure.gravatar.com/avatar/491b248bc5431fa4cfed4498e4633f51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tbaror&#39;s gravatar image" /><p><span>tbaror</span><br />
<span class="score" title="10 reputation points">10</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tbaror has no accepted answers">0%</span></p></div></div><div id="comments-container-37150" class="comments-container"></div><div id="comment-tools-37150" class="comment-tools"></div><div class="clear"></div><div id="comment-37150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37151"></span>

<div id="answer-container-37151" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37151-score" class="post-score" title="current number of votes">1</div><span id="post-37151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tbaror has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Look at the <code>-T fields</code> and <code>-e xxx</code> options. Note that you can apply as many -e options as you wish.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '14, 07:01</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-37151" class="comments-container"></div><div id="comment-tools-37151" class="comment-tools"></div><div class="clear"></div><div id="comment-37151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

