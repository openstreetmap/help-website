+++
type = "question"
title = "How to enable the tshark name resolution while exporting to csv from an already captured pcapng file"
description = '''Hi, How to enable the tshark name resolution while exporting to a csv from an already captured pcapng file.. When export from wireshark UI i get the resolved src/dest ip...but when i try to do from tshark the name resolution is not working...is there anything i need to do to get the resolved names i...'''
date = "2012-08-02T02:56:00Z"
lastmod = "2012-08-03T01:38:00Z"
weight = 13310
keywords = [ "pcapng", "csv", "export", "tshark", "wireshark" ]
aliases = [ "/questions/13310" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to enable the tshark name resolution while exporting to csv from an already captured pcapng file](/questions/13310/how-to-enable-the-tshark-name-resolution-while-exporting-to-csv-from-an-already-captured-pcapng-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13310-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, How to enable the tshark name resolution while exporting to a csv from an already captured pcapng file.. When export from wireshark UI i get the resolved src/dest ip...but when i try to do from tshark the name resolution is not working...is there anything i need to do to get the resolved names in the csv ?</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags">pcapng csv export tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '12, 02:56</strong></p><img src="https://secure.gravatar.com/avatar/0cc304949a3522f39e3564b6ef633717?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ArunDev&#39;s gravatar image" /><p>ArunDev<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ArunDev has no accepted answers">0%</span></p></div></div><div id="comments-container-13310" class="comments-container"></div><div id="comment-tools-13310" class="comment-tools"></div><div class="clear"></div><div id="comment-13310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13340"></span>

<div id="answer-container-13340" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13340-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First check if network name resolving is enabled:</p><blockquote><p><strong><code>windows:</code></strong><code>tshark -G currentprefs | find "resolve"</code><br />
<strong><code>unix:</code></strong><code>tshark -G currentprefs | grep "resolve"</code><br />
<code>Result: name_resolve: FALSE</code><br />
</p></blockquote><p>FALSE: disabled<br />
TRUE: enabled (in 1.8.1 it's not TRUE, but some other value !?!)</p><p>If it's disabled, please enable it in the preferenes (wireshark GUI).</p><blockquote><p><code>Preferences -&gt; Name Resolution -&gt; Enable Network Name Resolution</code></p></blockquote><p>Then run this command (just an example to show you how it works):</p><blockquote><p><code>tshark -r input.cap -T fields -e ip.src -e ip.src_host -e ip.dst -e ip.dst_host -E header=y -E separator=,</code><br />
</p></blockquote><p><code>ip.src</code> and <code>ip.dst</code> are the unresolved IP addresses and <code>ip.src_host/ip.dst_host</code> are the resolved host names.</p><p><strong>HINT:</strong> Be prepared, that the export with name resolving enabled, will take MUCH longer!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '12, 01:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Aug '12, 01:42</p></div></div><div id="comments-container-13340" class="comments-container"></div><div id="comment-tools-13340" class="comment-tools"></div><div class="clear"></div><div id="comment-13340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

