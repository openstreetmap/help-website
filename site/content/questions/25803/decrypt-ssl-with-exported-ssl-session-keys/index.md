+++
type = "question"
title = "Decrypt SSL with exported SSL Session Keys"
description = '''Hi all, I am new to Wireshark, I run v1.6.7 on Ubuntu Desktop. I can decrypt HTTPS Traffic with my private key, works fine. I can see decrypted traffic as http. In order to send the capture to a vendor, I export the SSL Session Keys to file. Before sending the Session Keys and capture to the 3rd par...'''
date = "2013-10-09T05:13:00Z"
lastmod = "2013-10-09T13:43:00Z"
weight = 25803
keywords = [ "ssl", "master-key", "decryption" ]
aliases = [ "/questions/25803" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Decrypt SSL with exported SSL Session Keys](/questions/25803/decrypt-ssl-with-exported-ssl-session-keys)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25803-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am new to Wireshark, I run v1.6.7 on Ubuntu Desktop. I can decrypt HTTPS Traffic with my private key, works fine. I can see decrypted traffic as http.</p><p>In order to send the capture to a vendor, I export the SSL Session Keys to file. Before sending the Session Keys and capture to the 3rd party, I want to test the decryption with the exported SessionKeys. I create a new profile, protocols and for (Pre)-master-secret log file name I put the path of the SSL Session Keys. However, if I click on apply, nothing happens. The SSL debug log file is empty.</p><p>What do I miss ?</p><p>Thanks in advance for your answers.</p></div><div id="question-tags" class="tags-container tags">ssl master-key decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '13, 05:13</strong></p><img src="https://secure.gravatar.com/avatar/327e6ad928ce4a003114019c57ffccab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dragisa&#39;s gravatar image" /><p>Dragisa<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dragisa has no accepted answers">0%</span></p></div></div><div id="comments-container-25803" class="comments-container"></div><div id="comment-tools-25803" class="comment-tools"></div><div class="clear"></div><div id="comment-25803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25847"></span>

<div id="answer-container-25847" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25847-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Were there any keys saved in the file to which you exported the SSL Session Keys? Do the Session-ID's match the ones seen in the trace file?</p><p>The SSL debug file should at least list that it sees SSL traffic. Do you see SSL in the packet list? Are you running SSL on a non-standard port? If so, please add the port to the HTTP settings.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '13, 13:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-25847" class="comments-container"><span id="25861"></span><div id="comment-25861" class="comment"><div id="post-25861-score" class="comment-score"></div><div class="comment-text"><p>Hi SYN-bit,</p><p>Thanks for your answer. I got it now...In the HTTP settings I fogot to add the non-standard port as SSL/TLS port. After this it worked.</p><p>Thanks!</p></div><div id="comment-25861-info" class="comment-info"><span class="comment-age">(10 Oct '13, 02:35)</span> Dragisa</div></div><span id="25862"></span><div id="comment-25862" class="comment"><div id="post-25862-score" class="comment-score"></div><div class="comment-text"><p>@Dragisa, if an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-25862-info" class="comment-info"><span class="comment-age">(10 Oct '13, 02:54)</span> grahamb ♦</div></div></div><div id="comment-tools-25847" class="comment-tools"></div><div class="clear"></div><div id="comment-25847-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

