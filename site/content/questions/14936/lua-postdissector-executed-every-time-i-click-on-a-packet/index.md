+++
type = "question"
title = "Lua postdissector executed every time I click on a packet"
description = '''Hi, I wrote a simple postdissector in lua but it seems to be executed twice when wireshark is opened and then every time for a packet I click on, or move to another packet with arrow keys. I&#x27;ve also noticed that if I restrict the execution by tracking how many times it was run for a given packet the...'''
date = "2012-10-11T09:28:00Z"
lastmod = "2012-10-11T10:39:00Z"
weight = 14936
keywords = [ "lua", "postdissector" ]
aliases = [ "/questions/14936" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Lua postdissector executed every time I click on a packet](/questions/14936/lua-postdissector-executed-every-time-i-click-on-a-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14936-score" class="post-score" title="current number of votes">0</div><span id="post-14936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I wrote a simple postdissector in lua but it seems to be executed twice when wireshark is opened and then every time for a packet I click on, or move to another packet with arrow keys.</p><p>I've also noticed that if I restrict the execution by tracking how many times it was run for a given packet the new tree item will be removed. As if the display with new tree item was constructed on a click or move.</p><p>Is that behavior expected ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-postdissector" rel="tag" title="see questions tagged &#39;postdissector&#39;">postdissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '12, 09:28</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p><span>izopizo</span><br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-14936" class="comments-container"></div><div id="comment-tools-14936" class="comment-tools"></div><div class="clear"></div><div id="comment-14936-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14938"></span>

<div id="answer-container-14938" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14938-score" class="post-score" title="current number of votes">2</div><span id="post-14938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="izopizo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, this is expected behavior. The protocol tree is rebuilt each time you click on the item so that Wireshark does not have to keep (all!) the protocol trees in memory. IOW, the only protocol tree Wireshark keeps in memory is that of the currently-displayed frame. To do that, it must rebuild the tree each time you select the frame.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '12, 10:39</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-14938" class="comments-container"></div><div id="comment-tools-14938" class="comment-tools"></div><div class="clear"></div><div id="comment-14938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

