+++
type = "question"
title = "Wireshark Tapping plugin"
description = '''Hey, I am trying to write a tap plugin, I am being quite successful, however, I am facing a problem. I cannot access on the tap all fields of a protocol, in some cases the &quot;abbrev&quot; returns &quot;Text Item&quot; and the value is &quot;Text&quot;.  Anyone can explain me why ?  Thanks in advance.'''
date = "2013-07-22T09:02:00Z"
lastmod = "2013-07-22T09:49:00Z"
weight = 23235
keywords = [ "tapping", "tap", "plugin" ]
aliases = [ "/questions/23235" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Tapping plugin](/questions/23235/wireshark-tapping-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23235-score" class="post-score" title="current number of votes">0</div><span id="post-23235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey,</p><p>I am trying to write a tap plugin, I am being quite successful, however, I am facing a problem. I cannot access on the tap all fields of a protocol, in some cases the "abbrev" returns "Text Item" and the value is "Text".</p><p>Anyone can explain me why ?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tapping" rel="tag" title="see questions tagged &#39;tapping&#39;">tapping</span> <span class="post-tag tag-link-tap" rel="tag" title="see questions tagged &#39;tap&#39;">tap</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '13, 09:02</strong></p><img src="https://secure.gravatar.com/avatar/59d7003122714cb35c62fa5eadd34177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rogerpt&#39;s gravatar image" /><p><span>rogerpt</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rogerpt has no accepted answers">0%</span></p></div></div><div id="comments-container-23235" class="comments-container"></div><div id="comment-tools-23235" class="comment-tools"></div><div class="clear"></div><div id="comment-23235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23239"></span>

<div id="answer-container-23239" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23239-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23239-score" class="post-score" title="current number of votes">4</div><span id="post-23239-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's because some fields in the protocol aren't named fields; they're being added with <code>proto_item_add_text()</code>, so they just show up as "Text".</p><p>If you or somebody in your organization wrote the dissector, change it to use named fields rather than <code>proto_item_add_text()</code> for the fields in question.</p><p>If it's part of the standard Wireshark release, file a bug on it at <a href="http://bugs.wireshark.org">the Wireshark bugzilla</a> saying it should use named fields.</p><p>If it's somebody else's plugin, ask them to use named fields.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '13, 09:49</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23239" class="comments-container"></div><div id="comment-tools-23239" class="comment-tools"></div><div class="clear"></div><div id="comment-23239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

