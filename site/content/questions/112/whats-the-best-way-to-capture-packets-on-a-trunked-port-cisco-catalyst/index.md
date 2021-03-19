+++
type = "question"
title = "What&#x27;s the best way to capture packets on a trunked port (Cisco Catalyst)?"
description = '''We are trying to capture VLAN tagged packets on a Cisco Catalyst 3750. We have a VoIP phone that boots on our DATA VLAN and gets settings pushed to it from DHCP Scope option 242. One of these options tells the phone to boot on the VoIP VLAN. Anyways, I&#x27;ve been doing a simple &quot;monitor session&quot; on the...'''
date = "2010-09-15T14:01:00Z"
lastmod = "2010-09-15T14:38:00Z"
weight = 112
keywords = [ "vlan", "cisco", "trunk" ]
aliases = [ "/questions/112" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What's the best way to capture packets on a trunked port (Cisco Catalyst)?](/questions/112/whats-the-best-way-to-capture-packets-on-a-trunked-port-cisco-catalyst)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-112-score" class="post-score" title="current number of votes">2</div><span id="post-112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>We are trying to capture VLAN tagged packets on a Cisco Catalyst 3750. We have a VoIP phone that boots on our DATA VLAN and gets settings pushed to it from DHCP Scope option 242. One of these options tells the phone to boot on the VoIP VLAN.</p><p>Anyways, I've been doing a simple "monitor session" on the Cisco Catalyst for this but it doesn't appear we're seeing all of the VLAN tagged data. Our vendor suggests the best solution is to break out and use a hub. I tend to agree, but would like to know if I was over-looking a capture option on the Cisco platform.</p><p>thanks, Geoff</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span> <span class="post-tag tag-link-cisco" rel="tag" title="see questions tagged &#39;cisco&#39;">cisco</span> <span class="post-tag tag-link-trunk" rel="tag" title="see questions tagged &#39;trunk&#39;">trunk</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '10, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/a00c3e32ea96f4989d9360937a93c73f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeoffP&#39;s gravatar image" /><p><span>GeoffP</span><br />
<span class="score" title="40 reputation points">40</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeoffP has no accepted answers">0%</span></p></div></div><div id="comments-container-112" class="comments-container"></div><div id="comment-tools-112" class="comment-tools"></div><div class="clear"></div><div id="comment-112-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="113"></span>

<div id="answer-container-113" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-113-score" class="post-score" title="current number of votes">5</div><span id="post-113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="GeoffP has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In order for the 3750 to keep vlan tags when spanning a trunk port, you need to add <strong>encapsulation replicate</strong> when configuring your destination port.</p><p>Of course you also need to make sure that your capturing device does not strip the tags. See: <a href="http://wiki.wireshark.org/CaptureSetup/VLAN">http://wiki.wireshark.org/CaptureSetup/VLAN</a></p><p>Cheers, Sake</p><hr /><p>From <a href="http://www.cisco.com/en/US/docs/switches/lan/catalyst3750/software/release/12.1_19_ea1/configuration/guide/swspan.html">http://www.cisco.com/en/US/docs/switches/lan/catalyst3750/software/release/12.1_19_ea1/configuration/guide/swspan.html</a>:</p><p>However, when you enter the <strong>encapsulation replicate</strong> keywords when configuring a destination port, these changes occur:</p><p>•Packets are sent on the destination port with the same encapsulation—untagged, IEEE 802.1Q, or Inter-Switch Link (ISL)—that they had on the source port.</p><p>•Packets of all types, including BPDU and Layer 2 protocol packets are monitored.</p><p>Therefore, a local SPAN session with encapsulation replicate enabled can have a mixture of untagged, 802.1Q, and ISL tagged packets appear on the destination port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '10, 14:08</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Sep '10, 14:42</strong> </span></p></div></div><div id="comments-container-113" class="comments-container"></div><div id="comment-tools-113" class="comment-tools"></div><div class="clear"></div><div id="comment-113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="114"></span>

<div id="answer-container-114" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-114-score" class="post-score" title="current number of votes">2</div><span id="post-114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Geoff,</p><p>In addition to this you may also need to configure your OS/Driver to pass the Vlan tag to Wireshark. How to do this see http://wiki.wireshark.org/CaptureSetup/VLAN</p><p>regards Oliver</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '10, 14:38</strong></p><img src="https://secure.gravatar.com/avatar/ea89a7136cee2bff4cc1ddbaf5e1b676?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Oliver&#39;s gravatar image" /><p><span>Oliver</span><br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Oliver has no accepted answers">0%</span></p></div></div><div id="comments-container-114" class="comments-container"></div><div id="comment-tools-114" class="comment-tools"></div><div class="clear"></div><div id="comment-114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

