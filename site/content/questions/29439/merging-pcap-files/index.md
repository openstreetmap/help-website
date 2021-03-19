+++
type = "question"
title = "Merging PCAP files"
description = '''I know it is possible to merge 2 pcap files by selecting File-&amp;gt;Merge, but is it possible to merge more than 2 PCAP file using command line interface of Wireshark ?'''
date = "2014-02-04T21:50:00Z"
lastmod = "2014-02-04T22:17:00Z"
weight = 29439
keywords = [ "merge", "command-line" ]
aliases = [ "/questions/29439" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Merging PCAP files](/questions/29439/merging-pcap-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29439-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know it is possible to merge 2 pcap files by selecting File-&gt;Merge, but is it possible to merge more than 2 PCAP file using command line interface of Wireshark ?</p></div><div id="question-tags" class="tags-container tags">merge command-line</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '14, 21:50</strong></p><img src="https://secure.gravatar.com/avatar/bc835c49c84e7410e78b82e40ac9620e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ashiq&#39;s gravatar image" /><p>Ashiq<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ashiq has no accepted answers">0%</span></p></div></div><div id="comments-container-29439" class="comments-container"></div><div id="comment-tools-29439" class="comment-tools"></div><div class="clear"></div><div id="comment-29439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29441"></span>

<div id="answer-container-29441" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29441-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use mergecap to achieve this</p><pre><code>mergecap -w merged.pcapng  input_traces*</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '14, 22:17</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-29441" class="comments-container"><span id="29442"></span><div id="comment-29442" class="comment"><div id="post-29442-score" class="comment-score"></div><div class="comment-text"><p>Thanks, It works great. Is there a website where I can get a list of all commands related to wireshark ???</p></div><div id="comment-29442-info" class="comment-info"><span class="comment-age">(04 Feb '14, 22:22)</span> Ashiq</div></div><span id="29443"></span><div id="comment-29443" class="comment"><div id="post-29443-score" class="comment-score"></div><div class="comment-text"><p><a href="http://www.wireshark.org/docs/man-pages/">http://www.wireshark.org/docs/man-pages/</a></p></div><div id="comment-29443-info" class="comment-info"><span class="comment-age">(04 Feb '14, 23:02)</span> mrEEde</div></div></div><div id="comment-tools-29441" class="comment-tools"></div><div class="clear"></div><div id="comment-29441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

