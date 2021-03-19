+++
type = "question"
title = "[closed] UDP packets not received"
description = '''I am trying to build a socket to retrieve the ethernet packets from ecu. When i run my code on windows there is no problem and the code runs correctly. But when i run my code on Linux it gets stuck at s.recv(65565) as no udp messages are received by Debian(raspberry pi). I have already set static ip...'''
date = "2015-05-11T07:27:00Z"
lastmod = "2015-05-11T08:16:00Z"
weight = 42304
keywords = [ "capture", "udp", "raspberry", "socket", "debian" ]
aliases = [ "/questions/42304" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] UDP packets not received](/questions/42304/udp-packets-not-received)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42304-score" class="post-score" title="current number of votes">0</div><span id="post-42304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to build a socket to retrieve the ethernet packets from ecu. When i run my code on windows there is no problem and the code runs correctly. But when i run my code on Linux it gets stuck at s.recv(65565) as no udp messages are received by Debian(raspberry pi). I have already set static ip in /etc/network/interfaces as follows: <code>iface eth0 inet static  address 160.48.199.91  netmask 255.255.255.0  gateway 160.48.199.1</code></p><p>The code is as below:</p><pre><code> import socket
    import sys
    HOST = &quot;160.48.199.91&quot;
    port = 30490
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    s.bind((HOST, 30490))
    while True:
         data = s.recvfrom(65565)
         print(data)</code></pre><p>There is no LAN or Router. When i check netstat -s i see that there are 0 UDP and 0 TCP messages received. But when i check in Wireshark on Debian i could see the displayed UDP packets. Does it mean that the UDP packets are reaching the Raspberry Pi but not received by Debian OS ?</p><p>I know this is not related to this forum. But any help would be appreciated as i need to solve this problem urgently for my thesis.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-raspberry" rel="tag" title="see questions tagged &#39;raspberry&#39;">raspberry</span> <span class="post-tag tag-link-socket" rel="tag" title="see questions tagged &#39;socket&#39;">socket</span> <span class="post-tag tag-link-debian" rel="tag" title="see questions tagged &#39;debian&#39;">debian</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '15, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/85652400f627dbc4dbd4d0d09e03ecee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Praju&#39;s gravatar image" /><p><span>Praju</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Praju has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>11 May '15, 08:16</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-42304" class="comments-container"><span id="42307"></span><div id="comment-42307" class="comment"><div id="post-42307-score" class="comment-score"></div><div class="comment-text"><p>Sorry, you're much more likely to get help in a Python focused site.</p></div><div id="comment-42307-info" class="comment-info"><span class="comment-age">(11 May '15, 08:16)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-42304" class="comment-tools"></div><div class="clear"></div><div id="comment-42304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by grahamb 11 May '15, 08:16

</div>

</div>

</div>

