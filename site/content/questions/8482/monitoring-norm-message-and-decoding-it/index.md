+++
type = "question"
title = "Monitoring NORM message and decoding it"
description = '''Attempting to capture NORM message at the Ethernet port. Changed the filter selection only to NORM and TCP. Wireshark capture window displays UNKONWN on protocol column. Please help where I am making mistake. I am using Wireshark 1.6.0 on Windows XP machine. Also, do I need a Wireshark decoder plugi...'''
date = "2012-01-19T11:15:00Z"
lastmod = "2012-01-20T02:44:00Z"
weight = 8482
keywords = [ "norm" ]
aliases = [ "/questions/8482" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Monitoring NORM message and decoding it](/questions/8482/monitoring-norm-message-and-decoding-it)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8482-score" class="post-score" title="current number of votes">0</div><span id="post-8482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Attempting to capture NORM message at the Ethernet port. Changed the filter selection only to NORM and TCP. Wireshark capture window displays UNKONWN on protocol column.</p><p>Please help where I am making mistake. I am using Wireshark 1.6.0 on Windows XP machine.</p><p>Also, do I need a Wireshark decoder plugin</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-norm" rel="tag" title="see questions tagged &#39;norm&#39;">norm</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '12, 11:15</strong></p><img src="https://secure.gravatar.com/avatar/a40a3b588b5ac9a3e74ad29e53abc13b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sss&#39;s gravatar image" /><p><span>sss</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sss has no accepted answers">0%</span></p></div></div><div id="comments-container-8482" class="comments-container"></div><div id="comment-tools-8482" class="comment-tools"></div><div class="clear"></div><div id="comment-8482-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8496"></span>

<div id="answer-container-8496" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8496-score" class="post-score" title="current number of votes">0</div><span id="post-8496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I guess you are referring to <a href="http://tools.ietf.org/html/rfc5740">NACK-Oriented Reliable Multicast (NORM) Transport Protocol</a>? Its dissector does exist, just make sure to set its preference "Try to decode UDP packets as NORM packets."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '12, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-8496" class="comments-container"></div><div id="comment-tools-8496" class="comment-tools"></div><div class="clear"></div><div id="comment-8496-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

