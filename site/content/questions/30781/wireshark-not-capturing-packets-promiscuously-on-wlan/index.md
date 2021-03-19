+++
type = "question"
title = "Wireshark not capturing packets promiscuously on WLAN"
description = '''Hi So I am trying to capture my LAN traffic ( all traffic from all devices on my LAN ) on my Macbook Pro over Wifi.  I have &quot;use promiscuous mode on all interfaces&quot; enabled in capture options. However when I run the capture, I am only able to capture all traffic from my macbook and broadcast packets...'''
date = "2014-03-13T18:25:00Z"
lastmod = "2014-03-13T19:29:00Z"
weight = 30781
keywords = [ "decryption", "promiscuous-mode", "802.11", "monitor-mode" ]
aliases = [ "/questions/30781" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not capturing packets promiscuously on WLAN](/questions/30781/wireshark-not-capturing-packets-promiscuously-on-wlan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30781-score" class="post-score" title="current number of votes">1</div><span id="post-30781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>So I am trying to capture my LAN traffic ( all traffic from all devices on my LAN ) on my Macbook Pro over Wifi.</p><p>I have "use promiscuous mode on all interfaces" enabled in capture options. However when I run the capture, I am only able to capture all traffic from my macbook and broadcast packets from all other devices on the LAN.</p><p>I have set my router on WPA/WP2 personal mode. I am aware other devices in my LAN will have their traffic encrypted because of this. <strong>I don't mind seeing the encrypted traffic , But i still want to capture it.</strong> How do I go about doing that ?</p><p>Regarding decryption:</p><p>I tried capturing all traffic from all devices on my LAN by enabling monitor mode. I understand I need to capture EAPOL handshake of the device I am trying to decrypt. Is this correct ? What happens if I don't capture the EAPOL handshake of my laptop but I do capture the handshake of another device? Does that mean I can decypt the packets of the other device but not of my laptop.? Or do I need EAPOL of both my laptop and the other devices to decrypt anything ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-promiscuous-mode" rel="tag" title="see questions tagged &#39;promiscuous-mode&#39;">promiscuous-mode</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-monitor-mode" rel="tag" title="see questions tagged &#39;monitor-mode&#39;">monitor-mode</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '14, 18:25</strong></p><img src="https://secure.gravatar.com/avatar/c4c0b379a32fb823f73293fbf3dee5bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sukhvir%20Notra&#39;s gravatar image" /><p><span>Sukhvir Notra</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sukhvir Notra has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Mar '14, 19:29</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-30781" class="comments-container"></div><div id="comment-tools-30781" class="comment-tools"></div><div class="clear"></div><div id="comment-30781-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30783"></span>

<div id="answer-container-30783" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30783-score" class="post-score" title="current number of votes">1</div><span id="post-30783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As one of the tags you put on your question suggests, you need <em>monitor</em> mode, not <em>promiscuous</em> mode; promiscuous mode doesn't necessarily do anything useful on Wi-Fi adapters.</p><p>See <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">the WLAN (802.11) Capture Setup</a> page on the Wireshark Wiki for more details.</p><p>As for decryption (which should have been asked in a separate question):</p><p>See the <a href="http://wiki.wireshark.org/HowToDecrypt802.11">How To Decrypt 802.11</a> page on the Wireshark Wiki.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '14, 19:27</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Mar '14, 19:29</strong> </span></p></div></div><div id="comments-container-30783" class="comments-container"><span id="30784"></span><div id="comment-30784" class="comment"><div id="post-30784-score" class="comment-score"></div><div class="comment-text"><p>Yes I tried using monitor mode. Could you please answer my questions under the " Regarding decryption" heading in my question</p></div><div id="comment-30784-info" class="comment-info"><span class="comment-age">(13 Mar '14, 19:29)</span> <span class="comment-user userinfo">Sukhvir Notra</span></div></div></div><div id="comment-tools-30783" class="comment-tools"></div><div class="clear"></div><div id="comment-30783-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

