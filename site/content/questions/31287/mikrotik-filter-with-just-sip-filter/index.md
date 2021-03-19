+++
type = "question"
title = "Mikrotik filter with just SIP filter"
description = '''Hi, I am using Mikrotik to stream to Wireshark. To see only the Mikrotik stream and not my local interface I use: udp.port == 37008 How can I drill down into this data stream and only show for example my VoIP (rtp) traffic which comes from my Mikrotik router?'''
date = "2014-03-29T16:28:00Z"
lastmod = "2014-03-30T12:44:00Z"
weight = 31287
keywords = [ "mikrotikfilter" ]
aliases = [ "/questions/31287" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mikrotik filter with just SIP filter](/questions/31287/mikrotik-filter-with-just-sip-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31287-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31287-score" class="post-score" title="current number of votes">0</div><span id="post-31287-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am using Mikrotik to stream to Wireshark. To see only the Mikrotik stream and not my local interface I use: udp.port == 37008</p><p>How can I drill down into this data stream and only show for example my VoIP (rtp) traffic which comes from my Mikrotik router?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mikrotikfilter" rel="tag" title="see questions tagged &#39;mikrotikfilter&#39;">mikrotikfilter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '14, 16:28</strong></p><img src="https://secure.gravatar.com/avatar/6946ceaa2a7d4603cd969529a037019d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hoender&#39;s gravatar image" /><p><span>Hoender</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hoender has no accepted answers">0%</span></p></div></div><div id="comments-container-31287" class="comments-container"></div><div id="comment-tools-31287" class="comment-tools"></div><div class="clear"></div><div id="comment-31287-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31294"></span>

<div id="answer-container-31294" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31294-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31294-score" class="post-score" title="current number of votes">0</div><span id="post-31294-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It would help if you can post a screenshot of the packet details you see for a packet that should be decoded as SIP. Or better yet post a pcap file somewhere, for example on cloudshark.org.</p><p>From reading the Mikrotik docs, it looks like they encapsulate the packets in TZSP, which Wireshark does support and should automatically decode on UDP port 37008.</p><p>Are you seeing "TZSP" as the protocol inside the UDP packets?</p><p>If so, the next packet inside the TZSP should be the link-layer packet - either Ethernet or 802.11, and from there it should decode the rest automatically.</p><p>If the original SIP packets didn't use TCP or UDP port 5060, though, it won't decode them as SIP. You'll have to force it by doing one of the "Decode as..." methods.</p><p>But again, if you can post the pcap file it would help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '14, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-31294" class="comments-container"></div><div id="comment-tools-31294" class="comment-tools"></div><div class="clear"></div><div id="comment-31294-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

