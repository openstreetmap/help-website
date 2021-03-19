+++
type = "question"
title = "LLDP unicast doesnt show up in the packet capture"
description = '''Setup: 2960S running SE6 image:  PD(Power Device) connected to port g2/0/47: SPAN port g2/0/14 I am trying to capture the LLDP negotiations between the PD and and the cisco switch. I have the following config on the cisco switch. I have configured the SPAN to capture both side traffic (Rx and Tx) no...'''
date = "2015-05-20T12:05:00Z"
lastmod = "2015-05-20T12:05:00Z"
weight = 42590
keywords = [ "lldp" ]
aliases = [ "/questions/42590" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [LLDP unicast doesnt show up in the packet capture](/questions/42590/lldp-unicast-doesnt-show-up-in-the-packet-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42590-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Setup: 2960S running SE6 image:<br />
PD(Power Device) connected to port g2/0/47:<br />
SPAN port g2/0/14</p><p>I am trying to capture the LLDP negotiations between the PD and and the cisco switch. I have the following config on the cisco switch. I have configured the SPAN to capture both side traffic (Rx and Tx) no cdp lldp run monitor session 1 source interface Gi2/0/47 monitor session 1 destination interface Gi2/0/14 encapsulation replicate</p><p>However, when I capture packets using wireshark on port Gi2/0/14 I only see the LLDP mulicasts and dont see the negotiations between the switch and the PD.</p><p>Any pointers on how to capture the unicasts or if I am missing soemthing?</p><p>Appreciate the help.</p><p>Thanks, RJ</p></div><div id="question-tags" class="tags-container tags">lldp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '15, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/f3baec8dcc041b95ecf9ea6207a77d5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rj251&#39;s gravatar image" /><p>rj251<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rj251 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-42590" class="comments-container"><span id="42595"></span><div id="comment-42595" class="comment"><div id="post-42595-score" class="comment-score"></div><div class="comment-text"><p>You should over to a Cisco users forum, since this is a question on how to configure a Cisco switch for this particular situation.</p></div><div id="comment-42595-info" class="comment-info"><span class="comment-age">(20 May '15, 22:43)</span> Jaap ♦</div></div></div><div id="comment-tools-42590" class="comment-tools"></div><div class="clear"></div><div id="comment-42590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

