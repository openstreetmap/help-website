+++
type = "question"
title = "Filtering 802.11 MAC Addresses"
description = '''I am using an AirPcap with Wireshark for the first time and receiving lots of wireless packets. I am trying to filter by MAC address. So I tried using wlan_mgt.fixed.src_mac_addr == 00:06:66:54:21:75 for the MAC address that is transmitting but when I apply the filter it filters out everything inclu...'''
date = "2013-07-02T12:58:00Z"
lastmod = "2013-07-02T14:12:00Z"
weight = 22568
keywords = [ "kirk" ]
aliases = [ "/questions/22568" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering 802.11 MAC Addresses](/questions/22568/filtering-80211-mac-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22568-score" class="post-score" title="current number of votes">0</div><span id="post-22568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using an AirPcap with Wireshark for the first time and receiving lots of wireless packets. I am trying to filter by MAC address. So I tried using wlan_mgt.fixed.src_mac_addr == 00:06:66:54:21:75 for the MAC address that is transmitting but when I apply the filter it filters out everything including the packets sent by 00:06:66:54:21:75. So is there a way to filter 802.11 MAC addresses?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-kirk" rel="tag" title="see questions tagged &#39;kirk&#39;">kirk</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '13, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/a64b625e37896ea75ba768a7bf8f598a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="funonline41&#39;s gravatar image" /><p><span>funonline41</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="funonline41 has no accepted answers">0%</span></p></div></div><div id="comments-container-22568" class="comments-container"></div><div id="comment-tools-22568" class="comment-tools"></div><div class="clear"></div><div id="comment-22568-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22571"></span>

<div id="answer-container-22571" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22571-score" class="post-score" title="current number of votes">0</div><span id="post-22571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>wlan_mgt.fixed.src_mac_addr</code> isn't the source address of an 802.11 packet, it's a field in the body of a management frame. Data and control frames don't even <em>have</em> that field.</p><p>If you want the source address of an 802.11 frame, it's <code>wlan.sa</code>, so what you want is <code>wlan.sa == 00:06:66:54:21:75</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '13, 13:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-22571" class="comments-container"><span id="22574"></span><div id="comment-22574" class="comment"><div id="post-22574-score" class="comment-score"></div><div class="comment-text"><p>Thanks - That worked!</p></div><div id="comment-22574-info" class="comment-info"><span class="comment-age">(02 Jul '13, 14:12)</span> <span class="comment-user userinfo">funonline41</span></div></div></div><div id="comment-tools-22571" class="comment-tools"></div><div class="clear"></div><div id="comment-22571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

