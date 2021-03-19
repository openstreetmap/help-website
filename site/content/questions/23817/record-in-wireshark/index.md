+++
type = "question"
title = "record in wireshark"
description = '''hello, I have a problem with a server. I want to see the traffic on the sever in 4:00 a.m. until 5:00 a.m. I use in port mirror in cisco switch becasuse I can&#x27;t use in wireshark on the server. When I use wireshark a lot of time the software stop (not respond). How I can to record the traffic in spec...'''
date = "2013-08-16T01:16:00Z"
lastmod = "2013-08-16T02:05:00Z"
weight = 23817
keywords = [ "recording" ]
aliases = [ "/questions/23817" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [record in wireshark](/questions/23817/record-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23817-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello,</p><p>I have a problem with a server. I want to see the traffic on the sever in 4:00 a.m. until 5:00 a.m. I use in port mirror in cisco switch becasuse I can't use in wireshark on the server. When I use wireshark a lot of time the software stop (not respond).</p><p>How I can to record the traffic in specific time?</p><p>thanks...</p></div><div id="question-tags" class="tags-container tags">recording</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '13, 01:16</strong></p><img src="https://secure.gravatar.com/avatar/9786e797f30b0128817e09416256fdcc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ron1990&#39;s gravatar image" /><p>ron1990<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ron1990 has no accepted answers">0%</span></p></div></div><div id="comments-container-23817" class="comments-container"></div><div id="comment-tools-23817" class="comment-tools"></div><div class="clear"></div><div id="comment-23817-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23818"></span>

<div id="answer-container-23818" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23818-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark may be stopping because it is <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">out of memory</a>. This is a known problem when capturing large amounts of data. Instead of using Wireshark (or tshark), use dumpcap which only creates capture files and doesn't do any parsing and then use Wireshark on the output files. I say files because dumping all the data into a single file may still be too big for Wireshark to handle.</p><p>You can use dumpcap with the <code>-a duration</code> parameter to set the capture time length, e.g. <code>-a duration:3600</code> for a total capture time of 1 hour and the <code>-b filesize:</code> parameter to set the individual capture file length, e.g. <code>-b filesize:100000</code> to have 100MB files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '13, 02:05</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-23818" class="comments-container"></div><div id="comment-tools-23818" class="comment-tools"></div><div class="clear"></div><div id="comment-23818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

