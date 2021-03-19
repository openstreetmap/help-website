+++
type = "question"
title = "DNS IPV6 query/reponse"
description = '''In my traces I can see a DNS AAAA query and response but after the response is received I see DNS A (IPv4) query and response. Now if I have an IPv6 address why do I need to get the IPv4 ? Maybe I can&#x27;t use IPv6 addresses because my ISP might not support it? Screenshot Trace file: cloudshark'''
date = "2011-11-18T23:43:00Z"
lastmod = "2013-03-29T02:35:00Z"
weight = 7514
keywords = [ "dns", "ipv6" ]
aliases = [ "/questions/7514" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [DNS IPV6 query/reponse](/questions/7514/dns-ipv6-queryreponse)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7514-score" class="post-score" title="current number of votes">0</div><span id="post-7514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In my traces I can see a DNS AAAA query and response but after the response is received I see DNS A (IPv4) query and response. Now if I have an IPv6 address why do I need to get the IPv4 ?</p><p>Maybe I can't use IPv6 addresses because my ISP might not support it?</p><p><a href="http://postimage.org/image/olgv77hbr/">Screenshot</a></p><p>Trace file: <a href="http://cloudshark.org/captures/f7cfe4f0a897">cloudshark</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span> <span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '11, 23:43</strong></p><img src="https://secure.gravatar.com/avatar/5d64d21de6598960bf2db61f1ca705cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ddayan&#39;s gravatar image" /><p><span>ddayan</span><br />
<span class="score" title="41 reputation points">41</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ddayan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Jan '12, 03:07</strong> </span></p></div></div><div id="comments-container-7514" class="comments-container"></div><div id="comment-tools-7514" class="comment-tools"></div><div class="clear"></div><div id="comment-7514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="8534"></span>

<div id="answer-container-8534" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8534-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8534-score" class="post-score" title="current number of votes">0</div><span id="post-8534-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ddayan has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is there any traffic between the IPv6 response and the IPv4 query? The client would not know that IPv6 isn't supported by the ISP. Normally, after the IPv6 response, the client would attempt to make a connection using IPv6. If the connection attempt fails, then the client would do an IPv4 query followed by an IPv4 connection attempt, assuming that it receives a DNS response to the IPv4 query.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '12, 20:47</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-8534" class="comments-container"><span id="8536"></span><div id="comment-8536" class="comment"><div id="post-8536-score" class="comment-score"></div><div class="comment-text"><p>That's what so weird, there's no attempt it fires ipv4 straight away. Btw its a linux box and it happens when I use wget. I made a screenshot and uploaded the trace if that helps. http://www.2shared.com/file/RzP3DZf3/packet_dump-1.html</p></div><div id="comment-8536-info" class="comment-info"><span class="comment-age">(22 Jan '12, 01:17)</span> <span class="comment-user userinfo">ddayan</span></div></div><span id="8555"></span><div id="comment-8555" class="comment"><div id="post-8555-score" class="comment-score"></div><div class="comment-text"><p>How do you know there's no attempt? Are you tracing the socket layer?</p><p>Further: what's wgets prefer-family setting?</p><p>Final: please share capture files through <a href="http://cloudshark.org/">CloudShark</a>.</p></div><div id="comment-8555-info" class="comment-info"><span class="comment-age">(23 Jan '12, 01:09)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="8556"></span><div id="comment-8556" class="comment"><div id="post-8556-score" class="comment-score"></div><div class="comment-text"><p>I've done some tests and it looks like it only happens when wget is used. What do you mean by tracing the socket layer? I know how to set the prefer-family value, but how do I retrive it?</p><p>heres the capture file: http://cloudshark.org/captures/f7cfe4f0a897</p></div><div id="comment-8556-info" class="comment-info"><span class="comment-age">(23 Jan '12, 03:06)</span> <span class="comment-user userinfo">ddayan</span></div></div><span id="8580"></span><div id="comment-8580" class="comment"><div id="post-8580-score" class="comment-score"></div><div class="comment-text"><p>Check <a href="http://www.twam.info/software/wget-and-ipv6">this</a>.</p></div><div id="comment-8580-info" class="comment-info"><span class="comment-age">(24 Jan '12, 04:54)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="8581"></span><div id="comment-8581" class="comment"><div id="post-8581-score" class="comment-score"></div><div class="comment-text"><p>my wgetrc doesn't specify prefer-family, but it looks like wget asks for IPV6 first, maybe the version on backtrack 5 is modified</p></div><div id="comment-8581-info" class="comment-info"><span class="comment-age">(24 Jan '12, 06:18)</span> <span class="comment-user userinfo">ddayan</span></div></div><span id="8599"></span><div id="comment-8599" class="comment not_top_scorer"><div id="post-8599-score" class="comment-score"></div><div class="comment-text"><p>This comment from the referred article says it all IMHO: <code>But wget prefers IPv4 over IPv6, meaning if your download mirror supports IPv6, wget doesn’t use it by default.</code></p><p>You assume that IPv6 name resolution means an attempt on an IPv6 connection. That is <em>not</em> true. It's no more than gathering information on the available options. The preference then says what to try first. the above quoted comment says it's IPv4. That's what you see.</p></div><div id="comment-8599-info" class="comment-info"><span class="comment-age">(25 Jan '12, 02:16)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="8603"></span><div id="comment-8603" class="comment not_top_scorer"><div id="post-8603-score" class="comment-score"></div><div class="comment-text"><p>yea thats what I thought, it just doen't make sense seems like waste of time</p></div><div id="comment-8603-info" class="comment-info"><span class="comment-age">(25 Jan '12, 06:33)</span> <span class="comment-user userinfo">ddayan</span></div></div></div><div id="comment-tools-8534" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-8534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7517"></span>

<div id="answer-container-7517" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7517-score" class="post-score" title="current number of votes">0</div><span id="post-7517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What does the AAAA response say? Does it contain an actual answer, or is it just confirmation the DNS has processed the request and has no answer for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '11, 01:13</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7517" class="comments-container"><span id="7527"></span><div id="comment-7527" class="comment"><div id="post-7527-score" class="comment-score"></div><div class="comment-text"><p>It returns an answer: gb.releases.ubuntu.com: type AAAA, class IN, addr 2a01:450:10:1::10</p></div><div id="comment-7527-info" class="comment-info"><span class="comment-age">(21 Nov '11, 02:35)</span> <span class="comment-user userinfo">ddayan</span></div></div></div><div id="comment-tools-7517" class="comment-tools"></div><div class="clear"></div><div id="comment-7517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7528"></span>

<div id="answer-container-7528" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7528-score" class="post-score" title="current number of votes">0</div><span id="post-7528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How much time is there between the AAAA response and the A request? Is your host IPv6 enabled? And your ISP? Do you see traffic to the IPv6 address in the AAAA response? Do you get a response?</p><p>As most OS's give IPv6 a higher preference than IPv4, my bet would be that this system tries to use IPv6 and falls back to IPv4 after discovering that it can't use IPv6 for it's task.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '11, 02:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7528" class="comments-container"><span id="8532"></span><div id="comment-8532" class="comment"><div id="post-8532-score" class="comment-score"></div><div class="comment-text"><p>Sorry I forgot about this question. I know that my ISP doen't support it but the trace has a AAAA query and response with an answer after one second. Immediately after it receives the ipv6 answer it does a A query and the answer is also received one sec after. How does the Client knows ipv6 is not supported by the ISP, and that it needs the IPV4 address?</p></div><div id="comment-8532-info" class="comment-info"><span class="comment-age">(21 Jan '12, 16:52)</span> <span class="comment-user userinfo">ddayan</span></div></div></div><div id="comment-tools-7528" class="comment-tools"></div><div class="clear"></div><div id="comment-7528-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19926"></span>

<div id="answer-container-19926" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19926-score" class="post-score" title="current number of votes">0</div><span id="post-19926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A record has IPv4 address.AAAA has IPv6 address record. So when you request for a A record it returns a 32-bit IPv4 address, most commonly used to map hostnames to an IP address of the host.If you have IPV6 ,the need of IPV4 is A record.A record is set using the Ip-Address V4.If your service provider doesn't have Ip address version 6 ,better search a online provider who provides IPV6 .You can visit the <a href="http://www.whoisxy.com/dns-query.aspx">WhoisXY.com</a> to find the A record and AAAA record .The DNS query service is useful for it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '13, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/3451ad5c7bc454155d41dbdbb215a6ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hasini&#39;s gravatar image" /><p><span>hasini</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hasini has no accepted answers">0%</span></p></div></div><div id="comments-container-19926" class="comments-container"></div><div id="comment-tools-19926" class="comment-tools"></div><div class="clear"></div><div id="comment-19926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

