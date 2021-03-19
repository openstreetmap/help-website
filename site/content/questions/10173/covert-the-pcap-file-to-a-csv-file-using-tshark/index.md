+++
type = "question"
title = "Covert the .pcap file to a .csv file using tshark"
description = '''What is the &quot;tshark&quot; command for to converting the .pcap file to a .csv file? The packet capture data will be monitored using Splunk.'''
date = "2012-04-16T01:10:00Z"
lastmod = "2012-04-16T10:55:00Z"
weight = 10173
keywords = [ "conversion", "csv", "pcap", "tshark" ]
aliases = [ "/questions/10173" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Covert the .pcap file to a .csv file using tshark](/questions/10173/covert-the-pcap-file-to-a-csv-file-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10173-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>What is the "tshark" command for to converting the .pcap file to a .csv file? The packet capture data will be monitored using Splunk.</p></div><div id="question-tags" class="tags-container tags">conversion csv pcap tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '12, 01:10</strong></p><img src="https://secure.gravatar.com/avatar/94990dfa38fcf1b33157bef842da0291?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misteryuku&#39;s gravatar image" /><p>misteryuku<br />
<span class="score" title="20 reputation points">20</span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misteryuku has no accepted answers">0%</span></p></div></div><div id="comments-container-10173" class="comments-container"></div><div id="comment-tools-10173" class="comment-tools"></div><div class="clear"></div><div id="comment-10173-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10193"></span>

<div id="answer-container-10193" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10193-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That depends on which particular fields you want to use in the CSV file. Once you've decided which named fields to put into the CSV file, then you would run a command such as</p><pre><code>tshark -T fields -n -r {the pathname of the capture file} -E separator=, -e {first field name} -e {second field name} ... &gt;{the pathname of the output file}</code></pre><p>where {the pathname of the capture file} is the pathname of the capture file you're reading and {first field name}, {second field name} and so on are the names of the fields, and {the pathname of the output file} is the pathname of the output file, for example</p><pre><code>tshark -T fields -n -r capture.pcap -E separator=, -e ip.src -e ip.dst ... &gt;output.txt</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '12, 10:55</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Apr '12, 23:40</p></div></div><div id="comments-container-10193" class="comments-container"><span id="10255"></span><div id="comment-10255" class="comment"><div id="post-10255-score" class="comment-score"></div><div class="comment-text"><p>How do i specify the output csv file pathname into this tshark command above??</p></div><div id="comment-10255-info" class="comment-info"><span class="comment-age">(18 Apr '12, 17:52)</span> misteryuku</div></div><span id="10257"></span><div id="comment-10257" class="comment"><div id="post-10257-score" class="comment-score"></div><div class="comment-text"><p>I've updated the anser to show that, and gave an example.</p></div><div id="comment-10257-info" class="comment-info"><span class="comment-age">(18 Apr '12, 23:41)</span> Guy Harris ♦♦</div></div><span id="10260"></span><div id="comment-10260" class="comment"><div id="post-10260-score" class="comment-score"></div><div class="comment-text"><p>What does "this" in "so this applies to a .txt file..." refer to?</p><p>The <em>text output</em> of TShark is specified by redirecting its output to a file no matter <em>what</em> type of output is produced.</p><p>The <code>-T fields</code>, <code>-E separator=,</code>, and <code>-e</code> flags applies to a <em>CSV</em> file, which means that each line contains a Comma-Separated list of Values, with <em>NO</em> keys. There <em>IS</em> no option to TShark to make it produce output with key=value pairs.</p></div><div id="comment-10260-info" class="comment-info"><span class="comment-age">(18 Apr '12, 23:56)</span> Guy Harris ♦♦</div></div><span id="10263"></span><div id="comment-10263" class="comment"><div id="post-10263-score" class="comment-score"></div><div class="comment-text"><p>okay i see besides outputting the ip.src and the ip.dst , what is the syntax for outputting the values for no, time, protocol, length and Info field column names from the Wireshark Graphical User Interface??</p></div><div id="comment-10263-info" class="comment-info"><span class="comment-age">(19 Apr '12, 00:05)</span> misteryuku</div></div><span id="10264"></span><div id="comment-10264" class="comment"><div id="post-10264-score" class="comment-score"></div><div class="comment-text"><p>There are no fields corresponding to the protocol and info columns, so you'd have to do something such as</p><pre><code>tshark -n -r {the pathname of the capture file}</code></pre><p>to have it print out the columns. The output would <em>NOT</em> be comma-separated, and would <em>NOT</em> have key= tags; it would look something like</p><pre><code>1   0.000000 xxx.xxx.xxx.xxx -&gt; xxx.xxx.xxx.xxx TCP 54 5165 &gt; http [SYN] Seq=0 Win=16384 Len=0
2   0.000001 xxx.xxx.xxx.xxx -&gt; xxx.xxx.xxx.xxx TCP 54 14378 &gt; http [SYN] Seq=0 Win=16384 Len=0
3   0.000003 xxx.xxx.xxx.xxx -&gt; xxx.xxx.xxx.xxx TCP 54 31944 &gt; http [SYN] Seq=0 Win=16384 Len=0</code></pre></div><div id="comment-10264-info" class="comment-info"><span class="comment-age">(19 Apr '12, 00:30)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-10193" class="comment-tools"></div><div class="clear"></div><div id="comment-10193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

