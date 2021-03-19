+++
type = "question"
title = "How to Export the pcap file statistics with csv file format."
description = '''Hello I&#x27;d like to export the pcap ip conversation ststistics to csv file format. I ran the below command But output is not looks like csv format.  &#x27;tshark -nr badcase.cap -z conv,ip -q &amp;gt;&amp;gt; aa.csv&#x27; Result IPv4 Conversations Filter:&amp;lt;no filter=&quot;&quot;&amp;gt;  | &amp;lt;- | | -&amp;gt;  | | Total | Relative | D...'''
date = "2013-07-09T00:54:00Z"
lastmod = "2013-07-09T02:53:00Z"
weight = 22749
keywords = [ "csv" ]
aliases = [ "/questions/22749" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to Export the pcap file statistics with csv file format.](/questions/22749/how-to-export-the-pcap-file-statistics-with-csv-file-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22749-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I'd like to export the pcap ip conversation ststistics to csv file format. I ran the below command But output is not looks like csv format.</p><hr /><p>'tshark -nr badcase.cap -z conv,ip -q &gt;&gt; aa.csv'</p><p><em>Result</em></p><p>IPv4 Conversations Filter:&lt;no filter=""&gt; | &lt;- | | -&gt; | | Total | Relative | Duration | | Frames Bytes | | Frames Bytes | | Frames Bytes | Start | | 38.123.0.241 &lt;-&gt; 38.120.0.4 2131 381775 4880 702985 2 7011 7411627 0.000000000 46.5388 203.236.39.130 &lt;-&gt; 10.24.20.142 2127 381128 4876 702918 2 7003 7410310 16.775635010 29.7632 211.233.41.229 &lt;-&gt; 10.24.20.142 4 647 4 67 0 8 1317 0.000000000 39.6715</p><hr /><p>Any way to solve this problem? Thanks</p></div><div id="question-tags" class="tags-container tags">csv</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '13, 00:54</strong></p><img src="https://secure.gravatar.com/avatar/ef90d75294c5fbe5160c35e5434507e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JasonK&#39;s gravatar image" /><p>JasonK<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JasonK has no accepted answers">0%</span></p></div></div><div id="comments-container-22749" class="comments-container"></div><div id="comment-tools-22749" class="comment-tools"></div><div class="clear"></div><div id="comment-22749-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22750"></span>

<div id="answer-container-22750" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22750-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you need the data in CSV format, there are (at least) these options:</p><ul><li>Use the GUI: <strong>Statistics -&gt; Conversations -&gt; TCP -&gt; Copy</strong>. This will copy the screen content as CSV into the clipboard.</li><li>Use tshark: tshark will not export the conversation data in CSV format, so you either convert it to CSV with Excel (while importing the data) or use a script (perl, python, watherver) to convert that output to csv.</li><li>Extend the tshark code to export CSV structured data.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '13, 02:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jul '13, 06:22</p></div></div><div id="comments-container-22750" class="comments-container"><span id="22776"></span><div id="comment-22776" class="comment"><div id="post-22776-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurk, Thank you for your reply. I fully understand your explanation. and got a further question. Any plan to support the CSV format export feature on tshark? (We have some local project and we need to get the csv format conversation data on cli mode)</p><p>Thanks Jason Kim</p></div><div id="comment-22776-info" class="comment-info"><span class="comment-age">(09 Jul '13, 17:23)</span> JasonK</div></div><span id="22783"></span><div id="comment-22783" class="comment"><div id="post-22783-score" class="comment-score"></div><div class="comment-text"><p>as there is no road map for Wireshark, I can't tell you if or when such a feature will be added. If you want to have it, please file an enhancement request at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p></div><div id="comment-22783-info" class="comment-info"><span class="comment-age">(10 Jul '13, 00:39)</span> Kurt Knochner ♦</div></div><span id="22784"></span><div id="comment-22784" class="comment"><div id="post-22784-score" class="comment-score"></div><div class="comment-text"><p>To raise an enhancement request, add an item to the <a href="https://bugs.wireshark.org/bugzilla/">Wireshark Bugzilla</a> for TShark and mark the "Importance" as an enhancement.</p><p>Please comment back here with the bug ID for the benefit of other users.</p></div><div id="comment-22784-info" class="comment-info"><span class="comment-age">(10 Jul '13, 00:45)</span> grahamb ♦</div></div></div><div id="comment-tools-22750" class="comment-tools"></div><div class="clear"></div><div id="comment-22750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

