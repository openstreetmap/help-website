+++
type = "question"
title = "Dropbox LAN sync?"
description = '''Hello, I have never installed dropbox on my computer so why does wireshark show the following? 2279 813.777864000 192.168.1.4 255.255.255.255 DB-LSP-DISC 157 Dropbox LAN sync Discovery Protocol  im running windows 7 thanks'''
date = "2015-01-25T15:01:00Z"
lastmod = "2015-01-26T02:44:00Z"
weight = 39393
keywords = [ "dropbox", "lan", "sync" ]
aliases = [ "/questions/39393" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Dropbox LAN sync?](/questions/39393/dropbox-lan-sync)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39393-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have never installed dropbox on my computer so why does wireshark show the following?</p><pre><code>2279    813.777864000   192.168.1.4 255.255.255.255 DB-LSP-DISC 157 Dropbox LAN sync Discovery Protocol</code></pre><p>im running windows 7</p><p>thanks</p></div><div id="question-tags" class="tags-container tags">dropbox lan sync</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '15, 15:01</strong></p><img src="https://secure.gravatar.com/avatar/95e5894c1aa14b63cde12fa80eda2c0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shinbone&#39;s gravatar image" /><p>shinbone<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shinbone has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jan '15, 02:38</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-39393" class="comments-container"></div><div id="comment-tools-39393" class="comment-tools"></div><div class="clear"></div><div id="comment-39393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39397"></span>

<div id="answer-container-39397" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39397-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Another possibility is that something else happens to use the port (17500) that the Dropbox Lan Sync dissector registers for. There doesn't appear to be any validation in the dissector that the protocol is the expected one.<br />
</p><p>What did the protocol tree show for the packet in question? Can you post the capture somewhere public, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive or (oh the irony) Dropbox?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '15, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></p></div></div><div id="comments-container-39397" class="comments-container"></div><div id="comment-tools-39397" class="comment-tools"></div><div class="clear"></div><div id="comment-39397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39395"></span>

<div id="answer-container-39395" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39395-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Another system on your network (192.168.1.4) is probably using Dropbox. If that is your address, you should probably check if Dropbox was installed as an "add-on" for another piece of software.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '15, 17:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-39395" class="comments-container"><span id="39400"></span><div id="comment-39400" class="comment"><div id="post-39400-score" class="comment-score"></div><div class="comment-text"><p>I forgot my gf is using dropbox. anyway I didnt expect to see it on my pc as I thought wireshark only shows network connections on my own pc. thanks</p></div><div id="comment-39400-info" class="comment-info"><span class="comment-age">(26 Jan '15, 07:52)</span> shinbone</div></div><span id="39406"></span><div id="comment-39406" class="comment"><div id="post-39406-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-39406-info" class="comment-info"><span class="comment-age">(26 Jan '15, 10:50)</span> Jaap ♦</div></div></div><div id="comment-tools-39395" class="comment-tools"></div><div class="clear"></div><div id="comment-39395-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

