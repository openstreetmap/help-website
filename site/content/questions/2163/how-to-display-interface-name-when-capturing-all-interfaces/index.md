+++
type = "question"
title = "How to display interface name when capturing all interfaces?"
description = '''I am performing capture on all devices, and end with messed output. It would be helpfull to have additional column with interface name. Is there a way to add such column to packet list view?'''
date = "2011-02-04T23:56:00Z"
lastmod = "2011-02-05T16:26:00Z"
weight = 2163
keywords = [ "device", "capture", "interfaces", "devices" ]
aliases = [ "/questions/2163" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to display interface name when capturing all interfaces?](/questions/2163/how-to-display-interface-name-when-capturing-all-interfaces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2163-score" class="post-score" title="current number of votes">0</div><span id="post-2163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am performing capture on all devices, and end with messed output. It would be helpfull to have additional column with interface name.</p><p>Is there a way to add such column to packet list view?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-device" rel="tag" title="see questions tagged &#39;device&#39;">device</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-interfaces" rel="tag" title="see questions tagged &#39;interfaces&#39;">interfaces</span> <span class="post-tag tag-link-devices" rel="tag" title="see questions tagged &#39;devices&#39;">devices</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '11, 23:56</strong></p><img src="https://secure.gravatar.com/avatar/1509286f3954a13d56a9dffcea12511a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Witek&#39;s gravatar image" /><p><span>Witek</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Witek has no accepted answers">0%</span></p></div></div><div id="comments-container-2163" class="comments-container"></div><div id="comment-tools-2163" class="comment-tools"></div><div class="clear"></div><div id="comment-2163-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="2164"></span>

<div id="answer-container-2164" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2164-score" class="post-score" title="current number of votes">1</div><span id="post-2164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Witek has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Linux 'all' interface doesn't provide that information in its cooked capture, therefore it can't be presented.</p><p>A simultaneous capture into pcap-ng would allow for this, but that hasn't been developed, yet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '11, 01:07</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2164" class="comments-container"></div><div id="comment-tools-2164" class="comment-tools"></div><div class="clear"></div><div id="comment-2164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2165"></span>

<div id="answer-container-2165" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2165-score" class="post-score" title="current number of votes">0</div><span id="post-2165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not even minor number of interfaces? Shame.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '11, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/1509286f3954a13d56a9dffcea12511a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Witek&#39;s gravatar image" /><p><span>Witek</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Witek has no accepted answers">0%</span></p></div></div><div id="comments-container-2165" class="comments-container"></div><div id="comment-tools-2165" class="comment-tools"></div><div class="clear"></div><div id="comment-2165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2171"></span>

<div id="answer-container-2171" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2171-score" class="post-score" title="current number of votes">0</div><span id="post-2171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you have multiple interfaces and want to keep traffic separated, just launch multiple instances of dumpcap and capture from each interface to a separate file. You can merge later if you need to using mergecap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '11, 16:26</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-2171" class="comments-container"></div><div id="comment-tools-2171" class="comment-tools"></div><div class="clear"></div><div id="comment-2171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

