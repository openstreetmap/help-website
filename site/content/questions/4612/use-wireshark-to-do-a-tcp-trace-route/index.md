+++
type = "question"
title = "Use Wireshark to do a &quot;TCP Trace Route&quot;?"
description = '''Hello... I have a problem where I cannot connect to a remote server. A Wireshark capture from my (client) end shows my TCP SYN packets receive no response. But, how to tell if the SYN is making it to the server, and being ignored, or... if the SYN gets dropped by a firewall/router, and never arrives...'''
date = "2011-06-17T16:47:00Z"
lastmod = "2011-06-19T14:27:00Z"
weight = 4612
keywords = [ "traceroute", "tcp" ]
aliases = [ "/questions/4612" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Use Wireshark to do a "TCP Trace Route"?](/questions/4612/use-wireshark-to-do-a-tcp-trace-route)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4612-score" class="post-score" title="current number of votes">0</div><span id="post-4612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello...</p><p>I have a problem where I cannot connect to a remote server. A Wireshark capture from my (client) end shows my TCP SYN packets receive no response. But, how to tell if the SYN is making it to the server, and being ignored, or... if the SYN gets dropped by a firewall/router, and never arrives at the server???</p><p>An ICMP-based TraceRoute is no good, because PINGs are often blocked by firewalls. So, a TraceRoute will tell me how far an ICMP packet gets, but it won't tell me how far my TCP packet gets.</p><p>I seem to remember that one can use Wireshark to edit and generate packets. If so, I thought it might not be too hard to create a series of TCP SYN packets, with ever increasing TTL values, to mimic a trace route.</p><p>Has anyone done this? If not, does it seem like something that could be done with, perhaps, an hour's worth of effort?</p><p>thx, feenyman99</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-traceroute" rel="tag" title="see questions tagged &#39;traceroute&#39;">traceroute</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '11, 16:47</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p><span>feenyman99</span><br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span></p></div></div><div id="comments-container-4612" class="comments-container"></div><div id="comment-tools-4612" class="comment-tools"></div><div class="clear"></div><div id="comment-4612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4613"></span>

<div id="answer-container-4613" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4613-score" class="post-score" title="current number of votes">1</div><span id="post-4613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="feenyman99 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, Wireshark does not have the capability to edit or generate packets. Colasoft Packet Builder will do what you want. It allows you to generate TCP packets, to set the SYN bit, to edit the TTL, and then to transmit those packets onto the network.</p><p>Does this remote server belong to your organization? If not, the information returned by your TCP traceroute may not be all that helpful. Since you get no response (no SYN/ACK, no RST, no ICMP Destination Unreachable), then something along the path is silently dropping your SYN packet. Your TCP traceroute should get an ICMP Time-to-Live Exceeded in Transit packet back from every device along the path that processes your packet. So, the device that's dropping your packet is likely the one AFTER the last one that responds. Unless you have some knowledge of the remote network, you won't know whether that next device is the server or a firewall or router, especially if NAT is deployed in the remote network.</p><p>If the remote server does belong to your organization, it might be quicker to have someone at the remote site do some Wireshark captures.</p><p>BTW, it's also possible, although unlikely, that your SYN is getting through, but the SYN/ACK is not getting back.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '11, 17:54</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-4613" class="comments-container"><span id="4614"></span><div id="comment-4614" class="comment"><div id="post-4614-score" class="comment-score"></div><div class="comment-text"><p>Jim,</p><p>I just downloaded Colasoft - it looks like just what I need. I'll play with that a little later. Awesome thanx!!!</p><blockquote><blockquote><p>"Does this remote server belong to your organization?"</p></blockquote></blockquote><p>Yes and No. They belong to my overall organization (LARGE global company), but to a different team, and I'm brand new to this organization, with no technical contacts yet, so, for several reasons, I'd like to gather all the evidence before I go looking for help.</p><blockquote><blockquote><p>"So, the device that's dropping your packet is likely the one AFTER the last one that responds."</p></blockquote></blockquote><p>Great point! But, minimally, I can provide evidence that a network component is dropping the SYN, and not the server. This should help get the right team (network vs. server) involved, when I go asking for help. If I can get the network team involved, they should be able to tell me what the next device in the path is, that is dropping the SYN.</p><p>THANX for your tool recommendation, and your comments! They are helping me to crystallize my game plan :-)</p><p>feenyman99</p></div><div id="comment-4614-info" class="comment-info"><span class="comment-age">(18 Jun '11, 05:59)</span> <span class="comment-user userinfo">feenyman99</span></div></div><span id="4619"></span><div id="comment-4619" class="comment"><div id="post-4619-score" class="comment-score"></div><div class="comment-text"><p>SUCCESS!! I was able to use Colasoft Packet Builder to do a "TCP Trace Route", sending several SYN packets, with increasing TTL. It worked like a charm, and proved that something is dropping my SYN packet before it gets to the server. (It's the same device where the ICMP Traceroute dies.)</p><p>Thanx, Jim, for your Colasoft reference - invaluable!!</p><p>feenyman99</p></div><div id="comment-4619-info" class="comment-info"><span class="comment-age">(18 Jun '11, 20:26)</span> <span class="comment-user userinfo">feenyman99</span></div></div><span id="4622"></span><div id="comment-4622" class="comment"><div id="post-4622-score" class="comment-score"></div><div class="comment-text"><p>(converted your answers to comments, see the FAQ)</p></div><div id="comment-4622-info" class="comment-info"><span class="comment-age">(19 Jun '11, 14:27)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-4613" class="comment-tools"></div><div class="clear"></div><div id="comment-4613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

