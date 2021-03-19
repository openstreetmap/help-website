+++
type = "question"
title = "Can&#x27;t capture HTTP on my Wi-Fi network"
description = '''Hello! I am new to Wireshark, and I&#x27;m using an Alfa AWUS036h USB Wireless adapter on Backtrack5 r3. I set up the alfa card and set it to monitor mode. Then i ran Wireshark, using the mon0 interface i created. Then i used airodump-ng and found the channel to use. The adapter manages to capture packet...'''
date = "2013-06-13T04:37:00Z"
lastmod = "2013-06-14T14:07:00Z"
weight = 22002
keywords = [ "http", "udp", "alfa", "awus036h", "802.11" ]
aliases = [ "/questions/22002" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't capture HTTP on my Wi-Fi network](/questions/22002/cant-capture-http-on-my-wi-fi-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22002-score" class="post-score" title="current number of votes">0</div><span id="post-22002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! I am new to Wireshark, and I'm using an Alfa AWUS036h USB Wireless adapter on Backtrack5 r3. I set up the alfa card and set it to monitor mode. Then i ran Wireshark, using the mon0 interface i created. Then i used airodump-ng and found the channel to use.</p><p>The adapter manages to capture packets, but only with protocol 802.11, NBNS, UDP, and SSDP (And some other protocols, but these are the ones that are captures the most). Especially the 802.11 is overflowing wireshark. And the thing i want to capture is HTTP.</p><p>What have I done wrong?</p><p>Thank you! I really appreciate help.</p><p>And sorry if there is something obvious I have overlooked, as mentioned I am new.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-alfa" rel="tag" title="see questions tagged &#39;alfa&#39;">alfa</span> <span class="post-tag tag-link-awus036h" rel="tag" title="see questions tagged &#39;awus036h&#39;">awus036h</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '13, 04:37</strong></p><img src="https://secure.gravatar.com/avatar/5a82ec592f9ae58b528b4ba33f30588f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cheesedoodal&#39;s gravatar image" /><p><span>cheesedoodal</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cheesedoodal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jun '13, 11:38</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-22002" class="comments-container"><span id="22010"></span><div id="comment-22010" class="comment"><div id="post-22010-score" class="comment-score"></div><div class="comment-text"><p>Using encryption on WLAN? WPA/WEP whatever?</p></div><div id="comment-22010-info" class="comment-info"><span class="comment-age">(13 Jun '13, 06:30)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="22068"></span><div id="comment-22068" class="comment"><div id="post-22068-score" class="comment-score"></div><div class="comment-text"><p>No, it is open. I am using my own router for testing, so I removed encryption. At least, on the router page I set Security mode to Disabled. My router is a Belkin router.</p></div><div id="comment-22068-info" class="comment-info"><span class="comment-age">(14 Jun '13, 10:59)</span> <span class="comment-user userinfo">cheesedoodal</span></div></div><span id="22073"></span><div id="comment-22073" class="comment"><div id="post-22073-score" class="comment-score"></div><div class="comment-text"><p>Open doesn't mean not encrypted. Wireless has OPEN authentication and TKIP/AES encryption on most of today's systems. You'd better doublecheck on that</p></div><div id="comment-22073-info" class="comment-info"><span class="comment-age">(14 Jun '13, 14:07)</span> <span class="comment-user userinfo">Landi</span></div></div></div><div id="comment-tools-22002" class="comment-tools"></div><div class="clear"></div><div id="comment-22002-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22023"></span>

<div id="answer-container-22023" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22023-score" class="post-score" title="current number of votes">0</div><span id="post-22023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The NBNS, UDP, and SSDP packets are probably broadcast packets, and you're probably on a protected network (encrypted with WEP or WPA/WPA2).</p><p>On a protected network, broadcast packets are transmitted in a fashion that allows all packets on the network to see their contents, as that's the intent of broadcasting; if they're encrypted, your 802.11 adapter may be decrypting them and handing them to the host, so Wireshark can see them.</p><p>Unicast packets are, however, encrypted in a way that is intended not to allow hosts other than the intended recipient to see their contents, i.e. they're intended not to be easily sniffable. <a href="http://wiki.wireshark.org/HowToDecrypt802.11">Wireshark can, in some cases, decrypt those packets</a>; you will need to supply the password for the network and, for WPA/WPA2, you will have to be running in "personal" mode and will have to capture the 4-way handshake as the hosts join the network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '13, 11:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-22023" class="comments-container"><span id="22069"></span><div id="comment-22069" class="comment"><div id="post-22069-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your response, but my network is open, so I don't believe it is encrypted.</p></div><div id="comment-22069-info" class="comment-info"><span class="comment-age">(14 Jun '13, 11:00)</span> <span class="comment-user userinfo">cheesedoodal</span></div></div></div><div id="comment-tools-22023" class="comment-tools"></div><div class="clear"></div><div id="comment-22023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

