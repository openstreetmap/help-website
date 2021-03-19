+++
type = "question"
title = "Capture my wireless (iPhone &amp; iPad) traffic"
description = '''I&#x27;m new to Wireshark, and packet capture, so please excuse my ignorance. I&#x27;ve installed Wireshark on my iMac, which is connected to an Apple Time Capsule/Airport via both ethernet and 802.11n (WPA/WPA2). I also connect my iPhone and iPad to the same Airport. What I&#x27;d like to like to do is capture al...'''
date = "2011-02-08T17:19:00Z"
lastmod = "2012-12-24T02:32:00Z"
weight = 2242
keywords = [ "ipad", "airport", "wpa2", "iphone" ]
aliases = [ "/questions/2242" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Capture my wireless (iPhone & iPad) traffic](/questions/2242/capture-my-wireless-iphone-ipad-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2242-score" class="post-score" title="current number of votes">0</div><span id="post-2242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new to Wireshark, and packet capture, so please excuse my ignorance.</p><p>I've installed Wireshark on my iMac, which is connected to an Apple Time Capsule/Airport via both ethernet and 802.11n (WPA/WPA2). I also connect my iPhone and iPad to the same Airport. What I'd like to like to do is capture all traffic from either or both of these devices. I have the IP and MAC addresses for each device, but am not sure how to create a filter to capture them.</p><p>I've poked around in the wiki, user docs, and this discussion board, but haven't been able to find much that can help me. Any suggestions?</p><p>Thanks, in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ipad" rel="tag" title="see questions tagged &#39;ipad&#39;">ipad</span> <span class="post-tag tag-link-airport" rel="tag" title="see questions tagged &#39;airport&#39;">airport</span> <span class="post-tag tag-link-wpa2" rel="tag" title="see questions tagged &#39;wpa2&#39;">wpa2</span> <span class="post-tag tag-link-iphone" rel="tag" title="see questions tagged &#39;iphone&#39;">iphone</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '11, 17:19</strong></p><img src="https://secure.gravatar.com/avatar/5326690b5a9d9bfa88b6ec1950a50bf4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kappabear&#39;s gravatar image" /><p><span>kappabear</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kappabear has no accepted answers">0%</span></p></div></div><div id="comments-container-2242" class="comments-container"><span id="3024"></span><div id="comment-3024" class="comment"><div id="post-3024-score" class="comment-score"></div><div class="comment-text"><p>Was there ever a resolution to this? I tried an article from - http://www.cardinalpeak.com/blog/?p=519 but it didn't work. Once I setup the computer-to-computer network, I couldn't see any interfaces to capture in Wireshark.</p></div><div id="comment-3024-info" class="comment-info"><span class="comment-age">(22 Mar '11, 07:35)</span> <span class="comment-user userinfo">dekstrom</span></div></div></div><div id="comment-tools-2242" class="comment-tools"></div><div class="clear"></div><div id="comment-2242-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="2243"></span>

<div id="answer-container-2243" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2243-score" class="post-score" title="current number of votes">0</div><span id="post-2243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I found an article online, and followed the instructions below.</p><blockquote><p>Start Wireshark, ignore the dialog boxes (there should be one informing you about a potentially long startup time, and one about missing stuff while loading MIBs). Open the Capture menu, and select Intefaces. Identify your WiFi interface (en1), click the Options button, change the Link-layer header type to IEEE 802.11 plus radiotap WLAN header, and enable Promiscuous mode.</p></blockquote><p>However, I still wasn't able to capture any traffic from my iPhone. All I see is my router broadcasting it's SSID names.</p><p>Any suggestions? I'm trying to do this, as I'd like to know which off the apps I use, send in ClearText.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '11, 18:34</strong></p><img src="https://secure.gravatar.com/avatar/5326690b5a9d9bfa88b6ec1950a50bf4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kappabear&#39;s gravatar image" /><p><span>kappabear</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kappabear has no accepted answers">0%</span></p></div></div><div id="comments-container-2243" class="comments-container"></div><div id="comment-tools-2243" class="comment-tools"></div><div class="clear"></div><div id="comment-2243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17202"></span>

<div id="answer-container-17202" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17202-score" class="post-score" title="current number of votes">0</div><span id="post-17202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use <a href="http://www.iwaxx.com/debookee">Debookee</a>, a Mac OS X application which can intercept the traffic of any device on your network.</p><ul><li>Scan your network and discover your iPhone and iPad</li><li>Select your iPhone and iPad as Targets</li><li>Their traffic is now intercepted, you'll see all protocols used and URLs visited: HTTP, HTTPS, TCP, SIP etc, ...</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '12, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/02d240cf8c02781ff4689a9002a320dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David5774&#39;s gravatar image" /><p><span class="suspended-user">David5774</span><br />
(suspended)<br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David5774 has no accepted answers">0%</span></p></div></div><div id="comments-container-17202" class="comments-container"><span id="17207"></span><div id="comment-17207" class="comment"><div id="post-17207-score" class="comment-score"></div><div class="comment-text"><p>How is a Mac OS X product <strong>related to iPhone/iPad</strong>?? Can you please stop spamming the site with your numerous advertisements for your product?</p><p>Thank you!</p><p>Regards<br />
Kurt</p></div><div id="comment-17207-info" class="comment-info"><span class="comment-age">(23 Dec '12, 13:47)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17212"></span><div id="comment-17212" class="comment"><div id="post-17212-score" class="comment-score"></div><div class="comment-text"><p>Well, I guess it is kinda related since it claims to be able to capture any traffic on the network. My guess is that it is basically just an ARP spoofing/capturing tool like Cain&amp;Abel does for Windows - but wait, this one costs money, C&amp;A doesn't ;-)</p><p>Still, <span>@David5774</span>, you should stop spamming the site with advertisements to commercial tools or someone might get angry...</p></div><div id="comment-17212-info" class="comment-info"><span class="comment-age">(23 Dec '12, 18:07)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-17202" class="comment-tools"></div><div class="clear"></div><div id="comment-17202-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17227"></span>

<div id="answer-container-17227" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17227-score" class="post-score" title="current number of votes">0</div><span id="post-17227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If your iPhone/iPod touch/iPad is running iOS 5 or later, you could set up a <a href="http://developer.apple.com/library/mac/#qa/qa1176/_index.html#//apple_ref/doc/uid/DTS10001707-CH1-SECRVI">remote virtual interface</a> and capture IP traffic to or from the iPhone/iPod touch/iPad.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Dec '12, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></p></div></div><div id="comments-container-17227" class="comments-container"></div><div id="comment-tools-17227" class="comment-tools"></div><div class="clear"></div><div id="comment-17227-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

