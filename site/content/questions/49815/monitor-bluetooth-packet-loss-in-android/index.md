+++
type = "question"
title = "Monitor Bluetooth packet loss in android"
description = '''Hallo all, I am currently involed in a project to detect the % of packet loss in Bluetooth transfer between two android devices. I am able to take HCI packet Snoop Log file from one of the android device. Can i use wireshark to detect the packet loss between the two devices when it communicates via ...'''
date = "2016-02-04T05:38:00Z"
lastmod = "2016-02-10T03:38:00Z"
weight = 49815
keywords = [ "android", "bluetooth", "wireshark", "packetloss" ]
aliases = [ "/questions/49815" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Monitor Bluetooth packet loss in android](/questions/49815/monitor-bluetooth-packet-loss-in-android)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49815-score" class="post-score" title="current number of votes">0</div><span id="post-49815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hallo all,</p><p>I am currently involed in a project to detect the % of packet loss in Bluetooth transfer between two android devices.</p><p>I am able to take HCI packet Snoop Log file from one of the android device.</p><p>Can i use wireshark to detect the packet loss between the two devices when it communicates via bluetooth?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-bluetooth" rel="tag" title="see questions tagged &#39;bluetooth&#39;">bluetooth</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-packetloss" rel="tag" title="see questions tagged &#39;packetloss&#39;">packetloss</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '16, 05:38</strong></p><img src="https://secure.gravatar.com/avatar/a0406967306a1200ed402afde64882fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harishdv&#39;s gravatar image" /><p><span>harishdv</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harishdv has no accepted answers">0%</span></p></div></div><div id="comments-container-49815" class="comments-container"></div><div id="comment-tools-49815" class="comment-tools"></div><div class="clear"></div><div id="comment-49815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50046"></span>

<div id="answer-container-50046" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50046-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50046-score" class="post-score" title="current number of votes">0</div><span id="post-50046-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Detecting packets loss is hard using Android Bluetooth Btsnoop log. There is no any helper in Wireshark.</p><p>However... If you have two logs, then you can compare them manually, one by one packet (enough for most cases [non-baseband/linklayer]).</p><p>If you have only one log (from Android device), then you can only base on your knowledge and specification - flows, etc. In most cases if one packet loss somewhere you can see it, because you know flow. But in some flows you cannot detect packet loss, like SCO or A2DP media stream, but in this case Wireshark has mechanism to compute how many music was send/receiver and how long you sending/receiving, so you can suspect if there are breaks in the stream (please note there is no high precision, because timestamp from system are not perfect, etc.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '16, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/6eabf35b1168a8242bb2d69db18a8a7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Micha%C5%82%20%C5%81ab%C4%99dzki&#39;s gravatar image" /><p><span>Michał Łabędzki</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michał Łabędzki has one accepted answer">8%</span></p></div></div><div id="comments-container-50046" class="comments-container"></div><div id="comment-tools-50046" class="comment-tools"></div><div class="clear"></div><div id="comment-50046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

