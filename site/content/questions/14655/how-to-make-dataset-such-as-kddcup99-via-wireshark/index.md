+++
type = "question"
title = "How to make dataset such as KDDCup99 via wireshark?"
description = '''I am going to make a dataset such as KDDCup99 for machine learning purposes, but I don&#x27;t know how can i extract intrinsic and time-based attributes from wireshark analyzer!! KDDCup99 introduces 43 attributes (intrinsic, time-based and host-based attributes), and I am going to extract this attributes...'''
date = "2012-10-02T23:49:00Z"
lastmod = "2012-12-18T10:03:00Z"
weight = 14655
keywords = [ "traffic", "networking", "wireshark" ]
aliases = [ "/questions/14655" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to make dataset such as KDDCup99 via wireshark?](/questions/14655/how-to-make-dataset-such-as-kddcup99-via-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14655-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am going to make a dataset such as KDDCup99 for machine learning purposes, but I don't know how can i extract intrinsic and time-based attributes from wireshark analyzer!! KDDCup99 introduces 43 attributes (intrinsic, time-based and host-based attributes), and I am going to extract this attributes from wireshark analyzer. How can i do it?</p></div><div id="question-tags" class="tags-container tags">traffic networking wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '12, 23:49</strong></p><img src="https://secure.gravatar.com/avatar/26438e9ac8caef64dba0f3edf62f644b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bluebit&#39;s gravatar image" /><p>Bluebit<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bluebit has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Oct '12, 23:51</p></div></div><div id="comments-container-14655" class="comments-container"><span id="19005"></span><div id="comment-19005" class="comment"><div id="post-19005-score" class="comment-score"></div><div class="comment-text"><p>You might like to consider <a href="https://www.itoc.usma.edu/research/dataset/">https://www.itoc.usma.edu/research/dataset/</a> also. This is a more recent unlabelled IDS dataset with more sophisticated attacks than the (as I look at it now) outdated KDDCup99.</p></div><div id="comment-19005-info" class="comment-info"><span class="comment-age">(28 Feb '13, 20:17)</span> pds</div></div></div><div id="comment-tools-14655" class="comment-tools"></div><div class="clear"></div><div id="comment-14655-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17045"></span>

<div id="answer-container-17045" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17045-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Jaap is mostly right.</p><p>One option is to:</p><ul><li>Use tshark to log packet data to CSV format.</li><li>Post process that dataset to produce the 'connection' and 'two-second time window' attribute sets.</li><li>Do <em>some other logging</em> to get 'root_shell','su_attempted', etc attributes. (In Linux: history, last/lastb and /var/log/secure may help.)</li></ul><p>A second option, if you need KDDCup99 data fields collected in real-time is to:</p><ul><li>download the Wireshark source code: <a href="http://anonsvn.wireshark.org/wireshark/releases/wireshark-1.8.5/">SVN Repo</a></li><li>hand-code the collection and processing in real-time using *shark's pre-parsed protocol fields in C;</li><li>then print to file using CSV file format.</li></ul><p>The following should help in producing the CSV output from tshark CLI to 'logfile.csv':</p><pre><code>tshark 
-i &lt;interface&gt; 
-w logfile.pcap
-c 100
-T fields
-E header=y -E separator=, -E quote=d -E occurrence=f
-e ip.src -e ip.dst -e ip.proto -e ip.checksum -e tcp.srcport -e tcp.dstport
&gt; logfile.csv</code></pre><p>Use Wireshark's packet header browser/details panel to choose which attributes you want to log, then add those attributes to the -e arguments list.</p><ul><li>KDDCUP99 description: <a href="http://www.sc.ehu.es/acwaldap/gureKddcup/README.pdf">http://www.sc.ehu.es/acwaldap/gureKddcup/README.pdf</a></li><li>KDDCUP99 description: <a href="http://kdd.ics.uci.edu/databases/kddcup99/task.html">http://kdd.ics.uci.edu/databases/kddcup99/task.html</a></li><li>Tshark Man Page: <a href="http://www.wireshark.org/docs/man-pages/tshark.html">http://www.wireshark.org/docs/man-pages/tshark.html</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Dec '12, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/ce3456976f76d2c2683e3ee92b6343b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pds&#39;s gravatar image" /><p>pds<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pds has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Feb '13, 11:43</p></div></div><div id="comments-container-17045" class="comments-container"><span id="19002"></span><div id="comment-19002" class="comment"><div id="post-19002-score" class="comment-score"></div><div class="comment-text"><p>hey Friends ...me too working on kdd99cup data-set...my query is "how to trim (cut) data-set in 10% kdd99 cup...what are the factors we need to consider while trimming data"....kindly help me with algorithm or code to cut the data-set in to 10% of original...thanks</p></div><div id="comment-19002-info" class="comment-info"><span class="comment-age">(28 Feb '13, 19:32)</span> sac</div></div></div><div id="comment-tools-17045" class="comment-tools"></div><div class="clear"></div><div id="comment-17045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14663"></span>

<div id="answer-container-14663" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14663-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Tshark and post process the text output?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '12, 02:16</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-14663" class="comments-container"><span id="14668"></span><div id="comment-14668" class="comment"><div id="post-14668-score" class="comment-score"></div><div class="comment-text"><p>your comment is not clear for me!</p></div><div id="comment-14668-info" class="comment-info"><span class="comment-age">(03 Oct '12, 04:02)</span> Bluebit</div></div></div><div id="comment-tools-14663" class="comment-tools"></div><div class="clear"></div><div id="comment-14663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

