+++
type = "question"
title = "Is this normal ARP for cable service?"
description = '''http://www.cloudshark.org/captures/79e79275d8ce I sniffed this from a laptop plugged directly into my cable modem. I get HAMMERED with arp on my cable service. My ISP IT support is not very knowledgeable (did not know what ARP was) and my activity lights are on constant flicker mode. It really makes...'''
date = "2012-06-08T15:52:00Z"
lastmod = "2012-06-09T08:25:00Z"
weight = 11775
keywords = [ "arp", "flood", "security", "sniff" ]
aliases = [ "/questions/11775" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is this normal ARP for cable service?](/questions/11775/is-this-normal-arp-for-cable-service)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11775-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><a href="http://www.cloudshark.org/captures/79e79275d8ce">http://www.cloudshark.org/captures/79e79275d8ce</a></p><p>I sniffed this from a laptop plugged directly into my cable modem.</p><p>I get HAMMERED with arp on my cable service. My ISP IT support is not very knowledgeable (did not know what ARP was) and my activity lights are on constant flicker mode. It really makes the lights useless and all the traffic cannot be good for anything.</p><p>I read in a few places this could be considered normal or might be due to virus infected machines on my subnet? Is this normal? Can I do anything about it?</p><p>Thank you,</p></div><div id="question-tags" class="tags-container tags">arp flood security sniff</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '12, 15:52</strong></p><img src="https://secure.gravatar.com/avatar/2b1d4ebc68ff2908f81bbfd9a43aaf78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pluribus&#39;s gravatar image" /><p>pluribus<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pluribus has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jun '12, 15:53</p></div></div><div id="comments-container-11775" class="comments-container"><span id="11776"></span><div id="comment-11776" class="comment"><div id="post-11776-score" class="comment-score"></div><div class="comment-text"><p>PS I have a router running dd-wrt between the modem and my LAN normally but I want to be clear that this traffic is directly from the modem.</p><p>When I hook back in the router, the lights on that go insane as well, I assume from dropping all those ARP packets?</p><p>Confused, seems really extreme.</p></div><div id="comment-11776-info" class="comment-info"><span class="comment-age">(08 Jun '12, 15:56)</span> pluribus</div></div></div><div id="comment-tools-11775" class="comment-tools"></div><div class="clear"></div><div id="comment-11775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11785"></span>

<div id="answer-container-11785" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11785-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Seems pretty normal to me. I have a cable modem as well, and tons of ARP requests on it. As far as I know cable modem providers usually have all (or at least a lot) of their customers in the same broadcast domain, which leads to all the ARPs requests showing up.</p><p>You can see in your trace that the query is coming from the .1 IP ("who has xyz, please tell a.b.c.1"). That is usually the default gateway, looking for one of the nodes in the subnet. The replies are unicast frames, which is why you don't see them.</p><p>And no, you can't do anything about the requests. The provider could by redesigning his network architecture, but I doubt he will - and I'm not sure it is even possible for cable modem architectures. So all <strong>you</strong> can do is drop all the unwanted stuff at your firewall/router.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '12, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-11785" class="comments-container"></div><div id="comment-tools-11785" class="comment-tools"></div><div class="clear"></div><div id="comment-11785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

