+++
type = "question"
title = "Seeing lots of ARP requests even though the hosts have the MAC address in their ARP cache already"
description = '''Hello can someone please help me with the following question. We are trying to troubleshoot a performance issue between a Windows Server/s and a NetApp c-mode filer (network attached storage device) We have a number of Windows Servers which each having two network cards one card is attached to VLAN-...'''
date = "2016-11-08T09:11:00Z"
lastmod = "2016-11-08T13:52:00Z"
weight = 57174
keywords = [ "arp" ]
aliases = [ "/questions/57174" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Seeing lots of ARP requests even though the hosts have the MAC address in their ARP cache already](/questions/57174/seeing-lots-of-arp-requests-even-though-the-hosts-have-the-mac-address-in-their-arp-cache-already)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57174-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57174-score" class="post-score" title="current number of votes">0</div><span id="post-57174-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>can someone please help me with the following question.</p><p>We are trying to troubleshoot a performance issue between a Windows Server/s and a NetApp c-mode filer (network attached storage device)</p><p>We have a number of Windows Servers which each having two network cards one card is attached to VLAN-A and the other network card on VLAN-B. VLAN-B being the VLAN where the NetApp storage device is also connected (there is no default gateway for any host on VLAN-B as it does not need to be routable)</p><p>Did a quick WireShare trace and we saw lots (and I mean lots) of ARP broadcasts where the Windows Servers (e.g. the IP addresses attached to VLAB-B) are asking who has IP address x.x.x.x, in other words, the network IP address for the NIC on the NetApp filers also on VLAN-B.</p><p>When you look at the ARP cache on these Windows Servers you can see the MAC address in question is already in the cache, therefore I cannot see why these Windows Server keep ARPing when they already have an entry in their ARP cache.</p><p>Any advice most welcome</p><p>Thanks Ernie</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '16, 09:11</strong></p><img src="https://secure.gravatar.com/avatar/ff39c11ae2cb05528da757366e76d84b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EBrant&#39;s gravatar image" /><p><span>EBrant</span><br />
<span class="score" title="1 reputation points">1</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EBrant has no accepted answers">0%</span></p></div></div><div id="comments-container-57174" class="comments-container"><span id="57176"></span><div id="comment-57176" class="comment"><div id="post-57176-score" class="comment-score"></div><div class="comment-text"><p>Could you provide us a trace at public accessible place; like cloudshark or google drive.</p></div><div id="comment-57176-info" class="comment-info"><span class="comment-age">(08 Nov '16, 09:15)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-57174" class="comment-tools"></div><div class="clear"></div><div id="comment-57174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57179"></span>

<div id="answer-container-57179" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57179-score" class="post-score" title="current number of votes">2</div><span id="post-57179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Depending on your Windows version you might see different behavior in the TCP/IP stack. I hope that you are using not using Server 2003 / Windows XP or anything older.</p><p>First, Windows has a habit of refreshing the ARP cache. This is a normal, as long as the ARP requests are not excessive. There is a good description of the ARP behavior in Microsofts <a href="https://support.microsoft.com/en-us/kb/949589">KB949589</a>.</p><p>Another point in the Windows operating system is a multi homed network on a disjoint network. "Multi homed" means that you have two or more network interfaces. "Disjoint" means that the two network segments are not connected. On older systems (i. e. pre-Vista) Windows would handle the situation poorly and requires serious tweaking. This became better with the rewritten TCP/IP in Vista. A few recommendations are given in a <a href="https://blogs.technet.microsoft.com/networking/2009/04/24/source-ip-address-selection-on-a-multi-homed-windows-computer/">Technet Blog entry</a></p><p>Lastly, certain cluster protocols can mess with the IP stack. For a more detailed analysis, as pointed out by Christian_R, a trace would be helpful.</p><p>Good hunting</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '16, 10:07</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-57179" class="comments-container"><span id="57183"></span><div id="comment-57183" class="comment"><div id="post-57183-score" class="comment-score"></div><div class="comment-text"><p><span>@packethunter</span> Interesting links. Thanks.</p></div><div id="comment-57183-info" class="comment-info"><span class="comment-age">(08 Nov '16, 11:46)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="57185"></span><div id="comment-57185" class="comment"><div id="post-57185-score" class="comment-score"></div><div class="comment-text"><p>Hello Packet Hunter</p><p>Thanks for taking the time to give me a detailed answer with several options to look at. I am not in the office tomorrow so will with go over the links you posted later in the week.</p><p>FYI, I am seeing ARPs several times a second, and several times in a row. The NetApp cluster has 4 LIFs whereby one if preferred and the others standby so maybe it is not configured as it should be and flipping between these 4 possible paths (I will have to ask the NetApp guys to check if this is possible).</p><p>Thanks very much again, once I have read your links I will try to post a trace</p><p>Ernie</p></div><div id="comment-57185-info" class="comment-info"><span class="comment-age">(08 Nov '16, 13:52)</span> <span class="comment-user userinfo">EBrant</span></div></div></div><div id="comment-tools-57179" class="comment-tools"></div><div class="clear"></div><div id="comment-57179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

