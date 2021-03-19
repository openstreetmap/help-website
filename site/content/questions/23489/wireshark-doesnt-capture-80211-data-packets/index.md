+++
type = "question"
title = "Wireshark doesn&#x27;t capture 802.11 data packets"
description = '''Lately I have been trying to analyze wifi traffic over my own test router. I looked on the wireshark website on how to do this and setup my own testing network. my network: -dd-wrt router with WPA2 personal mixed security using tkip+aes. -kali linux capture machine with wireshark 1.8.5 -android phon...'''
date = "2013-07-31T12:15:00Z"
lastmod = "2013-07-31T12:15:00Z"
weight = 23489
keywords = [ "wpa-psk", "802.11", "eapol", "wpa-pwd", "wpa2" ]
aliases = [ "/questions/23489" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark doesn't capture 802.11 data packets](/questions/23489/wireshark-doesnt-capture-80211-data-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23489-score" class="post-score" title="current number of votes">0</div><span id="post-23489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Lately I have been trying to analyze wifi traffic over my own test router. I looked on the wireshark website on how to do this and setup my own testing network.</p><p>my network:</p><p>-dd-wrt router with WPA2 personal mixed security using tkip+aes.</p><p>-kali linux capture machine with wireshark 1.8.5</p><p>-android phone for producing traffic</p><p>I then put the wireless interface of my kali laptop into monitor mode user airmon-ng</p><pre><code>airmon-ng start wlan0</code></pre><p>To check if the created monitor interface(mon0) worked I would use airodump-ng. When I knew that my monitor interface was working, I started up Wireshark. I selected mon0 as capture interface and pressed options. In Capture options I put the mac adress of my router, which I got through airodump-ng, in the capture filter area.</p><p>I then would take care of the packet decryption that would be needed for me to see the actual data. I went to the following webpage: <a href="http://wiki.wireshark.org/HowToDecrypt802.11">http://wiki.wireshark.org/HowToDecrypt802.11</a></p><p>I followed the instructions there.(Only the way I need to put in the decryption keys is different than the key#1 system that is described on the page. I get a new window in which I need to select a security method wep,wpa-pwd or wpa-psk and input the key). I used the wireshark wpa psk generator tool to get the right pre-shared key.</p><p><a href="http://www.wireshark.org/tools/wpa-psk.html">http://www.wireshark.org/tools/wpa-psk.html</a></p><p>Essid: "testnet"</p><p>Password: "wachtwoord"</p><p>psk: 33fe484e651381b15859e539279f2991c0f5e5e751ef17f82104d4ad528718ca</p><p>I put in 2 new keys. One being wpa-pwd with wachtwoord as its value. The second being wpa-psk with the psk mentioned above as its value.</p><p>I applied all the settings, and checked the enable decryption checkbox.</p><p>So I clicked the start capture button and saw a whole bunch of beacon frames rolling in. I associated my android phone with the AP so I knew I capture the eapol packets(I checked this using the filter and I had all 4 packets).</p><p>After filtering with "data", I saw that I didn't capture any data packets.</p><p>I then expected to see the actual traffic, but this was not the case. airdecap-ng did not see any WPA packets in the capture file.</p><p>My only theory left after hours of puzzeling is lack of driver support. Please tell me what I am doing wrong?</p><p>Thank you!</p><p>tl;dr: My computer does not capture 802.11 wpa2 data packets, and I can't figure out why.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wpa-psk" rel="tag" title="see questions tagged &#39;wpa-psk&#39;">wpa-psk</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-eapol" rel="tag" title="see questions tagged &#39;eapol&#39;">eapol</span> <span class="post-tag tag-link-wpa-pwd" rel="tag" title="see questions tagged &#39;wpa-pwd&#39;">wpa-pwd</span> <span class="post-tag tag-link-wpa2" rel="tag" title="see questions tagged &#39;wpa2&#39;">wpa2</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '13, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/b8170408363aa47915fc5cdfb1c35d19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joren485&#39;s gravatar image" /><p><span>joren485</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joren485 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Jul '13, 13:00</strong> </span></p></div></div><div id="comments-container-23489" class="comments-container"></div><div id="comment-tools-23489" class="comment-tools"></div><div class="clear"></div><div id="comment-23489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

