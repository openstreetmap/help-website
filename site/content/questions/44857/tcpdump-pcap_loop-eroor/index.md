+++
type = "question"
title = "tcpdump pcap_loop eroor"
description = '''Hi When i use tcpdump along with Gulp I get an error  tcpdump: pcap_loop: error reading dump file: Interrupted system call The code I used is   ./gulp -i eth1 -r 1024 -p 10 | taskset -c 2 tcpdump -r- -C 2 -W 5 -Z root -w /share/capture/job.pcap  Could you please help me with this??'''
date = "2015-08-05T01:52:00Z"
lastmod = "2015-08-11T16:36:00Z"
weight = 44857
keywords = [ "tcpdump" ]
aliases = [ "/questions/44857" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tcpdump pcap\_loop eroor](/questions/44857/tcpdump-pcap_loop-eroor)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44857-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi When i use tcpdump along with Gulp I get an error</p><p><code>tcpdump: pcap_loop: error reading dump file: Interrupted system call</code></p><p>The code I used is</p><pre><code> ./gulp  -i eth1 -r 1024  -p 10 | taskset -c 2 tcpdump -r- -C 2 -W 5 -Z root -w /share/capture/job.pcap</code></pre><p>Could you please help me with this??</p></div><div id="question-tags" class="tags-container tags">tcpdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '15, 01:52</strong></p><img src="https://secure.gravatar.com/avatar/5bf5e940f9cb50a96c3ee06e808e5eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jichu&#39;s gravatar image" /><p>jichu<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jichu has no accepted answers">0%</span></p></div></div><div id="comments-container-44857" class="comments-container"></div><div id="comment-tools-44857" class="comment-tools"></div><div class="clear"></div><div id="comment-44857-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44976"></span>

<div id="answer-container-44976" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44976-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think that <strong>taskset</strong> will pass STDIN to tcpdump. Please try your command without taskset.</p><blockquote><p>./gulp -i eth1 -r 1024 -p 10 | tcpdump -r- -C 2 -W 5 -Z root -w /share/capture/job.pcap</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '15, 16:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-44976" class="comments-container"></div><div id="comment-tools-44976" class="comment-tools"></div><div class="clear"></div><div id="comment-44976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

