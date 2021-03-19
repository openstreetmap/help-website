+++
type = "question"
title = "Capture http Get request"
description = '''Here is the first line of a captured get request,   qqCcEv#C@lbPk^PGET / HTTP/1.1 Here is another first line- to the same site,  qqCcErWC@lbP-5 #PGET / HTTP/1.1 The wierd qq.. bytes before the &#x27;GET&#x27;, what are they for? I am getting drastically different responses depending on their content.'''
date = "2012-11-11T16:11:00Z"
lastmod = "2012-11-11T17:13:00Z"
weight = 15805
keywords = [ "get", "http", "wireshark" ]
aliases = [ "/questions/15805" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture http Get request](/questions/15805/capture-http-get-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15805-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15805-score" class="post-score" title="current number of votes">0</div><span id="post-15805-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Here is the first line of a captured get request, qqCcEv#<span class="__cf_email__" data-cfemail="9cdfdcf0feccf7">[email protected]</span>^PGET / HTTP/1.1</p><p>Here is another first line- to the same site, <span class="__cf_email__" data-cfemail="3d4c4c7e5e784f6a7e7d515f6d1008">[email protected]</span> #PGET / HTTP/1.1</p><p>The wierd qq.. bytes before the 'GET', what are they for? I am getting drastically different responses depending on their content.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-get" rel="tag" title="see questions tagged &#39;get&#39;">get</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Nov '12, 16:11</strong></p><img src="https://secure.gravatar.com/avatar/49f47caf6f6bcac15faff47677079dcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmu2101&#39;s gravatar image" /><p><span>jmu2101</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmu2101 has no accepted answers">0%</span></p></div></div><div id="comments-container-15805" class="comments-container"><span id="15806"></span><div id="comment-15806" class="comment"><div id="post-15806-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The wierd qq.. bytes before the 'GET', what are they for?</p></blockquote><p>hard to say without the full packet. Can you please post the whole packet that contains that request? You can export just that one packet and upload it to <a href="http://cloudshark.org">cloudshark.org</a> (or any other online storage). If it's possible to upload the response of the server as well, please do so.</p><p>Regards Kurt</p></div><div id="comment-15806-info" class="comment-info"><span class="comment-age">(11 Nov '12, 16:44)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-15805" class="comment-tools"></div><div class="clear"></div><div id="comment-15805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15807"></span>

<div id="answer-container-15807" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15807-score" class="post-score" title="current number of votes">1</div><span id="post-15807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You're not looking at the bytes in the packets that appear <em>before</em> the GET request, are you? In the link-layer packet that contains the first part of the GET request (or all of it if it fits in a single TCP segment), before the GET request you'll have a TCP header, and before the TCP header you'll have an IPv4 or an IPv6 header, and before the IP header you'll probably have some link-layer header such as an Ethernet header or an 802.11 header or a PPP header or....</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '12, 17:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-15807" class="comments-container"></div><div id="comment-tools-15807" class="comment-tools"></div><div class="clear"></div><div id="comment-15807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

