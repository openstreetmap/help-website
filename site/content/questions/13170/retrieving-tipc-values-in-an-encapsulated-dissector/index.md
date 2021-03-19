+++
type = "question"
title = "Retrieving TIPC values in an encapsulated dissector"
description = '''I am trying to create a dissector for packets which use the TIPC encoding. The dissector will convert the destination port into a meaningful value by comparing against a table as well as doing some analysis on the data. This information would be presented as well as all the TIPC information. I curre...'''
date = "2012-07-31T00:51:00Z"
lastmod = "2012-08-08T08:07:00Z"
weight = 13170
keywords = [ "encapsulation", "tipc" ]
aliases = [ "/questions/13170" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Retrieving TIPC values in an encapsulated dissector](/questions/13170/retrieving-tipc-values-in-an-encapsulated-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13170-score" class="post-score" title="current number of votes">0</div><span id="post-13170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to create a dissector for packets which use the TIPC encoding. The dissector will convert the destination port into a meaningful value by comparing against a table as well as doing some analysis on the data. This information would be presented as well as all the TIPC information. I currently have it so "dissect_mydissect(tvbuff_t <em>tvb, packet_info</em> pinfo, proto_tree *tree)" is called for the correct packets, but the data being passed to it in tvb is only the data inside the TIPC packet not the information I need. I see its possible to get the Ethernet and frame data for a packet but is it possible to get the TIPC (or any encapsulating value for that matter) or would I need to create my own TIPC dissector and add my functionality to that.</p><p>Thanks for your time,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-encapsulation" rel="tag" title="see questions tagged &#39;encapsulation&#39;">encapsulation</span> <span class="post-tag tag-link-tipc" rel="tag" title="see questions tagged &#39;tipc&#39;">tipc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '12, 00:51</strong></p><img src="https://secure.gravatar.com/avatar/f8fcb6da439fcfcf31a94bf2c9b25aa3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John%20Smith&#39;s gravatar image" /><p><span>John Smith</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John Smith has no accepted answers">0%</span></p></div></div><div id="comments-container-13170" class="comments-container"></div><div id="comment-tools-13170" class="comment-tools"></div><div class="clear"></div><div id="comment-13170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13200"></span>

<div id="answer-container-13200" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13200-score" class="post-score" title="current number of votes">1</div><span id="post-13200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="John Smith has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If a dissector needs/want information from the encapsulating layer, then that dissector must make that data available somehow and pass it down. That is what packet_info is for. If you have control over both dissectors, you could pass info via a structure in packet_info.private_data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '12, 14:26</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-13200" class="comments-container"><span id="13261"></span><div id="comment-13261" class="comment"><div id="post-13261-score" class="comment-score"></div><div class="comment-text"><p>Thanks for that, I was using the inbuilt TIPC dissector but as far as I can see it doesn't pass anything into .private_data. I am going to look into possible ways to create my own TIPC plugin by just copying the code and making the plugin overwrite the inbuilt TIPC one and pass through what I need. Failing that I am probably just going to need my own version of Wireshark with a modified TIPC dissector. Those seem the only real two options I have, unless I am missing something obvious. Will post what I ended up doing.</p></div><div id="comment-13261-info" class="comment-info"><span class="comment-age">(01 Aug '12, 09:02)</span> <span class="comment-user userinfo">John Smith</span></div></div><span id="13474"></span><div id="comment-13474" class="comment"><div id="post-13474-score" class="comment-score"></div><div class="comment-text"><p>For my uses I only needed to convert the address into something more meaningful. In order to do this I ended up using "tvb-&gt;ds_tvb" where tvb is the passed in value from dissect_mydissect. One problem I had with this is the values appear to be byte reversed but I just did a work around for it. It isn't a pretty way of doing it, and there is almost definitely a better way out there, but for my uses it was fine.</p></div><div id="comment-13474-info" class="comment-info"><span class="comment-age">(08 Aug '12, 08:07)</span> <span class="comment-user userinfo">John Smith</span></div></div></div><div id="comment-tools-13200" class="comment-tools"></div><div class="clear"></div><div id="comment-13200-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

