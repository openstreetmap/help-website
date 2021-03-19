+++
type = "question"
title = "Find Vlan ID&#x27;s"
description = '''Hi,  We have been attempting to find the VLAN ID&#x27;s without success. We&#x27;ve found some steps in other forums but seem to be missing one somewhere along the line. Can someone provide a step by step on how to find these using wireshark?  thanks. '''
date = "2016-09-15T15:32:00Z"
lastmod = "2016-09-15T23:03:00Z"
weight = 55574
keywords = [ "vlan", "valn", "id" ]
aliases = [ "/questions/55574" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Find Vlan ID's](/questions/55574/find-vlan-ids)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55574-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We have been attempting to find the VLAN ID's without success. We've found some steps in other forums but seem to be missing one somewhere along the line. Can someone provide a step by step on how to find these using wireshark?<br />
</p><p>thanks.</p></div><div id="question-tags" class="tags-container tags">vlan valn id</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '16, 15:32</strong></p><img src="https://secure.gravatar.com/avatar/a8b1db1997265f0598bdc37ec3ffabd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SiO2yH2o&#39;s gravatar image" /><p>SiO2yH2o<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SiO2yH2o has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-55574" class="comments-container"><span id="55575"></span><div id="comment-55575" class="comment"><div id="post-55575-score" class="comment-score"></div><div class="comment-text"><p>What is your OS and which version and what is your Wireshark version?</p></div><div id="comment-55575-info" class="comment-info"><span class="comment-age">(15 Sep '16, 15:51)</span> Jaap ♦</div></div><span id="55609"></span><div id="comment-55609" class="comment"><div id="post-55609-score" class="comment-score"></div><div class="comment-text"><p>We have tried several different machines with different windows OS's. Most recently we are using a Lenovo t61 running windows 8.1. the wireshark version is 2.2.0.</p></div><div id="comment-55609-info" class="comment-info"><span class="comment-age">(16 Sep '16, 15:21)</span> SiO2yH2o</div></div></div><div id="comment-tools-55574" class="comment-tools"></div><div class="clear"></div><div id="comment-55574-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55581"></span>

<div id="answer-container-55581" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55581-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello,</p><p>If I understood the issue correctly: It depends on where you are trying to capture the traffic. If you are connected to an access switchport you won't be able to see the VLAN tag, the traffic is not encapsulated, try setting up a SPAN/RSPAN port and mirror the traffic from a trunk switchport and there you will see all the 802.1q header.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '16, 23:03</strong></p><img src="https://secure.gravatar.com/avatar/736170f27313125d7a9c6d3f7f9e9cda?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="panai&#39;s gravatar image" /><p>panai<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="panai has no accepted answers">0%</span></p></div></div><div id="comments-container-55581" class="comments-container"><span id="55599"></span><div id="comment-55599" class="comment"><div id="post-55599-score" class="comment-score"></div><div class="comment-text"><p>We'll give it a shot. Thanks.</p></div><div id="comment-55599-info" class="comment-info"><span class="comment-age">(16 Sep '16, 10:07)</span> SiO2yH2o</div></div><span id="55602"></span><div id="comment-55602" class="comment"><div id="post-55602-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-55602-info" class="comment-info"><span class="comment-age">(16 Sep '16, 12:10)</span> Jaap ♦</div></div><span id="55608"></span><div id="comment-55608" class="comment"><div id="post-55608-score" class="comment-score"></div><div class="comment-text"><p>The reason why @Jaap was asking what OS you use was that most network card drivers on Windows strip the VLAN tags off the incoming frames before handing them over to the capturing filter of WinPcap or NPcap even if they let VLAN-tagged frames in. So even if you have a monitoring port of a switch which sends you mirrored traffic of a source port through which tagged packets flow, you may not see the tags if capturing on Windows. On most linux drivers this is not a problem. I have no experience on OS X.</p></div><div id="comment-55608-info" class="comment-info"><span class="comment-age">(16 Sep '16, 13:39)</span> sindy</div></div><span id="55610"></span><div id="comment-55610" class="comment"><div id="post-55610-score" class="comment-score"></div><div class="comment-text"><p>Thanks Sindy, that would make sense on why we can't see the id. Any suggestions?</p></div><div id="comment-55610-info" class="comment-info"><span class="comment-age">(16 Sep '16, 15:22)</span> SiO2yH2o</div></div><span id="55611"></span><div id="comment-55611" class="comment"><div id="post-55611-score" class="comment-score"></div><div class="comment-text"><p>on Windows it can be enabled for some Intel NICs: <a href="http://www.intel.com/content/www/us/en/support/network-and-i-o/ethernet-products/000005498.html">http://www.intel.com/content/www/us/en/support/network-and-i-o/ethernet-products/000005498.html</a></p></div><div id="comment-55611-info" class="comment-info"><span class="comment-age">(16 Sep '16, 15:57)</span> Christian_R</div></div><span id="55613"></span><div id="comment-55613" class="comment not_top_scorer"><div id="post-55613-score" class="comment-score"></div><div class="comment-text"><p><a href="https://wiki.wireshark.org/CaptureSetup/VLAN">https://wiki.wireshark.org/CaptureSetup/VLAN</a> might help as well.</p></div><div id="comment-55613-info" class="comment-info"><span class="comment-age">(16 Sep '16, 19:55)</span> Jaap ♦</div></div><span id="55667"></span><div id="comment-55667" class="comment not_top_scorer"><div id="post-55667-score" class="comment-score"></div><div class="comment-text"><p>much appreciated.</p></div><div id="comment-55667-info" class="comment-info"><span class="comment-age">(19 Sep '16, 10:05)</span> SiO2yH2o</div></div></div><div id="comment-tools-55581" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-55581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

