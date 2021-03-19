+++
type = "question"
title = "calculate tcp retransmission rate"
description = '''I ran the following command..  gunzip -c 201509211400.dump.gz | tshark -nr - -Y &quot;tcp.analysis.retransmission&quot; -T fields -e tcp.stream -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport -e expert.message &amp;gt; table1.txt 13 197.94.235.198 80 152.188.170.15 43372 Retransmission (suspected) 77 443 40383 ...'''
date = "2015-09-24T11:53:00Z"
lastmod = "2015-09-24T11:53:00Z"
weight = 46121
keywords = [ "filter", "rate", "retransmission", "tcp" ]
aliases = [ "/questions/46121" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [calculate tcp retransmission rate](/questions/46121/calculate-tcp-retransmission-rate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46121-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I ran the following command.. gunzip -c 201509211400.dump.gz | tshark -nr - -Y "tcp.analysis.retransmission" -T fields -e tcp.stream -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport -e expert.message &gt; table1.txt</p><p>13 197.94.235.198 80 152.188.170.15 43372 Retransmission (suspected)</p><p>77 443 40383 Retransmission (suspected)</p><p>Now i do not understand why there is no IP addresses for tcp streams 77?</p><p>I want to count tcp retransmission rate for each connection in my pcap file. I am using following method: The above command will give me all tcp streams with retransmissions. Then i am running following command..</p><p>tshark -nr file.pcap -Y "tcp.stream = x" -z conv,"tcp" x = one of the streams given by first command</p><p>then rate = ((no. of times x appear in the first command's o/p)/(total line in the conversation i.e second command o/p)) * 100</p><p>Is it the right way?</p></div><div id="question-tags" class="tags-container tags">filter rate retransmission tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '15, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/0c09b4363e1422b3e5a5cee5a17abd3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sahaj&#39;s gravatar image" /><p>sahaj<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sahaj has no accepted answers">0%</span></p></div></div><div id="comments-container-46121" class="comments-container"></div><div id="comment-tools-46121" class="comment-tools"></div><div class="clear"></div><div id="comment-46121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

