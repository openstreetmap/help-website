+++
type = "question"
title = "network interface tries to send a message to itself"
description = '''this is one of many of the same packet happening every second - 2014-04-23 12:07:29.378767000 Enerpoin_02:6d:de Broadcast ARP 60 Who has 192.168.1.82? Tell 0.0.0.0 the mac address - Enerpoin (00:0a:3c) 02:6d:de - is a cctv dvr (although it does not follow mac address rules, hence it is showing as En...'''
date = "2014-04-27T05:38:00Z"
lastmod = "2014-04-27T12:02:00Z"
weight = 32214
keywords = [ "broadcast" ]
aliases = [ "/questions/32214" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [network interface tries to send a message to itself](/questions/32214/network-interface-tries-to-send-a-message-to-itself)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32214-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>this is one of many of the same packet happening every second - 2014-04-23 12:07:29.378767000 Enerpoin_02:6d:de Broadcast ARP 60 Who has 192.168.1.82? Tell 0.0.0.0 the mac address - Enerpoin (00:0a:3c) 02:6d:de - is a cctv dvr (although it does not follow mac address rules, hence it is showing as Enerpoin) and it has the ip address 192.168.1.82 so it seems that the dvr is trying to locate itself to send a message to itself, am I right? anyone have any ideas?</p></div><div id="question-tags" class="tags-container tags">broadcast</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '14, 05:38</strong></p><img src="https://secure.gravatar.com/avatar/2d0b09466fbe47f7f3d75b798a37acb8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brunobri&#39;s gravatar image" /><p>brunobri<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brunobri has no accepted answers">0%</span></p></div></div><div id="comments-container-32214" class="comments-container"><span id="32328"></span><div id="comment-32328" class="comment"><div id="post-32328-score" class="comment-score"></div><div class="comment-text"><p>Enerpoin is the mfg OUI that 00:0a:3c is assigned to. Wireshark looks that up for you in its OUI database. You can manually look up the MAC address at [<a href="http://www.wireshark.org/tools/oui-lookup.html%5D">http://www.wireshark.org/tools/oui-lookup.html]</a> and see it resolves to Enerpoint Ltd.</p></div><div id="comment-32328-info" class="comment-info"><span class="comment-age">(30 Apr '14, 16:39)</span> Rooster_50</div></div><span id="32336"></span><div id="comment-32336" class="comment"><div id="post-32336-score" class="comment-score"></div><div class="comment-text"><p>Thanks Rooster_50, but as I stated, wireshark quite rightly states that 00:0a:3c is Enerpoint Ltd, but I know that this is my Swann dvr box. So I don't understand why Swann do not follow Mac addressing rules!</p></div><div id="comment-32336-info" class="comment-info"><span class="comment-age">(01 May '14, 02:20)</span> brunobri</div></div><span id="32339"></span><div id="comment-32339" class="comment"><div id="post-32339-score" class="comment-score">2</div><div class="comment-text"><p>Maybe they are using Enerpoint components.</p></div><div id="comment-32339-info" class="comment-info"><span class="comment-age">(01 May '14, 05:55)</span> Kurt Knochner ♦</div></div><span id="32352"></span><div id="comment-32352" class="comment"><div id="post-32352-score" class="comment-score"></div><div class="comment-text"><p>What Kurt said...</p></div><div id="comment-32352-info" class="comment-info"><span class="comment-age">(01 May '14, 09:33)</span> Rooster_50</div></div><span id="32377"></span><div id="comment-32377" class="comment"><div id="post-32377-score" class="comment-score"></div><div class="comment-text"><p>Yeh, they probably have used some of Enerpoints chips, but looking on there website they are a solar energy company, can't understand what they can put in a cctv dvr!</p></div><div id="comment-32377-info" class="comment-info"><span class="comment-age">(01 May '14, 22:09)</span> brunobri</div></div></div><div id="comment-tools-32214" class="comment-tools"></div><div class="clear"></div><div id="comment-32214-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32221"></span>

<div id="answer-container-32221" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32221-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's (most certainly) an ARP probe request according to <a href="https://tools.ietf.org/html/rfc5227#section-2.1.1">RFC 5227</a> and should look like this one:</p><blockquote><p><a href="https://www.cloudshark.org/captures/ef136da1ae79">https://www.cloudshark.org/captures/ef136da1ae79</a></p></blockquote><p>The device is probably trying to detect if the IP address is available on the network.</p><p>Another reason for probe frames could be to announce it's existence on the network to some sort of CCTV management tool.</p><p>Nothing you should be worried about.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '14, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32221" class="comments-container"><span id="32238"></span><div id="comment-32238" class="comment"><div id="post-32238-score" class="comment-score"></div><div class="comment-text"><p>Thanks for that Kurt</p></div><div id="comment-32238-info" class="comment-info"><span class="comment-age">(28 Apr '14, 02:50)</span> brunobri</div></div><span id="32257"></span><div id="comment-32257" class="comment"><div id="post-32257-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-32257-info" class="comment-info"><span class="comment-age">(28 Apr '14, 08:13)</span> Kurt Knochner ♦</div></div><span id="32383"></span><div id="comment-32383" class="comment"><div id="post-32383-score" class="comment-score"></div><div class="comment-text"><p>Yes, this is called a gratuitous ARP, where it is announcing itself. If it gets a response, and hence a duplicate IP, it might report that via a management interface. It might be triggered where it previously had obtained the address dynamically (eg via DHCP) but is not able to renew it at the moment</p></div><div id="comment-32383-info" class="comment-info"><span class="comment-age">(02 May '14, 01:12)</span> martyvis</div></div><span id="32387"></span><div id="comment-32387" class="comment"><div id="post-32387-score" class="comment-score"></div><div class="comment-text"><p>Actually a gratuitous ARP looks silghtly different.</p><p><strong>Gratuitous ARP:</strong> <a href="https://www.cloudshark.org/captures/54af88021aa8">https://www.cloudshark.org/captures/54af88021aa8</a></p><pre><code>Is gratuitous: True
Sender MAC address: Vmware_37:5f:f5 (00:0c:29:37:5f:f5)
Sender IP address: 192.168.130.128 (192.168.130.128)
Target MAC address: 00:00:00_00:00:00 (00:00:00:00:00:00)
Target IP address: 192.168.130.128 (192.168.130.128)</code></pre><p>Sender IP address and Target IP address <strong>identical</strong>.</p><p><strong>ARP probe:</strong> <a href="https://www.cloudshark.org/captures/ef136da1ae79">https://www.cloudshark.org/captures/ef136da1ae79</a></p><pre><code>Sender MAC address: Vmware_c5:f6:9b (00:0c:29:c5:f6:9b)
Sender IP address: 0.0.0.0 (0.0.0.0)
Target MAC address: Broadcast (ff:ff:ff:ff:ff:ff)
Target IP address: 192.168.1.82 (192.168.1.82)</code></pre><p>Sender IP address and Target IP address <strong>different</strong> (0.0.0.0), to prevent ARP cache updates for the probed IP address on the receiving systems.</p><p>From RFC 5227: <a href="https://tools.ietf.org/html/rfc5227#section-2.1.1">https://tools.ietf.org/html/rfc5227#section-2.1.1</a></p><p>Cite:</p><pre><code>The &#39;sender IP address&#39; field MUST be set to all zeroes; this 
is to avoid polluting ARP caches in other hosts on the same 
link in the case where the address turns out to be already in 
use by another host.</code></pre></div><div id="comment-32387-info" class="comment-info"><span class="comment-age">(02 May '14, 03:16)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-32221" class="comment-tools"></div><div class="clear"></div><div id="comment-32221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

