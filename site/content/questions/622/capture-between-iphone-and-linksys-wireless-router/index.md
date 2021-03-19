+++
type = "question"
title = "Capture between iPhone and Linksys wireless router??"
description = '''I want to monitor wireless traffic that occurs between an iphone and my home linksys wireless router. The only computer I have at home is my windows laptop, so I would be loading wireshark on that? Can I really &quot;see&quot; what the person is looking at on the iphone? I have watched the videos on the websi...'''
date = "2010-10-25T08:30:00Z"
lastmod = "2010-10-25T19:11:00Z"
weight = 622
keywords = [ "linksys", "iphone" ]
aliases = [ "/questions/622" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture between iPhone and Linksys wireless router??](/questions/622/capture-between-iphone-and-linksys-wireless-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-622-score" class="post-score" title="current number of votes">0</div><span id="post-622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to monitor wireless traffic that occurs between an iphone and my home linksys wireless router. The only computer I have at home is my windows laptop, so I would be loading wireshark on that?</p><p>Can I really "see" what the person is looking at on the iphone? I have watched the videos on the website but I am a bit confused. I specifically need to track websites, and email log ins.</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-linksys" rel="tag" title="see questions tagged &#39;linksys&#39;">linksys</span> <span class="post-tag tag-link-iphone" rel="tag" title="see questions tagged &#39;iphone&#39;">iphone</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '10, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/efca4d8667e981e40801272ea104b02a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BobtheBuilder&#39;s gravatar image" /><p><span>BobtheBuilder</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BobtheBuilder has no accepted answers">0%</span></p></div></div><div id="comments-container-622" class="comments-container"></div><div id="comment-tools-622" class="comment-tools"></div><div class="clear"></div><div id="comment-622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="623"></span>

<div id="answer-container-623" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-623-score" class="post-score" title="current number of votes">1</div><span id="post-623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need an adapter that can go into both promiscuous mode and monitor mode to be able to listen in on another device's wireless traffic.</p><p>I also work on a Windows host, but I use an AirPcap adapter (www.cacetech.com) which can go into monitor mode. There's a video over at www.wiresharkbook.com/coffee showing adapter tests.</p><p>If your WLAN adapter can't go into monitor mode then you will only see your own WLAN traffic and the 802.11 header will be replaced with an Ethernet header - doesn't do you much good.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '10, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-623" class="comments-container"><span id="644"></span><div id="comment-644" class="comment"><div id="post-644-score" class="comment-score"></div><div class="comment-text"><p>"If your WLAN adapter can't go into monitor mode" mainly means "if your OS, or the driver for your adapter, or *pcap, doesn't support putting the WLAN adapter into monitor mode", although some adapters might not support that in hardware. On Windows, you'll need an AirPcap adapter - WinPcap doesn't support monitor mode.</p><p>Note also that if the network uses WEP or WPA, you'll have to tell Wireshark what the password is for the network (and, in the case of WPA, you'll have to capture the initial EAPOL setup - try turning the iPhone off, starting the capture, and turning it back on again).</p></div><div id="comment-644-info" class="comment-info"><span class="comment-age">(25 Oct '10, 19:11)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-623" class="comment-tools"></div><div class="clear"></div><div id="comment-623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

