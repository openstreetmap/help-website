+++
type = "question"
title = "Gbps over Cat5 cable"
description = '''I have some areas of my network that have Cat5 (not Cat5e) cable installed. I was told at one time that Cat5e cable is necessary for good 1Gbps data transmission. Now I&#x27;m hearing that Cat5 is just fine. How can I use Wireshark to test this for myself? What should I expect to see if a certain cable i...'''
date = "2010-12-20T07:16:00Z"
lastmod = "2010-12-20T18:48:00Z"
weight = 1405
keywords = [ "1gbps", "cat5e", "speed", "cat5" ]
aliases = [ "/questions/1405" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Gbps over Cat5 cable](/questions/1405/gbps-over-cat5-cable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1405-score" class="post-score" title="current number of votes">0</div><span id="post-1405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have some areas of my network that have Cat5 (not Cat5e) cable installed. I was told at one time that Cat5e cable is necessary for good 1Gbps data transmission. Now I'm hearing that Cat5 is just fine. How can I use Wireshark to test this for myself? What should I expect to see if a certain cable install is not adequate for 1Gbps? Have I been misinformed? Thanks in advance for this great resource and your comments.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-1gbps" rel="tag" title="see questions tagged &#39;1gbps&#39;">1gbps</span> <span class="post-tag tag-link-cat5e" rel="tag" title="see questions tagged &#39;cat5e&#39;">cat5e</span> <span class="post-tag tag-link-speed" rel="tag" title="see questions tagged &#39;speed&#39;">speed</span> <span class="post-tag tag-link-cat5" rel="tag" title="see questions tagged &#39;cat5&#39;">cat5</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '10, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/118ba0647042a5b2634b267f7291ed7e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Network%20Dude&#39;s gravatar image" /><p><span>Network Dude</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Network Dude has no accepted answers">0%</span></p></div></div><div id="comments-container-1405" class="comments-container"></div><div id="comment-tools-1405" class="comment-tools"></div><div class="clear"></div><div id="comment-1405-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1409"></span>

<div id="answer-container-1409" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1409-score" class="post-score" title="current number of votes">0</div><span id="post-1409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Welcome in <em>intermittend problem</em> hell. You'll never know when a connection lands on bad link. Once you do find out, you may be able to track it from one of the involved nodes, looking how error recovery procedures kick in for the applicable transport protocol (if present) (like TCP retransmissions), or higher up, like SIP transactions producing repeats. Tricky stuff.</p><p>A better source would be to look at network equipment, especially interface statistics, to see if there are transmission problems at the lowest layers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Dec '10, 14:51</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1409" class="comments-container"></div><div id="comment-tools-1409" class="comment-tools"></div><div class="clear"></div><div id="comment-1409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1417"></span>

<div id="answer-container-1417" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1417-score" class="post-score" title="current number of votes">0</div><span id="post-1417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Gigabit Ethernet over copper (or officially IEEE 802.3 1000BaseT or something like that) was always designed to work on Category5 cable. Provided all of the field cable, patch and termination panels, and patch cables meet the required specs for Cat5 it will work. (Cable equipment vendors will twist the meaning of this to convince you otherwise).</p><p>If you want to test a cable plant for Category 5 compliance you realy need to do this at the electrical level. This means analogue equipment that measure attenuation, bandwidth, cross-talk etc. The problem of testing digitally only (that is, sending lots of packets and measuring the bit error rate) is that a lot of network equipment will perform with no problems even if the cable is less than Cat5 standard. If the receivers are better than required they will recover from noise and so forth. The issue then is if you change out your test equipment (say your 2 laptops) and put in the production equipment who is to say whether they can operate as well at the limits of the cable.</p><p>Wireshark only gets presented packets that have passed the CRC integrity check of the NIC. So you won't see packets with bit errors - as Jaap has said, you might be able to infer there are issues by seeing retransmissions or missing packets. As long as there are no other issues (like congestion on the hosts) then this can be useful. However you might be better off looking at stats available at the NIC level on your hosts and or switches. You should not see any Rx errors if the cable plant is good - as below (from a "show int" on a HP ProCurve)</p><p>Link Status : Up<br />
</p><p>Bytes Rx : 2,025,057,903 Unicast Rx : 9,877,380 Bcast/Mcast Rx : 37,539 Bytes Tx : 1,328,887,948 Unicast Tx : 9,827,047 Bcast/Mcast Tx : 1,730,731</p><p>FCS Rx : 0 Alignment Rx : 0 Runts Rx : 0 Giants Rx : 0 Total Rx Errors: 0 Drops Tx : 0 Collisions Tx : 0 Late Colln Tx : 0 Excessive Colln: 0 Deferred Tx : 0</p><p>Basically to test this digital, just use "iperf" or simple file transfer to generate a lot of traffic at close to the 1Gbps line rate. Watch the error counters as above and make sure they don't increment. But as I have said earlier, that really only tests <em>that</em> cable plant, with <em>that</em> equipment. It won't prove it is Category5 compliant in general terms.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Dec '10, 18:48</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span> </br></p></div></div><div id="comments-container-1417" class="comments-container"></div><div id="comment-tools-1417" class="comment-tools"></div><div class="clear"></div><div id="comment-1417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

