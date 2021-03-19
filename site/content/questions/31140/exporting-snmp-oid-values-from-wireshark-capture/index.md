+++
type = "question"
title = "Exporting SNMP OID values from wireshark capture?"
description = '''I am trying to figure out how I can export the SNMP OID values that wireshark picked up. My issue is that when I export the raw data it is all together and not seperated. All I want to to is get only the actual SNMP values it is sending back. When I open up the packet in wireshark I can see it neatl...'''
date = "2014-03-25T01:06:00Z"
lastmod = "2014-03-26T08:13:00Z"
weight = 31140
keywords = [ "sniffing", "mib", "snmp", "tshark", "wireshark" ]
aliases = [ "/questions/31140" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Exporting SNMP OID values from wireshark capture?](/questions/31140/exporting-snmp-oid-values-from-wireshark-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31140-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to figure out how I can export the SNMP OID values that wireshark picked up. My issue is that when I export the raw data it is all together and not seperated.</p><p>All I want to to is get only the actual SNMP values it is sending back. When I open up the packet in wireshark I can see it neatly presented.</p><p>Can anyone offer any assistance?</p><p>Also could you help me do the same with tshark, the command line for wireshark?</p><p>EDIT: As you can see it is sending the values back in hex, this is exactly what I am looking for. I want to export each individual value to a text file.</p></div><div id="question-tags" class="tags-container tags">sniffing mib snmp tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '14, 01:06</strong></p><img src="https://secure.gravatar.com/avatar/6438826b56b89f1ac63250ed5f455095?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joe%20Page&#39;s gravatar image" /><p>Joe Page<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joe Page has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Mar '14, 01:08</p></div></div><div id="comments-container-31140" class="comments-container"><span id="31143"></span><div id="comment-31143" class="comment"><div id="post-31143-score" class="comment-score"></div><div class="comment-text"><p>In Wireshark you could create a column for the field, export it as CSV and customize it in Excel.</p></div><div id="comment-31143-info" class="comment-info"><span class="comment-age">(25 Mar '14, 01:58)</span> Roland</div></div></div><div id="comment-tools-31140" class="comment-tools"></div><div class="clear"></div><div id="comment-31140-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31174"></span>

<div id="answer-container-31174" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31174-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try this</p><blockquote><p>tshark.exe -nr input.pcap -Y "snmp" -T fields -e frame.number -e snmp.name -E header=yes -E separator=;</p></blockquote><p>Hint: If -Y does not work on your system, try -R.</p><p>Sample output:</p><pre><code>frame.number;snmp.name
1;1.3.6.1.2.1.1.2.0
2;1.3.6.1.2.1.1.2.0
3;1.3.6.1.2.1.1.5.0,1.3.6.1.2.1.1.6.0
4;1.3.6.1.2.1.1.5.0,1.3.6.1.2.1.1.6.0</code></pre><p>Obviously you can add more fields with -e xxxx (see the <a href="http://www.wireshark.org/docs/dfref/">display filter reference guide</a>).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '14, 08:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Mar '14, 08:13</p></div></div><div id="comments-container-31174" class="comments-container"></div><div id="comment-tools-31174" class="comment-tools"></div><div class="clear"></div><div id="comment-31174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

