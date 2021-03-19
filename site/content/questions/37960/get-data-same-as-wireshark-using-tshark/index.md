+++
type = "question"
title = "Get Data same as Wireshark using Tshark"
description = '''tshark.exe -i 1 -P -V -S &#92;&quot;End of Packet&#92;&quot; -x  gives all the required data of the packet, packet detail as well as packet bytes but how can I split the  Frames Ethernet IP Version TCP etc tried using : -E&amp;lt;fieldsoption&amp;gt;=&amp;lt;value&amp;gt; set options for output when -Tfields selected:  header=y|n sw...'''
date = "2014-11-19T01:59:00Z"
lastmod = "2014-11-19T02:15:00Z"
weight = 37960
keywords = [ "packet-display", "tshark", "wireshark" ]
aliases = [ "/questions/37960" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Get Data same as Wireshark using Tshark](/questions/37960/get-data-same-as-wireshark-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37960-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>tshark.exe -i 1 -P -V -S \&quot;End of Packet\&quot; -x</code></pre><p>gives all the required data of the packet, packet detail as well as packet bytes</p><p>but how can I split the Frames Ethernet IP Version TCP</p><p>etc</p><p>tried using :</p><pre><code>-E&lt;fieldsoption&gt;=&lt;value&gt; set options for output when -Tfields selected:
 header=y|n            switch headers on and off
 separator=/t|/s|&lt;char&gt; select tab, space, printable character as separator
 occurrence=f|l|a      print first, last or all occurrences of each field
 aggregator=,|/s|&lt;char&gt; select comma, space, printable character as
                       aggregator</code></pre><p>Thanks, in advance</p></div><div id="question-tags" class="tags-container tags">packet-display tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '14, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/d1fba3d75c7af8dc47876eede9fb1191?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erarijit&#39;s gravatar image" /><p>erarijit<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erarijit has no accepted answers">0%</span></p></div></div><div id="comments-container-37960" class="comments-container"></div><div id="comment-tools-37960" class="comment-tools"></div><div class="clear"></div><div id="comment-37960-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37963"></span>

<div id="answer-container-37963" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37963-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You must add a <code>-T fields</code> parameter to use <code>-E</code> and <code>-e</code>. What did you try?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '14, 02:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Nov '14, 02:25</p></div></div><div id="comments-container-37963" class="comments-container"><span id="37964"></span><div id="comment-37964" class="comment"><div id="post-37964-score" class="comment-score"></div><div class="comment-text"><p>no I didn't added -T fields</p><p>can you show me an example if you have?</p></div><div id="comment-37964-info" class="comment-info"><span class="comment-age">(19 Nov '14, 02:19)</span> erarijit</div></div><span id="37966"></span><div id="comment-37966" class="comment"><div id="post-37966-score" class="comment-score"></div><div class="comment-text"><p>I've corrected my answer a bit. Use <code>-T fields</code> to switch to fields mode, use <code>-E</code> to set field options such as separator and quotes and then use multiple <code>-e fieldname</code> parameters to specify the fields.</p><p>There are examples of the parameters in the <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a>, and Google and this site should show you lots more.</p></div><div id="comment-37966-info" class="comment-info"><span class="comment-age">(19 Nov '14, 02:30)</span> grahamb ♦</div></div></div><div id="comment-tools-37963" class="comment-tools"></div><div class="clear"></div><div id="comment-37963-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

