+++
type = "question"
title = "Connecting to an HP 2510g-28 Switch"
description = '''Hi there, I would like to connect my Wireshark to my HP 2510g-48 network switch so I can analyze the network traffic. I know the switch is capable of mirroring on specific ports. I have promiscous mode set on my NIC. Can anyone advise me on which steps I need to take next in order to recieve all net...'''
date = "2012-04-30T01:59:00Z"
lastmod = "2012-05-04T16:58:00Z"
weight = 10511
keywords = [ "wireshark" ]
aliases = [ "/questions/10511" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Connecting to an HP 2510g-28 Switch](/questions/10511/connecting-to-an-hp-2510g-28-switch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10511-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there, I would like to connect my Wireshark to my HP 2510g-48 network switch so I can analyze the network traffic. I know the switch is capable of mirroring on specific ports. I have promiscous mode set on my NIC. Can anyone advise me on which steps I need to take next in order to recieve all network traffic on Wireshark?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '12, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/fa3b0bb1e872b69f465332e68b8c9735?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="computer_guy&#39;s gravatar image" /><p>computer_guy<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="computer_guy has no accepted answers">0%</span></p></div></div><div id="comments-container-10511" class="comments-container"></div><div id="comment-tools-10511" class="comment-tools"></div><div class="clear"></div><div id="comment-10511-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10512"></span>

<div id="answer-container-10512" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10512-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>May I suggest, that you just look at the specific section inside the manual?</p><p>At <a href="http://cdn.procurve.com/training/Manuals/2510G-MgmtCfg-Jun2008-59923095.pdf">http://cdn.procurve.com/training/Manuals/2510G-MgmtCfg-Jun2008-59923095.pdf</a> in Section B-23 (google is your friend) you find the details on how to configure port monitoring</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '12, 02:18</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-10512" class="comments-container"><span id="10513"></span><div id="comment-10513" class="comment"><div id="post-10513-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your quick answer. I have already enabled monitoring on port 36. The cable from 36 goes into the system I have wireshark on. Is there any way I can check that it is mirroring corretly. When I ssh onto the switch, it shows Monotoring Enabled: YES Monitoring Port: 36</p><p>Any help would be really good.</p></div><div id="comment-10513-info" class="comment-info"><span class="comment-age">(30 Apr '12, 02:55)</span> computer_guy</div></div><span id="10514"></span><div id="comment-10514" class="comment"><div id="post-10514-score" class="comment-score">1</div><div class="comment-text"><p>Thats dependend on WHAT exactly you want to monitor - check IPs, VLAN Tags etc. inside your wireshark trace and look if the corresponding endpoints appear inside your data</p></div><div id="comment-10514-info" class="comment-info"><span class="comment-age">(30 Apr '12, 04:00)</span> Landi</div></div><span id="10515"></span><div id="comment-10515" class="comment"><div id="post-10515-score" class="comment-score"></div><div class="comment-text"><p>Ok, thanks. One last question. My switch is part of a stack. It is the commander switch. Does this mean if I monitor on my commander (Like I am doing), I will get traffic via wireshark for all four switches in my stack?</p></div><div id="comment-10515-info" class="comment-info"><span class="comment-age">(30 Apr '12, 04:12)</span> computer_guy</div></div><span id="10516"></span><div id="comment-10516" class="comment"><div id="post-10516-score" class="comment-score">1</div><div class="comment-text"><p>Good question, since I don't know HP switches too good I can only guess that you configure your port locally meaning only on your current physical device if there is no other configuration setting like e.g. a module/slot number or anything referring to one of the stacked devices, but that's just a guess</p></div><div id="comment-10516-info" class="comment-info"><span class="comment-age">(30 Apr '12, 05:07)</span> Landi</div></div><span id="10536"></span><div id="comment-10536" class="comment"><div id="post-10536-score" class="comment-score"></div><div class="comment-text"><p>if you enable monitoring on port 36, should'nt you connect the sniffer to another port, the mirroing port?</p><p>Regards<br />
Kurt</p></div><div id="comment-10536-info" class="comment-info"><span class="comment-age">(30 Apr '12, 13:58)</span> Kurt Knochner ♦</div></div><span id="10581"></span><div id="comment-10581" class="comment not_top_scorer"><div id="post-10581-score" class="comment-score"></div><div class="comment-text"><p>Kurt, thanks for your message. I believe that on HP switches, monitoring and mirroring are the same thing, so I have plugged sniffer into port configured as monitoring port (36).</p></div><div id="comment-10581-info" class="comment-info"><span class="comment-age">(02 May '12, 03:36)</span> computer_guy</div></div></div><div id="comment-tools-10512" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-10512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10690"></span>

<div id="answer-container-10690" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10690-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are two steps you need for monitoring. First you need to configure the mirror-port, which is where your Wireshark will be capturing packets. You have set port 36 for this. Then you need to select the ports you wish to monitor. (In some models you can also select VLANs to monitor). When you have done that, a copy of traffic on the monitored port(s) (or VLANs) will be sent to the mirror-port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '12, 16:58</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span> </br></p></div></div><div id="comments-container-10690" class="comments-container"></div><div id="comment-tools-10690" class="comment-tools"></div><div class="clear"></div><div id="comment-10690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

