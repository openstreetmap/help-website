+++
type = "question"
title = "How to filter the whole TCP streams based on inner protocol condition"
description = '''Hi guys, I would like to learn, how to filter multiple whole TCP streams based on inner protocol condition, e.g. HTTP header values. E.g. I have a capture from a proxy with lot of users, and I want to see only TCP streams which are connecting to www.google.com. The point here is to see the whole TCP...'''
date = "2012-11-22T07:48:00Z"
lastmod = "2012-11-26T12:00:00Z"
weight = 16216
keywords = [ "inside", "protocol", "stream", "tcp", "inner" ]
aliases = [ "/questions/16216" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter the whole TCP streams based on inner protocol condition](/questions/16216/how-to-filter-the-whole-tcp-streams-based-on-inner-protocol-condition)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16216-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>I would like to learn, how to filter multiple whole TCP streams based on inner protocol condition, e.g. HTTP header values.</p><p>E.g. I have a capture from a proxy with lot of users, and I want to see only TCP streams which are connecting to <a href="http://www.google.com">www.google.com</a>. The point here is to see the whole TCP stream, not only the frames containing HTTP header with "Host: <a href="http://www.google.com">www.google.com</a>"</p><p>Of course, I can always use "<strong>http.host==<a href="http://www.google.com">www.google.com</a></strong>", extract the TCP stream number, and rewrite the filter to "<strong>tcp.stream==X</strong>". However, this starts to be a annoying problem, if I have tens or hundreds of connections. It takes lot of time and is not flexible.</p><p>In an object language, I would write something like</p><p><em>tcp.stream==(http.host==<a href="http://www.google.com">www.google.com</a>).tcp.stream</em></p><p>Thanks in advance!!!</p><p>Jozef</p></div><div id="question-tags" class="tags-container tags">inside protocol stream tcp inner</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '12, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/42a921ab52e4dad9ac3b633ca91a6c57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jozef&#39;s gravatar image" /><p>Jozef<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jozef has no accepted answers">0%</span></p></div></div><div id="comments-container-16216" class="comments-container"></div><div id="comment-tools-16216" class="comment-tools"></div><div class="clear"></div><div id="comment-16216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16218"></span>

<div id="answer-container-16218" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16218-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sad enough conditional filtering is not working in wireshark. What you CAN do to accomplish those tasks where you want to filter based on another filter is to use tshark scripting to do the following:</p><pre><code>tshark -r trace.pcap -R &quot;http.host==www.google.com&quot; -n -Tfields -e tcp.stream</code></pre><p>` This gives you a list of the stream indexes that match your filter. After that with the use of cli tools like sort,uniq,sed etc. you can in a second step (or all in one) produce a long display filter containing all "or-ed" tcp.stream values you are looking for.</p><p>e.g.</p><p><code>tshark -r trace.pcap -R "http.host==www.google.com" -n -Tfields -e tcp.stream | sort -un | sed ':a;N;$!ba;s/\n/ or tcp.stream==/g'</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '12, 08:06</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-16218" class="comments-container"><span id="16221"></span><div id="comment-16221" class="comment"><div id="post-16221-score" class="comment-score"></div><div class="comment-text"><p>Hi Landi,</p><p>Thanks. Currently I'm doing it in a very similar way: I use <strong>http.host==<a href="http://www.google.com">www.google.com</a></strong> filter, export packet dissections to a text file, and as you said, using grep, awk and sed I prepare a long or-ed list. Not that elegant as with your tshark, however.</p><p>Anyway, tshark can save me a minute or so, however it still cuts my thoughts when I'm trying to focus on investigating a problem and I often lose concentration while playing with those filters. I would prefer something quicker. But thanks anyway. Maybe in newer versions there will be conditional filtering or some other sort of backreference.</p><p>Thank you.</p><p>Jozef</p></div><div id="comment-16221-info" class="comment-info"><span class="comment-age">(22 Nov '12, 13:39)</span> Jozef</div></div></div><div id="comment-tools-16218" class="comment-tools"></div><div class="clear"></div><div id="comment-16218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16334"></span>

<div id="answer-container-16334" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16334-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could probably achieve what you want with <a href="http://wiki.wireshark.org/Mate">MATE</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '12, 12:00</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-16334" class="comments-container"></div><div id="comment-tools-16334" class="comment-tools"></div><div class="clear"></div><div id="comment-16334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

