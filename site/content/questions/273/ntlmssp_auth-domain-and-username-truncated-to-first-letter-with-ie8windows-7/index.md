+++
type = "question"
title = "NTLMSSP_AUTH domain and username truncated to first letter with IE8/Windows 7"
description = '''Hi -  While debugging an issue with Windows 7/IE8 and NTLM authentication with our proxy server, noticed that wireshark (observed in versions 1.2.5 and 1.4.0) is truncating the domain name and username in NTLMSSP_AUTH messages to the first letter of each. So... instead of showing the full domain of ...'''
date = "2010-09-22T14:08:00Z"
lastmod = "2010-09-22T15:44:00Z"
weight = 273
keywords = [ "ie8", "windows7", "ntlm" ]
aliases = [ "/questions/273" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [NTLMSSP\_AUTH domain and username truncated to first letter with IE8/Windows 7](/questions/273/ntlmssp_auth-domain-and-username-truncated-to-first-letter-with-ie8windows-7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-273-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi -</p><p>While debugging an issue with Windows 7/IE8 and NTLM authentication with our proxy server, noticed that wireshark (observed in versions 1.2.5 and 1.4.0) is truncating the domain name and username in NTLMSSP_AUTH messages to the first letter of each. So... instead of showing the full domain of MYDOMAIN it lists only "M" and instead of showing the full username USERID, it only lists "U".</p><p>This is specific to the NTLMSSP_AUTH (NTLM message type 3) message.</p><p>That lead us down the WRONG path troubleshooting-wise... Can you please fix?</p></div><div id="question-tags" class="tags-container tags">ie8 windows7 ntlm</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '10, 14:08</strong></p><img src="https://secure.gravatar.com/avatar/b1a12a51e1e6bb7e533ba92e43e913ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Denee&#39;s gravatar image" /><p>Denee<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Denee has no accepted answers">0%</span></p></div></div><div id="comments-container-273" class="comments-container"></div><div id="comment-tools-273" class="comment-tools"></div><div class="clear"></div><div id="comment-273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="279"></span>

<div id="answer-container-279" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-279-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Would you be so kind to add a bug report at https://bugs.wireshark.org ? It would really help us fix this problem if you also attach a tracefile there that shows this behavior.</p><p>(this site is a more like a knowledge base)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '10, 15:44</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-279" class="comments-container"></div><div id="comment-tools-279" class="comment-tools"></div><div class="clear"></div><div id="comment-279-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

