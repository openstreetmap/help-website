+++
type = "question"
title = "Client stream seems not arrive at server side"
description = '''I put Wireshark to both client and server, and captured something I cannot understand. This wrong behavior also cause client try to reset the connection and the original socket seems dropped.  Client screen shot (LargePic Port-52604):  Server screen shot (LargePic Port-8777):   As you can see, every...'''
date = "2015-12-03T18:57:00Z"
lastmod = "2015-12-04T00:12:00Z"
weight = 48240
keywords = [ "rst", "tcp", "wireshark" ]
aliases = [ "/questions/48240" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Client stream seems not arrive at server side](/questions/48240/client-stream-seems-not-arrive-at-server-side)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48240-score" class="post-score" title="current number of votes">0</div><span id="post-48240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I put Wireshark to both client and server, and captured something I cannot understand. This wrong behavior also cause client try to reset the connection and the original socket seems dropped.</p><ul><li>Client screen shot (<a href="http://file.laobian.me/web/wireshark/client1.png">LargePic</a> Port-52604): <img src="http://file.laobian.me/web/wireshark/client1.png" alt="client" /></li><li>Server screen shot (<a href="http://file.laobian.me/web/wireshark/server1.png">LargePic</a> Port-8777): <img src="http://file.laobian.me/web/wireshark/server1.png" alt="server" /></li></ul><p>As you can see, everything is fine until the client sent <code>[PSH, ACK] Seq=260...</code> to server. For some reason(I would love to know) the server side didn't captured this log, and also the server wouldn't sent <code>[ACK]</code> back to client then. Due to this, the client retransport this stream for five times, after it failed, it just thought it has to send <code>[RST]</code> to other side. That's what I understand the behavior is.</p><p>However, another strange thing is: in server side, after 8-9 minutes it does send a <code>[PSH, ACK] Seq=40 ...</code> stream, it seems it's not response to the original failed stream client sent.</p><p>Please help me to analysis what's going on during this process. It seems the client can reproduce this issue once 4-5 minutes when no communication between the two sides.</p><p>Please ask me if more information needed.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '15, 18:57</strong></p><img src="https://secure.gravatar.com/avatar/483b1f0eb6d5a8fd4100088cb2530e6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JerryBian&#39;s gravatar image" /><p><span>JerryBian</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JerryBian has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Dec '15, 19:00</strong> </span></p></div></div><div id="comments-container-48240" class="comments-container"><span id="48243"></span><div id="comment-48243" class="comment"><div id="post-48243-score" class="comment-score"></div><div class="comment-text"><p>What is between the client and the server? A piece of cable, LAN with several switches, the internet...?</p></div><div id="comment-48243-info" class="comment-info"><span class="comment-age">(03 Dec '15, 22:30)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-48240" class="comment-tools"></div><div class="clear"></div><div id="comment-48240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48246"></span>

<div id="answer-container-48246" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48246-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48246-score" class="post-score" title="current number of votes">0</div><span id="post-48246-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like the server has a TCP Keepalive timer of 10 minutes. This might be too long to stay in a firewall's connection table. "It seems the client can reproduce this issue once 4-5 minutes when no communication between the two sides." If this assumption is true then reducing the Keepalive interval at the server below 5 minutes should fix this...</p><p><a href="http://www.tldp.org/HOWTO/html_single/TCP-Keepalive-HOWTO/#preventingdisconnection">http://www.tldp.org/HOWTO/html_single/TCP-Keepalive-HOWTO/#preventingdisconnection</a></p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '15, 00:12</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-48246" class="comments-container"></div><div id="comment-tools-48246" class="comment-tools"></div><div class="clear"></div><div id="comment-48246-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

