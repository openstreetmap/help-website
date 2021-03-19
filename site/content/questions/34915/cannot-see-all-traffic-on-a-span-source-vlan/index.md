+++
type = "question"
title = "Cannot see all traffic on a span source vlan"
description = '''I&#x27;m sending traffic to wireshark on a span port source vlan 110. I&#x27;m seeing traffic but only traffic on the VLAN. The destination is all broadcast and multicast. Why am I not seeing traffic to my other VLANS/Networks? '''
date = "2014-07-25T13:38:00Z"
lastmod = "2014-07-26T21:44:00Z"
weight = 34915
keywords = [ "vlan", "span" ]
aliases = [ "/questions/34915" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot see all traffic on a span source vlan](/questions/34915/cannot-see-all-traffic-on-a-span-source-vlan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34915-score" class="post-score" title="current number of votes">0</div><span id="post-34915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm sending traffic to wireshark on a span port source vlan 110. I'm seeing traffic but only traffic on the VLAN. The destination is all broadcast and multicast. Why am I not seeing traffic to my other VLANS/Networks?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span> <span class="post-tag tag-link-span" rel="tag" title="see questions tagged &#39;span&#39;">span</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '14, 13:38</strong></p><img src="https://secure.gravatar.com/avatar/8f27ed3d96846021d5c0498b6102bf64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="judgejudy&#39;s gravatar image" /><p><span>judgejudy</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="judgejudy has no accepted answers">0%</span></p></div></div><div id="comments-container-34915" class="comments-container"><span id="34927"></span><div id="comment-34927" class="comment"><div id="post-34927-score" class="comment-score"></div><div class="comment-text"><p>A few questions:</p><ul><li>Are you applying any filters to your Wireshark trace? Note that a capture filter would need the "vlan" keyword to capture any traffic with 802.1q frames.</li><li>Are you sure your SPAN configuration is correct? Assuming Cisco IOS, does the output of "show port monitor" confirm the vlan in question has traffic forwarded to the interface you have the trace running on?</li><li>Note that vlan-based SPAN is only going to forward the traffic that this particular switch sees on this vlan, unless you've also configured remote SPAN sessions on upstream switches. For the traffic that you want to see, can you confirm if the traffic is on this switch or on another?</li><li>For the broadcast traffic you see, are these broadcasts for the vlan you have the monitor session for? If the port is a SPAN port, you should see no traffic other than what is being monitored coming toward you.</li></ul></div><div id="comment-34927-info" class="comment-info"><span class="comment-age">(26 Jul '14, 21:44)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-34915" class="comment-tools"></div><div class="clear"></div><div id="comment-34915-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

