+++
type = "question"
title = "Geting rx/tx timestamps from TP-Link 722N"
description = '''I am trying to measure distance between two computers who are connected with a wifi ad-hoc by using time of arrival to determine the distance. I am using TP-Link 722N with Atheros AR9271 chipset and ath9k_htc Driver i am trying to get rx/tx timestamps from the wlan card, is there any way to get rx/t...'''
date = "2014-08-08T06:26:00Z"
lastmod = "2014-08-11T04:12:00Z"
weight = 35329
keywords = [ "mactime", "timestamp" ]
aliases = [ "/questions/35329" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Geting rx/tx timestamps from TP-Link 722N](/questions/35329/geting-rxtx-timestamps-from-tp-link-722n)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35329-score" class="post-score" title="current number of votes">0</div><span id="post-35329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to measure distance between two computers who are connected with a wifi ad-hoc by using time of arrival to determine the distance.</p><p>I am using TP-Link 722N with Atheros AR9271 chipset and ath9k_htc Driver i am trying to get rx/tx timestamps from the wlan card, is there any way to get rx/tx timestamps to do the necessary calculations to get the distance between the computers?<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mactime" rel="tag" title="see questions tagged &#39;mactime&#39;">mactime</span> <span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '14, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/a29ccbb7adecd03fb78cd25bdb44eb1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fredrik00&#39;s gravatar image" /><p><span>Fredrik00</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fredrik00 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-35329" class="comments-container"></div><div id="comment-tools-35329" class="comment-tools"></div><div class="clear"></div><div id="comment-35329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35372"></span>

<div id="answer-container-35372" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35372-score" class="post-score" title="current number of votes">0</div><span id="post-35372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't know if the AR9271 is at all able to generate HW timestamps. Please read my answer to the following questions for similar questions:</p><blockquote><p><a href="http://ask.wireshark.org/questions/28525/wlanwifi-adapters-that-support-hardware-timestamp">http://ask.wireshark.org/questions/28525/wlanwifi-adapters-that-support-hardware-timestamp</a><br />
<a href="http://ask.wireshark.org/questions/28683/recommended-wireless-adapter-usb-with-linux-wireshark-that-reports-mactime-in-radiotap-header">http://ask.wireshark.org/questions/28683/recommended-wireless-adapter-usb-with-linux-wireshark-that-reports-mactime-in-radiotap-header</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '14, 07:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-35372" class="comments-container"><span id="35397"></span><div id="comment-35397" class="comment"><div id="post-35397-score" class="comment-score"></div><div class="comment-text"><p>With the lines you suggested in one of the other discussions <span class="__cf_email__" data-cfemail="32405d5d467259535e5b">[email protected]</span>:~# airmon-ng start wlan0 <span class="__cf_email__" data-cfemail="0674696972466d676a6f">[email protected]</span>:~# tcpdump -ni mon0 -w /tmp/k1.pcap</p><p><span class="__cf_email__" data-cfemail="f785989883b79c969b9e">[email protected]</span>:~# tshark -nr /tmp/k1.pcap -T fields -e frame.number -e radiotap.mactime</p><p>it does give me values so if I understand you correctly that should mean that the wlan card supports hardware timestamps.</p><p>-Fredrik</p></div><div id="comment-35397-info" class="comment-info"><span class="comment-age">(11 Aug '14, 04:07)</span> <span class="comment-user userinfo">Fredrik00</span></div></div><span id="35399"></span><div id="comment-35399" class="comment"><div id="post-35399-score" class="comment-score"></div><div class="comment-text"><blockquote><p>it does give me values so if I understand you correctly that should mean that the wlan card supports hardware timestamps.</p></blockquote><p>Without having seen a capture file, I'd say: I guess so...</p></div><div id="comment-35399-info" class="comment-info"><span class="comment-age">(11 Aug '14, 04:12)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-35372" class="comment-tools"></div><div class="clear"></div><div id="comment-35372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

