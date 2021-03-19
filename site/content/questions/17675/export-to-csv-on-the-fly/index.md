+++
type = "question"
title = "Export to csv on the fly."
description = '''I have incoming streaming data packets. I need to  Isolate the packets from a certain ip. Filter only those of certain length From those filtered packets I need to filter the last 7 bytes. The data should be inserted on the fly to a comma based csv file.  Is this possible with Wireshark?'''
date = "2013-01-14T13:51:00Z"
lastmod = "2013-01-14T15:10:00Z"
weight = 17675
keywords = [ "csv" ]
aliases = [ "/questions/17675" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Export to csv on the fly.](/questions/17675/export-to-csv-on-the-fly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17675-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have incoming streaming data packets. I need to</p><ol><li>Isolate the packets from a certain ip.</li><li>Filter only those of certain length</li><li>From those filtered packets I need to filter the last 7 bytes.</li><li>The data should be inserted on the fly to a comma based csv file.</li></ol><p>Is this possible with Wireshark?</p></div><div id="question-tags" class="tags-container tags">csv</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '13, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/cbe818b0c449bece8779758f078f7393?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="berkz&#39;s gravatar image" /><p>berkz<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="berkz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Jan '13, 13:56</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-17675" class="comments-container"></div><div id="comment-tools-17675" class="comment-tools"></div><div class="clear"></div><div id="comment-17675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17679"></span>

<div id="answer-container-17679" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17679-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you could do that with wireshark by writing a <a href="http://wiki.wireshark.org/Lua">Lua</a> script for it. However, Wireshark accumulates state information, so you will run out of memory in the long run (or less long run on high bandwidth networks). I think writing a little libpcap application in C or Perl or any language of your choice is a better bet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '13, 15:10</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17679" class="comments-container"><span id="17681"></span><div id="comment-17681" class="comment"><div id="post-17681-score" class="comment-score"></div><div class="comment-text"><p>Thx for the quick reply. Also I've been checking out the command line interface. Is it possible to filter by packet lenght using the CLI ?</p></div><div id="comment-17681-info" class="comment-info"><span class="comment-age">(14 Jan '13, 16:47)</span> berkz</div></div><span id="17684"></span><div id="comment-17684" class="comment"><div id="post-17684-score" class="comment-score">1</div><div class="comment-text"><p>Yes, you can use a display filter like this:</p><pre><code>tshark -r &lt;file&gt; -R frame.len==1510</code></pre><p>Or a capture filter like this:</p><pre><code>tshark -i &lt;interface&gt; -f len=1510</code></pre></div><div id="comment-17684-info" class="comment-info"><span class="comment-age">(14 Jan '13, 23:21)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-17679" class="comment-tools"></div><div class="clear"></div><div id="comment-17679-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

