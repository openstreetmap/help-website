+++
type = "question"
title = "How to force capinfos to show exact packet count?"
description = '''I&#x27;m using capinfos as follow to get number of packets in my pcap file: capinfos MY_PCAP_FILE -c  There result does not show the exact number of packets:  Number of packets: 2264 k  Is there any way to force it to show packet count in right manner?'''
date = "2015-02-05T05:03:00Z"
lastmod = "2015-02-05T05:58:00Z"
weight = 39661
keywords = [ "count", "capinfos" ]
aliases = [ "/questions/39661" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to force capinfos to show exact packet count?](/questions/39661/how-to-force-capinfos-to-show-exact-packet-count)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39661-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using capinfos as follow to get number of packets in my pcap file:</p><pre><code>capinfos MY_PCAP_FILE -c</code></pre><p>There result does not show the exact number of packets:</p><blockquote><p>Number of packets: <strong>2264 k</strong></p></blockquote><p>Is there any way to force it to show packet count in right manner?</p></div><div id="question-tags" class="tags-container tags">count capinfos</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '15, 05:03</strong></p><img src="https://secure.gravatar.com/avatar/71d18146e011b67e81934ee506cf6b08?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SuBCo&#39;s gravatar image" /><p>SuBCo<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SuBCo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Feb '15, 05:04</p></div></div><div id="comments-container-39661" class="comments-container"></div><div id="comment-tools-39661" class="comment-tools"></div><div class="clear"></div><div id="comment-39661-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39664"></span>

<div id="answer-container-39664" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39664-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sure, add <code>-M</code> to the parameters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '15, 05:58</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-39664" class="comments-container"></div><div id="comment-tools-39664" class="comment-tools"></div><div class="clear"></div><div id="comment-39664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

