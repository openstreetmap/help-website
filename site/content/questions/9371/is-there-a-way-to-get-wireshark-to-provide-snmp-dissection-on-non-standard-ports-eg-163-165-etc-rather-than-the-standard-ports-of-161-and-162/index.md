+++
type = "question"
title = "Is there a way to get Wireshark to provide SNMP dissection on non-standard ports (e.g. 163, 165, etc.) rather than the standard ports of 161 and 162"
description = '''I have Wireshark performing SNMP dissection of custom MIB. This works great on the standards SNMP ports of 161 and 162. However, when I setup an SNMP agent to use non-standard ports like 163 and 164, multiple agents on a single IP, Wireshark no longer provides SNMP decode. How can I add several port...'''
date = "2012-03-05T16:25:00Z"
lastmod = "2012-03-05T16:41:00Z"
weight = 9371
keywords = [ "dissection", "snmp" ]
aliases = [ "/questions/9371" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a way to get Wireshark to provide SNMP dissection on non-standard ports (e.g. 163, 165, etc.) rather than the standard ports of 161 and 162](/questions/9371/is-there-a-way-to-get-wireshark-to-provide-snmp-dissection-on-non-standard-ports-eg-163-165-etc-rather-than-the-standard-ports-of-161-and-162)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9371-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have Wireshark performing SNMP dissection of custom MIB. This works great on the standards SNMP ports of 161 and 162. However, when I setup an SNMP agent to use non-standard ports like 163 and 164, multiple agents on a single IP, Wireshark no longer provides SNMP decode. How can I add several ports to provide SNMP dissection for display?</p></div><div id="question-tags" class="tags-container tags">dissection snmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '12, 16:25</strong></p><img src="https://secure.gravatar.com/avatar/44c47b4e3980eaf5eb6f365d274b53a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bob2oneil&#39;s gravatar image" /><p>bob2oneil<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bob2oneil has no accepted answers">0%</span></p></div></div><div id="comments-container-9371" class="comments-container"></div><div id="comment-tools-9371" class="comment-tools"></div><div class="clear"></div><div id="comment-9371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9372"></span>

<div id="answer-container-9372" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9372-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sure, just take a look at the first example : <a href="http://wiki.wireshark.org/Lua/Examples">http://wiki.wireshark.org/Lua/Examples</a><br />
Replace port numbers and dissector and you should be good.</p><p>Otherwise, simply use "Decode As" on a file by file basis.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '12, 16:41</strong></p><img src="https://secure.gravatar.com/avatar/e177d49ca6cc8f53ee58cb3de1c4fbaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yul_analyzer&#39;s gravatar image" /><p>yul_analyzer<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yul_analyzer has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Mar '12, 16:53</p></div></div><div id="comments-container-9372" class="comments-container"></div><div id="comment-tools-9372" class="comment-tools"></div><div class="clear"></div><div id="comment-9372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

