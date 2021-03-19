+++
type = "question"
title = "Why can&#x27;t I capture Source or Destination IP addresses, only MAC ID&#x27;s?"
description = '''I am using an older USB AirPcap dongle to sniff WiFi signals. In Wireshark I can capture Source and Destination MAC ID&#x27;s but when I edit the column to capture/display IP source or destination port, the capture continues but the column I edited is blank. I want to be able to filter and search for IP ...'''
date = "2016-01-31T15:54:00Z"
lastmod = "2016-02-01T02:52:00Z"
weight = 49665
keywords = [ "ipport" ]
aliases = [ "/questions/49665" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Why can't I capture Source or Destination IP addresses, only MAC ID's?](/questions/49665/why-cant-i-capture-source-or-destination-ip-addresses-only-mac-ids)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49665-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using an older USB AirPcap dongle to sniff WiFi signals. In Wireshark I can capture Source and Destination MAC ID's but when I edit the column to capture/display IP source or destination port, the capture continues but the column I edited is blank. I want to be able to filter and search for IP addresses.</p></div><div id="question-tags" class="tags-container tags">ipport</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '16, 15:54</strong></p><img src="https://secure.gravatar.com/avatar/1e149675cdc5b54f9a9da72b7621f67d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Miguel1234&#39;s gravatar image" /><p>Miguel1234<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Miguel1234 has no accepted answers">0%</span></p></div></div><div id="comments-container-49665" class="comments-container"></div><div id="comment-tools-49665" class="comment-tools"></div><div class="clear"></div><div id="comment-49665-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="49675"></span>

<div id="answer-container-49675" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49675-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The MAC address is used by both 801.11 and Ethernet protocol. From your screenshots it is clear that you can see the MAC addresses at 802.11 level. If the WLAN you capture uses encryption, then <em>everything</em> in the frames above the 802.11 level is encrypted, i.e. including the IP addresses. So if it does use encryption, search through this site for "wireless decryption", "802.11 decryption", "WPA decryption", "EAPOL" etc. to find out what you have to do to get access to the payload.</p><p>And specifically for your case, as you use multi-SSID mode, you have to tell Wireshark the SSID and passphrase for all SSIDs whose traffic you wish to decrypt.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '16, 23:00</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-49675" class="comments-container"><span id="49749"></span><div id="comment-49749" class="comment"><div id="post-49749-score" class="comment-score"></div><div class="comment-text"><p>Just wanted to thank you for the response. I checked the EAPOL section you recommended and realized I was missing the initial packets when connecting to the network. That solved the problem. Thanks!</p></div><div id="comment-49749-info" class="comment-info"><span class="comment-age">(02 Feb '16, 15:42)</span> Miguel1234</div></div></div><div id="comment-tools-49675" class="comment-tools"></div><div class="clear"></div><div id="comment-49675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49667"></span>

<div id="answer-container-49667" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49667-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Miguel, I think your problem lies in the router. The fact that you can't see IP addresses in your wireshark capture, but can see MAC addresses, tells me that (1) your switch is working but (2) your router isn't. Make sure you are connected to the internet, and then try the wireshark capture again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '16, 16:29</strong></p><img src="https://secure.gravatar.com/avatar/d9a151081bbdcf69cccfb940f82816ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DanielChen&#39;s gravatar image" /><p>DanielChen<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DanielChen has no accepted answers">0%</span></p></div></div><div id="comments-container-49667" class="comments-container"><span id="49668"></span><div id="comment-49668" class="comment"><div id="post-49668-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_4h1pKXS.PNG" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture2.PNG" alt="alt text" /></p></div><div id="comment-49668-info" class="comment-info"><span class="comment-age">(31 Jan '16, 17:30)</span> Miguel1234</div></div><span id="49669"></span><div id="comment-49669" class="comment"><div id="post-49669-score" class="comment-score"></div><div class="comment-text"><p>Hi Miguel, If you look and see the text above the pictures you took, I think you'll see the words "Wireless controls are not supported in this version of Wireshark." Is it possible that you could update to a newer version of Wireshark that would still allow you to use AirPCAP while also letting you see internet traffic?</p></div><div id="comment-49669-info" class="comment-info"><span class="comment-age">(31 Jan '16, 17:39)</span> DanielChen</div></div><span id="49670"></span><div id="comment-49670" class="comment"><div id="post-49670-score" class="comment-score"></div><div class="comment-text"><p>That is why I made sure I included that text in my response. I wasn't sure if that was the problem. I just downloaded Wireshark today but will look again. thx.</p></div><div id="comment-49670-info" class="comment-info"><span class="comment-age">(31 Jan '16, 17:46)</span> Miguel1234</div></div></div><div id="comment-tools-49667" class="comment-tools"></div><div class="clear"></div><div id="comment-49667-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49677"></span>

<div id="answer-container-49677" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49677-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The packets in the screenshot are 802.11 management frames; those are not IP packets and do not <em>have</em> IP addresses.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '16, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></img></div></div><div id="comments-container-49677" class="comments-container"></div><div id="comment-tools-49677" class="comment-tools"></div><div class="clear"></div><div id="comment-49677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

