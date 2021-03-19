+++
type = "question"
title = "How to check RLC-LTE -Logger  output in wireshark"
description = '''Hi all, Thank you for your valuable support. I want to run the rlc_lte_logger.c which is available in RLC-LTE Wireshark link.Whether I have to run from source code directory or somewhere in wireshark installed directory.How to check the RLC-LTE PDU FRAMES output in wireshark window.what are the sett...'''
date = "2015-03-28T23:50:00Z"
lastmod = "2015-03-29T01:52:00Z"
weight = 40976
keywords = [ "dissector" ]
aliases = [ "/questions/40976" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to check RLC-LTE -Logger output in wireshark](/questions/40976/how-to-check-rlc-lte-logger-output-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40976-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>Thank you for your valuable support.</p><p>I want to run the rlc_lte_logger.c which is available in RLC-LTE Wireshark link.Whether I have to run from source code directory or somewhere in wireshark installed directory.How to check the RLC-LTE PDU FRAMES output in wireshark window.what are the settings I have to make in wireshark.Please explain me in detail.<br />
</p><p>Thanks and regards, Sathish.</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '15, 23:50</strong></p><img src="https://secure.gravatar.com/avatar/7ba5607f38325cbf87766b918e1d76a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sathish%20kannan&#39;s gravatar image" /><p>Sathish kannan<br />
<span class="score" title="6 reputation points">6</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sathish kannan has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-40976" class="comments-container"></div><div id="comment-tools-40976" class="comment-tools"></div><div class="clear"></div><div id="comment-40976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40979"></span>

<div id="answer-container-40979" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40979-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In Wireshark, you must ensure that the following options are checked:</p><ul><li>Edit -&gt; Preferences -&gt; Protocols -&gt; UDP -&gt; Try heuristic sub-dissectors first</li><li>Edit -&gt; Preferences -&gt; Protocols -&gt; RLC-LTE -&gt; Try heuristic LTE-RLC over UDP framing</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '15, 01:52</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-40979" class="comments-container"><span id="40983"></span><div id="comment-40983" class="comment"><div id="post-40983-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal,</p><p>Thank you for your reply.</p><p>I want to know in which directory in the wireshark I can run that sample rlc-lte logger program which is available in RLC-LTE wiki.<br />
</p><p>Thanks, Sathish</p></div><div id="comment-40983-info" class="comment-info"><span class="comment-age">(29 Mar '15, 10:14)</span> Sathish kannan</div></div><span id="40984"></span><div id="comment-40984" class="comment"><div id="post-40984-score" class="comment-score"></div><div class="comment-text"><p>The sample program is completely independent of Wireshark. It opens a UDP socket towards the IP address and port given as argument, and sends 3 hardcoded PDUs. It can be run from whatever place you want.</p></div><div id="comment-40984-info" class="comment-info"><span class="comment-age">(29 Mar '15, 11:21)</span> Pascal Quantin</div></div><span id="40988"></span><div id="comment-40988" class="comment"><div id="post-40988-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal,</p><p>Thank you for your reply.</p><p>I want to know how to check 3 hardcoded RLC-LTE PDUs in wireshark. whether it shows like UDP PROTOCOL or RLC-LTE PROTOCOL.</p><p>Thanks, Sathish</p></div><div id="comment-40988-info" class="comment-info"><span class="comment-age">(29 Mar '15, 23:28)</span> Sathish kannan</div></div><span id="41002"></span><div id="comment-41002" class="comment"><div id="post-41002-score" class="comment-score"></div><div class="comment-text"><p>You need to capture on the interface corresponding to the address you give as parameter to the rlc_lte_logger program (that you compiled yourself- see the source code for details) and configure Wireshark per my first answer. If everything is configured properly, it will appear as RLC-LTE.</p><p>To compile the program, by default it expects to be in a folder next to wireshark source code:</p><p>include "../wireshark/epan/dissectors/packet-rlc-lte.h"</p><p>You can modify this line according to your needs.</p></div><div id="comment-41002-info" class="comment-info"><span class="comment-age">(30 Mar '15, 04:32)</span> Pascal Quantin</div></div></div><div id="comment-tools-40979" class="comment-tools"></div><div class="clear"></div><div id="comment-40979-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

