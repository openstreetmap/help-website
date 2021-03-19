+++
type = "question"
title = "How do I capture RTP traffic with Wireshark 2.0.3?"
description = '''I am running Windows 7 and I have a Realtec PCI family controller. I am trying to capture Sip and RTP traffic from a Avaya 1120 set with port mirroring turned on. I don&#x27;t see any sip or RTP packets at all when I have a call up on the avaya set. Any thoughts?'''
date = "2016-06-06T10:00:00Z"
lastmod = "2016-06-06T12:08:00Z"
weight = 53243
keywords = [ "rtp" ]
aliases = [ "/questions/53243" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I capture RTP traffic with Wireshark 2.0.3?](/questions/53243/how-do-i-capture-rtp-traffic-with-wireshark-203)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53243-score" class="post-score" title="current number of votes">0</div><span id="post-53243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running Windows 7 and I have a Realtec PCI family controller. I am trying to capture Sip and RTP traffic from a Avaya 1120 set with port mirroring turned on. I don't see any sip or RTP packets at all when I have a call up on the avaya set. Any thoughts?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '16, 10:00</strong></p><img src="https://secure.gravatar.com/avatar/d406b18a3b191e4da7e75f5097ce8472?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carchibald&#39;s gravatar image" /><p><span>carchibald</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carchibald has no accepted answers">0%</span></p></div></div><div id="comments-container-53243" class="comments-container"><span id="53245"></span><div id="comment-53245" class="comment"><div id="post-53245-score" class="comment-score"></div><div class="comment-text"><p>Before digging any deeper, have you set promiscuous mode on? Can you see in the capture any other frames except ones your NIC itself is sending?</p></div><div id="comment-53245-info" class="comment-info"><span class="comment-age">(06 Jun '16, 10:28)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="53246"></span><div id="comment-53246" class="comment"><div id="post-53246-score" class="comment-score"></div><div class="comment-text"><p>Promiscuous mode is on but I am only seeing what my NIC card is sending. A Bunch ARP broadcasts.</p></div><div id="comment-53246-info" class="comment-info"><span class="comment-age">(06 Jun '16, 10:34)</span> <span class="comment-user userinfo">carchibald</span></div></div><span id="53249"></span><div id="comment-53249" class="comment"><div id="post-53249-score" class="comment-score"></div><div class="comment-text"><p>OK, so the traditional splitting of the problem into smaller ones has to take place.</p><p>Step 1, have you ever successfully captured any incoming traffic using that same PC connected to a regular switch port? If not, look for Answers to Questions like "cannot capture any incoming trafic". It is usually caused by an interference between security software drivers and WinPcap.</p><p>Step 2 would be to double-check the monitoring settings on the switch, as I've never heard that a promiscuous mode would not work on Realtech (nor any other wired NIC). You may be monitoring the switch port to which the phone is connected, and if the frames belonging to the VLAN dedicated for voice traffic are sent across that port tagged, your Realtec card/driver may ignore them rather than untag them as most other cards' Windows drivers do. If this is the case, you may need to search for an Answer to a Question dealing with Realtec and VLANs which has re-popped up here recently, or your switch may be able to monitor the VLAN instead of a port, and send the frames to the monitoring port without the tags in such case.</p></div><div id="comment-53249-info" class="comment-info"><span class="comment-age">(06 Jun '16, 12:08)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-53243" class="comment-tools"></div><div class="clear"></div><div id="comment-53243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

