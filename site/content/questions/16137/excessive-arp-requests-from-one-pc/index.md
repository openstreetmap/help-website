+++
type = "question"
title = "Excessive ARP requests from one PC"
description = '''I am fairly new at this so any extra information that may help me learn is appreciated. My laptop (which Wireshark is running on) seems to be sending a lot of ARP requests. It seems to be starting at 10.0.0.1 and runs all the way through to 10.0.0.255, asking about each ip multiple times. After it f...'''
date = "2012-11-20T16:13:00Z"
lastmod = "2012-11-22T04:23:00Z"
weight = 16137
keywords = [ "arp", "snmp", "excessive", "newbie" ]
aliases = [ "/questions/16137" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Excessive ARP requests from one PC](/questions/16137/excessive-arp-requests-from-one-pc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16137-score" class="post-score" title="current number of votes">0</div><span id="post-16137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am fairly new at this so any extra information that may help me learn is appreciated.</p><p>My laptop (which Wireshark is running on) seems to be sending a lot of ARP requests. It seems to be starting at 10.0.0.1 and runs all the way through to 10.0.0.255, asking about each ip multiple times. After it finishes it will stop for something like 15 seconds before starting over again. Statistics from the sample captured show 88 ARP packets in ten seconds.</p><p>I was also curious about the SNMP requests. Principally I can't think of anything that would be using that destination address, and I never see any response traffic.<br />
</p><p>\</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Untitled_5.png" alt="alt text" /></p><p>Again, any information at all would be helpful. Thank you much.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span> <span class="post-tag tag-link-snmp" rel="tag" title="see questions tagged &#39;snmp&#39;">snmp</span> <span class="post-tag tag-link-excessive" rel="tag" title="see questions tagged &#39;excessive&#39;">excessive</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '12, 16:13</strong></p><img src="https://secure.gravatar.com/avatar/55b52063c44b8c08c150c822f87c2812?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kineteks&#39;s gravatar image" /><p><span>kineteks</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kineteks has no accepted answers">0%</span> </br></p></img></div></div><div id="comments-container-16137" class="comments-container"></div><div id="comment-tools-16137" class="comment-tools"></div><div class="clear"></div><div id="comment-16137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16144"></span>

<div id="answer-container-16144" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16144-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16144-score" class="post-score" title="current number of votes">3</div><span id="post-16144-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This <a href="http://oid-info.com/get/1.3.6.1.2.1.25.3.5.1.1">OID</a> tells me you've got a crappy printer manager running, causing all this traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '12, 23:26</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-16144" class="comments-container"><span id="16188"></span><div id="comment-16188" class="comment"><div id="post-16188-score" class="comment-score"></div><div class="comment-text"><p>Thank you! Ended up removing all printers from Printers and Devices. No more SNMP traffic, and I learned a bit about OID's. Now if even has any ideas about the ARP traffic...</p></div><div id="comment-16188-info" class="comment-info"><span class="comment-age">(21 Nov '12, 21:26)</span> <span class="comment-user userinfo">kineteks</span></div></div><span id="16202"></span><div id="comment-16202" class="comment"><div id="post-16202-score" class="comment-score"></div><div class="comment-text"><p>Printer usually come with a CD with crappy printer manager software. If you installed it, it may still be scanning your network to find printers.</p></div><div id="comment-16202-info" class="comment-info"><span class="comment-age">(22 Nov '12, 04:23)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-16144" class="comment-tools"></div><div class="clear"></div><div id="comment-16144-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

