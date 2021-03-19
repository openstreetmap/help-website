+++
type = "question"
title = "Can&#x27;t decrypt ieee 802.11 hexdump"
description = '''I capture in my own network some traffic (as a hexdump) with a wireless antenna set in monitor mode. Now i want to decrypt this traffic (all protocols are just 802.11 instead of TCP, ARP, etc). I followed this guide: https://wiki.wireshark.org/HowToDecrypt802.11 But thats not work. I know the passwo...'''
date = "2017-07-21T23:14:00Z"
lastmod = "2017-07-27T03:29:00Z"
weight = 62999
keywords = [ "decryption" ]
aliases = [ "/questions/62999" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can't decrypt ieee 802.11 hexdump](/questions/62999/cant-decrypt-ieee-80211-hexdump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62999-score" class="post-score" title="current number of votes">0</div><span id="post-62999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I capture in my own network some traffic (as a hexdump) with a wireless antenna set in monitor mode. Now i want to decrypt this traffic (all protocols are just 802.11 instead of TCP, ARP, etc). I followed this guide: <a href="https://wiki.wireshark.org/HowToDecrypt802.11">https://wiki.wireshark.org/HowToDecrypt802.11</a></p><p>But thats not work. I know the password and the ssid, because its my own network. I selected wpa-psk and typed: mypassword:ssid (for example 123456789:my-network). Its also a valid syntax. But when i press OK, nothing happens, it's still encrypted.</p><p>The windows l(in the guide) ooks a bit different as mine: I have to select first the key type (wep, wpa-pwd and wpa-psk) and on the right side is a column "key". In this column i have password:ssid.</p><p>I use the newest wireshark version 2.4.0. in windows and 2.2.7. in linux.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '17, 23:14</strong></p><img src="https://secure.gravatar.com/avatar/053722853a0d66b9b999b6b4511c9f59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="decrypter&#39;s gravatar image" /><p><span>decrypter</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="decrypter has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jul '17, 23:34</strong> </span></p></div></div><div id="comments-container-62999" class="comments-container"></div><div id="comment-tools-62999" class="comment-tools"></div><div class="clear"></div><div id="comment-62999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="63012"></span>

<div id="answer-container-63012" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63012-score" class="post-score" title="current number of votes">0</div><span id="post-63012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It could be as simple as 'reloading' the trace after you enter the passphrase/SSID or as complex as needing a whole new set of hardware for proper capture.</p><p>I suggest you review other answers, such as here: <a href="https://ask.wireshark.org/questions/62901/wireshark-not-decrypting-wpa-psk-packets-recieving-only-80211-protocols">https://ask.wireshark.org/questions/62901/wireshark-not-decrypting-wpa-psk-packets-recieving-only-80211-protocols</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '17, 09:04</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-63012" class="comments-container"><span id="63166"></span><div id="comment-63166" class="comment"><div id="post-63166-score" class="comment-score"></div><div class="comment-text"><p>Yes, you need the 4-way eapol handshake as well. That information, plus the SSID and passphrase, allows Wireshark to calculate the PTK and GTK, which are used to actually encrypt/decrypt data.</p><p>So you need data to decrypt, the 4-way handshake, and the SSID/Passphrase. Don't forget to practice on the sample file for decryption at the wiki - if that doesn't work, trying your own will be just that much harder.</p></div><div id="comment-63166-info" class="comment-info"><span class="comment-age">(27 Jul '17, 02:52)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="63169"></span><div id="comment-63169" class="comment"><div id="post-63169-score" class="comment-score"></div><div class="comment-text"><p>The sample file works fine. Ok in this case i will deauth some client from my network to get the eapol handshake in my capture file. Thanks!</p></div><div id="comment-63169-info" class="comment-info"><span class="comment-age">(27 Jul '17, 03:29)</span> <span class="comment-user userinfo">decrypter</span></div></div></div><div id="comment-tools-63012" class="comment-tools"></div><div class="clear"></div><div id="comment-63012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="63014"></span>

<div id="answer-container-63014" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63014-score" class="post-score" title="current number of votes">0</div><span id="post-63014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks. So i need to capture the handshake as well? That would explain my issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '17, 11:27</strong></p><img src="https://secure.gravatar.com/avatar/053722853a0d66b9b999b6b4511c9f59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="decrypter&#39;s gravatar image" /><p><span>decrypter</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="decrypter has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Jul '17, 11:41</strong> </span></p></div></div><div id="comments-container-63014" class="comments-container"></div><div id="comment-tools-63014" class="comment-tools"></div><div class="clear"></div><div id="comment-63014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

