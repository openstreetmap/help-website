+++
type = "question"
title = "Can Wireshark show  a real time chart to show which PCs are consuming how much bandwidth."
description = '''Hi WireSharks, Can I use WireShark to track volume of traffic per device on a home network ? I have a home network with about 12 devices. Sometimes the network slows down and I would like a real time chart to show which PCs are consuming how much bandwidth. Can WireShark do that ?  For my purposes I...'''
date = "2014-05-04T12:53:00Z"
lastmod = "2014-05-04T13:15:00Z"
weight = 32505
keywords = [ "chart", "real-time" ]
aliases = [ "/questions/32505" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can Wireshark show a real time chart to show which PCs are consuming how much bandwidth.](/questions/32505/can-wireshark-show-a-real-time-chart-to-show-which-pcs-are-consuming-how-much-bandwidth)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32505-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi WireSharks,</p><p>Can I use WireShark to track volume of traffic per device on a home network ?</p><p>I have a home network with about 12 devices. Sometimes the network slows down and I would like a real time chart to show which PCs are consuming how much bandwidth. Can WireShark do that ?<br />
</p><p>For my purposes I do not even need the frames to be stored, I just need them to be just quickly inspected so that that the tool can provide a visualization, and ideally recent history, of network traffic per (PC or other device on the LAN) so I can identify and prove bandwidth hogs, ideally with time based trend graphs.</p><p>So assuming that my NIC support promiscuous mode, and assuming I plug directly into the router so the Hubs do not filter out Internet Traffic, can Wireshark help? or else, can you suggest or recommend and other tools than can do what I am looking to do ?</p><p>Thanks very much,</p><p>Terry Clancy</p></div><div id="question-tags" class="tags-container tags">chart real-time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 May '14, 12:53</strong></p><img src="https://secure.gravatar.com/avatar/5214edaac3a44ec12031c7471668baf5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="terryclancy&#39;s gravatar image" /><p>terryclancy<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="terryclancy has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-32505" class="comments-container"></div><div id="comment-tools-32505" class="comment-tools"></div><div class="clear"></div><div id="comment-32505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32506"></span>

<div id="answer-container-32506" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32506-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark / tshark always store packets to file and build their analysis on that. It's not possible to just visualize them and throw them away afterwards in real time.</p><p>I guess what you need is a Netflow/Openflow tool, not a packet capture. For tools like that you need a device that can provide netflow statistics, e.g. a switch or a router that comes with that feature.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '14, 13:15</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 May '14, 13:16</p></div></div><div id="comments-container-32506" class="comments-container"></div><div id="comment-tools-32506" class="comment-tools"></div><div class="clear"></div><div id="comment-32506-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

