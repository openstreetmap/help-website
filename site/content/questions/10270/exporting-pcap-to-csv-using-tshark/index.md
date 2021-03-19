+++
type = "question"
title = "Exporting pcap to csv using tshark"
description = '''I have a sample pcap file and i opened it as a wireshark GUI. On the wireshark GUI,i click file -&amp;gt; Export. I export it as a CSV file. I would like the output csv file output using tshark AS IF i export the pcap data to the csv file using Wireshark GUI. what is the TSHARK command for EXPORTING pca...'''
date = "2012-04-19T02:15:00Z"
lastmod = "2012-04-19T03:40:00Z"
weight = 10270
keywords = [ "csv", "pcap", "tshark" ]
aliases = [ "/questions/10270" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Exporting pcap to csv using tshark](/questions/10270/exporting-pcap-to-csv-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10270-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a sample pcap file and i opened it as a wireshark GUI. On the wireshark GUI,i click file -&gt; Export. I export it as a CSV file.</p><p>I would like the output csv file output using <strong>tshark</strong> <strong>AS IF</strong> i export the pcap data to the csv file <strong>using Wireshark GUI</strong>. what is the TSHARK command for EXPORTING pcap sample file to a csv file?</p><p>I want the csv file output to look like this when viewed in windows 7 .txt file:</p><p>"No.","Time","Source","Destination","Protocol","Length","Info" "1","0.000000","164.124.33.78","192.168.0.1","TCP","54","35165 &gt; http [SYN] Seq=0 Win=16384 Len=0" "2","0.000001","38.198.26.9","192.168.0.1","TCP","54","14378 &gt; http [SYN] Seq=0 Win=16384 Len=0" "3","0.000003","132.212.36.201","192.168.0.1","TCP","54","31944 &gt; http [SYN] Seq=0 Win=16384 Len=0" "4","0.000005","76.196.6.157","192.168.0.1","TCP","54","10404 &gt; http [RST] Seq=1 Win=0 Len=0" "5","0.000057","189.109.37.180","192.168.0.1","TCP","54","36076 &gt; http [SYN] Seq=0 Win=16384 Len=0" "6","0.000059","189.109.37.188","192.168.0.1","TCP","54","36084 &gt; http [SYN] Seq=0 Win=16384 Len=0" "7","0.000060","76.196.12.251","192.168.0.1","TCP","54","12034 &gt; http [SYN] Seq=0 Win=16384 Len=0" "8","0.000062","132.212.36.146","192.168.0.1","TCP","54","31889 &gt; http [SYN] Seq=0 Win=16384 Len=0"</p></div><div id="question-tags" class="tags-container tags">csv pcap tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '12, 02:15</strong></p><img src="https://secure.gravatar.com/avatar/94990dfa38fcf1b33157bef842da0291?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misteryuku&#39;s gravatar image" /><p>misteryuku<br />
<span class="score" title="20 reputation points">20</span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misteryuku has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Apr '12, 02:48</p></div></div><div id="comments-container-10270" class="comments-container"></div><div id="comment-tools-10270" class="comment-tools"></div><div class="clear"></div><div id="comment-10270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10273"></span>

<div id="answer-container-10273" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10273-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Misteryuku, please stop opening new questions again and again for the same questions you asked before -&gt; this is the 3rd or 4th question with the same topic, so if you don't agree with the Q&amp;A rules further questions like this will be closed !</p><p>One last time: Like already mentioned in your other question's answer <a href="http://ask.wireshark.org/questions/10256/converting-a-wireshark-pcap-file-to-a-windows-txt-file-that-contains-fieldvalue-data">http://ask.wireshark.org/questions/10256/converting-a-wireshark-pcap-file-to-a-windows-txt-file-that-contains-fieldvalue-data</a> there is no easy way of doing a .csv export via tshark in a way like available through wireshark's GUI as far as the tshark -h options are concerned.</p><p>You might however try to do a <code>tshark -r &lt;filename.pcap&gt; &gt; output.txt</code> and then use whitespace as a separator (which will not work with the info coloumn of course) or follow the Tfields approach by specifying specific fields to export together with -E separator=, for example.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '12, 03:40</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Apr '12, 03:45</p></div></div><div id="comments-container-10273" class="comments-container"><span id="10280"></span><div id="comment-10280" class="comment"><div id="post-10280-score" class="comment-score"></div><div class="comment-text"><p>Okay i understand. I'm sorry about it. I should been clearer about what i should be asking. This will be the last time i would be asking this question.</p></div><div id="comment-10280-info" class="comment-info"><span class="comment-age">(19 Apr '12, 06:31)</span> misteryuku</div></div></div><div id="comment-tools-10273" class="comment-tools"></div><div class="clear"></div><div id="comment-10273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

