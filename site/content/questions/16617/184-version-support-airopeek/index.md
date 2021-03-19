+++
type = "question"
title = "1.8.4 version support airopeek ?"
description = '''I was using wireshark 1.6.12 and decoding AIROPEEK package ok. After upgrading to 1.8.4, that option is gone from &quot;Decode As...&quot; option. Am I missing something here?'''
date = "2012-12-05T15:09:00Z"
lastmod = "2013-01-05T14:28:00Z"
weight = 16617
keywords = [ "airopeek" ]
aliases = [ "/questions/16617" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [1.8.4 version support airopeek ?](/questions/16617/184-version-support-airopeek)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16617-score" class="post-score" title="current number of votes">0</div><span id="post-16617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was using wireshark 1.6.12 and decoding AIROPEEK package ok. After upgrading to 1.8.4, that option is gone from "Decode As..." option. Am I missing something here?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-airopeek" rel="tag" title="see questions tagged &#39;airopeek&#39;">airopeek</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '12, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/81be229523eee98c8df436444218a42e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dbdiep&#39;s gravatar image" /><p><span>dbdiep</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dbdiep has no accepted answers">0%</span></p></div></div><div id="comments-container-16617" class="comments-container"><span id="17447"></span><div id="comment-17447" class="comment"><div id="post-17447-score" class="comment-score"></div><div class="comment-text"><p>I have the same question... Can anyone please answer? Thanks!</p></div><div id="comment-17447-info" class="comment-info"><span class="comment-age">(04 Jan '13, 10:13)</span> <span class="comment-user userinfo">difan</span></div></div><span id="17455"></span><div id="comment-17455" class="comment"><div id="post-17455-score" class="comment-score"></div><div class="comment-text"><p>I don't have an "airopeek" capture file at hand to test with. Could you post one on <a href="http://www.cloudshark.org">www.cloudshark.org</a> and paste the link to the file here to analyse?</p></div><div id="comment-17455-info" class="comment-info"><span class="comment-age">(04 Jan '13, 12:25)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-16617" class="comment-tools"></div><div class="clear"></div><div id="comment-16617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17468"></span>

<div id="answer-container-17468" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17468-score" class="post-score" title="current number of votes">2</div><span id="post-17468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Airopeek was ambiguous. There's the capture file format and UDP transported traffic. Therefore this last one was renamed PEEKREMOTE. See <a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=42377">this revision</a> of the change.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '13, 15:08</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-17468" class="comments-container"><span id="17477"></span><div id="comment-17477" class="comment"><div id="post-17477-score" class="comment-score"></div><div class="comment-text"><p>And the capture file format isn't "AiroPeek" - WildPackets' own terms for their two capture file formats, both of which have been used by versions of EtherPeek, TokenPeek, and AiroPeek, are "Peek classic" and "Peek tagged". The UDP-transported traffic, as the revision notes, is not unique to AiroPeek, so the protocol was renamed.</p></div><div id="comment-17477-info" class="comment-info"><span class="comment-age">(05 Jan '13, 14:28)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-17468" class="comment-tools"></div><div class="clear"></div><div id="comment-17468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

