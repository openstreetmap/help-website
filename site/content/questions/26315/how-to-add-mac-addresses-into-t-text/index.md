+++
type = "question"
title = "How to add mac-addresses into -T text ?"
description = '''Hu, guys! Is it possible to add mac-addresses into default output format for tshark? '''
date = "2013-10-23T02:15:00Z"
lastmod = "2013-10-24T10:20:00Z"
weight = 26315
keywords = [ "output", "tshark" ]
aliases = [ "/questions/26315" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to add mac-addresses into -T text ?](/questions/26315/how-to-add-mac-addresses-into-t-text)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26315-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hu, guys!</p><p>Is it possible to add mac-addresses into default output format for tshark?</p></div><div id="question-tags" class="tags-container tags">output tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '13, 02:15</strong></p><img src="https://secure.gravatar.com/avatar/7334f55881384d13512f7ffe4a8cda06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="itonohito&#39;s gravatar image" /><p>itonohito<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="itonohito has no accepted answers">0%</span></p></div></div><div id="comments-container-26315" class="comments-container"></div><div id="comment-tools-26315" class="comment-tools"></div><div class="clear"></div><div id="comment-26315-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26369"></span>

<div id="answer-container-26369" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26369-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The default columns that Wireshark uses are specified by the following in tshark:</p><ul><li><p>Windows:</p><p><code>tshark -o "column.format:\"No.\",\"%Cus:frame.number:0:R\",\"Time\",\"%t\",\"Source\",\"%s\",\"Destination\",\"%d\",\"Protocol\",\"%p\",\"Length\",\"%L\",\"Info\",\"%i\""</code></p></li><li><p>*Nix:</p><p><code>tshark -o 'column.format:"No.","%Cus:frame.number:0:R","Time","%t","Source","%s","Destination","%d","Protocol","%p","Length","%L","Info","%i"'</code></p></li></ul><p>If you want to display the mac addresses, you can modify that to use one or more of the following, giving any name you want for the format:</p><pre><code>Format  Description
%hd     Hardware dest addr
%hs     Hardware src addr
%rhd    Hw dest addr (resolved)
%uhd    Hw dest addr (unresolved)
%rhs    Hw src addr (resolved)
%uhs    Hw src addr (unresolved)</code></pre><p>For example:</p><pre><code>`tshark -o &#39;column.format:&quot;No.&quot;,&quot;%Cus:frame.number:0:R&quot;,&quot;Time&quot;,&quot;%t&quot;,&quot;HwSrc&quot;,&quot;%hs&quot;,&quot;HwDst&quot;,&quot;%hd&quot;&#39;`</code></pre><p>If you're using a version of Wireshark post <a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=52627">r52627</a>, then you can run <code>tshark -G column-formats</code> to see all the available column options. If not, then you can refer to the <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/column.c?revision=52802&amp;view=markup">Wireshark source code</a> for them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '13, 10:20</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-26369" class="comments-container"></div><div id="comment-tools-26369" class="comment-tools"></div><div class="clear"></div><div id="comment-26369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

