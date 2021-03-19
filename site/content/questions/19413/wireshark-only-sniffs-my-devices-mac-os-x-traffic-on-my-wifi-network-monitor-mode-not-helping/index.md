+++
type = "question"
title = "Wireshark only sniffs my device&#x27;s (Mac OS X) traffic on my wifi network. Monitor mode not helping"
description = '''The packets coming through are all from my own device, but the other devices connected to my wireless network (a PC, and a mobile phone) are not showing up at all. I did some research, and put it in &quot;monitor mode&quot;, but doing that changes the way the captured data looks. They are no longer color code...'''
date = "2013-03-12T22:33:00Z"
lastmod = "2013-03-13T01:27:00Z"
weight = 19413
keywords = [ "mac", "wifi", "monitor", "mode" ]
aliases = [ "/questions/19413" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark only sniffs my device's (Mac OS X) traffic on my wifi network. Monitor mode not helping](/questions/19413/wireshark-only-sniffs-my-devices-mac-os-x-traffic-on-my-wifi-network-monitor-mode-not-helping)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19413-score" class="post-score" title="current number of votes">0</div><span id="post-19413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The packets coming through are all from my own device, but the other devices connected to my wireless network (a PC, and a mobile phone) are not showing up at all. I did some research, and put it in "monitor mode", but doing that changes the way the captured data looks. They are no longer color coded, they are just plain text, and it doesn't seem to be tracking any of the information I want, all the results are now protocol: 802.11</p><p>The only way to fix it, is to uncheck monitor mode, but doing that will only show me my own traffic. Any idea what I should do?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span> <span class="post-tag tag-link-mode" rel="tag" title="see questions tagged &#39;mode&#39;">mode</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '13, 22:33</strong></p><img src="https://secure.gravatar.com/avatar/4c1c949caffacb0935fa806c6da57a0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dingoes45&#39;s gravatar image" /><p><span>dingoes45</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dingoes45 has no accepted answers">0%</span></p></div></div><div id="comments-container-19413" class="comments-container"></div><div id="comment-tools-19413" class="comment-tools"></div><div class="clear"></div><div id="comment-19413-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19414"></span>

<div id="answer-container-19414" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19414-score" class="post-score" title="current number of votes">2</div><span id="post-19414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I did some research, and put it in "monitor mode", but doing that changes the way the captured data looks. They are no longer color coded, they are just plain text,</p></blockquote><p>That's probably because your network is encrypted (WEP or WPA/WPA2), and, when you capture in monitor mode, the <em>un</em>encrypted packets are given to Wireshark by the kernel (BPF).</p><p>If you are on an encrypted network, and you want to capture other machines' traffic, you will have to get the password for your network, and <a href="http://wiki.wireshark.org/HowToDecrypt802.11">configure Wireshark to be able to decrypt that traffic</a>. For WPA/WPA2, this means that you will need to capture the traffic from those machines at the beginning of an encrypted session, which may require you to disconnect them from the network, start Wireshark, and reconnect them to the network. (After all, the whole point of encrypting a network is to make it <em>harder</em> to sniff it....)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '13, 22:53</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19414" class="comments-container"><span id="19415"></span><div id="comment-19415" class="comment"><div id="post-19415-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that's what I figured. I did, however, try that as well. And assuming I understood it correctly, I entered wpa-pwd:(password):(ssid) into the field. It still changes nothing in terms of the results I see when on monitor mode.</p></div><div id="comment-19415-info" class="comment-info"><span class="comment-age">(12 Mar '13, 23:04)</span> <span class="comment-user userinfo">dingoes45</span></div></div><span id="19416"></span><div id="comment-19416" class="comment"><div id="post-19416-score" class="comment-score"></div><div class="comment-text"><p>Is there something else I should be doing after I enter the network information?</p></div><div id="comment-19416-info" class="comment-info"><span class="comment-age">(12 Mar '13, 23:09)</span> <span class="comment-user userinfo">dingoes45</span></div></div><span id="19427"></span><div id="comment-19427" class="comment"><div id="post-19427-score" class="comment-score"></div><div class="comment-text"><p>Note that, as I said in my answer, if your network is a WPA/WPA2 network, you can only decrypt traffic to or from a given machine if you capture the initial <a href="https://en.wikipedia.org/wiki/Eapol">EAPOL</a> handshake. As the Wireshark Wiki page I linked to says:</p><blockquote><p>WPA and WPA2 use keys derived from an EAPOL handshake to encrypt traffic. Unless all four handshake packets are present for the session you're trying to decrypt, Wireshark won't be able to decrypt the traffic. You can use the display filter eapol to locate EAPOL packets in your capture.</p></blockquote></div><div id="comment-19427-info" class="comment-info"><span class="comment-age">(13 Mar '13, 01:27)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-19414" class="comment-tools"></div><div class="clear"></div><div id="comment-19414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

