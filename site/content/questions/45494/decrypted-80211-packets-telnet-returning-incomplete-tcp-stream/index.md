+++
type = "question"
title = "Decrypted 802.11 packets (telnet) returning incomplete TCP stream"
description = '''I have captured traffic from another wireless adapter (including the 4 necessary EAPOL packets), and decrypted it with the WPA2 password and SSID, so that all of the &quot;802.11&quot; traffic shows the correct/real protocol. To test the decryption (and my understanding), I logged in via telnet to a server on...'''
date = "2015-08-29T00:28:00Z"
lastmod = "2015-08-29T00:28:00Z"
weight = 45494
keywords = [ "decrypt", "follow.tcp.stream", "802.11", "incomplete", "telnet" ]
aliases = [ "/questions/45494" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypted 802.11 packets (telnet) returning incomplete TCP stream](/questions/45494/decrypted-80211-packets-telnet-returning-incomplete-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45494-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have captured traffic from another wireless adapter (including the 4 necessary EAPOL packets), and decrypted it with the WPA2 password and SSID, so that all of the "802.11" traffic shows the correct/real protocol.</p><p>To test the decryption (and my understanding), I logged in via telnet to a server on the target adapter. I am able to filter out the telnet packets, however when I "Follow the TCP Stream" I am getting partially decrypted results.</p><p>From my experience following a telnet stream over ethernet, the information is presented very similarly to command line and very readable (most importantly, it is complete with all of the information that was passed). However, with these decrypted packets, it is missing large portions of the information.</p><p>For Example, if I logged in via telnet with the account TestUser1 and Password1, the TCP stream would likely return "Tstser1" and "Paswod1".</p><p>Is this because my monitoring adapter is not capturing all of the packets?</p></div><div id="question-tags" class="tags-container tags">decrypt follow.tcp.stream 802.11 incomplete telnet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '15, 00:28</strong></p><img src="https://secure.gravatar.com/avatar/59d37f9f4353df07b602799c8cc24769?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WTFender&#39;s gravatar image" /><p>WTFender<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WTFender has no accepted answers">0%</span></p></div></div><div id="comments-container-45494" class="comments-container"><span id="45495"></span><div id="comment-45495" class="comment"><div id="post-45495-score" class="comment-score"></div><div class="comment-text"><p>Also, thanks for anybody that takes the time to help! It took me a long time of reading posts to get this far :P.</p></div><div id="comment-45495-info" class="comment-info"><span class="comment-age">(29 Aug '15, 00:33)</span> WTFender</div></div><span id="45496"></span><div id="comment-45496" class="comment"><div id="post-45496-score" class="comment-score"></div><div class="comment-text"><p>Yes it seems that you didn't capture every packet. Could you provide the trace, so it will be easier to help.</p></div><div id="comment-45496-info" class="comment-info"><span class="comment-age">(29 Aug '15, 01:25)</span> Christian_R</div></div></div><div id="comment-tools-45494" class="comment-tools"></div><div class="clear"></div><div id="comment-45494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

