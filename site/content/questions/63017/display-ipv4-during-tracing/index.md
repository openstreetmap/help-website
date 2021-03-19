+++
type = "question"
title = "Display IPV4 during tracing"
description = '''Hallo  I have a problem I can not switch the display from the source address from a Mac format to a IPV4 Format, I have taken a picture. I would be very glad If somebody can help me. Thanks Götz '''
date = "2017-07-23T12:10:00Z"
lastmod = "2017-07-23T12:48:00Z"
weight = 63017
keywords = [ "ipv4" ]
aliases = [ "/questions/63017" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Display IPV4 during tracing](/questions/63017/display-ipv4-during-tracing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63017-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hallo</p><p>I have a problem I can not switch the display from the source address from a Mac format to a IPV4 Format, I have taken a picture.</p><p>I would be very glad If somebody can help me.</p><p>Thanks</p><p>Götz <img src="https://osqa-ask.wireshark.org/upfiles/Bildschirmfoto_2017-07-23_um_21.10.01.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">ipv4</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jul '17, 12:10</strong></p><img src="https://secure.gravatar.com/avatar/27c1620987e88c1c8ee33a7c583f375f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="macosx&#39;s gravatar image" /><p>macosx<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="macosx has no accepted answers">0%</span></p></img></div></div><div id="comments-container-63017" class="comments-container"><span id="63018"></span><div id="comment-63018" class="comment"><div id="post-63018-score" class="comment-score"></div><div class="comment-text"><p>You haven't provided much information, dear Watson, but it is obvious that you use monitoring mode of your wireless interface, the WLAN you have captured is encrypted, and you haven't provided Wireshark with enough capture data (the EAPOL negotiation) or configuration (the WPA passphrase). Therefore, only MAC addresses are visible, as the rest of the frames, including the IP address part, is encrypted.</p><p>(if I'm wrong, kindly provide more information about your capture setup).</p></div><div id="comment-63018-info" class="comment-info"><span class="comment-age">(23 Jul '17, 12:24)</span> sindy</div></div><span id="63019"></span><div id="comment-63019" class="comment"><div id="post-63019-score" class="comment-score"></div><div class="comment-text"><p>You are not wrong what I have to do see more ? Or what kind of information did you need? Watson</p></div><div id="comment-63019-info" class="comment-info"><span class="comment-age">(23 Jul '17, 12:26)</span> macosx</div></div></div><div id="comment-tools-63017" class="comment-tools"></div><div class="clear"></div><div id="comment-63017-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63022"></span>

<div id="answer-container-63022" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63022-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>All the wisdom related to the task is concentrated at <a href="https://wiki.wireshark.org/HowToDecrypt802.11">this Wireshark Wiki page</a>.</p><p>Don't miss the following paragraph on that page:</p><blockquote><p>WPA and WPA2 use keys derived from an EAPOL handshake, which occurs when a machine joins a Wi-Fi network, to encrypt traffic. Unless all four handshake packets are present for the session you're trying to decrypt, Wireshark won't be able to decrypt the traffic. You can use the display filter eapol to locate EAPOL packets in your capture.</p></blockquote><p>To ensure the presence of EAPOL packets in the capture, you have to log off and back on that WLAN on every single client whose traffic you want to decrypt (switch WiFi off and on, or log on to another SSID and back to this one, or go to sleep mode of the device and than back again, ...)</p><p>Plus be aware that if the card you use for monitoring doesn't support the same WiFi modes like the client, or if it is too far from the client or from the AP, you may not capture a good deal of the traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '17, 12:48</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-63022" class="comments-container"></div><div id="comment-tools-63022" class="comment-tools"></div><div class="clear"></div><div id="comment-63022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

