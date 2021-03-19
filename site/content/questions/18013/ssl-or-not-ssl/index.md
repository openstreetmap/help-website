+++
type = "question"
title = "SSL or not SSL"
description = '''We have built a WCF Self-Hosted application that has a SSL cert attached to port 15014. All of that works like it should but it seems that i want to make sure i truly see the SSL handshake so I captured soem packets and what worries me is that it only hsows TCP and no SSLv?. IF i am trying to go to ...'''
date = "2013-01-28T12:26:00Z"
lastmod = "2013-01-28T12:44:00Z"
weight = 18013
keywords = [ "ssl" ]
aliases = [ "/questions/18013" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL or not SSL](/questions/18013/ssl-or-not-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18013-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have built a WCF Self-Hosted application that has a SSL cert attached to port 15014. All of that works like it should but it seems that i want to make sure i truly see the SSL handshake so I captured soem packets and what worries me is that it only hsows TCP and no SSLv?. IF i am trying to go to <a href="https://servername:15014">https://servername:15014</a> and should it not show some sort of SSL functionality in wireshark and not just TCP? Thanks</p></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jan '13, 12:26</strong></p><img src="https://secure.gravatar.com/avatar/c64d13d2389254d0a488bb0febe12d7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cptkirkh&#39;s gravatar image" /><p>cptkirkh<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cptkirkh has no accepted answers">0%</span></p></div></div><div id="comments-container-18013" class="comments-container"></div><div id="comment-tools-18013" class="comment-tools"></div><div class="clear"></div><div id="comment-18013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18014"></span>

<div id="answer-container-18014" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18014-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since you are running SSL on a non-standard SSL port, Wireshark does not know that it should interpret the packets as SSL. You can use "Decode As..." (rightclick on a packet) to tell Wireshark to interpret port 15014 as SSL.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '13, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-18014" class="comments-container"><span id="18017"></span><div id="comment-18017" class="comment"><div id="post-18017-score" class="comment-score"></div><div class="comment-text"><p>yes but why can i see inside the packet to the data being transmitted if i don't have the private key installed in Wireshark for decryption? Is this really secure if i can read the commands he is sending in plain text?</p></div><div id="comment-18017-info" class="comment-info"><span class="comment-age">(28 Jan '13, 14:06)</span> cptkirkh</div></div><span id="18018"></span><div id="comment-18018" class="comment"><div id="post-18018-score" class="comment-score"></div><div class="comment-text"><p>Which data do you see unencrypted? The certificate is being sent before encryption starts. Do you see other data unencrypted? Are you able to post an example to www.cloudshark.org?</p></div><div id="comment-18018-info" class="comment-info"><span class="comment-age">(28 Jan '13, 16:00)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-18014" class="comment-tools"></div><div class="clear"></div><div id="comment-18014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

