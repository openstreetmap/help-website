+++
type = "question"
title = "How to decrypt SSL on OS X"
description = '''Hi,  I&#x27;m trying to learn how to monitor what&#x27;s going on on my home network (cellphones, computers). Up to now, I was able to capture data in monitor mode, and I managed to decrypt 802.11 packets with my wifi keys provided to Wireshark and the complete capture of the Eapol handshake. (I&#x27;m a beginner ...'''
date = "2015-11-30T17:05:00Z"
lastmod = "2015-12-05T10:51:00Z"
weight = 48112
keywords = [ "chrome", "ssl", "decryption", "https", "osx" ]
aliases = [ "/questions/48112" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to decrypt SSL on OS X](/questions/48112/how-to-decrypt-ssl-on-os-x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48112-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm trying to learn how to monitor what's going on on my home network (cellphones, computers). Up to now, I was able to capture data in monitor mode, and I managed to decrypt 802.11 packets with my wifi keys provided to Wireshark and the complete capture of the Eapol handshake. (I'm a beginner btw.) Next step, I want to be able to decrypt SSL, since I'm certainly far from having a complete picture of my network's traffic without this figured out. I'd like to be able to decrypt what's going on my computer, but on the other devices' too. I tried the technique with the SSLKEYLOGFILE variable linking, but can't seem to be able to make that happen. Here's exactly what I did, thanks for helping me understand what I'm doing wrong:<br />
</p><ul><li>I type the following command in my Terminal: export SSLKEYLOGFILE=/Users/heresmyusername/sslkeylogs/output.log</li><li>followed by: open -a "Google Chrome"</li><li>followed by: wireshark</li><li>then I open in Wireshark the capture file I want to decrypt</li><li>and in preferences --&gt; protocole --&gt; SSL: I type the following in the pre-master-secret field: Users/heresmyusername/sslkeylogs/output.log and apply this configuration</li><li>and major failure.....</li></ul><p>My guess is that I make a syntax mistake..?</p><p>Thanks for your help!!</p></div><div id="question-tags" class="tags-container tags">chrome ssl decryption https osx</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '15, 17:05</strong></p><img src="https://secure.gravatar.com/avatar/59c88a2a6b37bab5dfbb493f83198cca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="p1020175&#39;s gravatar image" /><p>p1020175<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="p1020175 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Dec '15, 09:59</p></div></div><div id="comments-container-48112" class="comments-container"></div><div id="comment-tools-48112" class="comment-tools"></div><div class="clear"></div><div id="comment-48112-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48292"></span>

<div id="answer-container-48292" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48292-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have no personal experience with OS X, but I'd expect that the path to the ssl key log file should be absolute even there. So unless you've omitted it only when creating the question, the initial / is missing in the pre-master secret field.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '15, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48292" class="comments-container"></div><div id="comment-tools-48292" class="comment-tools"></div><div class="clear"></div><div id="comment-48292-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

