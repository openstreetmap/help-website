+++
type = "question"
title = "time of event  extraction for waveform generation"
description = '''Wireshark is capturing our SysLog broadcast packets which identify different waveform edges in a controller, such as &quot;1 rising edge&quot; and &quot;2 falling edge&quot; and we would like to automate the generation of timing diagrams and basically turn Wireshark into an oscilloscope. Seems like this would not be to...'''
date = "2015-07-28T10:49:00Z"
lastmod = "2015-07-28T11:40:00Z"
weight = 44573
keywords = [ "filter", "syslog", "waveform804" ]
aliases = [ "/questions/44573" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [time of event extraction for waveform generation](/questions/44573/time-of-event-extraction-for-waveform-generation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44573-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark is capturing our SysLog broadcast packets which identify different waveform edges in a controller, such as "1 rising edge" and "2 falling edge" and we would like to automate the generation of timing diagrams and basically turn Wireshark into an oscilloscope. Seems like this would not be to hard but do you have examples of extraction filters that could find SysLog (Port 514 UDP) and then match the first number in the field of the SysLog message? Thanks!</p></div><div id="question-tags" class="tags-container tags">filter syslog waveform804</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '15, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/683d81c0b9cff4fac2a396e04df5b51f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sam%20Mallicoat&#39;s gravatar image" /><p>Sam Mallicoat<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sam Mallicoat has no accepted answers">0%</span></p></div></div><div id="comments-container-44573" class="comments-container"></div><div id="comment-tools-44573" class="comment-tools"></div><div class="clear"></div><div id="comment-44573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44574"></span>

<div id="answer-container-44574" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44574-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried something like this: (udp.port == 514) and (udp[8:3]==81:60:03) or like this<br />
(udp.port == 514) and (syslog.msg matches "RegularExpression")</p><p>The reference can be found here: <a href="https://wiki.wireshark.org/DisplayFilters">https://wiki.wireshark.org/DisplayFilters</a></p><p>Furthermore I would suggest that you should use Version 1.99.8 because it comes with improved I/O Graph functions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '15, 11:40</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jul '15, 13:02</p></div></div><div id="comments-container-44574" class="comments-container"></div><div id="comment-tools-44574" class="comment-tools"></div><div class="clear"></div><div id="comment-44574-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

