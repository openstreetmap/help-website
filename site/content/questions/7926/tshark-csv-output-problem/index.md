+++
type = "question"
title = "TShark CSV output problem"
description = '''Hi all,  I am trying to create a nice CSV file from a trace, but instead of a readable CSV file I get a file with all sorts of characters all over the place. Am I doing something wrong with encoding or so (windows)? the command I used is below: tshark.exe -T fields -E separator=, -E quote=d -e frame...'''
date = "2011-12-12T14:02:00Z"
lastmod = "2011-12-12T14:08:00Z"
weight = 7926
keywords = [ "csv", "tshark" ]
aliases = [ "/questions/7926" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TShark CSV output problem](/questions/7926/tshark-csv-output-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7926-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I am trying to create a nice CSV file from a trace, but instead of a readable CSV file I get a file with all sorts of characters all over the place. Am I doing something wrong with encoding or so (windows)? the command I used is below:</p><p>tshark.exe -T fields -E separator=, -E quote=d -e frame.number -e ip.dst -e ip.src -e eth.dst -e eth.src -e tcp.srcport -e udp.srcport -e tcp.dstport -e upd.dstport -w stats.csv -r trace.pcap</p></div><div id="question-tags" class="tags-container tags">csv tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '11, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/45bf66a776fd2fd33d91ca2305ef07f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bram%20van%20den%20Bosch&#39;s gravatar image" /><p>Bram van den...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bram van den Bosch has no accepted answers">0%</span></p></div></div><div id="comments-container-7926" class="comments-container"></div><div id="comment-tools-7926" class="comment-tools"></div><div class="clear"></div><div id="comment-7926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7927"></span>

<div id="answer-container-7927" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7927-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>You're doing it <em>almost</em> right :-)</p><p>The "-w" means write the captured packets to disk (binary). What you want is to redirect your tshark output to file. You can do this with "&gt; file.csv". The command will become:</p><pre><code>tshark.exe -T fields -E separator=, -E quote=d -e frame.number -e ip.dst -e ip.src \
  -e eth.dst -e eth.src -e tcp.srcport -e udp.srcport -e tcp.dstport -e upd.dstport \
  -r trace.pcap &gt; stats.csv</code></pre><p>Hope this helps!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '11, 14:08</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7927" class="comments-container"><span id="7948"></span><div id="comment-7948" class="comment"><div id="post-7948-score" class="comment-score"></div><div class="comment-text"><p>Super, works like expected now. Thanks for the help</p></div><div id="comment-7948-info" class="comment-info"><span class="comment-age">(13 Dec '11, 09:51)</span> Bram van den...</div></div></div><div id="comment-tools-7927" class="comment-tools"></div><div class="clear"></div><div id="comment-7927-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

