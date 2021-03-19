+++
type = "question"
title = "Why isn&#x27;t Wireshark decrypting 802.11 traffic in my capture, even if the EAPOL handshake is present?"
description = '''I have read and followed Wireshark&#x27;s guide, and successfully decrypted the example file, but when it comes to my file it doesn&#x27;t work. I have made sure that both the SSID and the password are correctly spelled in the settings. The entire EAPOL handshake is present, so I don&#x27;t understand what I&#x27;m doi...'''
date = "2017-04-21T07:55:00Z"
lastmod = "2017-04-22T04:30:00Z"
weight = 60947
keywords = [ "encryption", "eapol", "wifi", "wpa", "decryption" ]
aliases = [ "/questions/60947" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why isn't Wireshark decrypting 802.11 traffic in my capture, even if the EAPOL handshake is present?](/questions/60947/why-isnt-wireshark-decrypting-80211-traffic-in-my-capture-even-if-the-eapol-handshake-is-present)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60947-score" class="post-score" title="current number of votes">0</div><span id="post-60947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have read and followed Wireshark's <a href="https://wiki.wireshark.org/HowToDecrypt802.11">guide</a>, and successfully decrypted the example file, but when it comes to my file it doesn't work. I have made sure that both the SSID and the password are correctly spelled in the settings. The entire EAPOL handshake is present, so I don't understand what I'm doing wrong.</p><p>Here is a screenshot of the handshake:</p><p><a href="https://i.stack.imgur.com/WJnnH.png"><img src="https://i.stack.imgur.com/WJnnH.png" alt="enter image description here" /></a></p><p>Maybe the problem is that there more than 4 packets?</p><p>Here is the <a href="https://drive.google.com/open?id=0B_FVGdqvgb2PUFd5c3dRU0dpTGM">pcap file</a>, in case it helps. The password for the AP is "privacyblibwifi".</p><p>Does anyone know how to solve this problem? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-encryption" rel="tag" title="see questions tagged &#39;encryption&#39;">encryption</span> <span class="post-tag tag-link-eapol" rel="tag" title="see questions tagged &#39;eapol&#39;">eapol</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-wpa" rel="tag" title="see questions tagged &#39;wpa&#39;">wpa</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '17, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/d558cf05b6d572a77a868f3c4a394b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="workin221&#39;s gravatar image" /><p><span>workin221</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="workin221 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-60947" class="comments-container"></div><div id="comment-tools-60947" class="comment-tools"></div><div class="clear"></div><div id="comment-60947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60951"></span>

<div id="answer-container-60951" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60951-score" class="post-score" title="current number of votes">1</div><span id="post-60951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It has worked for me with your trace: But I had to toggle the marked combo from "Wireshark" to "None" and back to "Wireshark". <img src="https://osqa-ask.wireshark.org/upfiles/21-04-_2017_22-24-22_Xxin8Tu.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/21-04-_2017_22-23-45.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '17, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></img></div></div><div id="comments-container-60951" class="comments-container"><span id="60965"></span><div id="comment-60965" class="comment"><div id="post-60965-score" class="comment-score"></div><div class="comment-text"><p>Sounds like a bug to me, is it?</p></div><div id="comment-60965-info" class="comment-info"><span class="comment-age">(22 Apr '17, 03:41)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="60968"></span><div id="comment-60968" class="comment"><div id="post-60968-score" class="comment-score"></div><div class="comment-text"><p>Not sure, for me it has always been a works as designed feature.</p></div><div id="comment-60968-info" class="comment-info"><span class="comment-age">(22 Apr '17, 04:30)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-60951" class="comment-tools"></div><div class="clear"></div><div id="comment-60951-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

