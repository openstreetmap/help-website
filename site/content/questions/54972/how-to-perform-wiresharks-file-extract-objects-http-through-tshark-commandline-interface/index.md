+++
type = "question"
title = "How to perform Wiresharks File-&gt;Extract Objects-&gt;HTTP through Tshark commandline interface?"
description = '''Using TShark, I want to be able to extract the payload in HTTP response from packets data captured through tshark in a .pcap file.  In the Wireshark GUI, I was able to do that by File &amp;gt; Extract Objects &amp;gt; HTTP, and then choosing a file from the HTTP Objects dialog (which shows a list of all HTT...'''
date = "2016-08-19T03:16:00Z"
lastmod = "2016-11-13T09:29:00Z"
weight = 54972
keywords = [ "http.response", "http", "tshark", "wireshark" ]
aliases = [ "/questions/54972" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to perform Wiresharks File-&gt;Extract Objects-&gt;HTTP through Tshark commandline interface?](/questions/54972/how-to-perform-wiresharks-file-extract-objects-http-through-tshark-commandline-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54972-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using TShark, I want to be able to extract the payload in HTTP response from packets data captured through tshark in a .pcap file.</p><p>In the Wireshark GUI, I was able to do that by <code>File &gt; Extract Objects &gt; HTTP</code>, and then choosing a file from the HTTP Objects dialog (which shows a list of all HTTP objects), and saving it on my disk. This process is described <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChIOExportSection.html#ChIOExportObjectsDialog">here</a>.</p><p>The question is that how can I do it in Tshark?</p></div><div id="question-tags" class="tags-container tags">http.response http tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '16, 03:16</strong></p><img src="https://secure.gravatar.com/avatar/d2c205566b4047d6494161edbd1223c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jesss&#39;s gravatar image" /><p>Jesss<br />
<span class="score" title="51 reputation points">51</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jesss has no accepted answers">0%</span></p></div></div><div id="comments-container-54972" class="comments-container"></div><div id="comment-tools-54972" class="comment-tools"></div><div class="clear"></div><div id="comment-54972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57363"></span>

<div id="answer-container-57363" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57363-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In short, not implemented yet :(</p><p>EDIT: As of Wireshark 2.3.0, this feature <strong>is</strong> available. As of December 2016, Wireshark 2.3.0 hasn't been released yet, so you can grab a daily build from <a href="https://www.wireshark.org/download/automated/win32/">here</a>. To extract HTTP objects from the command-line, run the following command:</p><pre><code>tshark -r mypcap.pcap --export-objects &quot;http,destdir&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '16, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/8df259c952186aa93179732461b8d1e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moshe&#39;s gravatar image" /><p>moshe<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moshe has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Dec '16, 15:30</p></div></div><div id="comments-container-57363" class="comments-container"></div><div id="comment-tools-57363" class="comment-tools"></div><div class="clear"></div><div id="comment-57363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

