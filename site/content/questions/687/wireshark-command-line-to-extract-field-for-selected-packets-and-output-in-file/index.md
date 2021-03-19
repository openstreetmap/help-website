+++
type = "question"
title = "Wireshark command line to extract field for selected packets and output in file"
description = '''How can I run wireshark from the command line to open a file, and output a file containing only the udp.length of every DNS packet? '''
date = "2010-10-26T16:29:00Z"
lastmod = "2010-10-26T16:47:00Z"
weight = 687
keywords = [ "udp", "extract", "dns" ]
aliases = [ "/questions/687" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark command line to extract field for selected packets and output in file](/questions/687/wireshark-command-line-to-extract-field-for-selected-packets-and-output-in-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-687-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I run wireshark from the command line to open a file, and output a file containing only the udp.length of every DNS packet?</p></div><div id="question-tags" class="tags-container tags">udp extract dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '10, 16:29</strong></p><img src="https://secure.gravatar.com/avatar/da051abac41879aed4060d544d37fd6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skypemesm&#39;s gravatar image" /><p>skypemesm<br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skypemesm has no accepted answers">0%</span></p></div></div><div id="comments-container-687" class="comments-container"></div><div id="comment-tools-687" class="comment-tools"></div><div class="clear"></div><div id="comment-687-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="688"></span>

<div id="answer-container-688" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-688-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You might want to take a look at <a href="http://www.wireshark.org/docs/man-pages/rawshark.html">rawshark</a> or at <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark's "-T fields" option</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '10, 16:47</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-688" class="comments-container"><span id="689"></span><div id="comment-689" class="comment"><div id="post-689-score" class="comment-score"></div><div class="comment-text"><p>tshark -R "dns" -r abc.pcap -T fields -e udp.length</p></div><div id="comment-689-info" class="comment-info"><span class="comment-age">(26 Oct '10, 17:38)</span> skypemesm</div></div><span id="693"></span><div id="comment-693" class="comment"><div id="post-693-score" class="comment-score">2</div><div class="comment-text"><p>and if you want to do the same for live traffic, try...</p><p>tshark -T fields -e udp.length -f "port 53"</p><p>throw a &gt; udplength.txt to export the info to a text file</p></div><div id="comment-693-info" class="comment-info"><span class="comment-age">(26 Oct '10, 19:38)</span> lchappell ♦</div></div></div><div id="comment-tools-688" class="comment-tools"></div><div class="clear"></div><div id="comment-688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

