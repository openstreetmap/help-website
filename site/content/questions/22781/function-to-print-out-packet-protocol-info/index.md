+++
type = "question"
title = "Function to print out packet protocol info"
description = '''When I debug Wireshark in VS2010 and I set a breakpoint at the place of :  row = packet_list_append(cinfo, fdata, &amp;amp;edt.pi);  I have noticed that the parameter of &quot;to_read&quot; means that Wireshark get a number of packets from the capture file in a &quot;while&quot; loop until &quot;to_read&quot; is zero.  The column in...'''
date = "2013-07-09T21:45:00Z"
lastmod = "2013-07-09T21:45:00Z"
weight = 22781
keywords = [ "print", "function", "code", "list", "packet" ]
aliases = [ "/questions/22781" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Function to print out packet protocol info](/questions/22781/function-to-print-out-packet-protocol-info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22781-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I debug Wireshark in VS2010 and I set a breakpoint at the place of : row = packet_list_append(cinfo, fdata, &amp;edt.pi); I have noticed that the parameter of "to_read" means that Wireshark get a number of packets from the capture file in a "while" loop until "to_read" is zero. The column info of each packet is filled in every time the packet is dissected. However, about the number of "to_read" of packet info are displayed in one step. There must be a packet list or some structure like that to store the printing info, I guess. Now I want to figure out the functions to print out the displayed info in the window as I am planning to insert these packets info into database in one step, too. Thank you!</p></div><div id="question-tags" class="tags-container tags">print function code list packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '13, 21:45</strong></p><img src="https://secure.gravatar.com/avatar/df5946b250ac0802ce044aef61aa1402?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="constance&#39;s gravatar image" /><p>constance<br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="constance has no accepted answers">0%</span></p></div></div><div id="comments-container-22781" class="comments-container"></div><div id="comment-tools-22781" class="comment-tools"></div><div class="clear"></div><div id="comment-22781-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

