+++
type = "question"
title = "2.2.0 saved tcp streams corrupted"
description = '''I always get corrupted data if I save a tcp stream (RAW) to disk in 2.2.0. It works fine in 2.0.6 Using latest Winpcap on Win10 64bit'''
date = "2016-09-18T11:05:00Z"
lastmod = "2016-09-18T12:25:00Z"
weight = 55632
keywords = [ "corrupted", "stream", "tcp", "2.2.0" ]
aliases = [ "/questions/55632" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [2.2.0 saved tcp streams corrupted](/questions/55632/220-saved-tcp-streams-corrupted)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55632-score" class="post-score" title="current number of votes">0</div><span id="post-55632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I always get corrupted data if I save a tcp stream (RAW) to disk in 2.2.0. It works fine in 2.0.6</p><p>Using latest Winpcap on Win10 64bit</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-corrupted" rel="tag" title="see questions tagged &#39;corrupted&#39;">corrupted</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-2.2.0" rel="tag" title="see questions tagged &#39;2.2.0&#39;">2.2.0</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '16, 11:05</strong></p><img src="https://secure.gravatar.com/avatar/6825c866bde4130fb7dcc896bf35813d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spider&#39;s gravatar image" /><p><span>spider</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spider has no accepted answers">0%</span></p></div></div><div id="comments-container-55632" class="comments-container"><span id="55633"></span><div id="comment-55633" class="comment"><div id="post-55633-score" class="comment-score"></div><div class="comment-text"><p>Seems to work for me.</p><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, google Drive, DropBox etc. (with the stream indicated) that illustrates the issue?</p></div><div id="comment-55633-info" class="comment-info"><span class="comment-age">(18 Sep '16, 11:18)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="55634"></span><div id="comment-55634" class="comment"><div id="post-55634-score" class="comment-score"></div><div class="comment-text"><p>Yes I'll do tomorrow after work</p></div><div id="comment-55634-info" class="comment-info"><span class="comment-age">(18 Sep '16, 11:28)</span> <span class="comment-user userinfo">spider</span></div></div></div><div id="comment-tools-55632" class="comment-tools"></div><div class="clear"></div><div id="comment-55632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55635"></span>

<div id="answer-container-55635" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55635-score" class="post-score" title="current number of votes">2</div><span id="post-55635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is a known issue currently tracked (and discussed) in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12855">bug 12855</a>. Hopefully we will solve it in time for Wireshark 2.0.1.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '16, 12:25</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-55635" class="comments-container"></div><div id="comment-tools-55635" class="comment-tools"></div><div class="clear"></div><div id="comment-55635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

