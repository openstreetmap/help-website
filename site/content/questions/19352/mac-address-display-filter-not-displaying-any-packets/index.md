+++
type = "question"
title = "MAC address display filter not displaying any packets"
description = '''Hi, This is a bit of a dumb question but I have been struggling with this for an hour or so without getting a resolution. I have a capture file containing WiFi packets. I want to filter out all packets not going to or from a particular access point. There are thousands of packets in the trace so I j...'''
date = "2013-03-11T04:27:00Z"
lastmod = "2013-03-12T10:40:00Z"
weight = 19352
keywords = [ "mac", "display-filter" ]
aliases = [ "/questions/19352" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MAC address display filter not displaying any packets](/questions/19352/mac-address-display-filter-not-displaying-any-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19352-score" class="post-score" title="current number of votes">0</div><span id="post-19352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>This is a bit of a dumb question but I have been struggling with this for an hour or so without getting a resolution. I have a capture file containing WiFi packets. I want to filter out all packets not going to or from a particular access point. There are thousands of packets in the trace so I just want to watch what is happening between my 4 clients and the access point. Should be easy enough. When I enter the required display filter, it appears in green, but when I apply it, no packets are displayed. This is the same whether I type in the source and destination in manually or I right click on a packet and select apply as filter. The capture is IEEE802 and RadioTap. IP address filtering works so it is not that the display filter is not working. I am sure I have used this in the past. The inverse of the filter doesn't work either - it displays all packets including those with the selected MAC address. Thanks in anticipation. (The same issue applies to older versions as well as the newest so it must be something I am doing wrong).</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '13, 04:27</strong></p><img src="https://secure.gravatar.com/avatar/daded68ea69d0dd1558fa0707db618b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DBBarrass&#39;s gravatar image" /><p><span>DBBarrass</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DBBarrass has no accepted answers">0%</span></p></div></div><div id="comments-container-19352" class="comments-container"><span id="19368"></span><div id="comment-19368" class="comment"><div id="post-19368-score" class="comment-score"></div><div class="comment-text"><p>What display filter are you using? 802.11 has more than just source and destination MAC addresses; which MAC addresses are you checking?</p></div><div id="comment-19368-info" class="comment-info"><span class="comment-age">(11 Mar '13, 20:00)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="19376"></span><div id="comment-19376" class="comment"><div id="post-19376-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy, thanks for the reply. The filter I am using is eth.src == 04:f0:21:03:7d:c0 also used in conjunction with eth.dst and the same MAC address so I can (hopefully) see both side of the conversation.</p><p>I have successfully used a capture filter using ether host with the same MAC address and this works well, I end up with a capture file containing only traffic relating to the WiFi access point I am tracing. However, this obviously doesn't work with an existing capture file containing traffic from several access points and clients.</p><p>Is there a way of uploading a (small) capture file if this would help?</p></div><div id="comment-19376-info" class="comment-info"><span class="comment-age">(12 Mar '13, 02:40)</span> <span class="comment-user userinfo">DBBarrass</span></div></div><span id="19377"></span><div id="comment-19377" class="comment"><div id="post-19377-score" class="comment-score"></div><div class="comment-text"><p>Yes, you can do that on <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> and post the URL here after uploading the file.</p></div><div id="comment-19377-info" class="comment-info"><span class="comment-age">(12 Mar '13, 02:51)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-19352" class="comment-tools"></div><div class="clear"></div><div id="comment-19352-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19379"></span>

<div id="answer-container-19379" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19379-score" class="post-score" title="current number of votes">1</div><span id="post-19379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>The filter I am using is eth.src == 04:f0:21:03:7d:c0</p></blockquote><p>That filter only matches packets that contain an Ethernet header, so it will not match <em>any</em> packets with an 802.11 header (except for ones that have an Ethernet packet encapsulated within them, and thus have both 802.11 and Ethernet headers).</p><p>For 802.11 packets, you would need the filter "wlan.src == 04:f0:21:03:7d:c0". (Note that this will not match a packet that was sent by some other MAC address to an access point with the MAC address of 04:f0:21:03:7d:c0.)</p><p>(And, yes, this means that there is no such thing as a generic MAC address display filter. That is a deficiency of the current display filter mechanism.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '13, 03:27</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Mar '13, 03:28</strong> </span></p></div></div><div id="comments-container-19379" class="comments-container"><span id="19395"></span><div id="comment-19395" class="comment"><div id="post-19395-score" class="comment-score"></div><div class="comment-text"><p>Aaargh - so obvious! Thanks a lot. Should have read the manual more closely. Thanks a bunch.</p></div><div id="comment-19395-info" class="comment-info"><span class="comment-age">(12 Mar '13, 10:40)</span> <span class="comment-user userinfo">DBBarrass</span></div></div></div><div id="comment-tools-19379" class="comment-tools"></div><div class="clear"></div><div id="comment-19379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

