+++
type = "question"
title = "modbus/tcp register address display look like a relative."
description = '''my customer captured that modbus/tcp data from PLC to PC. i want to find a unique int32 value by register address. but the data displayed register address look like a relative. e.g. Register 0(INT32):123 Register 2(INT32):123 Register 4(INT32):123  I want to display look like a absolute. e.g. Regist...'''
date = "2017-02-13T04:09:00Z"
lastmod = "2017-02-13T05:00:00Z"
weight = 59364
keywords = [ "modbus", "register", "tcp" ]
aliases = [ "/questions/59364" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [modbus/tcp register address display look like a relative.](/questions/59364/modbustcp-register-address-display-look-like-a-relative)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59364-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>my customer captured that modbus/tcp data from PLC to PC.<br />
i want to find a unique int32 value by register address.<br />
but the data displayed register address look like a relative.<br />
e.g.<br />
Register 0(INT32):123<br />
Register 2(INT32):123<br />
Register 4(INT32):123<br />
</p><p>I want to display look like a absolute.<br />
e.g.<br />
Register 40001(INT32):123<br />
Register 40003(INT32):123<br />
Register 40005(INT32):123</p><p>How's it change configure or solution.<br />
please tell me.<br />
Regards.</p></div><div id="question-tags" class="tags-container tags">modbus register tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '17, 04:09</strong></p><img src="https://secure.gravatar.com/avatar/1d56182a98e52e2d54112fb0c0c1639f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rockman29&#39;s gravatar image" /><p>Rockman29<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rockman29 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-59364" class="comments-container"></div><div id="comment-tools-59364" class="comment-tools"></div><div class="clear"></div><div id="comment-59364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59366"></span>

<div id="answer-container-59366" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59366-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't (without modifying the Modbus dissector), however it's mostly a matter of convention.</p><p>Modbus "programmers" (humans or software tools) use 1-based register addresses such as 40001 to indicate a 16 bit holding (output) register, but in the "over-the wire" protocol that actually becomes a "Read Holding Registers" command (0x03) with a starting address 0f 0x0000, as the protocol uses 0-based addresses and this is the source of lots of confusion. Similarly an input register "programmers" address such as 30001 appears as starting address 0x0000 for a "Read Input Registers" command (0x04).</p><p>The dissector displays the 0-based addresses of the protocol, not the 1-based addresses that "programmers" may be more familiar with. There are also Modbus programming tools out there that use the 3xxxx and 4xxxx based addresses but are 0-based, and there are other manufacturers, e.g. Koyo that instead of a leading 3 or 4 digit use text strings such as IR or HR (for Input Register and Holding Register respectively) and either 0-base or 1-based starting addresses.</p><p>There are further conventions such as combining multiple registers to create larger values, such as 2 off 16 bit registers into a 32 bit value, which the dissector does support in the preferences that allows you to set the Holding/Input Register format (as we can see from your example), but note that this setting applies to ALL Input/Holding registers so can be awkward if you have registers using mixed formats in the same PLC.</p><p>The dissector does not generate synthesised data such as the "programmers" address by converting a "Read Holding Registers" with starting address 0x0000 into 40001 as with all the possible 1-based and 0-based confusion, along with the other formats such as Koyo, doing so might mislead "programmers", so it's felt best to stick with the actual protocol values.</p><p><strong>Edit</strong></p><p>It's actually a little worse than I remembered, the Modbus protocol does not include the starting address in the response from the PLC, so a strict dissection of the response can't show the register address but the dissector "remembers" the address in the request (which shares the transaction identifier with the response) and uses that to display the register values in the response.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '17, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Feb '17, 09:05</p></div></div><div id="comments-container-59366" class="comments-container"><span id="59391"></span><div id="comment-59391" class="comment"><div id="post-59391-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your Answer.<br />
I got it.<br />
I didn't know Modbus protocol does not include the starting address.<br />
usually I show like absolutely address, because include query(have starting address) and response that linking automatically by wireshark.<br />
Regards.</p></div><div id="comment-59391-info" class="comment-info"><span class="comment-age">(13 Feb '17, 16:49)</span> Rockman29</div></div></div><div id="comment-tools-59366" class="comment-tools"></div><div class="clear"></div><div id="comment-59366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

