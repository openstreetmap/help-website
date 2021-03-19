+++
type = "question"
title = "cdp packets missing"
description = '''Hello; I am using Dell Latitude E6400, and my Wireshark version is version 1.6.7. When I try to capture through my interface, CDP packets are missing. It shows other multicast packets like HSRP, OSPF. What may be the reason and how to solve it? I am using Symantec End Point.'''
date = "2012-06-04T21:47:00Z"
lastmod = "2012-06-04T23:39:00Z"
weight = 11651
keywords = [ "cdp", "packets", "missing" ]
aliases = [ "/questions/11651" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [cdp packets missing](/questions/11651/cdp-packets-missing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11651-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello;</p><p>I am using Dell Latitude E6400, and my Wireshark version is version 1.6.7. When I try to capture through my interface, CDP packets are missing. It shows other multicast packets like HSRP, OSPF. What may be the reason and how to solve it?</p><p>I am using Symantec End Point.</p></div><div id="question-tags" class="tags-container tags">cdp packets missing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '12, 21:47</strong></p><img src="https://secure.gravatar.com/avatar/40796f32a9fd577fc290686f2ea160a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="afsal&#39;s gravatar image" /><p>afsal<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="afsal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jun '12, 19:55</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-11651" class="comments-container"></div><div id="comment-tools-11651" class="comment-tools"></div><div class="clear"></div><div id="comment-11651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11652"></span>

<div id="answer-container-11652" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11652-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>To know something is missing, you need to know that it was there to begin with. So lets start by verifying that CDP is indeed enabled on the port you are connected to. Could you run the command "sh cdp int &lt;interface-to-your-dell&gt;"? It should give you details like this:</p><pre><code>c2950#sh cdp int fa0/1
FastEthernet0/1 is up, line protocol is up
  Encapsulation ARPA
  Sending CDP packets every 60 seconds
  Holdtime is 180 seconds
c2950#</code></pre><p>Then capture long enough to see the actual packets. In my case I need to capture more than 60 seconds. You can use the capture filter "ether host 01:00:0c:cc:cc:cc" to capture only CDP packets.</p><p>If the packets are still missing in the capture, then <a href="http://wiki.wireshark.org/CaptureSetup/InterferingSoftware">maybe some software on your laptop is blocking those packets to get to WinPcap/Wireshark</a>. You may want to check with a linux live-CD and tcpdump to see if the packets indeed arrive on your port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '12, 23:39</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-11652" class="comments-container"></div><div id="comment-tools-11652" class="comment-tools"></div><div class="clear"></div><div id="comment-11652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

