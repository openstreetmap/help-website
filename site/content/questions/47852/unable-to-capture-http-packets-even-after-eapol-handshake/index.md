+++
type = "question"
title = "Unable to capture HTTP packets even after EAPOL handshake"
description = '''Hi there. I&#x27;m still new to wireshark and trying to learn capture packets on my home network protected by WPA2. Based on my understanding, in order to capture HTTP packets from other devices in my WPA2 network, I need to:  Enable monitor mode. Supply my wpa-pwd/wpa-psk key to wireshark reconnect my d...'''
date = "2015-11-22T19:09:00Z"
lastmod = "2015-11-29T17:49:00Z"
weight = 47852
keywords = [ "decryption", "http", "wpa2" ]
aliases = [ "/questions/47852" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to capture HTTP packets even after EAPOL handshake](/questions/47852/unable-to-capture-http-packets-even-after-eapol-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47852-score" class="post-score" title="current number of votes">0</div><span id="post-47852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there. I'm still new to wireshark and trying to learn capture packets on my home network protected by WPA2.</p><p>Based on my understanding, in order to capture HTTP packets from other devices in my WPA2 network, I need to:</p><ol><li>Enable monitor mode.</li><li>Supply my wpa-pwd/wpa-psk key to wireshark</li><li>reconnect my devices to the network</li><li>Ensure that 4-way EAPOL handshake is captured.</li><li>Browse a site on my other device to generate a HTTP request.</li></ol><p>However it seems that even though after EAPOL handshake is captured, I am unable to capture http packets. It seems to be a hit and miss: sometimes I capture HTTP packets, sometimes I don't capture any HTTP packets at all. Other times I would capture HTTP packets up to a point before it stop capturing any further for god knows what reason.</p><p>Can someone guide me on this? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-wpa2" rel="tag" title="see questions tagged &#39;wpa2&#39;">wpa2</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '15, 19:09</strong></p><img src="https://secure.gravatar.com/avatar/2900025f5298a755ecd393e8fcb3f921?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="davidsmith2&#39;s gravatar image" /><p><span>davidsmith2</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="davidsmith2 has no accepted answers">0%</span></p></div></div><div id="comments-container-47852" class="comments-container"><span id="47857"></span><div id="comment-47857" class="comment"><div id="post-47857-score" class="comment-score"></div><div class="comment-text"><p>maybe your client/AP changed the wifi channel and your capturing system did not? What is your capturing OS?</p></div><div id="comment-47857-info" class="comment-info"><span class="comment-age">(23 Nov '15, 01:02)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="47914"></span><div id="comment-47914" class="comment"><div id="post-47914-score" class="comment-score"></div><div class="comment-text"><p>I'm using kali linux (dual boot on a Macbook Pro 13" 2010 model). My router's wifi channel is manually set to a specific channel rather than automated though!</p></div><div id="comment-47914-info" class="comment-info"><span class="comment-age">(24 Nov '15, 02:16)</span> <span class="comment-user userinfo">davidsmith2</span></div></div><span id="47933"></span><div id="comment-47933" class="comment"><div id="post-47933-score" class="comment-score">1</div><div class="comment-text"><p>Hi David - I have experienced many issues (including missing packets during a capture) when using a dual boot computer. I am assuming you have both Mac-OS and Kali Linux as the dual boot options. I know this might not be much help, but after beating my head against the wall for months I decided to not use a dual boot computer. I was able to find a dedicated laptop and installed Ubuntu. Since then I have no issue.</p><p>I am not sure if you have that option, but you might want to check some forums regarding dual boot systems - especially ones using Kali and Mac-OS on the same hardware.</p></div><div id="comment-47933-info" class="comment-info"><span class="comment-age">(24 Nov '15, 10:09)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="48042"></span><div id="comment-48042" class="comment"><div id="post-48042-score" class="comment-score"></div><div class="comment-text"><p>Hi Amanto. You're right, I tried wireshark on a different computer and it seems to work fine. Not sure if it's a hardware issue. My Macbook Pro is using a b43 driver</p></div><div id="comment-48042-info" class="comment-info"><span class="comment-age">(28 Nov '15, 01:53)</span> <span class="comment-user userinfo">davidsmith2</span></div></div><span id="48043"></span><div id="comment-48043" class="comment"><div id="post-48043-score" class="comment-score"></div><div class="comment-text"><p>Update: I've bought myself a TP-LINK TL-WN722N and tried it with wireshark on my Macbook Pro. I swear the difference is HUGE, and now I'm able to capture all the HTTP packets. So I'm guessing the Macbook Pro's in-built wifi adapter isn't that great for monitoring?</p></div><div id="comment-48043-info" class="comment-info"><span class="comment-age">(28 Nov '15, 08:02)</span> <span class="comment-user userinfo">davidsmith2</span></div></div></div><div id="comment-tools-47852" class="comment-tools"></div><div class="clear"></div><div id="comment-47852-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48064"></span>

<div id="answer-container-48064" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48064-score" class="post-score" title="current number of votes">0</div><span id="post-48064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Converting my comment to an answer to assist others with a similar issue.</p><p>I have experienced many issues (including missing packets during a capture) when using a dual boot computer. I am assuming you have both Mac-OS and Kali Linux as the dual boot options. I know this might not be much help, but after beating my head against the wall for months I decided to not use a dual boot computer. I was able to find a dedicated laptop and installed Ubuntu. Since then I have no issue.</p><p>I am not sure if you have that option, but you might want to check some forums regarding dual boot systems - especially ones using Kali and Mac-OS on the same hardware</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '15, 17:49</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-48064" class="comments-container"></div><div id="comment-tools-48064" class="comment-tools"></div><div class="clear"></div><div id="comment-48064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

