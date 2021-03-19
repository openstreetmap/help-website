+++
type = "question"
title = "how to confirm encrypted data using WIRESHARK ?"
description = '''I am new to WIRESHARK have installed it. WIRESHARK provide many useful features but in start I want to just capture my required data. Can you please guide me how I can capture data relevant to a particular web site ? I want to confirm my user id and password are encrypted.  I highly appreciate your ...'''
date = "2012-10-08T17:23:00Z"
lastmod = "2012-10-08T19:13:00Z"
weight = 14802
keywords = [ "wireshark" ]
aliases = [ "/questions/14802" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [how to confirm encrypted data using WIRESHARK ?](/questions/14802/how-to-confirm-encrypted-data-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14802-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to WIRESHARK have installed it.</p><p>WIRESHARK provide many useful features but in start I want to just capture my required data. Can you please guide me how I can capture data relevant to a particular web site ? I want to confirm my user id and password are encrypted.</p><p>I highly appreciate your guidance on it.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '12, 17:23</strong></p><img src="https://secure.gravatar.com/avatar/422c603dd3b7d854936ed415e7c0ae94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Haansi&#39;s gravatar image" /><p>Haansi<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Haansi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Oct '12, 05:44</p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-14802" class="comments-container"></div><div id="comment-tools-14802" class="comment-tools"></div><div class="clear"></div><div id="comment-14802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14803"></span>

<div id="answer-container-14803" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14803-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>1) have the browser ready to go but don't hit ENTER after typing in the URL.</p><p>2) Open Wireshark.<br />
</p><p>3) Hit CTRL-K and pick the interface (use the IP address under the interface name to choose the correct one).</p><p>4) Click on START.</p><p>5) Switch to your browser, and hit ENTER.</p><p>6) After typing in the username/password, switch back to Wireshark.</p><p>7) Stop the Capture.</p><p>8) In wireshark, got to Statistics, Conversations, TCP. Find your web traffic.</p><p>9) Right click on the conversation, Apply as filter, Selected, A &lt;-&gt; B</p><p>10)Rick click on any part of the packet, and use Follow TCP Stream option.</p><p>You will see the data displayed as text. Save it and see if you can find your username.</p><p>You can do all of the above using other (quicker) ways, but based your question and lack of experience with Wireshark, I wanted to provide a step by step method. Good luck</p><p>hsb</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '12, 19:13</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Oct '12, 19:14</p></div></div><div id="comments-container-14803" class="comments-container"><span id="14804"></span><div id="comment-14804" class="comment"><div id="post-14804-score" class="comment-score"></div><div class="comment-text"><p>Also, after you capture the traffic, you can type in the following into the FILTER bar: http contains "YourUserName"</p></div><div id="comment-14804-info" class="comment-info"><span class="comment-age">(08 Oct '12, 19:17)</span> hansangb</div></div></div><div id="comment-tools-14803" class="comment-tools"></div><div class="clear"></div><div id="comment-14803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

