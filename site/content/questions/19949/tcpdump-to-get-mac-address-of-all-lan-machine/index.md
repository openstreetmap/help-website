+++
type = "question"
title = "tcpdump to get mac address of all lan machine"
description = '''I have a machine connected to LAN switch. How can i get mac address of all other LAN machines. enabled promiscuous mode then tried following command  tcpdump -i eth1 -vvv -qe 11:31:07.670442 84:2b:2b:0a:78:68 (oui Unknown) &amp;gt; Broadcast, ARP, length 42: Ethernet (len 6), IPv4 (len 4), Request who-h...'''
date = "2013-03-29T23:09:00Z"
lastmod = "2013-04-02T10:19:00Z"
weight = 19949
keywords = [ "tcpdump", "mac-address", "linux" ]
aliases = [ "/questions/19949" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [tcpdump to get mac address of all lan machine](/questions/19949/tcpdump-to-get-mac-address-of-all-lan-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19949-score" class="post-score" title="current number of votes">0</div><span id="post-19949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a machine connected to LAN switch.</p><p>How can i get mac address of all other LAN machines.</p><p>enabled promiscuous mode then tried following command</p><p><strong>tcpdump -i eth1 -vvv -qe</strong></p><p>11:31:07.670442 84:2b:2b:0a:78:68 (oui Unknown) &gt; Broadcast, ARP, length 42: Ethernet (len 6), IPv4 (len 4), Request who-has 192.168.30.36 tell 192.168.30.32, length 28</p><p>It is not showing any ARP reply.How can i find mac address of all machines?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-mac-address" rel="tag" title="see questions tagged &#39;mac-address&#39;">mac-address</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '13, 23:09</strong></p><img src="https://secure.gravatar.com/avatar/6a6d36cecf235655a1d157c269a4db88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krrypto&#39;s gravatar image" /><p><span>krrypto</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krrypto has no accepted answers">0%</span></p></div></div><div id="comments-container-19949" class="comments-container"></div><div id="comment-tools-19949" class="comment-tools"></div><div class="clear"></div><div id="comment-19949-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20025"></span>

<div id="answer-container-20025" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20025-score" class="post-score" title="current number of votes">1</div><span id="post-20025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="krrypto has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I have a machine <strong>connected to LAN switch</strong>. its active,but i dont know its ip address.Wont tcpdump -i eth1 with out filters show all ARP replys?</p></blockquote><p>no, not necessarily.</p><p>The ARP request is directed to the ethernet broadcast address (ff:ff:ff:ff:ff:ff) and thus you will see those requests on a switch port, as the switch will forward those packets to all ports.</p><p>The ARP reply is <strong>usually</strong> directed to the MAC address of the machine who sent the ARP request, so you will <strong>not</strong> see that response on a switch, as the switch will forward that packet only to the port where that MAC address is known to 'live'. However, there may be TCP/IP implementations, that send the ARP reply to a multicast address. In that case, you will see the reply.</p><p>From <a href="http://tools.ietf.org/html/rfc5227">RFC 5227</a></p><pre><code>   RFC 826 implies that replies to ARP Requests are usually delivered
   using unicast, but it is also acceptable to deliver ARP Replies using
   broadcast.</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '13, 10:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-20025" class="comments-container"></div><div id="comment-tools-20025" class="comment-tools"></div><div class="clear"></div><div id="comment-20025-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19950"></span>

<div id="answer-container-19950" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19950-score" class="post-score" title="current number of votes">0</div><span id="post-19950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, if 192.168.30.36 isn't active it won't be able to reply. You could potentially write a little script and subsequently ping all the ip addresses in ypur ip subnet and have a tcpdump running filtered on "arp" protocol - no need for promiscuous mode there as the successful arp replies will be destined to your MAC address.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '13, 23:28</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Mar '13, 23:31</strong> </span></p></div></div><div id="comments-container-19950" class="comments-container"><span id="19951"></span><div id="comment-19951" class="comment"><div id="post-19951-score" class="comment-score"></div><div class="comment-text"><p>its active,but i dont know its ip address.Wont tcpdump -i eth1 with out filters show all ARP replys?</p></div><div id="comment-19951-info" class="comment-info"><span class="comment-age">(29 Mar '13, 23:39)</span> <span class="comment-user userinfo">krrypto</span></div></div><span id="19953"></span><div id="comment-19953" class="comment"><div id="post-19953-score" class="comment-score"></div><div class="comment-text"><p>Not sure I get the point... You want to learn all MAC addresses in your LAN? You trace your eth1 unfiltered and you will get arp replies for all you arp requests that find an active ip-address on the LAN. For ip addresses that are in your arp cache there won't be arp requests though and therefore you won't find arp replies in your trace.</p></div><div id="comment-19953-info" class="comment-info"><span class="comment-age">(30 Mar '13, 03:05)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-19950" class="comment-tools"></div><div class="clear"></div><div id="comment-19950-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

