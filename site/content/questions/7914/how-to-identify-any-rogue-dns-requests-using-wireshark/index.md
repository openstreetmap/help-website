+++
type = "question"
title = "How to identify any rogue dns requests using wireshark?"
description = '''Hi, I am an administrator of a college and management is looking for a solution in order to identify if there are any rogue DNS requests to our DNS servers?  I have set a packet capture for 24 hours to provide enough requests for analysis. Thank you'''
date = "2011-12-12T08:48:00Z"
lastmod = "2011-12-15T15:15:00Z"
weight = 7914
keywords = [ "rogue", "dns" ]
aliases = [ "/questions/7914" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How to identify any rogue dns requests using wireshark?](/questions/7914/how-to-identify-any-rogue-dns-requests-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7914-score" class="post-score" title="current number of votes">0</div><span id="post-7914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am an administrator of a college and management is looking for a solution in order to identify if there are any rogue DNS requests to our DNS servers? I have set a packet capture for 24 hours to provide enough requests for analysis.</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rogue" rel="tag" title="see questions tagged &#39;rogue&#39;">rogue</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '11, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/f82784c530264281a029efeaf2731925?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="staramod&#39;s gravatar image" /><p><span>staramod</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="staramod has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Dec '11, 08:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-7914" class="comments-container"><span id="7923"></span><div id="comment-7923" class="comment"><div id="post-7923-score" class="comment-score"></div><div class="comment-text"><p>What constitutes a rogue DNS request for you?</p></div><div id="comment-7923-info" class="comment-info"><span class="comment-age">(12 Dec '11, 12:41)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="7992"></span><div id="comment-7992" class="comment"><div id="post-7992-score" class="comment-score"></div><div class="comment-text"><p>http://www.fbi.gov/news/stories/2011/november/malware_110911/dns-changer-malware.pdf</p><p>I am going to set the packet capture on my datacenter firewall and see if it catches any traffic to the rouge DNS servers.</p><p>Thank you all</p></div><div id="comment-7992-info" class="comment-info"><span class="comment-age">(15 Dec '11, 09:35)</span> <span class="comment-user userinfo">staramod</span></div></div><span id="7999"></span><div id="comment-7999" class="comment"><div id="post-7999-score" class="comment-score"></div><div class="comment-text"><p>So, that was a misleading question... the referenced document describes DNS changer malware that modifies the DNS settings at the clients, in order to have them access rogue DNS servers. Not clients making rogue requests to your good DNS servers. Anyway, checking the datacenter firewall for outgoing DNS traffic, while this should go through your DNS servers, is fine.</p></div><div id="comment-7999-info" class="comment-info"><span class="comment-age">(15 Dec '11, 15:15)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-7914" class="comment-tools"></div><div class="clear"></div><div id="comment-7914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="7921"></span>

<div id="answer-container-7921" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7921-score" class="post-score" title="current number of votes">2</div><span id="post-7921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By "rogue DNS requests" I assume you mean DNS requests from systems that shouldn't be using your DNS servers. If your network is 192.168.1.0/24, use a display filter something like this:</p><p>(dns) &amp;&amp; (dns.flags.response == 0) &amp;&amp; !(ip.src==192.168.1.0/24)</p><p>This will show all DNS queries that originate from machines that are NOT on your network.</p><p>Of course, substitute your actual subnet address and subnet mask for 192.168.1.0/24. If you have legitimate DNS requests coming from multiple subnets, the address portion of filter will be more complicated, but the principle is the same.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '11, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-7921" class="comments-container"><span id="7939"></span><div id="comment-7939" class="comment"><div id="post-7939-score" class="comment-score"></div><div class="comment-text"><p>Jim, Thanks for your reply. What I am looking here is a machine from my network which is sending abnormal DNS requests... May be packet size is lot bigger than normal or something that sort. And a machine which might send abnormally frequent requests to DNS server. I am trying to identify the machine that might be infected with a virus or been compromised.</p><p>Thank You Amod.</p></div><div id="comment-7939-info" class="comment-info"><span class="comment-age">(13 Dec '11, 03:01)</span> <span class="comment-user userinfo">staramod</span></div></div></div><div id="comment-tools-7921" class="comment-tools"></div><div class="clear"></div><div id="comment-7921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7922"></span>

<div id="answer-container-7922" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7922-score" class="post-score" title="current number of votes">1</div><span id="post-7922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It depends on what your definition of a "rogue" DNS request is. Are looking for users querying your DNS servers without being authorized to do so? You could filter on IP ranges then - for example if all autorized users have an IP address from the network 172.16.0.0/16 you could filter on <strong>(not ip.addr==172.16.0.0/16) and (ip.addr==<em>YourDNSServerIP</em> and (udp.port==53 or tcp.port==53))</strong> (substitute your network and mask). All that remain are not from your users IP range and should probably not be allowed to use the server.</p><p>If you're looking for other kinds of "rogue" DNS request you might want to specify what you're looking for, so we might be able to help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '11, 12:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-7922" class="comments-container"><span id="7940"></span><div id="comment-7940" class="comment"><div id="post-7940-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply Jasper. Please find above my comment against Jim's.</p><p>Regards, Amod</p></div><div id="comment-7940-info" class="comment-info"><span class="comment-age">(13 Dec '11, 03:03)</span> <span class="comment-user userinfo">staramod</span></div></div></div><div id="comment-tools-7922" class="comment-tools"></div><div class="clear"></div><div id="comment-7922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7943"></span>

<div id="answer-container-7943" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7943-score" class="post-score" title="current number of votes">0</div><span id="post-7943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming a Linux based DNS server, you should look into iptables. You can setup rules on the input chain which sort out 'larger than normal' packets and/or rate limits per host and log them. This not only allows logging of them, but also keeping them off your DNS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '11, 04:05</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7943" class="comments-container"></div><div id="comment-tools-7943" class="comment-tools"></div><div class="clear"></div><div id="comment-7943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7998"></span>

<div id="answer-container-7998" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7998-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7998-score" class="post-score" title="current number of votes">0</div><span id="post-7998-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Figure out what you think might constitute an "abnormal DNS request" and then filter on that. There are a lot possibilities. For packet sizes larger than normal, consider filtering on "dns &amp;&amp; udp.lenth &gt; <em>somevalue</em>" or "dns &amp;&amp; tcp.len &gt; <em>somevalue</em>" or even "dns &amp;&amp; frame.len &gt; <em>somevalue</em>" where <em>somevalue</em> is the number of bytes that you think is abnormally large.</p><p>Click on "Expression" to the right of the display filter input box, scroll down to DNS and take a look at all the possible filters relating to DNS.</p><p>You might consider filtering on "dns.count.queries &gt; <em>somevalue</em>" Sometimes bot-infected systems will query a large number of DNS names in a single query. Similarly, you might look for DNS responses that contain a large number of answers with "dns.count.answers &gt; <em>somevalue</em>, but this is not a foolproof indicator of illegitimate activity. Sites like google.com will return a large number of responses.</p><p>To find systems that are sending abnormally frequent DNS requests, filter on "(dns) &amp;&amp; (dns.flags.response == 0)" to limit the display to DNS requests only, then click on Statistics &gt; Conversations, and check "Limit to display filter." You can then select the tab you want (IPv4, IPv6, etc.) and sort by number of packets to see which systems are sending the most DNS requests.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '11, 13:32</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 May '13, 08:36</strong> </span></p></div></div><div id="comments-container-7998" class="comments-container"></div><div id="comment-tools-7998" class="comment-tools"></div><div class="clear"></div><div id="comment-7998-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

