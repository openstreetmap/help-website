+++
type = "question"
title = "Multiple monitor display issue"
description = '''I have 2 monitors - a 30 inch and a 20 inch. The 20 inch is positioned &quot;above and to the right&quot; of my 30 inch. I mean that it is physically placed above and to the right of my 30 inch. In the XP display properties the 20 inch monitor is placed in the same manner so that with a diagonal mouse move I ...'''
date = "2011-07-27T06:39:00Z"
lastmod = "2011-07-27T08:09:00Z"
weight = 5310
keywords = [ "multiple", "monitor" ]
aliases = [ "/questions/5310" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple monitor display issue](/questions/5310/multiple-monitor-display-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5310-score" class="post-score" title="current number of votes">0</div><span id="post-5310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have 2 monitors - a 30 inch and a 20 inch. The 20 inch is positioned "above and to the right" of my 30 inch. I mean that it is physically placed above and to the right of my 30 inch. In the XP display properties the 20 inch monitor is placed in the same manner so that with a diagonal mouse move I can go from the upper right corner of my 30 inch to the lower left corner of my 20 inch.<br />
</p><p>This arrangement causes Wireshark to display only the bottom half of itself on my 30 inch when not maximized. If I select the taskbar icon and select "move", attempt to move wireshark where I can see it, nothing will happen. When I again click on the taskbar icon, it will crash with a generic runtime error.</p><p>If I select "maximize" it consumes the entire 30 inch screen as I would expect.</p><p>Any ideas? I have 2 setups arranged like this and they both do this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '11, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/3a6a922ca513f2cc2384f30238412b20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sniffler&#39;s gravatar image" /><p><span>sniffler</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sniffler has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-5310" class="comments-container"><span id="5315"></span><div id="comment-5315" class="comment"><div id="post-5315-score" class="comment-score"></div><div class="comment-text"><p>Please file a bug at bugs.wireshark.org and describe the exact sequence which causes a crash.</p><p>This might be a Wireshark issue or it might be an issue with the underlying GTK library.</p><p>(For a previous "multiple monitor" issue see https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=553</p></div><div id="comment-5315-info" class="comment-info"><span class="comment-age">(27 Jul '11, 07:54)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-5310" class="comment-tools"></div><div class="clear"></div><div id="comment-5310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5311"></span>

<div id="answer-container-5311" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5311-score" class="post-score" title="current number of votes">0</div><span id="post-5311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While I can't speak to the crash, you can move the Wireshark window (like any other window) by right-clicking the taskbar item, selecting <strong>move</strong>, and then using the arrow keys on your keybaord to move the window until its title bar would be in view --this will allow you to move the window with the mouse.</p><p>In your case (the window is positioned above the visible area), you would select move and press the down arrow until moving the mouse moves the window to where you like.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '11, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-5311" class="comments-container"><span id="5317"></span><div id="comment-5317" class="comment"><div id="post-5317-score" class="comment-score"></div><div class="comment-text"><p>You can also move the window in bigger jumps and between monitors using the "Windows" key and the cursor keys. I'm not certain if this works in XP though.</p></div><div id="comment-5317-info" class="comment-info"><span class="comment-age">(27 Jul '11, 08:09)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-5311" class="comment-tools"></div><div class="clear"></div><div id="comment-5311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

