+++
type = "question"
title = "Why in v 2.0 did you have removed &quot;dns resolve&quot; on the right click in the single IP address entry?"
description = '''In version 1.12 and earlier I can right click on layer 3 IP address in Packet Details and click on &quot;resolve dns address&quot;, but this fictionality is missing on version 2.0. Why?'''
date = "2016-04-17T12:14:00Z"
lastmod = "2017-07-24T10:59:00Z"
weight = 51736
keywords = [ "wireshark-2.0", "right-click", "dns" ]
aliases = [ "/questions/51736" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why in v 2.0 did you have removed "dns resolve" on the right click in the single IP address entry?](/questions/51736/why-in-v-20-did-you-have-removed-dns-resolve-on-the-right-click-in-the-single-ip-address-entry)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51736-score" class="post-score" title="current number of votes">0</div><span id="post-51736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In version 1.12 and earlier I can right click on layer 3 IP address in Packet Details and click on "resolve dns address", but this fictionality is missing on version 2.0. Why?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark-2.0" rel="tag" title="see questions tagged &#39;wireshark-2.0&#39;">wireshark-2.0</span> <span class="post-tag tag-link-right-click" rel="tag" title="see questions tagged &#39;right-click&#39;">right-click</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '16, 12:14</strong></p><img src="https://secure.gravatar.com/avatar/00e8edc0dc2cb05ff49205edd695a958?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shadowsheep&#39;s gravatar image" /><p><span>shadowsheep</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shadowsheep has no accepted answers">0%</span></p></div></div><div id="comments-container-51736" class="comments-container"></div><div id="comment-tools-51736" class="comment-tools"></div><div class="clear"></div><div id="comment-51736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51740"></span>

<div id="answer-container-51740" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51740-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51740-score" class="post-score" title="current number of votes">2</div><span id="post-51740-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="shadowsheep has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It probably got lost in the conversion to Qt. Please file a bug for this on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a> so that its absence is recorded.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '16, 20:12</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Apr '16, 20:13</strong> </span></p></div></div><div id="comments-container-51740" class="comments-container"><span id="62927"></span><div id="comment-62927" class="comment"><div id="post-62927-score" class="comment-score"></div><div class="comment-text"><p>I've been missing this feature for a while, just found it is still present in the GTK version of 2.4 and likely the earlier 2.x versions.</p></div><div id="comment-62927-info" class="comment-info"><span class="comment-age">(20 Jul '17, 06:13)</span> <span class="comment-user userinfo">naskop</span></div></div><span id="62995"></span><div id="comment-62995" class="comment"><div id="post-62995-score" class="comment-score"></div><div class="comment-text"><p>Then <em>please file a bug</em>. We're <em>far</em> more likely to address a bug, or missing feature, if it's in the bug database.</p><p>And then put a link to that bug, giving the bug number as the link text, in a comment here.</p></div><div id="comment-62995-info" class="comment-info"><span class="comment-age">(21 Jul '17, 21:55)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="63056"></span><div id="comment-63056" class="comment"><div id="post-63056-score" class="comment-score"></div><div class="comment-text"><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12346">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12346</a></p></div><div id="comment-63056-info" class="comment-info"><span class="comment-age">(24 Jul '17, 10:59)</span> <span class="comment-user userinfo">naskop</span></div></div></div><div id="comment-tools-51740" class="comment-tools"></div><div class="clear"></div><div id="comment-51740-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

