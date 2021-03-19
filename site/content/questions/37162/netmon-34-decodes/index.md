+++
type = "question"
title = "netmon 3.4 decodes"
description = '''I captured some ICMP packets with Netmon 3.4 from my Wifi Adapter and while I can decode them correctly in Netmon, Wireshark only shows the 802.11 header in the return frames.'''
date = "2014-10-19T14:04:00Z"
lastmod = "2014-10-19T15:15:00Z"
weight = 37162
keywords = [ "3.4", "microsoft", "netmon" ]
aliases = [ "/questions/37162" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [netmon 3.4 decodes](/questions/37162/netmon-34-decodes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37162-score" class="post-score" title="current number of votes">0</div><span id="post-37162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I captured some ICMP packets with Netmon 3.4 from my Wifi Adapter and while I can decode them correctly in Netmon, Wireshark only shows the 802.11 header in the return frames.<img src="https://osqa-ask.wireshark.org/upfiles/Capture_Mrqk3ax.JPG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-3.4" rel="tag" title="see questions tagged &#39;3.4&#39;">3.4</span> <span class="post-tag tag-link-microsoft" rel="tag" title="see questions tagged &#39;microsoft&#39;">microsoft</span> <span class="post-tag tag-link-netmon" rel="tag" title="see questions tagged &#39;netmon&#39;">netmon</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '14, 14:04</strong></p><img src="https://secure.gravatar.com/avatar/dbc4d8cb6be85bd586ca4bf211e1337c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thetechfirm&#39;s gravatar image" /><p><span>thetechfirm</span><br />
<span class="score" title="64 reputation points">64</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thetechfirm has no accepted answers">0%</span></p></img></div></div><div id="comments-container-37162" class="comments-container"><span id="37164"></span><div id="comment-37164" class="comment"><div id="post-37164-score" class="comment-score"></div><div class="comment-text"><p>Update; I just did another test from the Ethernet card with no issue.</p></div><div id="comment-37164-info" class="comment-info"><span class="comment-age">(19 Oct '14, 14:08)</span> <span class="comment-user userinfo">thetechfirm</span></div></div></div><div id="comment-tools-37162" class="comment-tools"></div><div class="clear"></div><div id="comment-37162-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37163"></span>

<div id="answer-container-37163" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37163-score" class="post-score" title="current number of votes">1</div><span id="post-37163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please file a bug on this at <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a> and attach the capture file, so that we can get enough data to figure out what the problem is and try to fix it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '14, 14:07</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-37163" class="comments-container"><span id="37165"></span><div id="comment-37165" class="comment"><div id="post-37165-score" class="comment-score"></div><div class="comment-text"><p>done - logged as Bug 10593</p></div><div id="comment-37165-info" class="comment-info"><span class="comment-age">(19 Oct '14, 15:15)</span> <span class="comment-user userinfo">thetechfirm</span></div></div></div><div id="comment-tools-37163" class="comment-tools"></div><div class="clear"></div><div id="comment-37163-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

