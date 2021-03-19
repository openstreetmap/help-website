+++
type = "question"
title = "Best Practice?  Updating Wireshark version on Mac OS X"
description = '''I would like to update to 1.8.7 from 1.8.6. I assume the simplest method is to simply download the DMG file, but not sure whether to install on top of the current version or uninstall the older version and then install. Does anyone have a recommendation?'''
date = "2013-05-26T21:26:00Z"
lastmod = "2013-05-27T16:53:00Z"
weight = 21484
keywords = [ "mac", "upgrade" ]
aliases = [ "/questions/21484" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Best Practice? Updating Wireshark version on Mac OS X](/questions/21484/best-practice-updating-wireshark-version-on-mac-os-x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21484-score" class="post-score" title="current number of votes">0</div><span id="post-21484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to update to 1.8.7 from 1.8.6. I assume the simplest method is to simply download the DMG file, but not sure whether to install on top of the current version or uninstall the older version and then install. Does anyone have a recommendation?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-upgrade" rel="tag" title="see questions tagged &#39;upgrade&#39;">upgrade</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '13, 21:26</strong></p><img src="https://secure.gravatar.com/avatar/8563ff64789581b3c26cade38303f1e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Glen2013&#39;s gravatar image" /><p><span>Glen2013</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Glen2013 has no accepted answers">0%</span></p></div></div><div id="comments-container-21484" class="comments-container"></div><div id="comment-tools-21484" class="comment-tools"></div><div class="clear"></div><div id="comment-21484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21503"></span>

<div id="answer-container-21503" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21503-score" class="post-score" title="current number of votes">1</div><span id="post-21503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you're going from a 1.8.x release to a later 1.8.x release, installing on top of the current version should work.</p><p>If you're going from a pre-1.8.x release to a 1.8.x release, installing on top of the current version won't work, due to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7401">bug 7401</a>, unless you're going to 1.8.5 or later.</p><p>Installing future releases (1.10.0 and later) should also work without an uninstall (if not, that's a bug).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '13, 16:53</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-21503" class="comments-container"><span id="21502"></span><div id="comment-21502" class="comment"><div id="post-21502-score" class="comment-score"></div><div class="comment-text"><p>I still don't know the best practice, but (imho) doing a full uninstall and installing the new version may result in a cleaner install. In theory, simply installing the new version over top of the current version ought to be neat &amp; tidy too, I just don't know. Installing and staying current using MacPorts would alleviate this concern although there would be a lag waiting for the port process (not a criticism of MacPorts).</p><p>The original DMG file I used had a "Read me first.rtf" file describing how to do a full uninstall for Mac OS X.</p><p>Perhaps this will provide some insight into the best practice of staying current with the application.</p></div><div id="comment-21502-info" class="comment-info"><span class="comment-age">(27 May '13, 16:42)</span> <span class="comment-user userinfo">Glen2013</span></div></div></div><div id="comment-tools-21503" class="comment-tools"></div><div class="clear"></div><div id="comment-21503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

