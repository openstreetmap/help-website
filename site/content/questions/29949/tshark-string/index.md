+++
type = "question"
title = "tshark string"
description = '''hi all, How to extract only tcp streams containing a specific string to single pcap file using tshark.'''
date = "2014-02-17T21:22:00Z"
lastmod = "2014-02-19T05:57:00Z"
weight = 29949
keywords = [ "editshark" ]
aliases = [ "/questions/29949" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark string](/questions/29949/tshark-string)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29949-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi all, How to extract only tcp streams containing a specific string to single pcap file using tshark.</p></div><div id="question-tags" class="tags-container tags">editshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '14, 21:22</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p>kishan pandey<br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-29949" class="comments-container"></div><div id="comment-tools-29949" class="comment-tools"></div><div class="clear"></div><div id="comment-29949-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30003"></span>

<div id="answer-container-30003" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30003-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p><strong>tshark on Windows (DOS box):</strong></p><blockquote><p>tshark -nr input.pcap -Y "frame contains ""HTTP/1.0""" -w output.pcap</p></blockquote><p>Tripple quote (""") is intentional!</p><p><strong>tshark on Linux:</strong></p><blockquote><p>tshark -nr input.pcap -Y 'frame contains "HTTP/1.0"' -w output.pcap</p></blockquote><p><strong>ngrep:</strong> (another open source tool)<br />
</p><blockquote><p>ngrep -I input.pcap -i 'HTTP/1.0' -O output.pcap</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '14, 05:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Feb '14, 06:34</p></div></div><div id="comments-container-30003" class="comments-container"><span id="30005"></span><div id="comment-30005" class="comment"><div id="post-30005-score" class="comment-score">1</div><div class="comment-text"><p><strong>tshark on Windows PowerShell:</strong></p><pre><code>tshark -nr input.pcap -Y &#39;frame contains &quot;HTTP/1.0&quot;&#39; -w output.pcap</code></pre><p>i.e. the same as Linux.</p><p>I think you're missing a closing double quote on the Linux example.</p></div><div id="comment-30005-info" class="comment-info"><span class="comment-age">(19 Feb '14, 06:32)</span> grahamb ♦</div></div><span id="30007"></span><div id="comment-30007" class="comment"><div id="post-30007-score" class="comment-score"></div><div class="comment-text"><p>Yep. Thanks for the hint!! I fixed it in the answer.</p></div><div id="comment-30007-info" class="comment-info"><span class="comment-age">(19 Feb '14, 06:33)</span> Kurt Knochner ♦</div></div><span id="30096"></span><div id="comment-30096" class="comment"><div id="post-30096-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot kurt and graham,i will test this and revert.</p></div><div id="comment-30096-info" class="comment-info"><span class="comment-age">(21 Feb '14, 22:53)</span> kishan pandey</div></div></div><div id="comment-tools-30003" class="comment-tools"></div><div class="clear"></div><div id="comment-30003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

