+++
type = "question"
title = "Wireshark capture packets from one AP"
description = '''I want to capture packets from a specific AP. How can I do that in Wireshark? I also want to get the RSSI values. I am new to wireshark, please guide me'''
date = "2013-03-20T03:25:00Z"
lastmod = "2013-04-03T02:43:00Z"
weight = 19669
keywords = [ "capture", "accesspoint", "wireshark" ]
aliases = [ "/questions/19669" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark capture packets from one AP](/questions/19669/wireshark-capture-packets-from-one-ap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19669-score" class="post-score" title="current number of votes">0</div><span id="post-19669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to capture packets from a specific AP. How can I do that in Wireshark? I also want to get the RSSI values. I am new to wireshark, please guide me</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-accesspoint" rel="tag" title="see questions tagged &#39;accesspoint&#39;">accesspoint</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '13, 03:25</strong></p><img src="https://secure.gravatar.com/avatar/71ec8bdde4d589f81811f296c2ed74b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ships&#39;s gravatar image" /><p><span>ships</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ships has no accepted answers">0%</span></p></div></div><div id="comments-container-19669" class="comments-container"></div><div id="comment-tools-19669" class="comment-tools"></div><div class="clear"></div><div id="comment-19669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19798"></span>

<div id="answer-container-19798" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19798-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19798-score" class="post-score" title="current number of votes">0</div><span id="post-19798-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might consider using 'airodump-ng' (<a href="http://www.aircrack-ng.org/doku.php?id=airodump-ng">http://www.aircrack-ng.org/doku.php?id=airodump-ng</a>) instead of wireshark for capturing wireless-traffic. First you need to know the BSSID and also the channel the WLAN is running on. First start with a simple one like this:</p><p>airodump-ng wlan0</p><p>You'll easily see the channel and the BSSID of your accesspoint. Now adjust the following cmd with the just gathered information and analyze the "ap_linksys.cap" with wireshark afterwards.</p><p>airodump-ng --bssid 00:11:22:33:44:55 -c 7 -w ap_linksys wlan0</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '13, 00:30</strong></p><img src="https://secure.gravatar.com/avatar/7141e1bec61c168ead9f00d304b75859?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pfuender&#39;s gravatar image" /><p><span>pfuender</span><br />
<span class="score" title="56 reputation points">56</span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pfuender has no accepted answers">0%</span></p></div></div><div id="comments-container-19798" class="comments-container"><span id="19981"></span><div id="comment-19981" class="comment"><div id="post-19981-score" class="comment-score"></div><div class="comment-text"><p>i want to capture wireless-traffic how to use airodump in wireshark? please guide me..........</p></div><div id="comment-19981-info" class="comment-info"><span class="comment-age">(31 Mar '13, 20:49)</span> <span class="comment-user userinfo">csycisco</span></div></div><span id="20038"></span><div id="comment-20038" class="comment"><div id="post-20038-score" class="comment-score"></div><div class="comment-text"><p>airodump is a seperate tool. As stated in the above commandline, it will output all the captured traffic in the file 'ap_linksys', which you can then can just open with wireshark and analyze.</p></div><div id="comment-20038-info" class="comment-info"><span class="comment-age">(03 Apr '13, 02:43)</span> <span class="comment-user userinfo">pfuender</span></div></div></div><div id="comment-tools-19798" class="comment-tools"></div><div class="clear"></div><div id="comment-19798-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

