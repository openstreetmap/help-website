+++
type = "question"
title = "How do I un-ignore an ignored packet ?"
description = '''I &#x27;ignored&#x27; packet 915 as it is setting off wireshark&#x27;s dns.time calculation using right-click - Ignore (CTL-D)  How do I get the ignored packet back in to the display without closing and opening the trace file again? '''
date = "2016-07-29T12:43:00Z"
lastmod = "2016-07-30T22:45:00Z"
weight = 54446
keywords = [ "ignore", "unignore", "packet" ]
aliases = [ "/questions/54446" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do I un-ignore an ignored packet ?](/questions/54446/how-do-i-un-ignore-an-ignored-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54446-score" class="post-score" title="current number of votes">0</div><span id="post-54446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I 'ignored' packet 915 as it is setting off wireshark's dns.time calculation using right-click - Ignore (CTL-D)</p><p>How do I get the ignored packet back in to the display without closing and opening the trace file again?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_083.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ignore" rel="tag" title="see questions tagged &#39;ignore&#39;">ignore</span> <span class="post-tag tag-link-unignore" rel="tag" title="see questions tagged &#39;unignore&#39;">unignore</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '16, 12:43</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-54446" class="comments-container"></div><div id="comment-tools-54446" class="comment-tools"></div><div class="clear"></div><div id="comment-54446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54455"></span>

<div id="answer-container-54455" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54455-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54455-score" class="post-score" title="current number of votes">3</div><span id="post-54455-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mrEEde has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In your screen shot, you have applied a display filter of "dns.id==0x352c". When a packet is ignored, it is no longer dissected and effectively has no attributes, therefore it will not match your display filter (no matter what the display filter is). So when you ignore a packet with a display filter in place, it drops out of the display. The next displayed packet becomes the selected packet, so that's the packet that Ctrl-D now operates on.</p><p>You need to clear the display filter so that the ignored packet becomes visible again and can be selected. Then you can toggle the ignored status using Ctrl-D or right-click and then Ignore/Unignore Packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '16, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-54455" class="comments-container"><span id="54468"></span><div id="comment-54468" class="comment"><div id="post-54468-score" class="comment-score"></div><div class="comment-text"><p>That was it! When I remove the filter the ignored packet appears and can be unignored!<br />
Thanks</p></div><div id="comment-54468-info" class="comment-info"><span class="comment-age">(30 Jul '16, 22:40)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-54455" class="comment-tools"></div><div class="clear"></div><div id="comment-54455-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54447"></span>

<div id="answer-container-54447" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54447-score" class="post-score" title="current number of votes">0</div><span id="post-54447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use <code>CTRL-D</code> again; it acts as a toggle.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jul '16, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span> </br></p></div></div><div id="comments-container-54447" class="comments-container"><span id="54448"></span><div id="comment-54448" class="comment"><div id="post-54448-score" class="comment-score"></div><div class="comment-text"><p>unfortunately not, CTL_D ignores the next selected packet . I' using the latest code - currently 2.3.0-119</p></div><div id="comment-54448-info" class="comment-info"><span class="comment-age">(29 Jul '16, 12:50)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="54449"></span><div id="comment-54449" class="comment"><div id="post-54449-score" class="comment-score"></div><div class="comment-text"><p>Then that would appear to be a bug. I would suggest filing a <a href="https://bugs.wireshark.org/bugzilla/">bug report</a>.</p></div><div id="comment-54449-info" class="comment-info"><span class="comment-age">(29 Jul '16, 12:58)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="54450"></span><div id="comment-54450" class="comment"><div id="post-54450-score" class="comment-score"></div><div class="comment-text"><p>By the way, is it that only the <code>CTRL-D</code> doesn't unignore the packet or that the <code>Edit -&gt; Ignore/Unignore Packet</code> menu choice itself doesn't work either?</p></div><div id="comment-54450-info" class="comment-info"><span class="comment-age">(29 Jul '16, 13:26)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="54469"></span><div id="comment-54469" class="comment"><div id="post-54469-score" class="comment-score"></div><div class="comment-text"><p>As the ignored packet wasn't visible when the filter was applied the Edit menue path to un-ignore didn't work either</p></div><div id="comment-54469-info" class="comment-info"><span class="comment-age">(30 Jul '16, 22:45)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-54447" class="comment-tools"></div><div class="clear"></div><div id="comment-54447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

