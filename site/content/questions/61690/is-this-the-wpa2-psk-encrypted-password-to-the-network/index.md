+++
type = "question"
title = "Is this the WPA2-PSK encrypted password to the network?"
description = '''I have a URL http://imgur.com/a/0RmjL to an album with 6 pics in it. The album is called &quot;myhandshake&quot;, and the pics are captioned and listed from top to bottom as:  The screenshot of an initial WPA2-PSK handshake - This is a screenshot of the WPA2-PSK handshake of me authenticating with my network&#x27;...'''
date = "2017-05-29T23:34:00Z"
lastmod = "2017-05-30T03:16:00Z"
weight = 61690
keywords = [ "eapol" ]
aliases = [ "/questions/61690" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is this the WPA2-PSK encrypted password to the network?](/questions/61690/is-this-the-wpa2-psk-encrypted-password-to-the-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61690-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a URL <a href="http://imgur.com/a/0RmjL">http://imgur.com/a/0RmjL</a> to an album with 6 pics in it. The album is called "myhandshake", and the pics are captioned and listed from top to bottom as:</p><ol><li>The screenshot of an initial WPA2-PSK handshake - This is a screenshot of the WPA2-PSK handshake of me authenticating with my network's router to gain access to the wifi network.</li><li>packet1 - pretty self explanatory.</li><li>packet2 - pretty self explanatory.</li><li>packet3 - pretty self explanatory.</li><li>packet4 - pretty self explanatory.</li><li>Diagram of a WPA2-PSKA handshake - This is the diagram that I used as desktop wallpaper so that I could memorize the basic steps in the WPA2-PSK handshake.</li></ol><p>Eventually, I want to be able to associate each of those steps with what I'm looking at when going over handshake data in Wireshark.</p><p>My question revolves around the 4th pic, captioned "packet3". Looking in Wireshark's middle pane, at the highlighted line at the bottom of that pane, is that "WPA Key Data: 12bfb55a99d08b44136c7fbf84075cebbec1d67fbf6b1f22..." entry the encrypted password for the wifi network?</p><p>It appears that it's only partial, because its length is noted to be 56, and the entry also ends in "...", which I take to mean that there's more data that goes on the end of it. If I really need to get the whole thing, I guess I could go into Wireshark's bottom pane and get the entire thing from the Hex dump that's there.</p><p>If that is not the encrypted password, then which entry should I be looking at to see it? - Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">eapol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '17, 23:34</strong></p><img src="https://secure.gravatar.com/avatar/84329f95c80e854a31aeee2a61880b99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Airsniffer&#39;s gravatar image" /><p>Airsniffer<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Airsniffer has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 May '17, 02:41</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-61690" class="comments-container"></div><div id="comment-tools-61690" class="comment-tools"></div><div class="clear"></div><div id="comment-61690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61693"></span>

<div id="answer-container-61693" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61693-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The passphrase, encrypted or otherwise, is never sent over the network with WPA2. The PTK (pairwise transient key used to encrypt unicast data between AP and station) is never sent over the link either. There is no field to check for the keys you need as they are derived from the Passphrase and the Nonce values (random data included by each host in the authentication process). If you use Wireshark to decrypt, it will show you the PMK (fixed once the SSID and passphrase are known) and PTK/GTK in use (the 4-way handshake combined with the PMK will provide the actual keys use to encrypt data, the PTK &amp; GTK).</p><p>For the detail you request, see 802.11-2012 specification (available free), generally section 11 for security, and specifically for section 11.6 for keys and key distribution. This will have the definition of what is in each eapol message.</p><p>Key 3 of 4 is defined by: 11.6.6.4 4-Way Handshake Message 3 and the field you have a question about:</p><pre><code>Key Data = For PTK generation, the AP’s Beacon/Probe Response frame’s RSNE, and, optionally, a
second RSNE that is the Authenticator’s pairwise cipher suite assignment, and, if a group
cipher has been negotiated, the encapsulated GTK and the GTK’s key identifier (see 11.6.2),
and if management frame protection is negotiated, the IGTK KDE.  &lt;cut for brevity&gt;</code></pre><p>Basically, this field is the RSN information element that one would see in a Beacon or Probe Response frame and some other items like group key information. Per 802.11, this field is to be checked. Table 11-6—KDE shows the various fields that could be included.</p><p>Wireshark, in conjunction with wpa_supplicant on Linux in debug mode, can be very useful in digging into the details as the encrypted and unencrypted bytes can be analyzed with a lot of control over what is occurring.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '17, 03:16</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-61693" class="comments-container"></div><div id="comment-tools-61693" class="comment-tools"></div><div class="clear"></div><div id="comment-61693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

