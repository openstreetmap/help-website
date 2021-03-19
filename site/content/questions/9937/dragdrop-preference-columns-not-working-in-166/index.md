+++
type = "question"
title = "Drag/drop preference columns not working in 1.6.6"
description = '''Neither 1.6.5 nor 1.6.6 allows one to drag and drop columns in Preferences. This is running on Windows 7 64-bit. I create a new column which ends up at the end of the list . I click and drag it toward the top, but when I release the mouse button the new column floats back to the bottom of the list.'''
date = "2012-04-04T10:47:00Z"
lastmod = "2012-04-04T10:58:00Z"
weight = 9937
keywords = [ "drag", "drop", "preferences" ]
aliases = [ "/questions/9937" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Drag/drop preference columns not working in 1.6.6](/questions/9937/dragdrop-preference-columns-not-working-in-166)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9937-score" class="post-score" title="current number of votes">0</div><span id="post-9937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Neither 1.6.5 nor 1.6.6 allows one to drag and drop columns in Preferences. This is running on Windows 7 64-bit. I create a new column which ends up at the end of the list . I click and drag it toward the top, but when I release the mouse button the new column floats back to the bottom of the list.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-drag" rel="tag" title="see questions tagged &#39;drag&#39;">drag</span> <span class="post-tag tag-link-drop" rel="tag" title="see questions tagged &#39;drop&#39;">drop</span> <span class="post-tag tag-link-preferences" rel="tag" title="see questions tagged &#39;preferences&#39;">preferences</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '12, 10:47</strong></p><img src="https://secure.gravatar.com/avatar/47fd868f53437d9e76787bec0837085c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jimk01&#39;s gravatar image" /><p><span>Jimk01</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jimk01 has no accepted answers">0%</span></p></div></div><div id="comments-container-9937" class="comments-container"></div><div id="comment-tools-9937" class="comment-tools"></div><div class="clear"></div><div id="comment-9937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9940"></span>

<div id="answer-container-9940" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9940-score" class="post-score" title="current number of votes">1</div><span id="post-9940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is a known bug. See the <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6077">Wireshark Bugzilla #6077</a> for details. According to the bug comments, this has been fixed as of Wireshark 1.6.6 in 32-bit Windows, but is not yet fixed in 64-bit Windows. The problem is not actually with Wireshark, it's with the GTK toolkit that Wireshark uses, so the Wireshark developers have to wait for the GTK developers to actually fix the problem.</p><p>In the meantime, you can rearrange columns from the Packet Summary pane. Just remember to go back to Preferences and click Save or your changes will be lost when you shut down Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '12, 10:58</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-9940" class="comments-container"></div><div id="comment-tools-9940" class="comment-tools"></div><div class="clear"></div><div id="comment-9940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9938"></span>

<div id="answer-container-9938" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9938-score" class="post-score" title="current number of votes">0</div><span id="post-9938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is a known GTK-related bug being tracked in the Wireshark bug database as <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6077">bug 6077</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '12, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-9938" class="comments-container"><span id="9939"></span><div id="comment-9939" class="comment"><div id="post-9939-score" class="comment-score"></div><div class="comment-text"><p>thank you very much!</p></div><div id="comment-9939-info" class="comment-info"><span class="comment-age">(04 Apr '12, 10:55)</span> <span class="comment-user userinfo">Jimk01</span></div></div></div><div id="comment-tools-9938" class="comment-tools"></div><div class="clear"></div><div id="comment-9938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

