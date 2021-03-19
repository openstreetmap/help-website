+++
type = "question"
title = "Help with data element value in wireshark"
description = '''Consider the extract from a capture below Registrar Nonce  Data Element Type: Registrar Nonce (0x1039)  Data Element Length: 16  Registrar Nonce: 3aa9df80bb73ae86a2acb5724da5ad96  When I copy the Registrar Nonce value &quot;3aa9df80bb73ae86a2acb5724da5ad96&quot; and store it in a file in linux..the file size ...'''
date = "2015-03-28T14:53:00Z"
lastmod = "2015-03-28T15:56:00Z"
weight = 40962
keywords = [ "wireshark" ]
aliases = [ "/questions/40962" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Help with data element value in wireshark](/questions/40962/help-with-data-element-value-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40962-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Consider the extract from a capture below</p><pre><code>Registrar Nonce
 Data Element Type: Registrar Nonce (0x1039)
 Data Element Length: 16
 Registrar Nonce: 3aa9df80bb73ae86a2acb5724da5ad96</code></pre><p>When I copy the Registrar Nonce value "3aa9df80bb73ae86a2acb5724da5ad96" and store it in a file in linux..the file size reads 32 bytes instead of 16 bytes (according to the Data Element Length value)..? Which value is correct 16 bytes or 32 bytes?</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '15, 14:53</strong></p><img src="https://secure.gravatar.com/avatar/9b6feb2fd2e6a3f79bbcd81040063d5e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jay%20Dee&#39;s gravatar image" /><p>Jay Dee<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jay Dee has no accepted answers">0%</span></p></div></div><div id="comments-container-40962" class="comments-container"></div><div id="comment-tools-40962" class="comment-tools"></div><div class="clear"></div><div id="comment-40962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40968"></span>

<div id="answer-container-40968" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40968-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Each byte is represented by two hexadecimal characters. For example the most significant byte in your Nonce as the decimal value 58, which is 3a in hexadecimal. So the correct value is 16 bytes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '15, 15:56</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-40968" class="comments-container"><span id="40970"></span><div id="comment-40970" class="comment"><div id="post-40970-score" class="comment-score"></div><div class="comment-text"><p>thanks for explaining this..so the value "3aa9df80bb73ae86a2acb5724da5ad96" is equal to 32 bytes when stored in a file..is this because each character is considered a byte in the file?</p></div><div id="comment-40970-info" class="comment-info"><span class="comment-age">(28 Mar '15, 17:29)</span> Jay Dee</div></div><span id="40971"></span><div id="comment-40971" class="comment"><div id="post-40971-score" class="comment-score"></div><div class="comment-text"><p>It depends on the encoding used in the file, e.g. using UTF-8 as I think is common on Linux, each hex character is stored as 1 byte, but if using something such as UCS-2, as is common on Windows then there would be two bytes per character (plus a BOM at the front of the file).</p></div><div id="comment-40971-info" class="comment-info"><span class="comment-age">(28 Mar '15, 22:01)</span> grahamb ♦</div></div><span id="40977"></span><div id="comment-40977" class="comment"><div id="post-40977-score" class="comment-score"></div><div class="comment-text"><p>In the packet the binary element is 16 bytes, if yo copy the text representation which is 32 characters and paste it into a text file the length of the text file will be at least 32 bytes depending on how the binary representation of that text string is encoded in the text file.</p></div><div id="comment-40977-info" class="comment-info"><span class="comment-age">(29 Mar '15, 00:44)</span> Anders ♦</div></div><span id="40981"></span><div id="comment-40981" class="comment"><div id="post-40981-score" class="comment-score"></div><div class="comment-text"><p>thank You grahamb and Anders!!</p></div><div id="comment-40981-info" class="comment-info"><span class="comment-age">(29 Mar '15, 03:59)</span> Jay Dee</div></div></div><div id="comment-tools-40968" class="comment-tools"></div><div class="clear"></div><div id="comment-40968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

