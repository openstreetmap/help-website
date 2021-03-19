+++
type = "question"
title = "how to calculate total sum of ip.len field for wireshark trace"
description = '''Hello, I would like to calculate sum af all ip.len values in packets. There is option cumulative but it works only for frame.len value. Thanks'''
date = "2011-03-10T03:25:00Z"
lastmod = "2011-03-10T05:44:00Z"
weight = 2755
keywords = [ "length", "framelength" ]
aliases = [ "/questions/2755" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to calculate total sum of ip.len field for wireshark trace](/questions/2755/how-to-calculate-total-sum-of-iplen-field-for-wireshark-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2755-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I would like to calculate sum af all ip.len values in packets. There is option cumulative but it works only for frame.len value. Thanks</p></div><div id="question-tags" class="tags-container tags">length framelength</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '11, 03:25</strong></p><img src="https://secure.gravatar.com/avatar/bd2e9fd5927ea5cb7a241c3a7454111b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lavpivolav&#39;s gravatar image" /><p>lavpivolav<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lavpivolav has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 10 Mar '11, 08:42</p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span></p></div></div><div id="comments-container-2755" class="comments-container"></div><div id="comment-tools-2755" class="comment-tools"></div><div class="clear"></div><div id="comment-2755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2759"></span>

<div id="answer-container-2759" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2759-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use TShark.<br />
In this example the interval is 30 seconds.<br />
<br />
$ tshark -r test.pcap -q -z io,stat,30,COUNT"(tcp.len)tcp.len",MIN"(tcp.len)tcp.len",MAX"(tcp.len)tcp.len",AVG"(tcp.len)tcp.len" &gt; tcp.len.txt<br />
<br />
Output:<br />
IO Statistics<br />
Interval: 30.000 secs<br />
Column #0: COUNT(tcp.len)tcp.len<br />
Column #1: MIN(tcp.len)tcp.len<br />
Column #2: MAX(tcp.len)tcp.len<br />
Column #3: AVG(tcp.len)tcp.len<br />
</p><pre><code>                |   Column #0    |   Column #1    |   Column #2    |   Column #3  

Time            |          COUNT |            MIN |            MAX |            AVG 
000.000-030.000               802                0            29193              354 
030.000-060.000              1231                0            36500              397 
060.000-090.000              1478                0            37478              342 
090.000-120.000               418                0             2372              232 </code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '11, 05:44</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-2759" class="comments-container"><span id="2763"></span><div id="comment-2763" class="comment"><div id="post-2763-score" class="comment-score"></div><div class="comment-text"><p>Hello, Thanks on answer, it helped Best Regards</p></div><div id="comment-2763-info" class="comment-info"><span class="comment-age">(10 Mar '11, 09:21)</span> lavpivolav</div></div></div><div id="comment-tools-2759" class="comment-tools"></div><div class="clear"></div><div id="comment-2759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

