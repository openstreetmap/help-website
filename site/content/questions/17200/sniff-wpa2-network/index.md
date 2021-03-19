+++
type = "question"
title = "sniff wpa2 network"
description = '''I need to sniff HTTP traffic on WPA2 network at home.  I am running wireshark 1.8.2 on debian linux. I have TPLink TL-WN722N usb wireless adaptor on this machine. I have put this adaptor in monitor mode and also specified WPA2 password in preferences. I captured packets on mon0 interface. It does no...'''
date = "2012-12-23T12:48:00Z"
lastmod = "2012-12-24T08:06:00Z"
weight = 17200
keywords = [ "wpa2", "sniff" ]
aliases = [ "/questions/17200" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [sniff wpa2 network](/questions/17200/sniff-wpa2-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17200-score" class="post-score" title="current number of votes">1</div><span id="post-17200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to sniff HTTP traffic on WPA2 network at home. I am running wireshark 1.8.2 on debian linux. I have TPLink TL-WN722N usb wireless adaptor on this machine. I have put this adaptor in monitor mode and also specified WPA2 password in preferences. I captured packets on mon0 interface. It does not show any HTTP packets. I am not sure whether it was able to decrypt packets successfully. The protocol column in wireshark shows mostly 802.11. How can I get it to capture and show HTTP packets?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wpa2" rel="tag" title="see questions tagged &#39;wpa2&#39;">wpa2</span> <span class="post-tag tag-link-sniff" rel="tag" title="see questions tagged &#39;sniff&#39;">sniff</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Dec '12, 12:48</strong></p><img src="https://secure.gravatar.com/avatar/ecafc4c9453ccfdfe2ab446605e72c53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nash_rack1&#39;s gravatar image" /><p><span>nash_rack1</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nash_rack1 has no accepted answers">0%</span></p></div></div><div id="comments-container-17200" class="comments-container"></div><div id="comment-tools-17200" class="comment-tools"></div><div class="clear"></div><div id="comment-17200-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17208"></span>

<div id="answer-container-17208" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17208-score" class="post-score" title="current number of votes">1</div><span id="post-17208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nash_rack1 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With WPA2, the client negotiates a new key each time it connects to the access point. The WPA2 password is only used to securely establish the session key. For WPA2 decryption to work in wireshark, you will need to capture the 4 authentication packets at the beginning of the connection to the AP.</p><p>So, disconnect from the SSID, start capturing packets in wireshark, connect to the SSID and you should be able to see the IP (decrypted) traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '12, 13:54</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17208" class="comments-container"><span id="17233"></span><div id="comment-17233" class="comment"><div id="post-17233-score" class="comment-score"></div><div class="comment-text"><p>Your suggestion worked great. Now I can see decrypted traffic. Thanks a lot!</p></div><div id="comment-17233-info" class="comment-info"><span class="comment-age">(24 Dec '12, 07:11)</span> <span class="comment-user userinfo">nash_rack1</span></div></div><span id="17234"></span><div id="comment-17234" class="comment"><div id="post-17234-score" class="comment-score"></div><div class="comment-text"><p><span>@nash_rack1</span> If an answer solves your problem, please accept it by clicking the checkmark icon by the answer for the benefit of other users who may have the same question.</p></div><div id="comment-17234-info" class="comment-info"><span class="comment-age">(24 Dec '12, 08:06)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-17208" class="comment-tools"></div><div class="clear"></div><div id="comment-17208-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

