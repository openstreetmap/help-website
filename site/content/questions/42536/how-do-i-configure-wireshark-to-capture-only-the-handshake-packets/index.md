+++
type = "question"
title = "How do I configure Wireshark to capture ONLY the handshake packets?"
description = '''Using TCP as a filter does not do that as it still shows TLS and few other protocols. I just want to show someone the 3-way handshake process packets without anything else '''
date = "2015-05-19T04:34:00Z"
lastmod = "2015-05-19T06:08:00Z"
weight = 42536
keywords = [ "handshake" ]
aliases = [ "/questions/42536" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I configure Wireshark to capture ONLY the handshake packets?](/questions/42536/how-do-i-configure-wireshark-to-capture-only-the-handshake-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42536-score" class="post-score" title="current number of votes">0</div><span id="post-42536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using TCP as a filter does not do that as it still shows TLS and few other protocols. I just want to show someone the 3-way handshake process packets without anything else</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-handshake" rel="tag" title="see questions tagged &#39;handshake&#39;">handshake</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '15, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/36ef17ff0551513c785b531644bf1f6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="matka&#39;s gravatar image" /><p><span>matka</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="matka has no accepted answers">0%</span></p></div></div><div id="comments-container-42536" class="comments-container"></div><div id="comment-tools-42536" class="comment-tools"></div><div class="clear"></div><div id="comment-42536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42537"></span>

<div id="answer-container-42537" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42537-score" class="post-score" title="current number of votes">0</div><span id="post-42537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Do you need a capture filter, or will a display filter work for you? It's hard (if not impossible) to capture the third packet of the three way handshake with a filter, because you need TCP session tracking to determine which ACK is the third packet of a handshake.</p><p>A display filter can do it with a little trick though. If you can live with display filtering, take a look at this blog post:</p><p><a href="https://blog.packet-foo.com/2015/03/advanced-display-filtering/">https://blog.packet-foo.com/2015/03/advanced-display-filtering/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '15, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-42537" class="comments-container"><span id="42538"></span><div id="comment-42538" class="comment"><div id="post-42538-score" class="comment-score">1</div><div class="comment-text"><p>See also: <a href="https://ask.wireshark.org/questions/15057/how-to-capture-tcp-3-way-handshake">https://ask.wireshark.org/questions/15057/how-to-capture-tcp-3-way-handshake</a></p></div><div id="comment-42538-info" class="comment-info"><span class="comment-age">(19 May '15, 06:08)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-42537" class="comment-tools"></div><div class="clear"></div><div id="comment-42537-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

