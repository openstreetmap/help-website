+++
type = "question"
title = "cant capture packets in dell with broadcom wireless card?"
description = '''hi, i am using dell laptop with broadcom wireless card and i am not able to sniff using this? but i am able to get data using the ms network monitor? can anyone suggest how can i sniff from wireshark? -Ravi'''
date = "2014-10-29T03:47:00Z"
lastmod = "2014-10-29T04:48:00Z"
weight = 37427
keywords = [ "wireshark" ]
aliases = [ "/questions/37427" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [cant capture packets in dell with broadcom wireless card?](/questions/37427/cant-capture-packets-in-dell-with-broadcom-wireless-card)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37427-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37427-score" class="post-score" title="current number of votes">0</div><span id="post-37427-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, i am using dell laptop with broadcom wireless card and i am not able to sniff using this? but i am able to get data using the ms network monitor? can anyone suggest how can i sniff from wireshark?</p><p>-Ravi</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '14, 03:47</strong></p><img src="https://secure.gravatar.com/avatar/75101185e65422ba91a93262397adede?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nukalaraji&#39;s gravatar image" /><p><span>nukalaraji</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nukalaraji has no accepted answers">0%</span></p></div></div><div id="comments-container-37427" class="comments-container"></div><div id="comment-tools-37427" class="comment-tools"></div><div class="clear"></div><div id="comment-37427-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37429"></span>

<div id="answer-container-37429" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37429-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37429-score" class="post-score" title="current number of votes">0</div><span id="post-37429-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>WinPcap (the capture library of Wireshark on Windows) does not support <strong>monitor mode</strong> on Windows.</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/WLAN#Turning_on_monitor_mode">http://wiki.wireshark.org/CaptureSetup/WLAN#Turning_on_monitor_mode</a></p></blockquote><p>So, you can only capture your own wireless traffic. However, some wireless drivers don't support <strong>promiscuous mode</strong> either. In that case you won't be able to capture on that interface at all.</p><p>Sometimes, it's much easier to capture wireless traffic on Linux. So, you could try to run the laptop with Linux (Kali Linux).</p><blockquote><p><a href="http://www.kali.org/">http://www.kali.org/</a></p></blockquote><p>See also here:</p><blockquote><p><a href="https://ask.wireshark.org/questions/26347/unable-to-capture-wireless-traffic-on-monitor-mode-on-ubuntu-1004-version">https://ask.wireshark.org/questions/26347/unable-to-capture-wireless-traffic-on-monitor-mode-on-ubuntu-1004-version</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '14, 04:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37429" class="comments-container"></div><div id="comment-tools-37429" class="comment-tools"></div><div class="clear"></div><div id="comment-37429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

