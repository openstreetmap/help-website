+++
type = "question"
title = "high packets per second under LLC protocol"
description = '''Greetings all, I was doing a sniff with wireshark and noticed my network was sending between 400-800 packets per second with over 98% of them under the &#x27;OTHER&#x27; label when sniffing. They were labeled with the protocol LLC and my log was flooded with the screenshot below. Can anyone provide some insig...'''
date = "2013-06-12T09:30:00Z"
lastmod = "2013-06-12T13:08:00Z"
weight = 21964
keywords = [ "pps", "llc", "broadcast" ]
aliases = [ "/questions/21964" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [high packets per second under LLC protocol](/questions/21964/high-packets-per-second-under-llc-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21964-score" class="post-score" title="current number of votes">0</div><span id="post-21964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings all, I was doing a sniff with wireshark and noticed my network was sending between 400-800 packets per second with over 98% of them under the 'OTHER' label when sniffing. They were labeled with the protocol LLC and my log was flooded with the screenshot below.</p><p>Can anyone provide some insight as to what may be causing so many packets being generated on my network?</p><p>Thank you</p><p><img src="http://imgur.com/jPayMA5.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pps" rel="tag" title="see questions tagged &#39;pps&#39;">pps</span> <span class="post-tag tag-link-llc" rel="tag" title="see questions tagged &#39;llc&#39;">llc</span> <span class="post-tag tag-link-broadcast" rel="tag" title="see questions tagged &#39;broadcast&#39;">broadcast</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jun '13, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/4e45865242b0ad811535703ef7212cc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="billjackson&#39;s gravatar image" /><p><span>billjackson</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="billjackson has no accepted answers">0%</span></p></img></div></div><div id="comments-container-21964" class="comments-container"></div><div id="comment-tools-21964" class="comment-tools"></div><div class="clear"></div><div id="comment-21964-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21971"></span>

<div id="answer-container-21971" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21971-score" class="post-score" title="current number of votes">1</div><span id="post-21971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="billjackson has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would say, that the device with the MAC address 'ASUSTEKC_e7:0b:5e' is broken and thus it sends 'unstructured' data to the network (due to a broken driver or a broken NIC). Wireshark tries to decode that data as best as it can. And just by chance it decodes the packets as LLC and X.25.</p><p>Please identify that device on the network (you can use the switch 'CAM table' to find the port) and then figure out what's wrong with that device.</p><p>Maybe a simple reboot fixes the problem (if it is caused by a crashed driver).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '13, 12:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jun '13, 13:20</strong> </span></p></div></div><div id="comments-container-21971" class="comments-container"><span id="21974"></span><div id="comment-21974" class="comment"><div id="post-21974-score" class="comment-score"></div><div class="comment-text"><p>thank you Kurt Knocher, you are helpful. how do I give you karma too? i already gave some to Klodovic</p></div><div id="comment-21974-info" class="comment-info"><span class="comment-age">(12 Jun '13, 12:57)</span> <span class="comment-user userinfo">billjackson</span></div></div><span id="21975"></span><div id="comment-21975" class="comment"><div id="post-21975-score" class="comment-score"></div><div class="comment-text"><p>you can't as you don't have any karma left. "giving" extra karma, means donating some of your own karma.</p><p>If you select one answer as the correct one by using the check mark (after thoroughly checking its value) you can give 25 extra karma points to the one who helped you most with the his answer. Please see the FAQ.</p></div><div id="comment-21975-info" class="comment-info"><span class="comment-age">(12 Jun '13, 13:08)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-21971" class="comment-tools"></div><div class="clear"></div><div id="comment-21971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21968"></span>

<div id="answer-container-21968" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21968-score" class="post-score" title="current number of votes">1</div><span id="post-21968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Check out source MAC address of packets to determine which device is the source of unwanted traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '13, 12:03</strong></p><img src="https://secure.gravatar.com/avatar/0817cf7965ef06a56ada1be48a4244bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="klodovic&#39;s gravatar image" /><p><span>klodovic</span><br />
<span class="score" title="42 reputation points">42</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="klodovic has no accepted answers">0%</span></p></div></div><div id="comments-container-21968" class="comments-container"><span id="21969"></span><div id="comment-21969" class="comment"><div id="post-21969-score" class="comment-score"></div><div class="comment-text"><p>the source shows ASUSTEKC_e7:0b:5e , also i have over 100 devices on site here!!</p></div><div id="comment-21969-info" class="comment-info"><span class="comment-age">(12 Jun '13, 12:16)</span> <span class="comment-user userinfo">billjackson</span></div></div><span id="21970"></span><div id="comment-21970" class="comment"><div id="post-21970-score" class="comment-score"></div><div class="comment-text"><p>trace the ASUSTEKC_e7:0b:5e MAC address on your network segment to see on which switch and on which port of that switch is the ASUSTEKC_e7:0b:5e connected</p></div><div id="comment-21970-info" class="comment-info"><span class="comment-age">(12 Jun '13, 12:35)</span> <span class="comment-user userinfo">klodovic</span></div></div></div><div id="comment-tools-21968" class="comment-tools"></div><div class="clear"></div><div id="comment-21968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

