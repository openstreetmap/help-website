+++
type = "question"
title = "broadcast storm ?"
description = '''seeing a weird issue when trying to access a webserver 10.100.20.175 from my local PC 10.100.21.157 as you can see from the packet capture everything looks normal till no 9 , after which i start seeing a whole bunch of arp requests and the webpage on 10.100.20.175 never loads'''
date = "2014-10-15T08:01:00Z"
lastmod = "2014-10-20T21:14:00Z"
weight = 37068
keywords = [ "broadcast", "http", "missing_packets", "tcp" ]
aliases = [ "/questions/37068" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [broadcast storm ?](/questions/37068/broadcast-storm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37068-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37068-score" class="post-score" title="current number of votes">0</div><span id="post-37068-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>seeing a weird issue when trying to access a webserver 10.100.20.175 from my local PC 10.100.21.157</p><p>as you can see from the packet capture everything looks normal till no 9 , after which i start seeing a whole bunch of arp requests and the webpage on 10.100.20.175 never loads<img src="https://osqa-ask.wireshark.org/upfiles/ws.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-broadcast" rel="tag" title="see questions tagged &#39;broadcast&#39;">broadcast</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-missing_packets" rel="tag" title="see questions tagged &#39;missing_packets&#39;">missing_packets</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '14, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/0b247a9c8e15d271b4d37cedc0876022?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tmkunte&#39;s gravatar image" /><p><span>tmkunte</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tmkunte has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Oct '14, 03:03</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-37068" class="comments-container"></div><div id="comment-tools-37068" class="comment-tools"></div><div class="clear"></div><div id="comment-37068-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37176"></span>

<div id="answer-container-37176" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37176-score" class="post-score" title="current number of votes">1</div><span id="post-37176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, that's no broadcast storm for sure: look at the amount of time that passes between frames. Broadcast storms are thousands of packets per second (or at least hundreds). What you've got there looks pretty normal.</p><p>Is the problem consistent? Do you always get the lost segment at the beginning? For some reason one of the segments from the web server is missing and it doesn't appear to retransmit it (or at least Wireshark doesn't see the retransmission). I suppose it's possible the TCP stack over there is broken but I'd think it's more likely some firewall software or something is interfering.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '14, 03:02</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-37176" class="comments-container"><span id="37201"></span><div id="comment-37201" class="comment"><div id="post-37201-score" class="comment-score"></div><div class="comment-text"><p>its the same issue everytime.</p><p>another thing that was puzzling was no 19</p><p>why would the source 10.100.21.157 do an ARP request for the destination 10.100.20.175 when traffic is already flowing between the 2 ?</p></div><div id="comment-37201-info" class="comment-info"><span class="comment-age">(20 Oct '14, 06:51)</span> <span class="comment-user userinfo">tmkunte</span></div></div><span id="37202"></span><div id="comment-37202" class="comment"><div id="post-37202-score" class="comment-score"></div><div class="comment-text"><p>Maybe the server has a problem where it can't send the big packet (at least I'm guessing the missing packet is a big one. And doesn't retransmit. I'd guess the problem is on the server side.</p><p>ARP entries expire--even when there's traffic flowing (at least that's my experience).</p></div><div id="comment-37202-info" class="comment-info"><span class="comment-age">(20 Oct '14, 07:04)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="37215"></span><div id="comment-37215" class="comment"><div id="post-37215-score" class="comment-score"></div><div class="comment-text"><p>The ARP in packet 19 isn't a broadcast, but a unicast arp (that is, a refresh rather than a discover). This is all normal.</p><p>I think the most you can tell from that trace is that the client sends the GET message and the response isn't fully received by the client after that. I'd next want to trace at the server, and from there the question becomes why the server didn't fully respond to the GET (or, if it did, in which case what happened to the packets between the server and the client).</p></div><div id="comment-37215-info" class="comment-info"><span class="comment-age">(20 Oct '14, 21:14)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-37176" class="comment-tools"></div><div class="clear"></div><div id="comment-37176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

