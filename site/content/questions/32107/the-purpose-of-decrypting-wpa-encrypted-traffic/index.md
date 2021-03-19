+++
type = "question"
title = "The purpose of &quot;decrypting&quot; WPA-encrypted traffic"
description = '''Hi all, PROLOGUE: please kindly have a look at http://wiki.wireshark.org/HowToDecrypt802.11 coupled with http://www.wireshark.org/tools/wpa-psk.html MY ISSUE: Wireshark is known to be able to decrypt a WPA-encrypted traffic once you provide the PSK (which is built from the SSID and WPA network key)....'''
date = "2014-04-23T08:20:00Z"
lastmod = "2014-04-23T11:34:00Z"
weight = 32107
keywords = [ "decrypt", "wpa", "wireshark" ]
aliases = [ "/questions/32107" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [The purpose of "decrypting" WPA-encrypted traffic](/questions/32107/the-purpose-of-decrypting-wpa-encrypted-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32107-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>PROLOGUE: please kindly have a look at <a href="http://wiki.wireshark.org/HowToDecrypt802.11">http://wiki.wireshark.org/HowToDecrypt802.11</a> coupled with <a href="http://www.wireshark.org/tools/wpa-psk.html">http://www.wireshark.org/tools/wpa-psk.html</a></p><p>MY ISSUE: Wireshark is known to be able to decrypt a WPA-encrypted traffic once you provide the PSK (which is built from the SSID and WPA network key). In other words you have to first know the WPA key of an encrypted network so as to monitor its WPA-encrypted traffic. HENCE...where is the utility of Wireshark in such a scenario? I would like to be able to get the WPA password of a network and this seems not to be possible with Wireshark.</p><p>I'm doing my experiments AFTER handshaking occurred (i.e. beyond the very first connection between the router and PC) and it is impossible (as it is correctly stated by Wireshark manuals) to get the EAPOL strings. Since this is the common scenario...how would it ever be possible to get the WPA password with Wireshark? Hem...do I terribly miss anything?</p><p>Three hot kisses for any useful answer.</p></div><div id="question-tags" class="tags-container tags">decrypt wpa wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '14, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/4db892036453b3c4255c791dae151181?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reginaldo%20Occhiolini&#39;s gravatar image" /><p>Reginaldo Oc...<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reginaldo Occhiolini has no accepted answers">0%</span></p></div></div><div id="comments-container-32107" class="comments-container"></div><div id="comment-tools-32107" class="comment-tools"></div><div class="clear"></div><div id="comment-32107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32111"></span>

<div id="answer-container-32111" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32111-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>HENCE...where is the utility of Wireshark in such a scenario?</p></blockquote><p>To troubleshoot connection issues within encrypted wifi/wlan communication, like a mobile device being unable to access a web page via an encrypted wifi connection. How would you troubleshoot that, without decrypting the wifi traffic? That's what the wifi decryption feature of Wireshark is typically used for. And for that purpose you need to know the WPA passphrase.</p><blockquote><p>I would like to be able to get the WPA password of a network and this seems not to be possible with Wireshark.</p></blockquote><p>You can't get the secret key just by listening to wifi traffic with Wireshark. Thare are tools that are able to <strong>brute force/crack</strong> the key by listening to the EAPOL frames, but that's a totally different story. Please google: 'WEP cracking' or 'WPA cracking'</p><blockquote><p>how would it ever be possible to get the WPA password with Wireshark?</p></blockquote><p>You won't!</p><blockquote><p>Hem...do I terribly miss anything?</p></blockquote><p>Yes. See my explanation above.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '14, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Apr '14, 15:54</p></div></div><div id="comments-container-32111" class="comments-container"></div><div id="comment-tools-32111" class="comment-tools"></div><div class="clear"></div><div id="comment-32111-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

