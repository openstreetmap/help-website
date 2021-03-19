+++
type = "question"
title = "Capture filter with SSL hex output from tshark"
description = '''I&#x27;m using the answer from this question to hex data from SSL traffic, how do I add a capture filter along with this so that I get hex dump of only that hosts&#x27; application data. I tried using &#x27;host gateway.push.apple.com&#x27; but said that its a capture filter . I need to basically filter for this host a...'''
date = "2015-01-23T13:34:00Z"
lastmod = "2015-01-23T14:07:00Z"
weight = 39372
keywords = [ "filter", "ssl", "tshark", "capture" ]
aliases = [ "/questions/39372" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter with SSL hex output from tshark](/questions/39372/capture-filter-with-ssl-hex-output-from-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39372-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using the answer from <a href="https://ask.wireshark.org/questions/25371/how-to-extract-hex-data-from-ssl">this</a> question to hex data from SSL traffic, how do I add a capture filter along with this so that I get hex dump of only that hosts' application data. I tried using 'host gateway.push.apple.com' but said that its a capture filter . I need to basically filter for this host and need to get decrypted hex dump of application data alone. Can tshark do that?</p></div><div id="question-tags" class="tags-container tags">filter ssl tshark capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '15, 13:34</strong></p><img src="https://secure.gravatar.com/avatar/c4c458d132817abc7f621c553c64db41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arungeorg81&#39;s gravatar image" /><p>arungeorg81<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arungeorg81 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted 23 Jan '15, 14:03</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-39372" class="comments-container"></div><div id="comment-tools-39372" class="comment-tools"></div><div class="clear"></div><div id="comment-39372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39373"></span>

<div id="answer-container-39373" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39373-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming you're using a command line similar to that of the answer to which you attached your question, i.e.</p><pre><code>tshark -Vnxr pcap -R (filter) &gt; textfile</code></pre><p>Then the <code>-R (filter)</code> part of the answer is for a display filter. For a capture filter use <code>-f (filter)</code>, as explained in the <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark</a> help file or the output of <code>tshark -h</code>:</p><pre><code>Capture interface:                                                           
  -i &lt;interface&gt;      name or idx of interface (def: first non-loopback)
  -f &lt;capture filter&gt;      packet filter in libpcap filter syntax            
  ...</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '15, 14:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-39373" class="comments-container"></div><div id="comment-tools-39373" class="comment-tools"></div><div class="clear"></div><div id="comment-39373-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

