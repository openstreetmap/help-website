+++
type = "question"
title = "CIFS vs NETBIOS &amp; network performance"
description = '''Testing file open performance across a WAN vs LAN. I open a 1MB .rtf file. When opening on the LAN, the traffic is on port 445 (CIFS). When opening the same file from the same server across the WAN, the traffic is on port 139 (NETBIOS). My question for all of you protocol gurus:  Is there really any...'''
date = "2011-06-02T11:42:00Z"
lastmod = "2011-06-07T11:11:00Z"
weight = 4343
keywords = [ "performance", "cifs", "netbios" ]
aliases = [ "/questions/4343" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [CIFS vs NETBIOS & network performance](/questions/4343/cifs-vs-netbios-network-performance)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4343-score" class="post-score" title="current number of votes">0</div><span id="post-4343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Testing file open performance across a WAN vs LAN. I open a 1MB .rtf file. When opening on the LAN, the traffic is on port 445 (CIFS). When opening the same file from the same server across the WAN, the traffic is on port 139 (NETBIOS).</p><p>My question for all of you protocol gurus:</p><p>Is there really any difference in the traffic when using a different port to do the same activity? If so, what are those differences &amp; how does it contribute to end-user experience?</p><p>Some other information you might be interested in:</p><p>Number of packets LAN – 1,544 WAN – 1,864 Size of data packets LAN – 1,474 bytes WAN – 1,354 bytes Time to open (first packet to last packet) LAN – 3 secs WAN – 19 secs</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-cifs" rel="tag" title="see questions tagged &#39;cifs&#39;">cifs</span> <span class="post-tag tag-link-netbios" rel="tag" title="see questions tagged &#39;netbios&#39;">netbios</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '11, 11:42</strong></p><img src="https://secure.gravatar.com/avatar/d1f7fabf169915dc5ba93025794b84db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Labnuke&#39;s gravatar image" /><p><span>Labnuke</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Labnuke has no accepted answers">0%</span></p></div></div><div id="comments-container-4343" class="comments-container"></div><div id="comment-tools-4343" class="comment-tools"></div><div class="clear"></div><div id="comment-4343-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4367"></span>

<div id="answer-container-4367" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4367-score" class="post-score" title="current number of votes">4</div><span id="post-4367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jasper has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your time differences are most certainly related to the "chattiness" of SMB. Both ports work - for your simple file transfer - nearly the same way.</p><p>Your long response times are most certainly a result of the SMB protocol design and not of the different ports.</p><p>Understanding the differences between 139 and 445 is a lot easier with a bit of protocol history. So ...</p><p><strong>1. Protocol History</strong></p><p>TCP port 139 is used for "NetBIOS over TCP", sometimes called NBT. This protocol was created to make the "NetBIOS over Ethernet" (NetBEUI) protocol routable. This rather old NetBIOS protocol was never designed to connect two computer with anything else but a LAN.</p><p>NetBIOS has several characteristics of TCP, for example you have to establish a session or keep-alives. After starting the NetBIOS session the client negotiates a protocol version, authenticates, mounts a share and accesses files and services on the server. This last part would be SMB.</p><p>With Windows 2000 Microsoft felt that this can be improved. They added the port 445 for the same service. On port 445 SMB runs directly over TCP. The only difference is that the client skips the NetBIOS session (saves one round trip) then negotiates, authenticates, mounts etc.</p><p>Check the properties of your network card. Somewhere in the Advanced IP Settings is a checkbox "Enable NetBIOS over TCP". Activate it and your computer uses port 139. Deactivate the option and the system wants to use 445.</p><p>So the protocol layers are:</p><p>port 139: SMB -&gt; NetBIOS -&gt; TCP port 445: SMB -&gt; .... -&gt; TCP</p><p>The 4 dots are not exactly random. Microsoft leaves 4 empty bytes in place so the same source code can process the message, regardless of 139 or 445.</p><p>I remember pulling my hair out when I tried to connect a shiny Windows 2000 system to an NT server for the first time ....</p><p>So far the protocol history.</p><p><strong>2. System behaviour</strong></p><p>Most traces that I have seen lately show that workstations try to connect to 139 and 445 at the same time. Whatever ports gets the first response will be used for communications.</p><p>With the latest versions of Windows you want to use port 445.</p><p>With NetBIOS out of the picture you have less broadcast traffic, can use FQDNs to mount shares, and you can use larger buffers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '11, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-4367" class="comments-container"><span id="4440"></span><div id="comment-4440" class="comment"><div id="post-4440-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the rsponse. Good information.</p></div><div id="comment-4440-info" class="comment-info"><span class="comment-age">(07 Jun '11, 11:11)</span> <span class="comment-user userinfo">Labnuke</span></div></div></div><div id="comment-tools-4367" class="comment-tools"></div><div class="clear"></div><div id="comment-4367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4348"></span>

<div id="answer-container-4348" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4348-score" class="post-score" title="current number of votes">1</div><span id="post-4348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have no idea about the differences between the way services are offered on port 139 and 445. However, I do know that the SMB protocol is not very WAN friendly as data is transferred one block at a time (instead of streaming). Which means, for each blocksize of data you get 1 round-trip-time for free as an additional bonus. If your blocksize is 4KB (not uncommon) and your RTT is 40ms, you get an additional delay of 1MB/4KB * 60 ms = ~15sec.</p><p>Have a look at your packet capture and check whether that is indeed what is causing the extra delay. Comparing traces can also give you some insight in whether the protocols used are the same on each port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '11, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4348" class="comments-container"></div><div id="comment-tools-4348" class="comment-tools"></div><div class="clear"></div><div id="comment-4348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

