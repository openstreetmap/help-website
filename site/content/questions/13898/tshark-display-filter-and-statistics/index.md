+++
type = "question"
title = "TShark: Display Filter and Statistics"
description = '''Hello all, I am running CentOS v5.8 64bit. What is the correct display filter options to use in TShark if I want to redirect the output as CSV from reading a PCAP file? The columns will have the following output separated by commas:  timestamp,ip.src,source-port,ip.dst,destination-port,transport-lay...'''
date = "2012-08-26T19:37:00Z"
lastmod = "2012-08-27T00:42:00Z"
weight = 13898
keywords = [ "columns", "statistics", "csv", "display-filter", "tshark" ]
aliases = [ "/questions/13898" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TShark: Display Filter and Statistics](/questions/13898/tshark-display-filter-and-statistics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13898-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I am running CentOS v5.8 64bit. What is the correct display filter options to use in TShark if I want to redirect the output as CSV from reading a PCAP file? The columns will have the following output separated by commas:</p><blockquote><p>timestamp,ip.src,source-port,ip.dst,destination-port,transport-layer-protocol,upload-bandwidth,download-bandwidth</p></blockquote><p>Where:</p><ul><li>timestamp = the actual time of a packet</li><li>ip.src = the source IP address</li><li>source-port = the source port</li><li>ip.dst = the destination IP address</li><li>destination-port = the destination port</li><li>transport-layer-protocol = be it in TCP, UDP, SCTP, etc.</li><li>upload-bandwidth = the upload bandwidth in bytes</li><li>download-bandwidth = the download bandwidth in bytes</li></ul><p>My current tshark syntax is:</p><blockquote><p># tshark -n -r file.pcap -T fields -E separator=',' -e ip.src -e ip.dst</p></blockquote><p>As you can see, I still don't know what are the other display filters to use in order to achieve my requirement. I hope anyone from this community can help me.</p><p>Below is the screenshot from WireShark in customizing the display filter columns to which I would like to achieve in a single tshark command.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark_display_columns.png" alt="Customizing Display Filter Columns" /></p><p>Lastly, is there a way to get the statistics of the total upload bandwidth and the total download bandwidth by source IP address group by destination IP address, destination port or transport layer protocol as part of the TShark option?</p><p>Thank you in advance.</p></div><div id="question-tags" class="tags-container tags">columns statistics csv display-filter tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '12, 19:37</strong></p><img src="https://secure.gravatar.com/avatar/929188474427b5c0cd8e3de0670882f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bintut&#39;s gravatar image" /><p>bintut<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bintut has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 29 Aug '12, 02:55</p></div></div><div id="comments-container-13898" class="comments-container"><span id="13955"></span><div id="comment-13955" class="comment"><div id="post-13955-score" class="comment-score"></div><div class="comment-text"><p>I found the preferences file from my WireShark in my MS Windows 7 desktop and tried to execute the command in my CentOS v5.8 machine and I got an error:</p><blockquote><p># tshark -n -i eth0 -o column.format:""Time","%Cus:frame.time:0:R","Source IP Address","%us","Source Port","%uS","Destination IP Address","%ud","Destination Port","%uD","Protocol","%p","Packet Size","%L""</p><p>tshark: Invalid -o flag "column.format:Time,%Cus:frame.time:0:R,Source"</p></blockquote></div><div id="comment-13955-info" class="comment-info"><span class="comment-age">(29 Aug '12, 03:27)</span> bintut</div></div><span id="13960"></span><div id="comment-13960" class="comment"><div id="post-13960-score" class="comment-score"></div><div class="comment-text"><p>Now, the below command partially works for what I need:</p><blockquote><p># tshark -r file.pcap -o column.format:"Time","%Cus:frame.time","Source IP Address","%us","Source Port","%uS","Destination IP Address","%ud","Destination Port","%uD","Protocol","%p","Packet Size","%L"</p></blockquote><p>Now, how can I change the spaces/tabs into a comma? If I try to add the options:</p><blockquote><p>-T fields -E separator=','</p></blockquote><p>I am getting an error message:</p><blockquote><p>tshark: "-Tfields" was specified, but no fields were specified with "-e".</p></blockquote></div><div id="comment-13960-info" class="comment-info"><span class="comment-age">(29 Aug '12, 15:19)</span> bintut</div></div></div><div id="comment-tools-13898" class="comment-tools"></div><div class="clear"></div><div id="comment-13898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13907"></span>

<div id="answer-container-13907" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13907-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To find a <del>filter</del>field name, open a capture file in Wireshark, select the required node in the packet tree, e.g. tcp and then select the field required, e.g. the source port. The <del>filter</del>field name will be shown in the status bar at the bottom (tcp.srcport in this instance).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '12, 00:42</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Aug '12, 03:26</p></div></div><div id="comments-container-13907" class="comments-container"><span id="13952"></span><div id="comment-13952" class="comment"><div id="post-13952-score" class="comment-score"></div><div class="comment-text"><p>But in WireShark, you can specify the column names when you go to the "Edit &gt; Preferences &gt; User Interface &gt; Columns" as generic as shown in my screenshot above specially on the source port and destination port regardless of transport layer protocol. So, how am I able to execute a single tshark command from the CLI in order to achieve the CSV format that I want?</p></div><div id="comment-13952-info" class="comment-info"><span class="comment-age">(29 Aug '12, 02:56)</span> bintut</div></div><span id="13954"></span><div id="comment-13954" class="comment"><div id="post-13954-score" class="comment-score"></div><div class="comment-text"><p>When I mentioned "filter name" in my answer I really meant field name.</p><p>In the editor for the columns there is a field "Field name:", in your example "frame.time_epoch". This is the value you use in the tshark command line with the -e command, e.g. -e frame.time_epoch.</p></div><div id="comment-13954-info" class="comment-info"><span class="comment-age">(29 Aug '12, 03:22)</span> grahamb ♦</div></div><span id="13956"></span><div id="comment-13956" class="comment"><div id="post-13956-score" class="comment-score"></div><div class="comment-text"><p>I cannot get the source port and destination port in just one tshark command regardless of the transport layer protocol. In WireShark having the configuration I mentioned above, it can display the source port number and destination port number regardless if it's TCP, UDP, SCTP, etc. What I know for now in tshark is the "-e tcp.srcport" or "-e udp.srcport" but not without having only like "-e srcport".</p></div><div id="comment-13956-info" class="comment-info"><span class="comment-age">(29 Aug '12, 03:41)</span> bintut</div></div></div><div id="comment-tools-13907" class="comment-tools"></div><div class="clear"></div><div id="comment-13907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

