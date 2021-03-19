+++
type = "question"
title = "extract mac address using mate"
description = '''Hi, Part of the flow is the source and destination mac address but looks like mate isnt capable to extract eth.addr , can it be configured ? Sample which i tried: Pdu icmp_pdu Proto icmp Transport ip {  Extract addr From ip.addr;  Extract source_addr From eth.addr;  Extract icmp_type From icmp.type;...'''
date = "2011-05-09T00:45:00Z"
lastmod = "2011-05-09T06:00:00Z"
weight = 4013
keywords = [ "mate" ]
aliases = [ "/questions/4013" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [extract mac address using mate](/questions/4013/extract-mac-address-using-mate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4013-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Part of the flow is the source and destination mac address but looks like mate isnt capable to extract eth.addr , can it be configured ?</p><p>Sample which i tried:</p><p>Pdu icmp_pdu Proto icmp Transport ip {</p><pre><code>    Extract addr From ip.addr;
    Extract source_addr From eth.addr;
    Extract icmp_type From icmp.type;</code></pre><p>};</p><p>Gop icmp_ses On icmp_pdu Match (addr, addr, source_addr, source_addr) {</p><pre><code>Start (icmp_type=8);
Stop (icmp_type=0);
Extra (addr, addr, source_addr, source_addr, icmp_type);</code></pre><p>};</p><p>Done;</p></div><div id="question-tags" class="tags-container tags">mate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '11, 00:45</strong></p><img src="https://secure.gravatar.com/avatar/3b6ed2644a62e0d6abb85d364c7421bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="okochva&#39;s gravatar image" /><p>okochva<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="okochva has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 May '11, 01:37</p></div></div><div id="comments-container-4013" class="comments-container"></div><div id="comment-tools-4013" class="comment-tools"></div><div class="clear"></div><div id="comment-4013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4015"></span>

<div id="answer-container-4015" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4015-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>My suggestion would be to use eth.src and ip.src instead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '11, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4015" class="comments-container"></div><div id="comment-tools-4015" class="comment-tools"></div><div class="clear"></div><div id="comment-4015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

