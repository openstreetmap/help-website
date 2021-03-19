+++
type = "question"
title = "Is it always that the client send out ARP requests ?"
description = '''In one of the first few practicals in the Wireshark Analysis book, there&#x27;s this file called gen-googlemaps.pcapng which we are supposed to analyse. I realised that the 1st packet refers to the Asus client broadcasting an ARP request to find out who is the DNS server .   But when I did my own simple ...'''
date = "2013-03-24T20:49:00Z"
lastmod = "2013-03-24T23:38:00Z"
weight = 19791
keywords = [ "arp", "analysis" ]
aliases = [ "/questions/19791" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is it always that the client send out ARP requests ?](/questions/19791/is-it-always-that-the-client-send-out-arp-requests)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19791-score" class="post-score" title="current number of votes">0</div><span id="post-19791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In one of the first few practicals in the Wireshark Analysis book, there's this file called <em>gen-googlemaps.pcapng</em> which we are supposed to analyse.</p><p>I realised that the 1st packet refers to the Asus client broadcasting an ARP request to find out who is the DNS server . <img src="http://i.imgur.com/Odl8IYq.png?1" alt="alt text" /></p><p>But when I did my own simple scan after flushing my DNS cache, my laptop doesn't seem to broadcast any ARP request to find out who the DNS server is. All ARP requests in my simple scan comes from the router itself trying to find out the hosts which are connected to it.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '13, 20:49</strong></p><img src="https://secure.gravatar.com/avatar/9b52984d9786885d47fe81e43d8591ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dinged&#39;s gravatar image" /><p><span>Dinged</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dinged has no accepted answers">0%</span></p></img></div></div><div id="comments-container-19791" class="comments-container"></div><div id="comment-tools-19791" class="comment-tools"></div><div class="clear"></div><div id="comment-19791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19793"></span>

<div id="answer-container-19793" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19793-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19793-score" class="post-score" title="current number of votes">3</div><span id="post-19793-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dinged has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Clearing the DNS cache does not clear the ARP cache.</p><p>DNS maps domain names to IP addresses. ARP maps IP addresses to MAC addresses. The two processes are independent of each other. After you clear the DNS cache, the MAC address of the DNS server (or the default gateway, if the DNS server is on another network) can still be in the ARP cache, in which case, no ARP is necessary in order for your PC to communicate with the DNS server.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '13, 23:38</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-19793" class="comments-container"></div><div id="comment-tools-19793" class="comment-tools"></div><div class="clear"></div><div id="comment-19793-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19792"></span>

<div id="answer-container-19792" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19792-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19792-score" class="post-score" title="current number of votes">1</div><span id="post-19792-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Generally ARP is used to find target MAC Address.If your router needs to send a packet to your PC and it is not having mac address of your PC then it will trigger an ARP Request.It can be other way round too.If you want to send a packet to other hosts and not having MAC of your default gateway then your PC will trigger an ARP Request to find out the MAC of your Default router.</p><p>Now the DNS Part:</p><p>Assume a case where your DNS server resides in other network? ARP is a protocol works with in your broadcast domain.So it is not always necessary to expect an ARP request initiated to DNS Server.</p><p>Let us take this example:</p><p>My Laptop--------&gt;Home router-----------&gt;ISP Network</p><p>My home network is in private IP Range(192.168.1.x) and DNS Server IP is (75.75.75.75). In this case my laptop can't send any ARP Request to DNS Server as both are in different domain.Instead,it will send the packet to it's default gateway(home router) and for that reason it should know the MAC of default gateway and that is why it will trigger an ARP to find mac address of default gateway.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '13, 22:21</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Mar '13, 23:05</strong> </span></p></div></div><div id="comments-container-19792" class="comments-container"></div><div id="comment-tools-19792" class="comment-tools"></div><div class="clear"></div><div id="comment-19792-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

