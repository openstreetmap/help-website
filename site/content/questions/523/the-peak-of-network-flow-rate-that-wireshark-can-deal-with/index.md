+++
type = "question"
title = "the peak of network flow rate that wireshark can deal with"
description = '''I am wondering what is the peak of network flow rate that wireshark can deal with. Is it 1Gbps or 10Gbps? I need a answer. Thank you.'''
date = "2010-10-18T01:37:00Z"
lastmod = "2010-10-19T16:20:00Z"
weight = 523
keywords = [ "capture-limits", "rate", "flow" ]
aliases = [ "/questions/523" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [the peak of network flow rate that wireshark can deal with](/questions/523/the-peak-of-network-flow-rate-that-wireshark-can-deal-with)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-523-score" class="post-score" title="current number of votes">0</div><span id="post-523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am wondering what is the peak of network flow rate that wireshark can deal with. Is it 1Gbps or 10Gbps? I need a answer. Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-limits" rel="tag" title="see questions tagged &#39;capture-limits&#39;">capture-limits</span> <span class="post-tag tag-link-rate" rel="tag" title="see questions tagged &#39;rate&#39;">rate</span> <span class="post-tag tag-link-flow" rel="tag" title="see questions tagged &#39;flow&#39;">flow</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '10, 01:37</strong></p><img src="https://secure.gravatar.com/avatar/d348d2822cc91999eb8382c0c01cdb75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jerrylin&#39;s gravatar image" /><p><span>jerrylin</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jerrylin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Feb '16, 05:37</strong> </span></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span></p></div></div><div id="comments-container-523" class="comments-container"></div><div id="comment-tools-523" class="comment-tools"></div><div class="clear"></div><div id="comment-523-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="547"></span>

<div id="answer-container-547" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-547-score" class="post-score" title="current number of votes">4</div><span id="post-547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think it's mostly a hardware issue, and specifically how fast the data can be transported and written from the NIC PHY to the storage system. I would strongly recommend using PCI Express NICs (PCI-X or PCI are too slow for anything above 2-3 hundred MBit/s), and going for the fastest hard drives in a fast RAID setup (meaning: NOT RAID 5 or any other RAID level writing CRCs). I usually prefer RAID 10, but it can get quite expensive. I built a box once, using the Cacetech TurboCAP card on a XEON Quad Core with 8 300G Velociraptor SAS drives running on an ICP Vortex/Adaptec RAID card as RAID 10, and it had no trouble capturing 1G/s with zero packet drops and full packet size captured.</p><p>I did a test once, capturing a link providing 1GBit/s sustained traffic with a Core2Duo Laptop (2-3 years old) with a 4Gig of RAM, one 7200 2.5 SATA drive and a PCI-E Gigabit NIC. I had about 80% packet drops. After tuning Wireshark various capture settings I got down to 0% packet drops, but it required heavy frame slicing down to 64 bytes in the end, which is not applicable in all capture situations.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '10, 16:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-547" class="comments-container"></div><div id="comment-tools-547" class="comment-tools"></div><div class="clear"></div><div id="comment-547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="526"></span>

<div id="answer-container-526" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-526-score" class="post-score" title="current number of votes">2</div><span id="post-526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That all depends on:</p><ul><li>Your network interface</li><li>Your storage subsystem</li><li>Your processing platform</li></ul><p>You could take a look at <a href="http://www.cacetech.com/index.html">Cace Technologies</a> website for high rate capture solutions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '10, 09:36</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-526" class="comments-container"><span id="528"></span><div id="comment-528" class="comment"><div id="post-528-score" class="comment-score"></div><div class="comment-text"><p>Is that means wireshark can capture and analyse network flow at any rate if the hardware condition allows? The bottleneck is the hardware? For example, if the network flow rate is 10Gbps, the hardware is extremely strong(Intel(R) Xeon(R) CPU L5420， 8GB， 2TB), the platform is linux, can wireshark work with the rate normally?</p></div><div id="comment-528-info" class="comment-info"><span class="comment-age">(18 Oct '10, 19:36)</span> <span class="comment-user userinfo">jerrylin</span></div></div><span id="534"></span><div id="comment-534" class="comment"><div id="post-534-score" class="comment-score"></div><div class="comment-text"><p>It still depends - what kind of NIC are you using? Is it CPU dependent? What else is running on the box? Are you monitoring via SPAN or a tap? Are you running a full 10Gpbs?</p></div><div id="comment-534-info" class="comment-info"><span class="comment-age">(19 Oct '10, 07:40)</span> <span class="comment-user userinfo">GeonJay</span></div></div></div><div id="comment-tools-526" class="comment-tools"></div><div class="clear"></div><div id="comment-526-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

