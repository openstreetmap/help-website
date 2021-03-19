+++
type = "question"
title = "Slow loading internet pages"
description = '''Hello, I&#x27;m trying to troubleshoot an issue on my network where webpages are loading slowly over our network cards. Internet works just fine over wireless (sonicpoints connected to the sonicwall firewall). All my switches and firewalls are up to date and there are no errors or faults on any of them. ...'''
date = "2015-01-05T10:17:00Z"
lastmod = "2015-01-07T01:56:00Z"
weight = 38894
keywords = [ "wireless", "wireshark", "slowness", "internet" ]
aliases = [ "/questions/38894" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Slow loading internet pages](/questions/38894/slow-loading-internet-pages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38894-score" class="post-score" title="current number of votes">0</div><span id="post-38894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm trying to troubleshoot an issue on my network where webpages are loading slowly over our network cards. Internet works just fine over wireless (sonicpoints connected to the sonicwall firewall). All my switches and firewalls are up to date and there are no errors or faults on any of them. This slowness is happening with every computer in the office.</p><p>Our provider, Century Link, is running with no problem. Streaming and downloading is as fast as it usually is and speedtests show up to 45mbps free out of a 50mb internet connection.</p><p>I started running wireshark scans and I don't see a lot of broadcasts at all. I do however see a lot of tcp retransmissions and "previous segment not captured" when I run a capture on port 80 over the network card (with wireless disabled). Captures on the wireless show almost no TCP retransmissions at all.</p><p>Thoughts? How can I upload a capture?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-slowness" rel="tag" title="see questions tagged &#39;slowness&#39;">slowness</span> <span class="post-tag tag-link-internet" rel="tag" title="see questions tagged &#39;internet&#39;">internet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '15, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/2fbc0de6616e99cef0d836f3da497b4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RCFAdmin&#39;s gravatar image" /><p><span>RCFAdmin</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RCFAdmin has no accepted answers">0%</span></p></div></div><div id="comments-container-38894" class="comments-container"><span id="38899"></span><div id="comment-38899" class="comment"><div id="post-38899-score" class="comment-score"></div><div class="comment-text"><p>take a capture during issue and you can upload it to cloudshark.</p></div><div id="comment-38899-info" class="comment-info"><span class="comment-age">(05 Jan '15, 21:16)</span> <span class="comment-user userinfo">kishan pandey</span></div></div></div><div id="comment-tools-38894" class="comment-tools"></div><div class="clear"></div><div id="comment-38894-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38922"></span>

<div id="answer-container-38922" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38922-score" class="post-score" title="current number of votes">0</div><span id="post-38922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I do however see a lot of tcp retransmissions ... when I run a capture .... over the network card (with wireless disabled).<br />
Captures on the wireless show almost no TCP retransmissions at all.</p></blockquote><p>Sounds like a problem with your LAN infrastrcuture. Some ideas:</p><ul><li>The LAN interface of your SonicWall might be "broken". Please check the error counters for that interface. Your local SonicWall guru should know how to do that.</li><li>The Switch interface, where your SonicWall is connected to, might be broken. Please check the error counters for that interface on the switch. Your local switch guru should know how to do that.</li><li>One of the network switches could be overloaded. Maybe high CPU load due to a loop on that switch. Your local switch guru should know how to check that.</li><li>Check/Replace the network cables to/from the SonicWall to the switch</li><li>There might be a QoS policy configured on the SonicWall that applies only to traffic from the LAN and not from the Wireless network. Please check that as well.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '15, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-38922" class="comments-container"></div><div id="comment-tools-38922" class="comment-tools"></div><div class="clear"></div><div id="comment-38922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

