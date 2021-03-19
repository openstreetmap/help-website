+++
type = "question"
title = "Calculate RTT using TSecr field"
description = '''Hey guys, I have a basic question which I&#x27;m stucked.... Im trying to use the TSecr (tcp.options.timestamp.tsecr) in order to help me calculate RTT since its stores time info from the sending server... I just dont have any clue how to transform the values of Tsecr into time information in order to ca...'''
date = "2012-07-17T00:39:00Z"
lastmod = "2012-07-17T01:26:00Z"
weight = 12793
keywords = [ "rtt" ]
aliases = [ "/questions/12793" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Calculate RTT using TSecr field](/questions/12793/calculate-rtt-using-tsecr-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12793-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys,</p><p>I have a basic question which I'm stucked....</p><p>Im trying to use the TSecr (tcp.options.timestamp.tsecr) in order to help me calculate RTT since its stores time info from the sending server...</p><p>I just dont have any clue how to transform the values of Tsecr into time information in order to calculate the RTT. As far as I understood RTT would be RTT = Actual Time (for ACK) - TSecr but since it seems that TSecr is a field of 32 bits I have no clue how to transform it into time reference in order to help into RTT calculations.</p><p>Kind Regards Bruno</p></div><div id="question-tags" class="tags-container tags">rtt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '12, 00:39</strong></p><img src="https://secure.gravatar.com/avatar/bfffd4e7d5d1ae2e013132b7b84d62e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bmaia18&#39;s gravatar image" /><p>bmaia18<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bmaia18 has no accepted answers">0%</span></p></div></div><div id="comments-container-12793" class="comments-container"></div><div id="comment-tools-12793" class="comment-tools"></div><div class="clear"></div><div id="comment-12793-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12794"></span>

<div id="answer-container-12794" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12794-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The value of the TSecr field are in 'ticks' where the advise is to use a value between 1ms and 1s for each tick. But each system uses it's own tick value. So in order to use the TSecr value to calulate a time difference, you must first calculate the tick value for the specific host.</p><p>See <a href="http://www.ietf.org/rfc/rfc1323.txt">RFC 1323</a> paragraph 4.2.2</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '12, 01:26</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-12794" class="comments-container"></div><div id="comment-tools-12794" class="comment-tools"></div><div class="clear"></div><div id="comment-12794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

