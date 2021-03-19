+++
type = "question"
title = "Capturing SNMP Traces to MYSQL Database or CSV file at RunTime"
description = '''Is it possible via Wireshark to capture SNMP traces to mysql database or any csv file at runtime?'''
date = "2011-02-18T01:51:00Z"
lastmod = "2011-02-19T01:43:00Z"
weight = 2414
keywords = [ "mysql", "snmp", "csv", "wireshark" ]
aliases = [ "/questions/2414" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing SNMP Traces to MYSQL Database or CSV file at RunTime](/questions/2414/capturing-snmp-traces-to-mysql-database-or-csv-file-at-runtime)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2414-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible via Wireshark to capture SNMP traces to mysql database or any csv file at runtime?</p></div><div id="question-tags" class="tags-container tags">mysql snmp csv wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '11, 01:51</strong></p><img src="https://secure.gravatar.com/avatar/2cb4948e057882fc388865120eb28b67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="piyush&#39;s gravatar image" /><p>piyush<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="piyush has no accepted answers">0%</span></p></div></div><div id="comments-container-2414" class="comments-container"></div><div id="comment-tools-2414" class="comment-tools"></div><div class="clear"></div><div id="comment-2414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2424"></span>

<div id="answer-container-2424" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2424-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There's nothing out of the box that will work as far as I know, but with a bit of scripting you can do just that.</p><p>You have a choice of perl,python or lua For perl you'd have to parse output of tshark either via pdml or text directly</p><p>Python and lua allow you to write extensions/plugins in wireshark, give you access to filters and dissectors which is pretty cool.</p><p>My personal preference would be lua as it's been in wireshark longer and there are more examples out there.</p><p>Checkout "Dump VoIP calls into separate files" on wireshark wiki <a href="http://wiki.wireshark.org/Lua/Examples">Lua Examples</a> In this example you can see how SIP call records are being dumped into MySQL database. That should get you started.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '11, 01:43</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p>izopizo<br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Feb '11, 01:47</p></div></div><div id="comments-container-2424" class="comments-container"></div><div id="comment-tools-2424" class="comment-tools"></div><div class="clear"></div><div id="comment-2424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

