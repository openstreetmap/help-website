+++
type = "question"
title = "Wireshark shows high volume of DCE traffic"
description = '''Hello all...  In analyzing traffic for a particular application, I&#x27;m seeing that roughly half of the traffic is reported by Wireshark as &quot;Data Center Ethernet (DCE) protocol(Cisco)&quot;. It is consuming close to 2Gbps of link capacity. I have seen this type of traffic before, but I never gave it much th...'''
date = "2017-06-04T21:03:00Z"
lastmod = "2017-06-11T18:54:00Z"
weight = 61779
keywords = [ "dce" ]
aliases = [ "/questions/61779" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark shows high volume of DCE traffic](/questions/61779/wireshark-shows-high-volume-of-dce-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61779-score" class="post-score" title="current number of votes">0</div><span id="post-61779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all...</p><p>In analyzing traffic for a particular application, I'm seeing that roughly half of the traffic is reported by Wireshark as "Data Center Ethernet (DCE) protocol(Cisco)". It is consuming close to <strong>2Gbps</strong> of link capacity.</p><p>I have seen this type of traffic before, but I never gave it much thought, mainly because I have never seen a significant amount of it.</p><p>Has anyone seen this level of DCE traffic in their travels?</p><p>Any suggestions on how to diagnose why there is so much of it, and how to remove/reduce it?</p><p>Thx much.</p><p>Feenyman99</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dce" rel="tag" title="see questions tagged &#39;dce&#39;">dce</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '17, 21:03</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p><span>feenyman99</span><br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span></p></div></div><div id="comments-container-61779" class="comments-container"></div><div id="comment-tools-61779" class="comment-tools"></div><div class="clear"></div><div id="comment-61779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="61813"></span>

<div id="answer-container-61813" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61813-score" class="post-score" title="current number of votes">0</div><span id="post-61813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>One brief discussion of DCE is at <a href="http://wayback.archive.org/web/20160303235923/http://www.datacenterhandbook.com/2014/03/06/cisco-fabricpath/">this Data Center Handbook page</a> (saved on the Wayback Machine); DCE packets are the ones shown as "FP Frame Format". Here's <a href="https://www.packetmischief.ca/2012/04/17/five-functional-facts-about-fabricpath/">another page about FabricPath</a> and <a href="http://www.cisco.com/c/dam/en/us/products/collateral/switches/nexus-7000-series-switches/at_a_glance_c45-605626.pdf">a Cisco document about it</a>.</p><p>Wireshark <em>should</em> be dissecting the Ethernet traffic inside the FP frames, so it should show them as more than just "Data Center Ethernet"; if it's not, that's probably a Wireshark bug. If it does dissect the traffic inside the frames, then that'll tell you what type of traffic it is, at least at the Ethernet layer, and perhaps at layers above that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '17, 20:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-61813" class="comments-container"></div><div id="comment-tools-61813" class="comment-tools"></div><div class="clear"></div><div id="comment-61813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61940"></span>

<div id="answer-container-61940" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61940-score" class="post-score" title="current number of votes">0</div><span id="post-61940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>PROBLEM SOLVED...</p><p>It turns out, the packets identified by Wireshark as DCE, are actually Cisco FabricPath (CFP) encapsulated packets, as noted by Guy H.</p><p>The reason that Wireshark was not dissecting the Ethernet inside the CFP frames was: CFP dissection was not "fully" enabled. What I mean by that is...</p><p>When I went to Analyze -&gt; Enabled Protocols, I saw that “CFP” <strong>was</strong> enabled, but… the sub-protocol “fp_eth” was <strong>not</strong> enabled.</p><p>Once I checked that fp_eth box, Wireshark is now dissecting these packets with all layers interpreted, and the fog has lifted :-).</p><p>thx,</p><p>feenyman99</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '17, 18:54</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p><span>feenyman99</span><br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span></p></div></div><div id="comments-container-61940" class="comments-container"></div><div id="comment-tools-61940" class="comment-tools"></div><div class="clear"></div><div id="comment-61940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

