+++
type = "question"
title = "Cannot capture 802.11 data frames"
description = '''Hello! I&#x27;m a noob student who studying networking. I want to eavesdrop every packets in my network, but I cannot capture 802.11 data frames... I have total 4 devices -- 2 Macbook Airs, iMac, Desktop with Ubuntu 16.04. Every Mac has bcm43xx network adapter and Desktop has ath93xx network adapter. I t...'''
date = "2017-03-19T09:49:00Z"
lastmod = "2017-03-20T23:31:00Z"
weight = 60179
keywords = [ "mac", "802.11", "frame", "monitor-mode", "ubuntu" ]
aliases = [ "/questions/60179" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot capture 802.11 data frames](/questions/60179/cannot-capture-80211-data-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60179-score" class="post-score" title="current number of votes">0</div><span id="post-60179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! I'm a noob student who studying networking.</p><p>I want to eavesdrop every packets in my network, but I cannot capture 802.11 data frames...</p><p>I have total 4 devices -- 2 Macbook Airs, iMac, Desktop with Ubuntu 16.04. Every Mac has bcm43xx network adapter and Desktop has ath93xx network adapter.</p><p>I tried to capture every 802.11 frames in the air with using monitor mode, but I failed. Then, I turned every security stuff off and tried but it also failed too!</p><p>iMac and one-Macbook can capture 802.11 QoS Data frames but another Macbook and Ubuntu machine <strong>capture only CTS-RTS frames.</strong></p><p>I want to know why my Ubuntu machine cannot capture any 802.11 data frames. And, as I wrote above, I have 3 Mac with same network adapter but just one Macbook cannot capture any data frames.</p><p>Summary : I have 4 devices :</p><ul><li>Macbook #1 --&gt; can capture 802.11 data frames -</li><li>Macbook #2 --&gt; cannot capture 802.11 data frames</li><li>iMac --&gt; can capture 802.11 data frames</li><li>Desktop (Ubuntu 16.04) --&gt; cannot capture 802.11 data frames</li></ul></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-frame" rel="tag" title="see questions tagged &#39;frame&#39;">frame</span> <span class="post-tag tag-link-monitor-mode" rel="tag" title="see questions tagged &#39;monitor-mode&#39;">monitor-mode</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '17, 09:49</strong></p><img src="https://secure.gravatar.com/avatar/9c79dd2f8ef7fd4dc31511b1ef505e21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jayheo&#39;s gravatar image" /><p><span>jayheo</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jayheo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Mar '17, 09:49</strong> </span></p></div></div><div id="comments-container-60179" class="comments-container"><span id="60181"></span><div id="comment-60181" class="comment"><div id="post-60181-score" class="comment-score"></div><div class="comment-text"><p>Have you searched this site for the many related questions and answers to the same or similar topic?<br />
</p><p>Here is a good link:</p><p><a href="https://wiki.wireshark.org/CaptureSetup/WLAN">https://wiki.wireshark.org/CaptureSetup/WLAN</a></p></div><div id="comment-60181-info" class="comment-info"><span class="comment-age">(19 Mar '17, 12:04)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="60183"></span><div id="comment-60183" class="comment"><div id="post-60183-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply.</p><p>I've read the document already and seen several article about this undetected unicast data packet problem. For instances, downgrading WiFi version from ac to n, disabling network encryption(WPA2), and using aircrack-ng suite. But nothing worked for me.</p><p>Additionally, I have a question about my Macbook. I'm using two identical Macbook devices running vanilla Wireshark. But only one Macbook can capture unicast data packets and another Macbook can only capture RTS/CTS frame which are sent broadcast...</p><p>What I should do to capture unicast frames?</p></div><div id="comment-60183-info" class="comment-info"><span class="comment-age">(19 Mar '17, 21:47)</span> <span class="comment-user userinfo">jayheo</span></div></div><span id="60197"></span><div id="comment-60197" class="comment"><div id="post-60197-score" class="comment-score"></div><div class="comment-text"><p><span>@jayheo</span> = can you configure your WiFi network to "legacy" mode, in which 11n is also disabled (that would be 11a only for 5GHz and 11b/g for 2.4GHz)?</p><p>There are still some parameters within 11n that could lead to certain WiFi adapters not being able to decode WiFi data traffic.</p></div><div id="comment-60197-info" class="comment-info"><span class="comment-age">(20 Mar '17, 06:50)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-60179" class="comment-tools"></div><div class="clear"></div><div id="comment-60179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60211"></span>

<div id="answer-container-60211" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60211-score" class="post-score" title="current number of votes">0</div><span id="post-60211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For the difference between the Mac's... compare the WiFi driver versions on those two machines.</p><p>For Ubuntu, ensure you have the proper WiFi interface setup and detectable in WireShark.</p><p>Cheers,</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '17, 23:31</strong></p><img src="https://secure.gravatar.com/avatar/6c8f0de8cb4ef9ad7093eefe24030e4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbenton&#39;s gravatar image" /><p><span>wbenton</span><br />
<span class="score" title="29 reputation points">29</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbenton has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-60211" class="comments-container"></div><div id="comment-tools-60211" class="comment-tools"></div><div class="clear"></div><div id="comment-60211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

