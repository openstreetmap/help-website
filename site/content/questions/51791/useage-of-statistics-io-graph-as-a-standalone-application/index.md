+++
type = "question"
title = "Useage of Statistics -&gt; IO-graph as a standalone application"
description = '''Parsing a PCAP-file with tshark and generate a custom graph with python + matplotlib is my normal usecase. But this time, the build-in IO-graph would fit my needs completely, if I can automate the process. I&#x27;d like to call the IO-graph standalone application with the specific PCAP-file, filters and ...'''
date = "2016-04-19T09:10:00Z"
lastmod = "2016-04-19T13:42:00Z"
weight = 51791
keywords = [ "graphs", "iographs", "automation" ]
aliases = [ "/questions/51791" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Useage of Statistics -&gt; IO-graph as a standalone application](/questions/51791/useage-of-statistics-io-graph-as-a-standalone-application)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51791-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Parsing a PCAP-file with tshark and generate a custom graph with python + matplotlib is my normal usecase. But this time, the build-in IO-graph would fit my needs completely, if I can automate the process. I'd like to call the IO-graph standalone application with the specific PCAP-file, filters and so on. The expected output would be a PNG-file or similar.</p><p>Is it possible to use the IO-graph of wireshark as a standalone application from the commandline like tshark?What's the expected input dataset of the IO-graph?</p></div><div id="question-tags" class="tags-container tags">graphs iographs automation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '16, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/6fa89e16ec5e38f50bf1b04629f2ca26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oposum&#39;s gravatar image" /><p>oposum<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oposum has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Apr '16, 09:11</p></div></div><div id="comments-container-51791" class="comments-container"></div><div id="comment-tools-51791" class="comment-tools"></div><div class="clear"></div><div id="comment-51791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51800"></span>

<div id="answer-container-51800" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51800-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it possible to use the IO-graph of wireshark as a standalone application from the commandline like tshark?</p></blockquote><p>Not without a (larger) change of code. Sorry!</p><p>Alternatively you can use <strong>tshark -z io,stat,</strong> (see man page for details), but that won't generate PNG files. You can also use tshark to print frames or fields within frames and parse the output with python to generate input data for matplotlib, etc.</p><p>Instead of parsing the output of tshark, you can also check if Sharktools helps: <a href="https://github.com/armenb/sharktools">https://github.com/armenb/sharktools</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '16, 13:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Apr '16, 02:21</p></div></div><div id="comments-container-51800" class="comments-container"></div><div id="comment-tools-51800" class="comment-tools"></div><div class="clear"></div><div id="comment-51800-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

