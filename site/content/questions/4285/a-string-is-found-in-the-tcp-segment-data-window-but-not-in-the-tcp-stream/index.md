+++
type = "question"
title = "A string is found in the tcp segment data window but not in the tcp stream"
description = '''Hi,  I am searching for a specific xml data string and the pointer finds the specific packet number. Then I right click &quot;follow tcp stream&quot; and don&#x27;t find it (I am not talking about while it is written in &quot;white&quot;). Then I look at tcp data segment window below, and find it!  My question is why parts ...'''
date = "2011-05-30T03:13:00Z"
lastmod = "2013-05-01T11:25:00Z"
weight = 4285
keywords = [ "follow", "stream", "tcp" ]
aliases = [ "/questions/4285" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [A string is found in the tcp segment data window but not in the tcp stream](/questions/4285/a-string-is-found-in-the-tcp-segment-data-window-but-not-in-the-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4285-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4285-score" class="post-score" title="current number of votes">0</div><span id="post-4285-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am searching for a specific xml data string and the pointer finds the specific packet number. Then I right click "follow tcp stream" and don't find it (I am not talking about while it is written in "white"). Then I look at tcp data segment window below, and find it! My question is why parts of the xml are written in the follow tcp stream window and some are not (and are only available at the tcp data segment window)? BR, Yuval Sivan.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-follow" rel="tag" title="see questions tagged &#39;follow&#39;">follow</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '11, 03:13</strong></p><img src="https://secure.gravatar.com/avatar/6950c3ba92bb665a82b6cb08553e45cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuvalsivan&#39;s gravatar image" /><p><span>yuvalsivan</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuvalsivan has no accepted answers">0%</span></p></div></div><div id="comments-container-4285" class="comments-container"></div><div id="comment-tools-4285" class="comment-tools"></div><div class="clear"></div><div id="comment-4285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4327"></span>

<div id="answer-container-4327" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4327-score" class="post-score" title="current number of votes">1</div><span id="post-4327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Could it be that the XML object was compressed when it was sent over HTTP? The HTTP dissector is able to decompress the object, while "Follow TCP Stream" does just that, it shows you the raw data sent over TCP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '11, 23:23</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4327" class="comments-container"></div><div id="comment-tools-4327" class="comment-tools"></div><div class="clear"></div><div id="comment-4327-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20879"></span>

<div id="answer-container-20879" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20879-score" class="post-score" title="current number of votes">0</div><span id="post-20879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sadly, wireshark's capabilities are quite limited when working with tcp streams, especially those that are compressed. You can decompress the stream using tcpflow, however.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '13, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/a355f7a3b3404b578af95e47cd274cc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bhh&#39;s gravatar image" /><p><span>bhh</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bhh has no accepted answers">0%</span></p></div></div><div id="comments-container-20879" class="comments-container"></div><div id="comment-tools-20879" class="comment-tools"></div><div class="clear"></div><div id="comment-20879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

