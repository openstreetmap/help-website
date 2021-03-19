+++
type = "question"
title = "How to filter multiple packets with same IP ID ?"
description = '''Hello, I have to filter and find if in the Trace we get 2 packets with same IP ID. (Ofcourse i dont know the IP ID in advance else its a simple filter). So, an example: I have a 10,000 packets trace, i should show packets only which have same IP ID repeated. How can i do it ? Regards, TA.'''
date = "2011-10-15T04:44:00Z"
lastmod = "2011-10-15T11:21:00Z"
weight = 6903
keywords = [ "filter" ]
aliases = [ "/questions/6903" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter multiple packets with same IP ID ?](/questions/6903/how-to-filter-multiple-packets-with-same-ip-id)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6903-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have to filter and find if in the Trace we get 2 packets with same IP ID. (Ofcourse i dont know the IP ID in advance else its a simple filter).</p><p>So, an example: I have a 10,000 packets trace, i should show packets only which have same IP ID repeated.</p><p>How can i do it ?</p><p>Regards, TA.</p></div><div id="question-tags" class="tags-container tags">filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '11, 04:44</strong></p><img src="https://secure.gravatar.com/avatar/292e32158685866b7b425081df56f50a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ankur&#39;s gravatar image" /><p>Ankur<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ankur has no accepted answers">0%</span></p></div></div><div id="comments-container-6903" class="comments-container"></div><div id="comment-tools-6903" class="comment-tools"></div><div class="clear"></div><div id="comment-6903-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6905"></span>

<div id="answer-container-6905" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6905-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What about starting with <a href="http://www.wireshark.org/docs/man-pages/tshark.html">TShark</a>, part of the <a href="http://www.wireshark.org/docs/man-pages/">Wireshark distribution</a>, to create a list of ip.id's:<br />
$ tshark -r DB01-22022011-1128.pcap -T fields -e ip.id | sort | uniq -c | sort -r &gt; ip.id.csv<br />
</p><pre><code>Output:
    824 
    107 0x0000
     11 0x18e9
     10 0x1a6d
     10 0x1a69
     10 0x1a63
     10 0x1a61
     10 0x1a35
     10 0x18d4
      9 0x1ac2
    etc.</code></pre><p>Hope this helps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Oct '11, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Oct '11, 12:55</p></div></div><div id="comments-container-6905" class="comments-container"></div><div id="comment-tools-6905" class="comment-tools"></div><div class="clear"></div><div id="comment-6905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6904"></span>

<div id="answer-container-6904" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6904-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ankur,</p><p>You may find this useful.</p><p>I had a same query and mate can address this pretty well.</p><p><a href="http://ask.wireshark.org/questions/5083/how-to-check-number-of-packets-with-duplicate-ip-identification-field">http://ask.wireshark.org/questions/5083/how-to-check-number-of-packets-with-duplicate-ip-identification-field</a></p><p>Hope this helps.</p><p>Regards,</p><p>-Deepak</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Oct '11, 09:28</strong></p><img src="https://secure.gravatar.com/avatar/a8aa1b50bd4e70fe64d8c9612d100eb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Deepak&#39;s gravatar image" /><p>Deepak<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Deepak has one accepted answer">25%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Oct '11, 11:22</p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span></p></div></div><div id="comments-container-6904" class="comments-container"></div><div id="comment-tools-6904" class="comment-tools"></div><div class="clear"></div><div id="comment-6904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

