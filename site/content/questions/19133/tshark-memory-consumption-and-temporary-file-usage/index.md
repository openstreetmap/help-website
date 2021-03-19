+++
type = "question"
title = "tshark memory consumption and temporary file usage"
description = '''Hi all, I am using tshark to sniff http traffic on a very busy server. Over the course of a number of hours I see a drastic increase in memory usage and the size of the temporary file increases rapidly. Eventually the process fills the disk and memory is so high that the tool grinds to a halt. This ...'''
date = "2013-03-04T11:24:00Z"
lastmod = "2013-03-04T13:41:00Z"
weight = 19133
keywords = [ "performance", "temporary", "comsumption", "file", "memory" ]
aliases = [ "/questions/19133" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark memory consumption and temporary file usage](/questions/19133/tshark-memory-consumption-and-temporary-file-usage)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19133-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am using tshark to sniff http traffic on a very busy server. Over the course of a number of hours I see a drastic increase in memory usage and the size of the temporary file increases rapidly. Eventually the process fills the disk and memory is so high that the tool grinds to a halt.</p><p>This is the command line I am using:</p><p>tshark.exe -i3 -l -f "tcp port 80" -O http -d tcp.port==80,http -o "ip.use_geoip:FALSE" -R "not tcp.analysis.retransmission" -T fields -e ip.host -e tcp.port -e http.request.full_uri -e http.request.method -e http.response.code -e http.response.phrase -e http.content_length -e text -E separator=;2&gt;&amp;0</p><p>Are any of these options memory consumers or file bloaters? Is there any way I could optimize it to improve the situation?</p><p>Is there any way I can get the tshark to release its memory and or delete the temporary file periodically?</p><p>Thanks</p><p>David</p></div><div id="question-tags" class="tags-container tags">performance temporary comsumption file memory</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '13, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/0b0ac57ffe8e8e5747c4b0f5595a521f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20Sackstein&#39;s gravatar image" /><p>David Sackstein<br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David Sackstein has no accepted answers">0%</span></p></div></div><div id="comments-container-19133" class="comments-container"></div><div id="comment-tools-19133" class="comment-tools"></div><div class="clear"></div><div id="comment-19133-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19137"></span>

<div id="answer-container-19137" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19137-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately no. Tshark (and Wireshark) collect state information about conversations which isn't released even when using multiple files.</p><p>The normal recommendation is to use dumpcap (or tcpdump) for long running captures with multiple files then post-process the captures with tshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '13, 13:41</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-19137" class="comments-container"></div><div id="comment-tools-19137" class="comment-tools"></div><div class="clear"></div><div id="comment-19137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

