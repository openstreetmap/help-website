+++
type = "question"
title = "ModBus TCP continuously disconnecting"
description = '''Hi,  I have a Modbus device connected to an ABB CI867 interface using a Modbus/TCP converter. Connection keeps on dropping every 2 seconds. I have some issue understanding the WireShark analysis. Could anyone help me? Here is the Scan: https://www.cloudshark.org/captures/e383e599f1b4 Thank you for y...'''
date = "2014-03-19T17:43:00Z"
lastmod = "2014-03-20T03:13:00Z"
weight = 30977
keywords = [ "modbus", "tcp" ]
aliases = [ "/questions/30977" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [ModBus TCP continuously disconnecting](/questions/30977/modbus-tcp-continuously-disconnecting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30977-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a Modbus device connected to an ABB CI867 interface using a Modbus/TCP converter. Connection keeps on dropping every 2 seconds. I have some issue understanding the WireShark analysis. Could anyone help me?</p><p>Here is the Scan: <a href="https://www.cloudshark.org/captures/e383e599f1b4">https://www.cloudshark.org/captures/e383e599f1b4</a></p><p>Thank you for your help</p></div><div id="question-tags" class="tags-container tags">modbus tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '14, 17:43</strong></p><img src="https://secure.gravatar.com/avatar/e8feaa2577a31d3b2f6ed176b793881a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beber_NC&#39;s gravatar image" /><p>Beber_NC<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beber_NC has no accepted answers">0%</span></p></div></div><div id="comments-container-30977" class="comments-container"></div><div id="comment-tools-30977" class="comment-tools"></div><div class="clear"></div><div id="comment-30977-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30980"></span>

<div id="answer-container-30980" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30980-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Did you notice that the last message before the FIN packet in each session contains <em>"RTU check CRC failed, Receive query again"</em> ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '14, 22:43</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-30980" class="comments-container"></div><div id="comment-tools-30980" class="comment-tools"></div><div class="clear"></div><div id="comment-30980-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30982"></span>

<div id="answer-container-30982" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30982-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As per the answer by @mrEEde the RTU (172.19.197.32) is returning some ASCII text after its response to the query request, and it's likely that the Modbus master is choking on this and subsequently closing the connection.</p><p>The text "RTU check CRC failed, Receive query again" looks like some form of diagnostic output from the RTU which shouldn't be sent over the data connection. Note that when using Modbus/TCP the standard Modbus CRC isn't used, <del>is the RTU actually a serial device connected via some form of terminal server</del> I see you are using a Modbus/TCP converter, maybe it is incorrectly configured?</p><p>Another observation in your capture is duplicated packets, probably due to your capture setup involving mirroring or spanning switch ports. These dups can be removed by using editcap.</p><p>A final observation is that your capture also contains traffic not relevant to your question, that leaks details about your network environment, e.g. netbios-ns packets. You might want to filter your captures a little better before posting them publicly, although I don't think you've let anything too bad out this time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '14, 03:13</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-30982" class="comments-container"></div><div id="comment-tools-30982" class="comment-tools"></div><div class="clear"></div><div id="comment-30982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

