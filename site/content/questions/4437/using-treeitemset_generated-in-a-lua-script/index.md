+++
type = "question"
title = "using treeitem:set_generated() in a LUA script"
description = '''Hello, I have a basic lua dissector where data from the packet is being displayed properly in a tree view. I am trying to display some calculated values based on the data in the protocol; however, none of the data is being displayed as documented. Question: Has anybody successfully used the treeitem...'''
date = "2011-06-07T09:30:00Z"
lastmod = "2011-06-07T09:42:00Z"
weight = 4437
keywords = [ "lua" ]
aliases = [ "/questions/4437" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [using treeitem:set\_generated() in a LUA script](/questions/4437/using-treeitemset_generated-in-a-lua-script)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4437-score" class="post-score" title="current number of votes">0</div><span id="post-4437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a basic lua dissector where data from the packet is being displayed properly in a tree view. I am trying to display some calculated values based on the data in the protocol; however, none of the data is being displayed as documented.</p><p>Question: Has anybody successfully used the treeitem:set_generated() function as documented in the lua API?</p><p>Here's the basic construct that I am using:</p><p>local ABCD = Proto("ABCD") local ABCDFields = ABCD.fields</p><p>ABCDFields.f1 = ProtoField.uint32("ABCD.f1") -- data extracted from packet ABCDFields.f2 = ProtoField.uint32("ABCD.f2") -- data extracted from packet ABCDFields.f3 = ProtoField.double("ABCD.f3") -- calculated based on f1 and f2</p><p>function ABCD.dissector(buffer, pinfo, tree) local maxLen = buffer:len() local start = maxLen - 15 local f1 = tonumber('0x'..buffer:range(start, 4), 16) local f2 = tonumber('0x'..buffer:range(start+4, 4), 16) local f3 = &lt;do some="" math="" on="" f1="" and="" f2=""&gt;</p><p>local subtree = tree:add(ABCD, buffer()) subtree:add(ABCDFields.f1, f1) -- displays properly subtree:add(ABCDFields.f2, f2) -- displays properly subtree:add(ABCDFields.f3, f3) -- displays f3 subtree:set_generated() -- if this is added, then I would expect f3 to be displayed in brackets; however, this has no impact</p><p>end</p><p>...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '11, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/c68e030fe62af75dea74437883b4f6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrai&#39;s gravatar image" /><p><span>mrai</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrai has no accepted answers">0%</span></p></div></div><div id="comments-container-4437" class="comments-container"></div><div id="comment-tools-4437" class="comment-tools"></div><div class="clear"></div><div id="comment-4437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4438"></span>

<div id="answer-container-4438" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4438-score" class="post-score" title="current number of votes">1</div><span id="post-4438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is you're calling <code>set_generated()</code> on the root tree node when you actually want to call it on a child node (i.e., the tree node for <code>f3</code>).</p><p>Change the last two lines from:</p><pre><code>subtree:add(ABCDFields.f3, f3) -- displays f3
subtree:set_generated() -- if this is added, then I would expect f3 to be displayed in brackets; however, this has no impact</code></pre><p>to:</p><pre><code>subtree:add(ABCDFields.f3, f3):set_generated() -- displays f3 (generated)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '11, 09:42</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p><span>bstn</span><br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div></div><div id="comments-container-4438" class="comments-container"></div><div id="comment-tools-4438" class="comment-tools"></div><div class="clear"></div><div id="comment-4438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

