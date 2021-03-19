+++
type = "question"
title = "Print number of tcp flows"
description = '''I know that by doing  tshark -r pcap.pcap -qz conv,tcp  I can read all the TCP flows but I would like to see specifically the number of flows that exist on a pcap file. I do not want to do that through wc -l because I am not sure if the output is always similar and whether additional lines will be a...'''
date = "2016-01-28T07:55:00Z"
lastmod = "2016-01-28T08:15:00Z"
weight = 49598
keywords = [ "ip", "flow", "tcp" ]
aliases = [ "/questions/49598" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Print number of tcp flows](/questions/49598/print-number-of-tcp-flows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49598-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know that by doing</p><p><code>tshark -r pcap.pcap -qz conv,tcp</code></p><p>I can read all the TCP flows but I would like to see specifically the number of flows that exist on a pcap file. I do not want to do that through wc -l because I am not sure if the output is always similar and whether additional lines will be added.</p></div><div id="question-tags" class="tags-container tags">ip flow tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jan '16, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/93eb17372bd105d80fc159bb1c97d6fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="altdrugzgene&#39;s gravatar image" /><p>altdrugzgene<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="altdrugzgene has no accepted answers">0%</span></p></div></div><div id="comments-container-49598" class="comments-container"></div><div id="comment-tools-49598" class="comment-tools"></div><div class="clear"></div><div id="comment-49598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49599"></span>

<div id="answer-container-49599" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49599-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe use the fields option and directly output the tcp.stream field, then post-process that to find the highest unique value, e.g. using PowerShell:</p><pre><code>tshark -r pcap.pcap -T fields -e tcp.stream | foreach{ [int]$_ + 1 } | SortObject -Unique -Descending | Select-Object -First 1</code></pre><p>Basically sort the stream integers into descending order, omitting duplicates, then select the first 1 (or head).</p><p>Note that this will give a 0-based index of the streams, to get the actual stream count you still have to add 1.</p><p><strong>Update:</strong> Added coercion to int to fix numeric sort, plus an offset to make the numbers 1 based and the resulting count accurate.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '16, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jan '16, 09:47</p></div></div><div id="comments-container-49599" class="comments-container"><span id="49601"></span><div id="comment-49601" class="comment"><div id="post-49601-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply. Interestingly from the first piece tshark -r pcap.pcap -T fields -e tcp.stream I am getting 53 as the largest however I noticed that there are 54 flows! Is it starting counting from 0 ? I am using linux btw so no powershell for me! :P</p></div><div id="comment-49601-info" class="comment-info"><span class="comment-age">(28 Jan '16, 08:29)</span> altdrugzgene</div></div><span id="49604"></span><div id="comment-49604" class="comment"><div id="post-49604-score" class="comment-score"></div><div class="comment-text"><p>Note the last bit of my answer about the stream field being 0-based.</p><p>In bash you should be able to run <code>... | sort -ur | head -1</code></p></div><div id="comment-49604-info" class="comment-info"><span class="comment-age">(28 Jan '16, 08:46)</span> grahamb ♦</div></div><span id="49605"></span><div id="comment-49605" class="comment"><div id="post-49605-score" class="comment-score"></div><div class="comment-text"><p>This returns totally wrong number.. dunno why</p></div><div id="comment-49605-info" class="comment-info"><span class="comment-age">(28 Jan '16, 08:58)</span> altdrugzgene</div></div><span id="49606"></span><div id="comment-49606" class="comment"><div id="post-49606-score" class="comment-score"></div><div class="comment-text"><p>Add <code>-g</code> to the sort parms to make it a numeric sort?</p></div><div id="comment-49606-info" class="comment-info"><span class="comment-age">(28 Jan '16, 09:20)</span> grahamb ♦</div></div><span id="49607"></span><div id="comment-49607" class="comment"><div id="post-49607-score" class="comment-score"></div><div class="comment-text"><p>sweet that worked.. still have to get the first entry with -g though. I thought it would be possible to get it from tshark itself but ok. Cheers and Thanks</p></div><div id="comment-49607-info" class="comment-info"><span class="comment-age">(28 Jan '16, 09:27)</span> altdrugzgene</div></div></div><div id="comment-tools-49599" class="comment-tools"></div><div class="clear"></div><div id="comment-49599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

