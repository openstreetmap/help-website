+++
type = "question"
title = "How to filter a large group of different ip addresses?"
description = '''Hi every body, I want to know how I could filter a large group of ip addresses (in a Listener) which I can&#x27;t filter them using a network notation like(ip.addr==10.0.0.0&#92;8) because they are from different networks, and it will be too long to write them manually like this(ip.addr==141.55.12.13 or ip.a...'''
date = "2012-12-04T23:30:00Z"
lastmod = "2012-12-05T01:33:00Z"
weight = 16565
keywords = [ "lua", "wireshark" ]
aliases = [ "/questions/16565" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter a large group of different ip addresses?](/questions/16565/how-to-filter-a-large-group-of-different-ip-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16565-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi every body, I want to know how I could filter a large group of ip addresses (in a Listener) which I can't filter them using a network notation like(ip.addr==10.0.0.0\8) because they are from different networks, and it will be too long to write them manually like this(ip.addr==141.55.12.13 or ip.addr==212.67.108.5 or ....) Thanks</p></div><div id="question-tags" class="tags-container tags">lua wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '12, 23:30</strong></p><img src="https://secure.gravatar.com/avatar/912ebc145cb38ec3da99be6003d7d9b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leena&#39;s gravatar image" /><p>Leena<br />
<span class="score" title="51 reputation points">51</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leena has no accepted answers">0%</span></p></div></div><div id="comments-container-16565" class="comments-container"><span id="16568"></span><div id="comment-16568" class="comment"><div id="post-16568-score" class="comment-score">1</div><div class="comment-text"><p>where do you have the IP addresses, inside a text file or something line by line?</p></div><div id="comment-16568-info" class="comment-info"><span class="comment-age">(05 Dec '12, 00:14)</span> Landi</div></div><span id="16570"></span><div id="comment-16570" class="comment"><div id="post-16570-score" class="comment-score"></div><div class="comment-text"><p>you can say it inside a text file</p></div><div id="comment-16570-info" class="comment-info"><span class="comment-age">(05 Dec '12, 00:33)</span> Leena</div></div></div><div id="comment-tools-16565" class="comment-tools"></div><div class="clear"></div><div id="comment-16565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16575"></span>

<div id="answer-container-16575" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16575-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Under Linux you can use sed to replace the new lines in a given text file with a string of your choice, e.g.</p><pre><code>cat ip_list.txt |  sed &#39;:a;N;$!ba;s/\n/ or ip.addr==/g&#39;</code></pre><p>will replace each new line with " or ip.addr==" giving you a near working filter string for your shark, you just have to apply another "ip.addr==" just in front of the output before the very first IP address.</p><p>Under windows I do exactly the same Task using e.g. notepad++ with string replace using the radio button "enhanced search", which makes it able to search for \r\n and replace this with or 'ip.addr=='</p><p>Of course you can extend this by scripting the complete process, but that does the job in a very quick manner...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '12, 01:33</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Dec '12, 01:33</p></div></div><div id="comments-container-16575" class="comments-container"></div><div id="comment-tools-16575" class="comment-tools"></div><div class="clear"></div><div id="comment-16575-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16566"></span>

<div id="answer-container-16566" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16566-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You got the slash backwards, otherwise your idea is good. Use ip.addr==10.0.0.0/8, and you're good to go.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '12, 23:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-16566" class="comments-container"><span id="16567"></span><div id="comment-16567" class="comment"><div id="post-16567-score" class="comment-score">1</div><div class="comment-text"><p>He was saying that the IPs are NOT inside a CIDR notable subnet because in different networks</p></div><div id="comment-16567-info" class="comment-info"><span class="comment-age">(05 Dec '12, 00:13)</span> Landi</div></div><span id="16571"></span><div id="comment-16571" class="comment"><div id="post-16571-score" class="comment-score"></div><div class="comment-text"><p>this is exactly what I mean Landi. Thanks Jasper for the correction</p></div><div id="comment-16571-info" class="comment-info"><span class="comment-age">(05 Dec '12, 00:34)</span> Leena</div></div><span id="16574"></span><div id="comment-16574" class="comment"><div id="post-16574-score" class="comment-score"></div><div class="comment-text"><p>Okay, I wasn't awake when I read the question I think :-)</p></div><div id="comment-16574-info" class="comment-info"><span class="comment-age">(05 Dec '12, 01:28)</span> Jasper ♦♦</div></div></div><div id="comment-tools-16566" class="comment-tools"></div><div class="clear"></div><div id="comment-16566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

