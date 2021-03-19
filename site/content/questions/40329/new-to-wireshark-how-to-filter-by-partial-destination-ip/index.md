+++
type = "question"
title = "New to WireShark - how to filter by partial destination ip?"
description = '''New to wireshark. I want to use the tool to figure out what traffic is being sent over the internet. I already know what protocol i am looking for. So i want to create a filter for IP destination outside my LAN and protocol==TCP. How would i accomplish this? Thanks in advance, Bob'''
date = "2015-03-06T09:22:00Z"
lastmod = "2015-03-09T09:46:00Z"
weight = 40329
keywords = [ "filter", "outside", "destination", "lan" ]
aliases = [ "/questions/40329" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [New to WireShark - how to filter by partial destination ip?](/questions/40329/new-to-wireshark-how-to-filter-by-partial-destination-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40329-score" class="post-score" title="current number of votes">0</div><span id="post-40329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>New to wireshark. I want to use the tool to figure out what traffic is being sent over the internet. I already know what protocol i am looking for. So i want to create a filter for IP destination outside my LAN and protocol==TCP. How would i accomplish this?</p><p>Thanks in advance,</p><p>Bob</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-outside" rel="tag" title="see questions tagged &#39;outside&#39;">outside</span> <span class="post-tag tag-link-destination" rel="tag" title="see questions tagged &#39;destination&#39;">destination</span> <span class="post-tag tag-link-lan" rel="tag" title="see questions tagged &#39;lan&#39;">lan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '15, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/ac94592dc26bc9e0dd0f9143bd11b75f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blentz&#39;s gravatar image" /><p><span>blentz</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blentz has no accepted answers">0%</span></p></div></div><div id="comments-container-40329" class="comments-container"></div><div id="comment-tools-40329" class="comment-tools"></div><div class="clear"></div><div id="comment-40329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40330"></span>

<div id="answer-container-40330" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40330-score" class="post-score" title="current number of votes">2</div><span id="post-40330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Display filter "tcp &amp;&amp; !ip.dst==192.168.1.0/24" where 192.168.1.0/24 is your LAN subnet. Substitute your actual LAN address range.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '15, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-40330" class="comments-container"><span id="40385"></span><div id="comment-40385" class="comment"><div id="post-40385-score" class="comment-score"></div><div class="comment-text"><p>sorry but i don't understand the 0/24 - what is that? My lan subnet is 192.168.1.0-254</p></div><div id="comment-40385-info" class="comment-info"><span class="comment-age">(09 Mar '15, 08:18)</span> <span class="comment-user userinfo">blentz</span></div></div><span id="40389"></span><div id="comment-40389" class="comment"><div id="post-40389-score" class="comment-score"></div><div class="comment-text"><p>An IPv4 address is 32 bits (four bytes). The "/24" means we only care about the first 24 bits (the first three bytes). So "192.168.1.0/24" means any address that has 192.168.1 as the first three bytes. We don't care what the fourth byte is. So 192.168.1.0/24 is equivalent to 192.168.1.0-254.</p></div><div id="comment-40389-info" class="comment-info"><span class="comment-age">(09 Mar '15, 09:46)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-40330" class="comment-tools"></div><div class="clear"></div><div id="comment-40330-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

