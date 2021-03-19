+++
type = "question"
title = "Batch file to read pcap file ? how"
description = '''i am making batch file that read pcap file here is my batch file code  tshark -r C:&#92;Program Files&#92;Wireshark&#92;sample.pcap -q -z conv,ip   -E separator=, -e ip.src -e ip.dst &amp;gt; &quot;d:&#92;logcapture.txt&quot;  that creates an empty output file in d directory i have tested my command con tshark here is command  t...'''
date = "2016-03-21T01:38:00Z"
lastmod = "2016-03-21T10:17:00Z"
weight = 51057
keywords = [ "tcpdump", "pcap", "tshark", "batch" ]
aliases = [ "/questions/51057" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Batch file to read pcap file ? how](/questions/51057/batch-file-to-read-pcap-file-how)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51057-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>i am making batch file that read pcap file here is my batch file code</p><pre><code> tshark -r C:\Program Files\Wireshark\sample.pcap -q -z conv,ip

  -E separator=, -e ip.src -e ip.dst &gt; &quot;d:\logcapture.txt&quot;</code></pre><p>that creates an empty output file in d directory i have tested my command con tshark here is command</p><pre><code>   tshark -r sample.pcap -q -z conv,ip</code></pre><p>that works sucessfully can you please tell me how to read and save text of pcap file using batch file?</p></div><div id="question-tags" class="tags-container tags">tcpdump pcap tshark batch</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '16, 01:38</strong></p><img src="https://secure.gravatar.com/avatar/ff1d12c62c198362915848012ff2a021?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Engr%20Nouman&#39;s gravatar image" /><p>Engr Nouman<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Engr Nouman has no accepted answers">0%</span></p></div></div><div id="comments-container-51057" class="comments-container"><span id="51072"></span><div id="comment-51072" class="comment"><div id="post-51072-score" class="comment-score"></div><div class="comment-text"><p>What kind of text are you trying to add to the pcap ? Have you researched "editcap" and "mergecap" ? I believe editcap should allow you to do what you need. I'd have to research it more to give you exact options, but both are powerful when it comes to editing pcap files.</p></div><div id="comment-51072-info" class="comment-info"><span class="comment-age">(21 Mar '16, 10:06)</span> msmorten</div></div></div><div id="comment-tools-51057" class="comment-tools"></div><div class="clear"></div><div id="comment-51057-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51073"></span>

<div id="answer-container-51073" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51073-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you post is exactly what you have in your batch file, then you'll need to quote the pcap filename. You may also need to quote the other parameters. Test by executing exactly the same command at the command prompt.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '16, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51073" class="comments-container"></div><div id="comment-tools-51073" class="comment-tools"></div><div class="clear"></div><div id="comment-51073-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

