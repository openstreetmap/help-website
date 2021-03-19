+++
type = "question"
title = "How to decode Timeticks (Hundreds seconds) to readable date time"
description = '''Hi All, sorry if I&#x27;m disturbing for probably stupid question . I&#x27;m looking for a way to decode directly from wireshark (I&#x27;m actually using release 1.8.2) the timeticks from the hundred seconds view, like: (Wireshark running on top of Windows XD Professional): Object Name: 1.3.6.1.2.1.1.3.0 (iso.3.6....'''
date = "2012-09-03T01:54:00Z"
lastmod = "2012-09-03T03:54:00Z"
weight = 14002
keywords = [ "eaping", "circuit" ]
aliases = [ "/questions/14002" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to decode Timeticks (Hundreds seconds) to readable date time](/questions/14002/how-to-decode-timeticks-hundreds-seconds-to-readable-date-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14002-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>sorry if I'm disturbing for probably stupid question .</p><p>I'm looking for a way to decode directly from wireshark (I'm actually using release 1.8.2) the timeticks from the hundred seconds view, like:</p><p>(Wireshark running on top of Windows XD Professional):</p><p>Object Name: 1.3.6.1.2.1.1.3.0 (iso.3.6.1.2.1.1.3.0) Value (TimeTicks): 129528167</p><p>to a readable values (Solaris 10 Example):</p><p>bash-3.00$ /usr/sfw/bin/snmpget -v2c -c public 10.194.34.18 1.3.6.1.2.1.1.3.0</p><p>DISMAN-EVENT-MIB::sysUpTimeInstance = Timeticks: (1525917187) <strong>176 days, 14:39:31.87</strong></p><p>is there any action that I can do on Wireshark or on Windows.</p><p>Best Regards</p><p>Alessandro.</p></div><div id="question-tags" class="tags-container tags">eaping circuit</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Sep '12, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/78f0241b8ff38fe426d3e512ffc23eeb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alessandro&#39;s gravatar image" /><p>Alessandro<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alessandro has no accepted answers">0%</span></p></div></div><div id="comments-container-14002" class="comments-container"></div><div id="comment-tools-14002" class="comment-tools"></div><div class="clear"></div><div id="comment-14002-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14003"></span>

<div id="answer-container-14003" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14003-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>is there any action that I can do on Wireshark or on Windows.</p></blockquote><p><strong>Wireshark</strong></p><ul><li>You can extend the <a href="http://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-snmp.c">SNMP dissector</a> to convert the time ticks</li><li>You can write a Lua SNMP Postdissector (<a href="http://lmgtfy.com/?q=Lua+postdissector">link#1</a> / <a href="http://lmgtfy.com/?q=site%3Aask.wireshark.org+Lua+postdissector">link#2</a>) to convert the time ticks.</li></ul><p><strong>Windows</strong></p><ul><li>Use the builtin calculator to convert the time.</li></ul><blockquote><p>1525917187 / 8640000 = <strong>days</strong> (+remainder) = <strong>176</strong>.6107855324074<br />
0.6107855324074 * 24 = <strong>hours</strong> (+remainder) = <strong>14</strong>.65885277777778<br />
0.65885277777778 * 60 = <strong>minutes</strong> (+remainder) = <strong>39</strong>.53116666666667<br />
0.53116666666667 * 60 = <strong>seconds.milliseconds</strong> = <strong>31.87</strong></p></blockquote><ul><li>Use your preferred scritping language to automate that process</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Sep '12, 03:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-14003" class="comments-container"><span id="14004"></span><div id="comment-14004" class="comment"><div id="post-14004-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>thanx for the answer, I appreciate.</p><p>I would like to use your first option adding an SNMP Dissector , but I don't know the procedure how to do it .</p><p>could you help on this too ?</p><p>Best Regards</p><p>Alessandro.</p></div><div id="comment-14004-info" class="comment-info"><span class="comment-age">(03 Sep '12, 05:02)</span> Alessandro</div></div><span id="14006"></span><div id="comment-14006" class="comment"><div id="post-14006-score" class="comment-score"></div><div class="comment-text"><p>you don't have to add a dissector, you just need to extend the existing SNMP dissector.</p><blockquote><p>but I don't know the procedure how to do it.</p></blockquote><p>O.K., you will need some programming skills and some C know how. Then read the developer guide and take a look at the SNMP dissector code.</p><blockquote><p><code>http://www.wireshark.org/docs/wsdg_html_chunked/</code><br />
<code>http://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-snmp.c</code></p></blockquote></div><div id="comment-14006-info" class="comment-info"><span class="comment-age">(03 Sep '12, 08:08)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-14003" class="comment-tools"></div><div class="clear"></div><div id="comment-14003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

