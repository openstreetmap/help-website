+++
type = "question"
title = "Raw Hex format of an http packet."
description = '''Can someone tell me how to look at a packet in raw form. I want to see the preamble and every octet after in binary or hex form. I want to look at the packet and find the destination ip adress,the payload length, the payload, etc.  For example I will go to google.com in my browser and then look at t...'''
date = "2012-08-14T13:41:00Z"
lastmod = "2012-08-14T14:53:00Z"
weight = 13635
keywords = [ "raw", "http", "packet", "hex" ]
aliases = [ "/questions/13635" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Raw Hex format of an http packet.](/questions/13635/raw-hex-format-of-an-http-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13635-score" class="post-score" title="current number of votes">0</div><span id="post-13635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can someone tell me how to look at a packet in raw form. I want to see the preamble and every octet after in binary or hex form. I want to look at the packet and find the destination ip adress,the payload length, the payload, etc.</p><p>For example I will go to <a href="http://google.com">google.com</a> in my browser and then look at the raw response.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-raw" rel="tag" title="see questions tagged &#39;raw&#39;">raw</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-hex" rel="tag" title="see questions tagged &#39;hex&#39;">hex</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '12, 13:41</strong></p><img src="https://secure.gravatar.com/avatar/00a2c27681c0b4fbe102c61e7f29008c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="guitardenver&#39;s gravatar image" /><p><span>guitardenver</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="guitardenver has no accepted answers">0%</span></p></div></div><div id="comments-container-13635" class="comments-container"></div><div id="comment-tools-13635" class="comment-tools"></div><div class="clear"></div><div id="comment-13635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13637"></span>

<div id="answer-container-13637" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13637-score" class="post-score" title="current number of votes">0</div><span id="post-13637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark will not show you the Ethernet preamble or the start-of-frame delimiter; they are not present in the frame when Wireshark sees it. Ethernet frames will start with the destination MAC address.</p><p>To see everything in hex, simply make sure the Packet Bytes pane is visible (View &gt; Packet Bytes). The packet contents will be shown on the left in hex, and on the right in ASCII.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '12, 14:53</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-13637" class="comments-container"></div><div id="comment-tools-13637" class="comment-tools"></div><div class="clear"></div><div id="comment-13637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

