+++
type = "question"
title = "gratuitous arp broadcast"
description = '''Hi,  I am connecting my STM32f4 board ( server) with my client computer via a switch using TCP protocol. Everything works fine but then If I unplug the power supply of STM board for &amp;gt;7 sec then plug back, the TCP connection breaks and cannot restore. IF I unplug the power supply of STM board for ...'''
date = "2015-03-04T00:25:00Z"
lastmod = "2015-03-04T05:24:00Z"
weight = 40245
keywords = [ "arp", "gratuitoussa" ]
aliases = [ "/questions/40245" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [gratuitous arp broadcast](/questions/40245/gratuitous-arp-broadcast)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40245-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am connecting my STM32f4 board ( server) with my client computer via a switch using TCP protocol. Everything works fine but then If I unplug the power supply of STM board for &gt;7 sec then plug back, the TCP connection breaks and cannot restore. IF I unplug the power supply of STM board for &lt;3 sec and plug back, the TCP connection can restore like normal. I then use Wireshark on the computer to trace the network traffic and see that for the second case (unplug&lt;3sec), when I plug back, the STM board sends out a gratuitous arp which somehow makes the whole system restore.</p><p><a href="http://postimg.org/image/54xz2oy1n/">plug &lt;3s</a></p><p>In the first case, when I plug back, the STM boards does not send any gratuitous arp package and then cannot connect.</p><p><a href="http://postimg.org/image/tmmy3oq8d/">plug &gt;7s</a></p><p>Could any one help to solve this problem? THanks.</p></div><div id="question-tags" class="tags-container tags">arp gratuitoussa</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '15, 00:25</strong></p><img src="https://secure.gravatar.com/avatar/a19014597e5da87f71bb18aa90866aa8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tako&#39;s gravatar image" /><p>tako<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tako has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Mar '15, 00:26</p></div></div><div id="comments-container-40245" class="comments-container"></div><div id="comment-tools-40245" class="comment-tools"></div><div class="clear"></div><div id="comment-40245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40255"></span>

<div id="answer-container-40255" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40255-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This ARP is only part of the deal, and is only a consequence of the TCP layer trying to get packets out.</p><p>The platform knows that it's lost the physical layer and hence cannot be sure it's connected to the same subnet as before when it got it's IP address. So it broadcasts an ARP. If after a while nothing comes back, it can safely assume there's no IP address collision on this subnet and carry on using its assigned IP.</p><p>Then it cleanly (somewhat, a reset is not clean, but common practice) terminates the TCP connection and let the client setup a new one.</p><p>In the second case the TCP layer just gave up, it could not get packets out. So when physical layer is restored, there's nothing to send, hence no need for an ARP broadcast. It also seems as if the ICMP broke, because there's no ICMP echo reply, nor port unreachable for the TCP port (if it is indeed shutdown).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '15, 05:24</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-40255" class="comments-container"><span id="40263"></span><div id="comment-40263" class="comment"><div id="post-40263-score" class="comment-score"></div><div class="comment-text"><p>Hi, Thank you for your nice explaination. I can now quite understand what is happening. As you said, the main difference between the two is that one tries to get packets out and another just gives up ( maybe after long-time trying).That may explain the difference between 7s off and 3s off. However, If flatform is poweroff, how could it is possible that the TCP layer tries to get the packets out? I think if the platform is powered off, the TCP layer also should stop working and both should behave the same when I plug back the power? And the problem does not happen when I unplug/plug in the Ethernet cable or if I connect the STM board directly to the client computer.</p></div><div id="comment-40263-info" class="comment-info"><span class="comment-age">(04 Mar '15, 18:36)</span> tako</div></div></div><div id="comment-tools-40255" class="comment-tools"></div><div class="clear"></div><div id="comment-40255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

