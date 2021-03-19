+++
type = "question"
title = "queries and answers of mDNS are in the same frame"
description = '''I use dns-sd -B _services._dns-sd._udp on my Mac to query dns-sd services in my home network, it does reply, but when I inspect it in wireshark, it shows like this: Frame 1: 142 bytes on wire (1136 bits), 142 bytes captured (1136 bits) on interface 0 Ethernet II, Src: Apple_ef:11:4b (7c:d1:c3:ef:11:...'''
date = "2017-03-06T18:21:00Z"
lastmod = "2017-03-06T21:28:00Z"
weight = 59874
keywords = [ "mdns", "multicast", "dns" ]
aliases = [ "/questions/59874" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [queries and answers of mDNS are in the same frame](/questions/59874/queries-and-answers-of-mdns-are-in-the-same-frame)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59874-score" class="post-score" title="current number of votes">0</div><span id="post-59874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use <code>dns-sd -B _services._dns-sd._udp</code> on my Mac to query dns-sd services in my home network, it does reply, but when I inspect it in wireshark, it shows like this:</p><pre><code>Frame 1: 142 bytes on wire (1136 bits), 142 bytes captured (1136 bits) on interface 0
Ethernet II, Src: Apple_ef:11:4b (7c:d1:c3:ef:11:4b), Dst: IPv4mcast_fb (01:00:5e:00:00:fb)
Internet Protocol Version 4, Src: 10.109.201.113, Dst: 224.0.0.251
User Datagram Protocol, Src Port: 5353, Dst Port: 5353
Multicast Domain Name System (query)
    Transaction ID: 0x0000
    Flags: 0x0000 Standard query
    Questions: 1
    Answer RRs: 2
    Authority RRs: 0
    Additional RRs: 0
    Queries
        _services._dns-sd._udp.local: type PTR, class IN, &quot;QU&quot; question
    Answers
        _services._dns-sd._udp.local: type PTR, class IN, _http._tcp.local
            Name: _services._dns-sd._udp.local
            Type: PTR (domain name PoinTeR) (12)
            .000 0000 0000 0001 = Class: IN (0x0001)
            0... .... .... .... = Cache flush: False
            Time to live: 3595
            Data length: 13
            Domain Name: _http._tcp.local
        _services._dns-sd._udp.local: type PTR, class IN, _apple-mobdev2._tcp.local
            Name: _services._dns-sd._udp.local
            Type: PTR (domain name PoinTeR) (12)
            .000 0000 0000 0001 = Class: IN (0x0001)
            0... .... .... .... = Cache flush: False
            Time to live: 4157
            Data length: 17
            Domain Name: _apple-mobdev2._tcp.local</code></pre><p>the query and answers are in the same frame, so the source and destination of query packet and answer packet are the same. My understanding is the query is from my computer to the multicast address(224.0.0.251) and the answer is in reverse, is it correct?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mdns" rel="tag" title="see questions tagged &#39;mdns&#39;">mdns</span> <span class="post-tag tag-link-multicast" rel="tag" title="see questions tagged &#39;multicast&#39;">multicast</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '17, 18:21</strong></p><img src="https://secure.gravatar.com/avatar/75de90cd2dddc1467b3f3db8d49dfb30?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfly&#39;s gravatar image" /><p><span>jfly</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfly has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Mar '17, 18:42</strong> </span></p></div></div><div id="comments-container-59874" class="comments-container"></div><div id="comment-tools-59874" class="comment-tools"></div><div class="clear"></div><div id="comment-59874-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59880"></span>

<div id="answer-container-59880" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59880-score" class="post-score" title="current number of votes">2</div><span id="post-59880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jfly has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I believe it is part of the "Known Answer Suppression" mechanism of mDNS.</p><p>See section 7.1 of RFC 6762 for further explanation. <a href="https://tools.ietf.org/html/rfc6762#section-7.1">[link]</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '17, 21:28</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p><span>Rooster_50</span><br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-59880" class="comments-container"></div><div id="comment-tools-59880" class="comment-tools"></div><div class="clear"></div><div id="comment-59880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

