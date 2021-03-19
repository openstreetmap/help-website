+++
type = "question"
title = "No data packets when turning on monitor mode"
description = '''Hi all, I&#x27;m a novice in Wireshark. I apologize if this question is silly. The problem is that when I turn on the wifi monitor mode and choose an appropriate channel, Wireshark can catch 802.11 management packets such as beacon, probe_request, but it can&#x27;t catch any user data packets such as the tcp ...'''
date = "2012-10-03T11:30:00Z"
lastmod = "2015-06-11T08:16:00Z"
weight = 14684
keywords = [ "user", "wifi", "packets", "monitor", "mode" ]
aliases = [ "/questions/14684" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [No data packets when turning on monitor mode](/questions/14684/no-data-packets-when-turning-on-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14684-score" class="post-score" title="current number of votes">0</div><span id="post-14684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm a novice in Wireshark. I apologize if this question is silly. The problem is that when I turn on the wifi monitor mode and choose an appropriate channel, Wireshark can catch 802.11 management packets such as beacon, probe_request, but it can't catch any user data packets such as the tcp packets. After I turn the wifi back to managed mode and connect to an AP, I can catch user data packets again. Is this the way I should expect Wireshark to behave? Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-user" rel="tag" title="see questions tagged &#39;user&#39;">user</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span> <span class="post-tag tag-link-mode" rel="tag" title="see questions tagged &#39;mode&#39;">mode</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '12, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/fdc6c35f907417f7e677808151d7f5be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="caesarxuchao&#39;s gravatar image" /><p><span>caesarxuchao</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="caesarxuchao has no accepted answers">0%</span></p></div></div><div id="comments-container-14684" class="comments-container"><span id="15429"></span><div id="comment-15429" class="comment"><div id="post-15429-score" class="comment-score"></div><div class="comment-text"><p>Hi</p><p>is there any news about this topic because i have the same problem</p><p>thanks</p></div><div id="comment-15429-info" class="comment-info"><span class="comment-age">(31 Oct '12, 11:56)</span> <span class="comment-user userinfo">Noury</span></div></div><span id="15430"></span><div id="comment-15430" class="comment"><div id="post-15430-score" class="comment-score"></div><div class="comment-text"><blockquote><p>is there any news about this topic because i have the same problem</p></blockquote><p>Are you on a WEP, WPA, or WPA2 network? If so, see my answer.</p></div><div id="comment-15430-info" class="comment-info"><span class="comment-age">(31 Oct '12, 11:58)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-14684" class="comment-tools"></div><div class="clear"></div><div id="comment-14684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="14693"></span>

<div id="answer-container-14693" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14693-score" class="post-score" title="current number of votes">2</div><span id="post-14693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="caesarxuchao has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On what operating system are you running Wireshark, and what type of 802.11 adapter do you have?</p><p>And are you seeing no data frames at all, or are the data frames just showing up as "Data" or "QoS Data" or..., without being dissected as, for example, TCP? If they're just showing up as "Data" and the like, the problem is that the networks you're listening to are "protected", i.e. using WEP or WPA, and you'd have to <a href="http://wiki.wireshark.org/HowToDecrypt802.11">follow these instructions for decrypting packets on protected 802.11 networks</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '12, 19:10</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-14693" class="comments-container"><span id="14696"></span><div id="comment-14696" class="comment"><div id="post-14696-score" class="comment-score"></div><div class="comment-text"><p>Thank you Guy Harris! This solves the problem. I shouldn't expect Wireshark to decipher the wpa2 key automatically :)</p><p>P.S. For people who are going to do the same thing, be sure to notice this sentence in the webpage Guy Harris pointed: "WPA and WPA2 use keys derived from an EAPOL handshake to encrypt traffic. Unless all four handshake packets are present for the session you're trying to decrypt, Wireshark won't be able to decrypt the traffic. You can use the display filter eapol to locate EAPOL packets in your capture."</p></div><div id="comment-14696-info" class="comment-info"><span class="comment-age">(03 Oct '12, 20:13)</span> <span class="comment-user userinfo">caesarxuchao</span></div></div></div><div id="comment-tools-14693" class="comment-tools"></div><div class="clear"></div><div id="comment-14693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14685"></span>

<div id="answer-container-14685" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14685-score" class="post-score" title="current number of votes">0</div><span id="post-14685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>unfortunately this can occur on some OS's and with some wireless cards. See the <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">WLAN Capture</a> page on the Wiki for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '12, 11:40</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-14685" class="comments-container"><span id="14687"></span><div id="comment-14687" class="comment"><div id="post-14687-score" class="comment-score"></div><div class="comment-text"><p>Thanks. But the page only says some wireless cards cannot turn on monitor mode and thus not capable of capturing non-data packets. My specific problem is on the contrary, that I can capture non-data packet but not data packets.</p></div><div id="comment-14687-info" class="comment-info"><span class="comment-age">(03 Oct '12, 11:58)</span> <span class="comment-user userinfo">caesarxuchao</span></div></div></div><div id="comment-tools-14685" class="comment-tools"></div><div class="clear"></div><div id="comment-14685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16054"></span>

<div id="answer-container-16054" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16054-score" class="post-score" title="current number of votes">0</div><span id="post-16054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello, Can you check the box "Capture packets in monitor mode" in Capture Options or do you have an error message ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '12, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/c2b51a0252510b9f47fde6df2f9e7bb1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chuinul&#39;s gravatar image" /><p><span>chuinul</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chuinul has no accepted answers">0%</span></p></div></div><div id="comments-container-16054" class="comments-container"></div><div id="comment-tools-16054" class="comment-tools"></div><div class="clear"></div><div id="comment-16054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43082"></span>

<div id="answer-container-43082" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43082-score" class="post-score" title="current number of votes">0</div><span id="post-43082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I've found that you can miss data packets due to feature mismatch between the capture hardware and the sending hardware and associated AP.</p><p>The problem I ran into was trying capture 802.11n HT mode packets on a non-HT capable device - so it was seeing the management traffic but when data packets were sent in HT mode they weren't being seen. My solution was disable HT mode on the AP. Alternatively one could obtain a more advanced WiFi card/dongle for the capture machine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '15, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/244c3e907ae3f16a00a6c18ea331b36b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pierz&#39;s gravatar image" /><p><span>pierz</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pierz has no accepted answers">0%</span></p></div></div><div id="comments-container-43082" class="comments-container"></div><div id="comment-tools-43082" class="comment-tools"></div><div class="clear"></div><div id="comment-43082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

