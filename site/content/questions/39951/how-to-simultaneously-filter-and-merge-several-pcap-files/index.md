+++
type = "question"
title = "how to simultaneously filter and merge several pcap files"
description = '''Hi all,  I would like to simultaneously filter and merge several pcap files.  Combination of tshark and mergecap is a costly operation in my context (the combination implies that one have to visit each packets twice: first for filtering, second for mering).  But I am looking for a tool which does th...'''
date = "2015-02-19T08:50:00Z"
lastmod = "2015-02-23T09:44:00Z"
weight = 39951
keywords = [ "filter", "pcap", "mergecap" ]
aliases = [ "/questions/39951" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to simultaneously filter and merge several pcap files](/questions/39951/how-to-simultaneously-filter-and-merge-several-pcap-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39951-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I would like to simultaneously filter and merge several pcap files. Combination of tshark and mergecap is a costly operation in my context (the combination implies that one have to visit each packets twice: first for filtering, second for mering). But I am looking for a tool which does that in one visit per packet (check if packet match with filter, then merge). After googling, I found someone did it with tracesplit but with no more explanation about the syntax...</p></div><div id="question-tags" class="tags-container tags">filter pcap mergecap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '15, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/31856543dad1a12f24073c17126cb1e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ikuzar&#39;s gravatar image" /><p>ikuzar<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ikuzar has no accepted answers">0%</span></p></div></div><div id="comments-container-39951" class="comments-container"></div><div id="comment-tools-39951" class="comment-tools"></div><div class="clear"></div><div id="comment-39951-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40031"></span>

<div id="answer-container-40031" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40031-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://manpages.ubuntu.com/manpages/hardy/man1/tracesplit.1.html">tracesplit</a> does the opposite or merging ("tracesplit splits one trace into multiple tracefiles").</p><p>To give any meaningful answer, please add more details.</p><ul><li>What do you mean exactly by "is a <strong>costly</strong> operation in my context"?</li><li>What kind of filters do you need? Capture filters or display filters?</li><li>How do you want to merge the files? Just append or in a chronological correct order?</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '15, 09:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-40031" class="comments-container"><span id="40035"></span><div id="comment-40035" class="comment"><div id="post-40035-score" class="comment-score"></div><div class="comment-text"><p>also, merging is a real fast process, especially if concatenating files, so filtering with tshark and then merging the filtered results is usually really quick.</p></div><div id="comment-40035-info" class="comment-info"><span class="comment-age">(23 Feb '15, 12:11)</span> Jasper ♦♦</div></div><span id="40991"></span><div id="comment-40991" class="comment"><div id="post-40991-score" class="comment-score"></div><div class="comment-text"><p>many process and threads are running in my program. I just want to optimize the execution time of filtering/merging/compressing. I need capture filters and I just want to merge by appending packets.</p></div><div id="comment-40991-info" class="comment-info"><span class="comment-age">(30 Mar '15, 02:49)</span> ikuzar</div></div><span id="40995"></span><div id="comment-40995" class="comment"><div id="post-40995-score" class="comment-score"></div><div class="comment-text"><p>can you please add an example of what you are trying to do?</p></div><div id="comment-40995-info" class="comment-info"><span class="comment-age">(30 Mar '15, 04:08)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-40031" class="comment-tools"></div><div class="clear"></div><div id="comment-40031-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

