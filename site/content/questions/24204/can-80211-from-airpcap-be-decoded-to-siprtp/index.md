+++
type = "question"
title = "Can 802.11 from AirPcap Be Decoded To SIP/RTP?"
description = '''Testing mobile apps which make phone calls using wifi connection, encountered a problem with audio quality and excessive delay on certain phones. Captured traffic between mobile phone and wifi router using AirPcap, but can not find a way to Decode As SIP/RTP. All packets shown as 802.11 protocol nat...'''
date = "2013-08-30T09:35:00Z"
lastmod = "2013-09-04T15:29:00Z"
weight = 24204
keywords = [ "sip", "802.11", "rtp" ]
aliases = [ "/questions/24204" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can 802.11 from AirPcap Be Decoded To SIP/RTP?](/questions/24204/can-80211-from-airpcap-be-decoded-to-siprtp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24204-score" class="post-score" title="current number of votes">0</div><span id="post-24204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Testing mobile apps which make phone calls using wifi connection, encountered a problem with audio quality and excessive delay on certain phones. Captured traffic between mobile phone and wifi router using AirPcap, but can not find a way to Decode As SIP/RTP. All packets shown as 802.11 protocol naturally.</p><p>Is there a way to decode the wifi packets into the SIP and RTP used for the VoIP call?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '13, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/f79f7a1a3ae3d1a2cf23a74f3756c7ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BobD8487&#39;s gravatar image" /><p><span>BobD8487</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BobD8487 has no accepted answers">0%</span></p></div></div><div id="comments-container-24204" class="comments-container"></div><div id="comment-tools-24204" class="comment-tools"></div><div class="clear"></div><div id="comment-24204-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24212"></span>

<div id="answer-container-24212" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24212-score" class="post-score" title="current number of votes">0</div><span id="post-24212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a way to decode the wifi packets into the SIP and RTP used for the VoIP call?</p></blockquote><p>Yes, but if they were captured on a "protected" network, using WEP or WPA/WPA2 encryption, you will have to <a href="http://wiki.wireshark.org/HowToDecrypt802.11">decrypt them</a>.</p><p>It's also possible configure AirPcap adapters to do the decryption for you when capturing; see the "Adding Keys: Wireless Toolbar" of the page I linked to. That won't handle an <em>existing</em> capture, however, it will only handle captures you make <em>after</em> you add the passwords.</p><p>Also, pay attention to the "Gotchas" section.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '13, 13:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-24212" class="comments-container"><span id="24216"></span><div id="comment-24216" class="comment"><div id="post-24216-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Guy. But you are such a tease. :-) You tell me "Yes" then do not tell me how it would be done. The AirPcap only does WEP so I would have to handle the WPA2 decryption within Wireshark <em>except</em> that I temporarily disabled my encryption to take the trace, so there is nothing to decrypt...except the 802.11 packets. I need to see SIP, and most importantly, RTP. If you can embelish on your "Yes" answer to tell me how this is done, I would very much appreciate it.<br />
</p><p>btw - I would have expected to be able to use the Wireshark Analyze&gt;Decode As option, however this option is grayed out.</p></div><div id="comment-24216-info" class="comment-info"><span class="comment-age">(30 Aug '13, 16:38)</span> <span class="comment-user userinfo">BobD8487</span></div></div><span id="24219"></span><div id="comment-24219" class="comment"><div id="post-24219-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I need to see SIP, and most importantly, RTP.</p></blockquote><p>If you're not seeing IP and TCP/UDP headers for the traffic you believe to be SIP and/or RTP, then your traffic is probably encrypted at the 802.11 layer, whether you believe you disabled that decryption or not (i.e., you didn't).</p><p>If you're seeing IP and TCP/UDP headers, you should be able to use Decode As to decode the packets as SIP and/or RTP.</p></div><div id="comment-24219-info" class="comment-info"><span class="comment-age">(30 Aug '13, 21:00)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="24359"></span><div id="comment-24359" class="comment"><div id="post-24359-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Guy. That must be it. I turned off the WPA2 encryption, but there must be something else turned on which is encrypting the data. I'll have a look through my router settings and see if there is something I missed. I will also go through the decryption section of this wiki to see if it mentions another layer I may have missed. Worst case I turn it back on, then decrypt in Wireshark (which is what I was trying to avoid thinking it was simpler...which was obviously not the case).</p></div><div id="comment-24359-info" class="comment-info"><span class="comment-age">(04 Sep '13, 15:29)</span> <span class="comment-user userinfo">BobD8487</span></div></div></div><div id="comment-tools-24212" class="comment-tools"></div><div class="clear"></div><div id="comment-24212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

