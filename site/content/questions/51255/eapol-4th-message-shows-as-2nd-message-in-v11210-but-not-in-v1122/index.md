+++
type = "question"
title = "EAPOL 4th message shows as 2nd message in v1.12.10, but not in v1.12.2"
description = '''hi, I captured a wireless transaction of WPA2-PSK, in which 4way handshake of EAPOL packets happened. I saved the capture and analysing in 2 different versions of wireshark. In the image attachedalt text, packet # 119 is the 4th message of EAPOL handshake. In v1.12.2, it shows the &#x27;message 4 of 4&#x27;. ...'''
date = "2016-03-29T05:54:00Z"
lastmod = "2016-04-02T07:26:00Z"
weight = 51255
keywords = [ "wpa2-psk", "aes", "eapol" ]
aliases = [ "/questions/51255" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [EAPOL 4th message shows as 2nd message in v1.12.10, but not in v1.12.2](/questions/51255/eapol-4th-message-shows-as-2nd-message-in-v11210-but-not-in-v1122)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51255-score" class="post-score" title="current number of votes">0</div><span id="post-51255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi,</p><p>I captured a wireless transaction of WPA2-PSK, in which 4way handshake of EAPOL packets happened. I saved the capture and analysing in 2 different versions of wireshark. In the image attached<a href="https://osqa-ask.wireshark.org/upfiles/eapol_4.jpg">alt text</a>, packet # 119 is the 4th message of EAPOL handshake.</p><p>In v1.12.2, it shows the 'message 4 of 4'. Same capture file when I opened in v1.12.10, it shows 'message 2 of 4'. Please tell which one is correct.</p><p>Thanks in advance. --uv.!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wpa2-psk" rel="tag" title="see questions tagged &#39;wpa2-psk&#39;">wpa2-psk</span> <span class="post-tag tag-link-aes" rel="tag" title="see questions tagged &#39;aes&#39;">aes</span> <span class="post-tag tag-link-eapol" rel="tag" title="see questions tagged &#39;eapol&#39;">eapol</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '16, 05:54</strong></p><img src="https://secure.gravatar.com/avatar/0441251303531abacc96f7d47c57b927?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ubuntuv&#39;s gravatar image" /><p><span>ubuntuv</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ubuntuv has no accepted answers">0%</span></p></div></div><div id="comments-container-51255" class="comments-container"></div><div id="comment-tools-51255" class="comment-tools"></div><div class="clear"></div><div id="comment-51255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51263"></span>

<div id="answer-container-51263" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51263-score" class="post-score" title="current number of votes">1</div><span id="post-51263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From the screenshot that you provided, it appears that Wireshark v1.12.2 is showing the correct information. It would be best to view the entire capture file to confirm (or at least the Association Request, Association Response and the EAPOL 4-way handshake frames).</p><p>I am making this assumption based on the IEEE specification, sections 11.6.6.3 and 11.6.6.5 which define the value for the WPA Key Nonce as following:</p><ul><li>Message #2, Key Nonce = SNonce (Supplicant Nonce)</li><li>Message #4, Key Nonce = 0</li></ul><p>As your screenshot shows, the Key Nonce is a non-zero value indicating a Message 2. However, there are other parameters that can be used to verify (e.g., Replay Counter).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '16, 11:31</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-51263" class="comments-container"><span id="51371"></span><div id="comment-51371" class="comment"><div id="post-51371-score" class="comment-score"></div><div class="comment-text"><p>Ok. Can someone confirm if this is a bug in wireshark. I need this for my work. Thanks in advance.</p><p>--uv.</p></div><div id="comment-51371-info" class="comment-info"><span class="comment-age">(02 Apr '16, 06:56)</span> <span class="comment-user userinfo">ubuntuv</span></div></div><span id="51372"></span><div id="comment-51372" class="comment"><div id="post-51372-score" class="comment-score"></div><div class="comment-text"><p>It is hard to get a better than the one that Amato gave you. But please read this bug report <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11994">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11994</a></p></div><div id="comment-51372-info" class="comment-info"><span class="comment-age">(02 Apr '16, 07:26)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-51263" class="comment-tools"></div><div class="clear"></div><div id="comment-51263-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

