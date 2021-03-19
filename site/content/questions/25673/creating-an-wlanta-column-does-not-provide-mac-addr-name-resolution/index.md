+++
type = "question"
title = "Creating an wlan.ta column does not provide MAC addr. name resolution."
description = '''Hi guys, I have used wireshark to capture a batch of 802.11 frame from certain access point in my school. Then, I plan to analyze the down link frame from AP to Client. However, wireshark only provide the column titled as Source, which is actually the Mac address of wire part Router. But what I need...'''
date = "2013-10-06T01:41:00Z"
lastmod = "2013-10-06T18:00:00Z"
weight = 25673
keywords = [ "name-resolving", "wlan" ]
aliases = [ "/questions/25673" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Creating an wlan.ta column does not provide MAC addr. name resolution.](/questions/25673/creating-an-wlanta-column-does-not-provide-mac-addr-name-resolution)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25673-score" class="post-score" title="current number of votes">0</div><span id="post-25673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>I have used wireshark to capture a batch of 802.11 frame from certain access point in my school. Then, I plan to analyze the down link frame from AP to Client. However, wireshark only provide the column titled as <em>Source</em>, which is actually the Mac address of wire part Router. But what I need is the AP Mac address (Transmitter address ) in my case. Hence, I add a custom column named wlan.ta, but it does not provide Mac addr. name resolution (like Cisco_XX:XX:XX). How to enable it, coz is great convenient for my analysis work.</p><p>Any help will be greatly appreciated.</p><p>Best, Kay</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-name-resolving" rel="tag" title="see questions tagged &#39;name-resolving&#39;">name-resolving</span> <span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '13, 01:41</strong></p><img src="https://secure.gravatar.com/avatar/03bb2eab8c06cd2083eb59f7759fe27d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ocgcyj&#39;s gravatar image" /><p><span>ocgcyj</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ocgcyj has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Oct '13, 18:21</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-25673" class="comments-container"></div><div id="comment-tools-25673" class="comment-tools"></div><div class="clear"></div><div id="comment-25673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25686"></span>

<div id="answer-container-25686" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25686-score" class="post-score" title="current number of votes">0</div><span id="post-25686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Basically, upgrade to <a href="http://anonsvn.wireshark.org/viewvc?revision=51742&amp;view=revision">revision 51742</a> or later, and then add <code>wlan.ta_resolved</code> as your custom column.</p><p>See the answer I provided to <a href="http://ask.wireshark.org/questions/24314/possible-to-use-the-mac-info-in-the-wireshark-manuf-file-as-part-of-display-filter">this</a> question for more details. And <a href="http://ask.wireshark.org/questions/25197/mac-address-resolution-in-tshark">here</a> is another related question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '13, 18:00</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-25686" class="comments-container"></div><div id="comment-tools-25686" class="comment-tools"></div><div class="clear"></div><div id="comment-25686-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

