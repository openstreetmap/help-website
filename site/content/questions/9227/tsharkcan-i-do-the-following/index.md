+++
type = "question"
title = "tshark...can I  do the following"
description = '''I use tshark to capture a group of packets. I&#x27;d like to use tshark a second time to: 1) look at a specific packet number 2) return the bytes in the data field (the actual textual response to an http query) to a file as text. Can I issue a single tshark command that does both things ?? thanks, wk '''
date = "2012-02-26T18:58:00Z"
lastmod = "2012-02-27T06:53:00Z"
weight = 9227
keywords = [ "link", "data", "tshark", "retrieval" ]
aliases = [ "/questions/9227" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tshark...can I do the following](/questions/9227/tsharkcan-i-do-the-following)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9227-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use tshark to capture a group of packets. I'd like to use tshark a second time to:</p><p>1) look at a specific packet number</p><p>2) return the bytes in the data field (the actual textual response to an http query) to a file as text.</p><p>Can I issue a single tshark command that does both things ??</p><p>thanks, wk</p></div><div id="question-tags" class="tags-container tags">link data tshark retrieval</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '12, 18:58</strong></p><img src="https://secure.gravatar.com/avatar/2b12f1f0687101a1dd8f75db884aed8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wakelt&#39;s gravatar image" /><p>wakelt<br />
<span class="score" title="13 reputation points">13</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wakelt has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '12, 20:32</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-9227" class="comments-container"></div><div id="comment-tools-9227" class="comment-tools"></div><div class="clear"></div><div id="comment-9227-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9228"></span>

<div id="answer-container-9228" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9228-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi wk,</p><p>To filter a specific packet number, you can use the -R option to set a display filter like the following where X is the packet you want.</p><pre><code>tshark -r &lt;infile&gt; -R frame.number==X</code></pre><p>Are you looking for the server response to an HTTP request? That is available with the following:</p><pre><code>tshark -r &lt;infile&gt; -R frame.number==X -T fields -e http.response.code -e http.response.phrase</code></pre><p>Getting back the full HTTP data response isn't as easy since the payload may be split over multiple packets. You can get back the TCP.data layer, but that will also contain any HTTP headers in the packet. Also the output seems to be only in Hex.</p><pre><code>tshark -r &lt;infile&gt; -R frame.number==X -T fields -e tcp.data</code></pre><p>Hope this helps somewhat, I'm not sure if the whole HTTP response can be pulled out of tshark easily.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '12, 20:00</strong></p><img src="https://secure.gravatar.com/avatar/365cfc3c62b61b2ed219b5d146e8ad3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zachad&#39;s gravatar image" /><p>zachad<br />
<span class="score" title="331 reputation points">331</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zachad has 3 accepted answers">21%</span></p></div></div><div id="comments-container-9228" class="comments-container"><span id="9243"></span><div id="comment-9243" class="comment"><div id="post-9243-score" class="comment-score"></div><div class="comment-text"><p>thanks Zachad !</p><p>I am trying to get at some data that is included in the http response. For example, there may be some text wrapped inside the http response.</p><p>I can use:</p><p>-T fields -e data-text-lines</p><p>This gets to me to the top of the data in the reassembled payload. The data of interest lies immediately below. How do I extract (=save in file) the remainder of the reassembled payload ?</p><p>-wk</p></div><div id="comment-9243-info" class="comment-info"><span class="comment-age">(27 Feb '12, 05:43)</span> wakelt</div></div><span id="9244"></span><div id="comment-9244" class="comment"><div id="post-9244-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment", please see the FAQ for details)</p></div><div id="comment-9244-info" class="comment-info"><span class="comment-age">(27 Feb '12, 06:51)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-9228" class="comment-tools"></div><div class="clear"></div><div id="comment-9228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9246"></span>

<div id="answer-container-9246" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9246-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can also use the "-V" option of tshark like this:</p><pre><code>tshark -r file.cap -R http -V</code></pre><p>This will give you full dissection on all protocols. You can restrict full dissection to only HTTP by adding "-O http".</p><p>Hope this helps...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '12, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9246" class="comments-container"><span id="9252"></span><div id="comment-9252" class="comment"><div id="post-9252-score" class="comment-score"></div><div class="comment-text"><p>Thanks SYN-Bit....<br />
</p><p>I don't see an -O option available for tshark. Did you mean something different ?? I suppose I could pipe the tshark output into a script that will strip out the data I'm looking for.</p></div><div id="comment-9252-info" class="comment-info"><span class="comment-age">(27 Feb '12, 11:58)</span> wakelt</div></div><span id="9253"></span><div id="comment-9253" class="comment"><div id="post-9253-score" class="comment-score"></div><div class="comment-text"><p>(please use "add new comment" instead of "answer", see the FAQ for details)</p><p>The -O option was added recently, so I think you will need version 1.7.x for it</p></div><div id="comment-9253-info" class="comment-info"><span class="comment-age">(27 Feb '12, 12:15)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-9246" class="comment-tools"></div><div class="clear"></div><div id="comment-9246-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

