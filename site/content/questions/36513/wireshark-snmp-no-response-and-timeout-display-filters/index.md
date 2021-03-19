+++
type = "question"
title = "Wireshark SNMP no-response and timeout display filters"
description = '''I&#x27;m using Wireshark 1.12.0 to analyze SNMP captures for timeouts. I have tried to examine Wireshark SNMP Display Filter Reference (https://www.wireshark.org/docs/dfref/s/snmp.html) without much success in figuring out the correct filters. Can someone please point me to how I can find out the answer ...'''
date = "2014-09-22T21:48:00Z"
lastmod = "2014-09-23T06:28:00Z"
weight = 36513
keywords = [ "wireshark-1.12", "snmpwireshark", "snmp" ]
aliases = [ "/questions/36513" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark SNMP no-response and timeout display filters](/questions/36513/wireshark-snmp-no-response-and-timeout-display-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36513-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using Wireshark 1.12.0 to analyze SNMP captures for timeouts. I have tried to examine Wireshark SNMP Display Filter Reference (<a href="https://www.wireshark.org/docs/dfref/s/snmp.html)">https://www.wireshark.org/docs/dfref/s/snmp.html)</a> without much success in figuring out the correct filters.</p><p>Can someone please point me to how I can find out the answer to the following questions:</p><p>1). What is the Wireshark display filter to identify SNMP requests that take more than X seconds to respond to?</p><p>2). What is the Wireshark display filter to identify SNMP requests that do not have corresponding responses?</p><p>Your assistance is greatly appreciated, thank you in advance.</p></div><div id="question-tags" class="tags-container tags">wireshark-1.12 snmpwireshark snmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '14, 21:48</strong></p><img src="https://secure.gravatar.com/avatar/6338dbe8035c332e699a984187f84768?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jasfoor&#39;s gravatar image" /><p>jasfoor<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jasfoor has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Sep '14, 05:39</p></div></div><div id="comments-container-36513" class="comments-container"></div><div id="comment-tools-36513" class="comment-tools"></div><div class="clear"></div><div id="comment-36513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36521"></span>

<div id="answer-container-36521" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36521-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you're out of luck, the SNMP dissector doesn't do any request\response tracking, so there's nothing to filter on.</p><p>You can probably achieve your requirements by some form of scripting, either internally in Wireshark using <a href="http://wiki.wireshark.org/Lua">Lua</a> or possibly <a href="http://wiki.wireshark.org/Mate">MATE</a>, or externally using the scripting technology of your choice to parse tshark output.</p><p>You could raise an enhancement request on the Wireshark <a href="https://bugs.wireshark.org/bugzilla/">Bugzilla</a> to add request\response tracking to the SNMP dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '14, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-36521" class="comments-container"><span id="36523"></span><div id="comment-36523" class="comment"><div id="post-36523-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the input @grahamb.</p></div><div id="comment-36523-info" class="comment-info"><span class="comment-age">(23 Sep '14, 07:46)</span> jasfoor</div></div><span id="36558"></span><div id="comment-36558" class="comment"><div id="post-36558-score" class="comment-score"></div><div class="comment-text"><p>I've given you all your reputation points back, to accept an answer simply click the checkmark icon next to the answer.</p></div><div id="comment-36558-info" class="comment-info"><span class="comment-age">(24 Sep '14, 02:04)</span> grahamb ♦</div></div></div><div id="comment-tools-36521" class="comment-tools"></div><div class="clear"></div><div id="comment-36521-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

