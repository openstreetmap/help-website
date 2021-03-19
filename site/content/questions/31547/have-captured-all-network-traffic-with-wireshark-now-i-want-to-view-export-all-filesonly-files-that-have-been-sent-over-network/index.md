+++
type = "question"
title = "have captured all network traffic with wireshark. now  i want to view (export) all files(only files) that have been  sent over network"
description = '''Hi, I have captured all network traffic with wireshark. now i want to view (export) all files(only files) that have been sent over network. Is it possible ? how to do that?'''
date = "2014-04-05T06:14:00Z"
lastmod = "2014-04-05T12:17:00Z"
weight = 31547
keywords = [ "file" ]
aliases = [ "/questions/31547" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [have captured all network traffic with wireshark. now i want to view (export) all files(only files) that have been sent over network](/questions/31547/have-captured-all-network-traffic-with-wireshark-now-i-want-to-view-export-all-filesonly-files-that-have-been-sent-over-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31547-score" class="post-score" title="current number of votes">0</div><span id="post-31547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have captured all network traffic with wireshark. now i want to view (export) all files(only files) that have been sent over network. Is it possible ? how to do that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '14, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/3c58a493605601b7b484885df88a0779?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hasanaliyev555&#39;s gravatar image" /><p><span>hasanaliyev555</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hasanaliyev555 has no accepted answers">0%</span></p></div></div><div id="comments-container-31547" class="comments-container"></div><div id="comment-tools-31547" class="comment-tools"></div><div class="clear"></div><div id="comment-31547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31549"></span>

<div id="answer-container-31549" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31549-score" class="post-score" title="current number of votes">0</div><span id="post-31549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unless your files have been transferred by HTTP or SMB this will be a lot of manual work if you want to do it with Wireshark. HTTP and SMB files can be exported from the File -&gt; Export Objects menu. Everything else may or may not be exported by carving it out of the "Follow TCP/UDP stream" content window that you have to call for each flow.</p><p>You can probably make your life a lot easier by using tools that are specialized on carving content from network packets, e.g. <a href="http://www.netresec.com/?page=NetworkMiner">Network Miner</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '14, 12:17</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-31549" class="comments-container"></div><div id="comment-tools-31549" class="comment-tools"></div><div class="clear"></div><div id="comment-31549-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

