+++
type = "question"
title = "Export Packet Bytes of decrypted SSL data"
description = '''I have a packet of SSL data which is in a proprietary format. The &quot;Decrypted SSL Data&quot; tab is open and correctly shows the decrypted data. I now need to export this decrypted data as binary. How do I do this in Wireshark 2.0.0rc1? I would expect to see an entry for unencrypted application data under...'''
date = "2015-10-27T05:24:00Z"
lastmod = "2015-10-27T06:21:00Z"
weight = 46983
keywords = [ "ssl", "export" ]
aliases = [ "/questions/46983" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Export Packet Bytes of decrypted SSL data](/questions/46983/export-packet-bytes-of-decrypted-ssl-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46983-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a packet of SSL data which is in a proprietary format.</p><p>The "Decrypted SSL Data" tab is open and correctly shows the decrypted data.</p><p>I now need to export this decrypted data as binary.</p><p>How do I do this in Wireshark 2.0.0rc1?</p><p>I would expect to see an entry for unencrypted application data under TLSv1 Record Layer in the tree view (as I think was the case under Wireshark 1.12.8) so I can right click and Export Packet Bytes, but there is no such entry in the tree for unencrypted application data, only an entry for encrypted application data.</p><p>I have also looked at Follow - Follow SSL, but this gives a blank dialog box. Also File - Export Packet Bytes exports the encrypted data, as you would expect.</p><p>Thanks</p><p>Robert</p></div><div id="question-tags" class="tags-container tags">ssl export</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '15, 05:24</strong></p><img src="https://secure.gravatar.com/avatar/03bd741d32edec34e0d3ec40d6f92fdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ronslow&#39;s gravatar image" /><p>ronslow<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ronslow has no accepted answers">0%</span></p></div></div><div id="comments-container-46983" class="comments-container"></div><div id="comment-tools-46983" class="comment-tools"></div><div class="clear"></div><div id="comment-46983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46985"></span>

<div id="answer-container-46985" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46985-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I just tried <a href="https://www.wireshark.org/download/automated/win64/Wireshark-win64-2.1.0-261-g616dbd7.exe">Wireshark-win64-2.1.0-261-g616dbd7.exe</a>. Follow -&gt; SSL Stream works for the snakeoil pcap. Maybe you want to try that version.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '15, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Oct '15, 06:22</p></div></div><div id="comments-container-46985" class="comments-container"><span id="46989"></span><div id="comment-46989" class="comment"><div id="post-46989-score" class="comment-score"></div><div class="comment-text"><p>Yup. Thanks Kurt. Upgrade solved the problem.</p></div><div id="comment-46989-info" class="comment-info"><span class="comment-age">(27 Oct '15, 07:02)</span> ronslow</div></div></div><div id="comment-tools-46985" class="comment-tools"></div><div class="clear"></div><div id="comment-46985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

