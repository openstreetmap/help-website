+++
type = "question"
title = "Save TFTP transferred file from capture"
description = '''I have monitored a TFTP session of a file being transfered. Is there any way to extract the file from the capture?'''
date = "2012-09-19T05:05:00Z"
lastmod = "2012-09-19T15:29:00Z"
weight = 14375
keywords = [ "capture", "tftp", "save", "file" ]
aliases = [ "/questions/14375" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Save TFTP transferred file from capture](/questions/14375/save-tftp-transferred-file-from-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14375-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have monitored a TFTP session of a file being transfered. Is there any way to extract the file from the capture?</p></div><div id="question-tags" class="tags-container tags">capture tftp save file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '12, 05:05</strong></p><img src="https://secure.gravatar.com/avatar/8c558c2a2390a75fbbbc4272d0ad8ada?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vlad&#39;s gravatar image" /><p>Vlad<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vlad has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Sep '12, 10:07</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-14375" class="comments-container"><span id="33482"></span><div id="comment-33482" class="comment"><div id="post-33482-score" class="comment-score">1</div><div class="comment-text"><p>The current development version of Wireshark (post 1.12) now does let you export files transferred over TFTP. See 'File | Export Objects | TFTP'. I'm thinking that a lot of the time you would really only use this to check which version of a file was transferred, so being able to see the length, and possibly also an MD5 digest of the whole file would be almost as useful as recovering the whole file.</p></div><div id="comment-33482-info" class="comment-info"><span class="comment-age">(05 Jun '14, 15:31)</span> MartinM</div></div></div><div id="comment-tools-14375" class="comment-tools"></div><div class="clear"></div><div id="comment-14375-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14389"></span>

<div id="answer-container-14389" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14389-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>you can do it as follows:</p><ul><li>use this display filter: <strong><code>tftp</code></strong></li><li>then select the first data packet. You will see the following text in the info column: <strong><code>Data Packet, Block: 1</code></strong></li><li>right click on that packet and select: <strong>Follow UDP Stream</strong></li><li>in the pop-up window select the conversation with the file. Use the drop down menu above the button labeled "Find". The data conversation should be colored blue.</li><li>then save that content in <strong>raw</strong> format (radio button) with "save as"</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '12, 15:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-14389" class="comments-container"><span id="14390"></span><div id="comment-14390" class="comment"><div id="post-14390-score" class="comment-score">1</div><div class="comment-text"><p>Hi. Thanks for the tip. It might work for a regular txt file but it doesn't for an *.gz file. Any idea why?</p></div><div id="comment-14390-info" class="comment-info"><span class="comment-age">(20 Sep '12, 00:28)</span> Vlad</div></div><span id="14401"></span><div id="comment-14401" class="comment"><div id="post-14401-score" class="comment-score">1</div><div class="comment-text"><p>Actually, this doesn't work for any file because "<strong>Follow UDP Stream</strong>" will include the entire UDP payload including the TFTP header, which you don't want. The closest you can get with Wireshark today (that I know of) would be to use Kurt's method to save the data side of the conversation, and then use an external tool/method to find/remove the TFTP header bytes from it. But even that won't work in all cases, such as if there is packet loss, retries, etc.</p><p>I would recommend filing an enhancement bug request to add a TFTP reassembly feature to Wireshark.</p></div><div id="comment-14401-info" class="comment-info"><span class="comment-age">(20 Sep '12, 09:49)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-14389" class="comment-tools"></div><div class="clear"></div><div id="comment-14389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

