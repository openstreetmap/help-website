+++
type = "question"
title = "Capture Filter, TCP port only using tshark, is my command syntax correct?"
description = '''Hi There, I&#x27;m new to tshark, and I want to run some tests before I give it a go on our live server.  I want to catch all packets on a single tcp port number, save them over ten files each with a size of 1KB.  I&#x27;ve tried the following command:  tshark -p -n -i eno1 -f &quot;tcp port 40000&quot; -a files:10 -b ...'''
date = "2016-04-22T01:39:00Z"
lastmod = "2016-04-22T03:34:00Z"
weight = 51863
keywords = [ "ringbuffer", "tshark", "tcp", "port" ]
aliases = [ "/questions/51863" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Capture Filter, TCP port only using tshark, is my command syntax correct?](/questions/51863/capture-filter-tcp-port-only-using-tshark-is-my-command-syntax-correct)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51863-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi There, I'm new to tshark, and I want to run some tests before I give it a go on our live server.</p><p>I want to catch all packets on a single tcp port number, save them over ten files each with a size of 1KB.</p><p>I've tried the following command:</p><pre><code>tshark -p -n -i eno1 -f &quot;tcp port 40000&quot; -a files:10 -b files:10 filesize:1024 -w /var/log/tshark/tcpds</code></pre><p>It appears to work, I get the following response:</p><pre><code>tshark: A capture filter was specified both with &quot;-f&quot; and with additional command-line arguments.</code></pre><p>But nothing is being saved at the location specified. I've tried it both with and without sudo, the response is the same. What am I doing wrong?</p></div><div id="question-tags" class="tags-container tags">ringbuffer tshark tcp port</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '16, 01:39</strong></p><img src="https://secure.gravatar.com/avatar/3ab01be5b3ec231ca1b6fee9c0c27582?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elektrovert&#39;s gravatar image" /><p>elektrovert<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elektrovert has no accepted answers">0%</span></p></div></div><div id="comments-container-51863" class="comments-container"></div><div id="comment-tools-51863" class="comment-tools"></div><div class="clear"></div><div id="comment-51863-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51865"></span>

<div id="answer-container-51865" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51865-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your second option for the <code>-b</code> parameter (<code>filesize:1024</code>) also needs a preceding <code>-b</code>, i.e.</p><p><code>tshark -p -n -i eno1 -f "tcp port 40000" -a files:10 -b files:10 -b filesize:1024 -w /var/log/tshark/tcpds</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '16, 03:34</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51865" class="comments-container"><span id="51867"></span><div id="comment-51867" class="comment"><div id="post-51867-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I'll try that out!</p></div><div id="comment-51867-info" class="comment-info"><span class="comment-age">(22 Apr '16, 04:46)</span> elektrovert</div></div></div><div id="comment-tools-51865" class="comment-tools"></div><div class="clear"></div><div id="comment-51865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

