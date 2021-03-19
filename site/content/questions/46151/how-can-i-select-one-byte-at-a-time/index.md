+++
type = "question"
title = "How can I select one byte at a time?"
description = '''I&#x27;m looking at a capture of a HTTP packet. If I let my mouse cursor hover the hex dump in the packet bytes panel, entire sections of bytes are selected or highlighted at the same time. For example, if I put my mouse cursor over the section belonging to a single HTTP header, the entire header is high...'''
date = "2015-09-25T03:54:00Z"
lastmod = "2015-09-25T04:05:00Z"
weight = 46151
keywords = [ "gui", "bytes" ]
aliases = [ "/questions/46151" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I select one byte at a time?](/questions/46151/how-can-i-select-one-byte-at-a-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46151-score" class="post-score" title="current number of votes">0</div><span id="post-46151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking at a capture of a HTTP packet. If I let my mouse cursor hover the hex dump in the packet bytes panel, entire sections of bytes are selected or highlighted at the same time. For example, if I put my mouse cursor over the section belonging to a single HTTP header, the entire header is highlighted.</p><p>How do I turn this behaviour off? I would like to only highlight a single byte at a time, as this is much more useful for debugging non-ASCII encodings.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gui" rel="tag" title="see questions tagged &#39;gui&#39;">gui</span> <span class="post-tag tag-link-bytes" rel="tag" title="see questions tagged &#39;bytes&#39;">bytes</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '15, 03:54</strong></p><img src="https://secure.gravatar.com/avatar/936383b387d6cc6d51279e429e5d7cd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Flimm&#39;s gravatar image" /><p><span>Flimm</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Flimm has no accepted answers">0%</span></p></div></div><div id="comments-container-46151" class="comments-container"></div><div id="comment-tools-46151" class="comment-tools"></div><div class="clear"></div><div id="comment-46151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46152"></span>

<div id="answer-container-46152" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46152-score" class="post-score" title="current number of votes">1</div><span id="post-46152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Flimm has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think that's possible at the moment. You might want to add a feature request by filing a "bug" at <a href="http://bugs.wireshark.org">BugZilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '15, 03:58</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-46152" class="comments-container"><span id="46153"></span><div id="comment-46153" class="comment"><div id="post-46153-score" class="comment-score"></div><div class="comment-text"><p>I've created a bug report: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11547">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11547</a></p></div><div id="comment-46153-info" class="comment-info"><span class="comment-age">(25 Sep '15, 04:05)</span> <span class="comment-user userinfo">Flimm</span></div></div></div><div id="comment-tools-46152" class="comment-tools"></div><div class="clear"></div><div id="comment-46152-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

