+++
type = "question"
title = "My log won&#x27;t decrypt!. WPA2-PSK. Have all 4 EAPOL packets, know SSID and passphrase. Tried entering as wpa-psk and wpa-pwd"
description = '''I have a log file from a WPA2-PSK network but Wireshark is not decrypting it for me despite entering the decrypting info as wpa-psk or wpa-pwd. I can see all four EAPOL packets in the log and also know the passphrase and SSID. What am I missing?'''
date = "2013-08-21T14:55:00Z"
lastmod = "2015-03-31T06:38:00Z"
weight = 23934
keywords = [ "wpa-psk", "decryption", "wpa2", "passphrase" ]
aliases = [ "/questions/23934" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [My log won't decrypt!. WPA2-PSK. Have all 4 EAPOL packets, know SSID and passphrase. Tried entering as wpa-psk and wpa-pwd](/questions/23934/my-log-wont-decrypt-wpa2-psk-have-all-4-eapol-packets-know-ssid-and-passphrase-tried-entering-as-wpa-psk-and-wpa-pwd)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23934-score" class="post-score" title="current number of votes">0</div><span id="post-23934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a log file from a WPA2-PSK network but Wireshark is not decrypting it for me despite entering the decrypting info as wpa-psk or wpa-pwd. I can see all four EAPOL packets in the log and also know the passphrase and SSID. What am I missing?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wpa-psk" rel="tag" title="see questions tagged &#39;wpa-psk&#39;">wpa-psk</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-wpa2" rel="tag" title="see questions tagged &#39;wpa2&#39;">wpa2</span> <span class="post-tag tag-link-passphrase" rel="tag" title="see questions tagged &#39;passphrase&#39;">passphrase</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '13, 14:55</strong></p><img src="https://secure.gravatar.com/avatar/871c45207376f007abc028e94d203eb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cloud9ine&#39;s gravatar image" /><p><span>cloud9ine</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cloud9ine has no accepted answers">0%</span></p></div></div><div id="comments-container-23934" class="comments-container"></div><div id="comment-tools-23934" class="comment-tools"></div><div class="clear"></div><div id="comment-23934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25085"></span>

<div id="answer-container-25085" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25085-score" class="post-score" title="current number of votes">0</div><span id="post-25085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Which version of Wireshark were you using? Have you tried <a href="http://www.wireshark.org/download.html">the most recent release</a>, (currently 1.10.2), which may have fixed this problem (assuming it was a Wireshark problem)?</p><p>Or, if you're running on a platform for which the <a href="http://buildbot.wireshark.org/trunk/waterfall">buildbots</a> generate installers, then you could try a recent <a href="http://www.wireshark.org/download/automated/">automated build</a>, which would have the most up-to-date fixes/enhancements - and yes, sometimes new bugs too - but which might fix the problem for you as well. (If you're on a platform for which no automated installer exists, then you could try to either build from the automated sources or <a href="http://www.wireshark.org/develop.html">directly from the repository</a>.)</p><p>If all else fails, please <a href="https://bugs.wireshark.org/bugzilla/">file a bug report</a> and attach a capture file so someone can take a look at it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '13, 18:12</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-25085" class="comments-container"></div><div id="comment-tools-25085" class="comment-tools"></div><div class="clear"></div><div id="comment-25085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41050"></span>

<div id="answer-container-41050" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41050-score" class="post-score" title="current number of votes">0</div><span id="post-41050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In case anybody else runs into this same problem. If you accidentally captured <strong>multiple EAPOL handshakes</strong> then decryption will only work for the MAC ID associated with the first EAPOL. This seems like a bit of a bug to me, but it's easy enough to work around once you know about it.</p><p>Unfortunately marking the unwanted EAPOL (from other devices) as deleted isn't enough, they must not appear in the capture at all. What I did was create a filter for the MAC address e.g.</p><pre><code>wlan.ta == 28:18:78:97:00:00 || wlan.ra == 28:18:78:97:00:00 || wlan.da == 28:18:78:97:00:00</code></pre><p>then:</p><pre><code>Edit -&gt; Mark All Displayed</code></pre><p>followed by:</p><pre><code>File -&gt; Export Specified Packets</code></pre><p>Select the "Marked packets only" radio box and save the file. Open the file you just saved, and the problem will be resolved.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '15, 03:40</strong></p><img src="https://secure.gravatar.com/avatar/2fa633c466363d5ae365a4aa98125bae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Benjamin%20Dobell&#39;s gravatar image" /><p><span>Benjamin Dobell</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Benjamin Dobell has no accepted answers">0%</span></p></div></div><div id="comments-container-41050" class="comments-container"><span id="41056"></span><div id="comment-41056" class="comment"><div id="post-41056-score" class="comment-score"></div><div class="comment-text"><p>How is this a Wireshark problem? Maybe I am not understanding the issue. From my understanding, you have captured traffic from multiple STA's trying to connect to an AP. These STA's successfully connect to the AP and you captured the EAP exchange. However, you are only interested in viewing traffic from a particular STA. If that is the case, you can configure a capture filter BEFORE starting the Wireshark capture. For example: ether host 00:00:00:00:00:01 where 00:00:00:00:00:01 = the MAC address of the STA you want to capture If I did not understand the problem correctly, please provide more details.</p></div><div id="comment-41056-info" class="comment-info"><span class="comment-age">(31 Mar '15, 06:13)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="41057"></span><div id="comment-41057" class="comment"><div id="post-41057-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@Amato_C</span> You're making some assumptions there. You're assuming the capture was made in Wireshark, or by some other tool that supports capture-time filtering. However, aside from that, what if someone actually wants to view traffic from an entire wireless network that uses encryption? It's simply not possible using one Wireshark session because Wireshark can't handle the situation where there are multiple devices using encryption (it only works for the first one). Given the EAPOL exchange occurs for a particular MAC address, there is no technical reason why Wireshark can't decrypt all packets for which it has the EAPOL exchange.</p></div><div id="comment-41057-info" class="comment-info"><span class="comment-age">(31 Mar '15, 06:18)</span> <span class="comment-user userinfo">Benjamin Dobell</span></div></div><span id="41058"></span><div id="comment-41058" class="comment"><div id="post-41058-score" class="comment-score"></div><div class="comment-text"><p><span>@Benjamin Dobell</span> - I am confused. Your answer creates a display filter that removes all the unwanted traffic besides the desired STA/AP. BTW, a simpler filter would be: wlan.addr == 28:18:78:97:00:00 My answer creates a capture filter that does the same thing. The difference = with capture filters, you cannot get the discarded packets back. I experienced the same issue and created bug #9313. In this case, a new EAPOL exchange occurs between the STA and AP. After the new EAP exchange the packets are decrypted.</p></div><div id="comment-41058-info" class="comment-info"><span class="comment-age">(31 Mar '15, 06:38)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-41050" class="comment-tools"></div><div class="clear"></div><div id="comment-41050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

