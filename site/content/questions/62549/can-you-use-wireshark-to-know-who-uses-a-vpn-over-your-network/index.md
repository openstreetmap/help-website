+++
type = "question"
title = "Can you use wireshark to know who uses a vpn over your network?"
description = '''I don&#x27;t want to know anything about what they visited while vpn was active or anything i just want to know if anyone uses a vpn on my network.'''
date = "2017-07-05T19:02:00Z"
lastmod = "2017-07-05T23:42:00Z"
weight = 62549
keywords = [ "vpn", "computernetwork" ]
aliases = [ "/questions/62549" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can you use wireshark to know who uses a vpn over your network?](/questions/62549/can-you-use-wireshark-to-know-who-uses-a-vpn-over-your-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62549-score" class="post-score" title="current number of votes">0</div><span id="post-62549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I don't want to know anything about what they visited while vpn was active or anything i just want to know if anyone uses a vpn on my network.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vpn" rel="tag" title="see questions tagged &#39;vpn&#39;">vpn</span> <span class="post-tag tag-link-computernetwork" rel="tag" title="see questions tagged &#39;computernetwork&#39;">computernetwork</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '17, 19:02</strong></p><img src="https://secure.gravatar.com/avatar/d0cbaff1212800fb8b7b0c91ab381f1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Someone%20who%20needs%20help&#39;s gravatar image" /><p><span>Someone who ...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Someone who needs help has no accepted answers">0%</span></p></div></div><div id="comments-container-62549" class="comments-container"></div><div id="comment-tools-62549" class="comment-tools"></div><div class="clear"></div><div id="comment-62549-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62552"></span>

<div id="answer-container-62552" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62552-score" class="post-score" title="current number of votes">0</div><span id="post-62552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First, let's assume you can capture at the router which connects everyone in your network to the internet. Capturing on wireless networks is another can of worms so better to avoid it if you can.</p><p>Second, I suppose you have in mind those VPNs which are used to obfuscate what the user is doing on the internet from the network administrator and to anonymize the user to the services he visits, not the VPNs which are used to connect remote users to company networks.</p><p>If so, a typical pattern would be that a local machine has one or several encrypted conversations with a single remote IP while almost no other traffic towards the internet exists from that machine. You cannot 100% rely on spotting well-known ports used by VPNs for remote access because some VPN sites may mask the traffic as https or imap over tls while others may use e.g. OpenVPN which normally uses UDP as transport for the encrypted data. Even the traffic flow may be artificially modified (by transmitting bogus data while no real data flow is necessary). And there are many other things which can be done to make VPN traffic look similar to a normal one, including establishing transport conversations with many IPs at different times and spreading the actual conversations among them. So you'll never be certain. That's the goal after all.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '17, 23:42</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-62552" class="comments-container"></div><div id="comment-tools-62552" class="comment-tools"></div><div class="clear"></div><div id="comment-62552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

