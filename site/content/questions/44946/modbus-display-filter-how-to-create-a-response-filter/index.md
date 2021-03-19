+++
type = "question"
title = "Modbus display filter - how to create a response filter"
description = '''I have a Modbus capture file that contains a total of 133,000 packets. Among those packets are 1,500 error register queries. How is a filter created to display the non-zero responses to that register query? '''
date = "2015-08-10T09:19:00Z"
lastmod = "2015-08-10T09:42:00Z"
weight = 44946
keywords = [ "modbus", "modbus-filter", "response-filter" ]
aliases = [ "/questions/44946" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Modbus display filter - how to create a response filter](/questions/44946/modbus-display-filter-how-to-create-a-response-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44946-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a Modbus capture file that contains a total of 133,000 packets. Among those packets are 1,500 error register queries.<br />
How is a filter created to display the non-zero responses to that register query?<br />
</p></div><div id="question-tags" class="tags-container tags">modbus modbus-filter response-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Aug '15, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/569e1e49378a146ced96ca53ececf1b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="capesp&#39;s gravatar image" /><p>capesp<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="capesp has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-44946" class="comments-container"></div><div id="comment-tools-44946" class="comment-tools"></div><div class="clear"></div><div id="comment-44946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44947"></span>

<div id="answer-container-44947" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44947-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's a bit tricky as there's no real "direction" indicator in Modbus so you'll maybe have to use the source IP address, are all the responses from the same RTU? If they are, use the RTU address as the source IP address, if not use the master's address as the destination IP address.</p><p>In addition, determining an error from a reply is done with the function code, an error has 0x80 added to the function code. I think you'll need something like:</p><p><code>(ip.src == "RTU IP") &amp;&amp; (modbus.func_code &lt; 0x80)</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '15, 09:42</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Aug '15, 09:42</p></div></div><div id="comments-container-44947" class="comments-container"><span id="44949"></span><div id="comment-44949" class="comment"><div id="post-44949-score" class="comment-score"></div><div class="comment-text"><p>Thank you, Graham, for your quick response.</p><p>The register data in the valid Modbus response contains the slave device error status that can be OR'd to include more than a single error. This requires a register data search for any non-zero data value.</p><p>The captured Modbus traffic is between only two devices 192.168.2.31 and 192.168.1.102. Filtering on FC '3' reduces the packet count to 98K, while filtering on (modbus.reference_num == 2110) reduces packet count to 1534.<br />
</p><p>The core of the problem is to identify the non-zero register values in the <em>responses</em> to a FC '3' query of register '2110'.</p></div><div id="comment-44949-info" class="comment-info"><span class="comment-age">(10 Aug '15, 10:01)</span> capesp</div></div><span id="44950"></span><div id="comment-44950" class="comment"><div id="post-44950-score" class="comment-score"></div><div class="comment-text"><p>OK, so not a modbus error, but a specific data value. Are the requests only for the single register 2110, or is that register found in other requests, maybe in the middle of a block?</p><p>If the register result is always at a specific offset in the response then a filter can be constructed for the offset.</p></div><div id="comment-44950-info" class="comment-info"><span class="comment-age">(10 Aug '15, 10:19)</span> grahamb ♦</div></div><span id="44951"></span><div id="comment-44951" class="comment"><div id="post-44951-score" class="comment-score"></div><div class="comment-text"><p>The request is always for the single register 2110 with FC 3.</p></div><div id="comment-44951-info" class="comment-info"><span class="comment-age">(10 Aug '15, 11:34)</span> capesp</div></div><span id="44959"></span><div id="comment-44959" class="comment"><div id="post-44959-score" class="comment-score">1</div><div class="comment-text"><p>That's more difficult as the response has no indication of which register(s) was requested, so this would require pattern matching across both the request and response which Wireshark filters can't do.</p><p>If all the read holding register (FC 3), single register responses are for the required register address then a filter can be constructed for the specific bytes you're interested in, however if there are reads for other single register addresses mixed in then this can't be done.</p><p>The Modbus dissector could be enhanced to add conversation info to the response indicating the requested register addresses to allow such a filter to be created. The <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a> is the place for an enhancement request.</p></div><div id="comment-44959-info" class="comment-info"><span class="comment-age">(11 Aug '15, 03:38)</span> grahamb ♦</div></div><span id="44972"></span><div id="comment-44972" class="comment"><div id="post-44972-score" class="comment-score"></div><div class="comment-text"><p>I appreciate your help and insight, Graham.</p><p>The answer was not as promising as I had hoped. Your suggestion for an enhancement to the Modbus dissector is the most probable solution in the long-term. A macro along with some manual searching might be the only way to identify the error packet in the short-term.</p><p>An expansion of the 'conversation' feature to a 'query conversation' would be a natural and useful extension of the Modbus dissector.</p></div><div id="comment-44972-info" class="comment-info"><span class="comment-age">(11 Aug '15, 15:41)</span> capesp</div></div></div><div id="comment-tools-44947" class="comment-tools"></div><div class="clear"></div><div id="comment-44947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

