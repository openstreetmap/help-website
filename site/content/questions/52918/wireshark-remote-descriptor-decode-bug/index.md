+++
type = "question"
title = "Wireshark remote descriptor decode bug"
description = '''Hi, I am using the latest Wireshark (2.0.3) and it seems it decodes the megaco message incorrectly: it identifies remote descriptor as local descriptor (eg. in an add command). Has anybody met this issue as well? Br, Maegoss'''
date = "2016-05-25T08:20:00Z"
lastmod = "2016-05-25T10:09:00Z"
weight = 52918
keywords = [ "remote-descriptor", "megaco" ]
aliases = [ "/questions/52918" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark remote descriptor decode bug](/questions/52918/wireshark-remote-descriptor-decode-bug)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52918-score" class="post-score" title="current number of votes">0</div><span id="post-52918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am using the latest Wireshark (2.0.3) and it seems it decodes the megaco message incorrectly: it identifies remote descriptor as local descriptor (eg. in an add command).</p><p>Has anybody met this issue as well?</p><p>Br, Maegoss</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-remote-descriptor" rel="tag" title="see questions tagged &#39;remote-descriptor&#39;">remote-descriptor</span> <span class="post-tag tag-link-megaco" rel="tag" title="see questions tagged &#39;megaco&#39;">megaco</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 May '16, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/db0ca15f86ebfc124b300043c47f8a63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maegoss&#39;s gravatar image" /><p><span>Maegoss</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maegoss has no accepted answers">0%</span></p></div></div><div id="comments-container-52918" class="comments-container"></div><div id="comment-tools-52918" class="comment-tools"></div><div class="clear"></div><div id="comment-52918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52929"></span>

<div id="answer-container-52929" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52929-score" class="post-score" title="current number of votes">0</div><span id="post-52929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>According to a quick search of <a href="https://bugs.wireshark.org/bugzilla/query.cgi">the bug database</a> no. So you could file a bug report on that, and don't forget to attach a capture file showing this problem, to verify and test a possible fix.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '16, 10:09</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-52929" class="comments-container"></div><div id="comment-tools-52929" class="comment-tools"></div><div class="clear"></div><div id="comment-52929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

