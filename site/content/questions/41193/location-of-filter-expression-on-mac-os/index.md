+++
type = "question"
title = "Location of Filter expression on Mac OS"
description = '''Where is the filter expression file located? The reason i ask is when I perform an uninstall my original filter expression remain.'''
date = "2015-04-04T15:30:00Z"
lastmod = "2015-04-06T10:34:00Z"
weight = 41193
keywords = [ "filter", "export" ]
aliases = [ "/questions/41193" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Location of Filter expression on Mac OS](/questions/41193/location-of-filter-expression-on-mac-os)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41193-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41193-score" class="post-score" title="current number of votes">0</div><span id="post-41193-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Where is the filter expression file located? The reason i ask is when I perform an uninstall my original filter expression remain.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '15, 15:30</strong></p><img src="https://secure.gravatar.com/avatar/a26768b463fa78c6915bbea890fca049?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mewireshark&#39;s gravatar image" /><p><span>mewireshark</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mewireshark has no accepted answers">0%</span></p></div></div><div id="comments-container-41193" class="comments-container"><span id="41194"></span><div id="comment-41194" class="comment"><div id="post-41194-score" class="comment-score"></div><div class="comment-text"><p>Which filter expressions? Color filters? Saved display filters?</p></div><div id="comment-41194-info" class="comment-info"><span class="comment-age">(04 Apr '15, 19:17)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="41203"></span><div id="comment-41203" class="comment"><div id="post-41203-score" class="comment-score"></div><div class="comment-text"><p>The filter expression found under edit-filter-preference.Also found on the first button right of the save button.</p></div><div id="comment-41203-info" class="comment-info"><span class="comment-age">(06 Apr '15, 02:21)</span> <span class="comment-user userinfo">mewireshark</span></div></div><span id="41207"></span><div id="comment-41207" class="comment"><div id="post-41207-score" class="comment-score"></div><div class="comment-text"><p>sounds like a duplicate to this question: <a href="https://ask.wireshark.org/questions/41038/mac-os-filter-removal">https://ask.wireshark.org/questions/41038/mac-os-filter-removal</a></p></div><div id="comment-41207-info" class="comment-info"><span class="comment-age">(06 Apr '15, 03:05)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-41193" class="comment-tools"></div><div class="clear"></div><div id="comment-41193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41227"></span>

<div id="answer-container-41227" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41227-score" class="post-score" title="current number of votes">0</div><span id="post-41227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>under edit-filter-preference</p></blockquote><p>Presumably you mean "under Edit -&gt; Preferences when you click on Filter Expressions".</p><p>Those are stored in ~/.wireshark/preferences; look for the heading</p><pre><code>####### Filter Expressions ########</code></pre><p>and the <code>gui.filter_expressions</code> items under it.</p><p>That's a personal file, not a system file, so it should not be surprising that uninstalling doesn't remove it. Uninstalling applications of <em>any</em> sort, not just Wireshark, tends not to uninstall personal configuration files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '15, 10:34</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-41227" class="comments-container"></div><div id="comment-tools-41227" class="comment-tools"></div><div class="clear"></div><div id="comment-41227-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

