+++
type = "question"
title = "I Can&#x27;t see any FTP traffic in WireShark log"
description = '''FTP server 10.10.1.4  |  |  |  HUB  | |   | |  FTP client Monitor PC 10.10.1.150 10.10.1.136 FTP client logon FTP server success , and download file from FTP server , i can&#x27;t see any traffic about FTP and  IP based 10.10.1.150 , i have no ideal why no traffic captured by wireshark , pls help me  '''
date = "2012-06-17T23:56:00Z"
lastmod = "2012-06-18T00:41:00Z"
weight = 12001
keywords = [ "ftp" ]
aliases = [ "/questions/12001" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [I Can't see any FTP traffic in WireShark log](/questions/12001/i-cant-see-any-ftp-traffic-in-wireshark-log)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12001-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>FTP server 10.10.1.4 | | | HUB | |<br />
| | FTP client Monitor PC 10.10.1.150 10.10.1.136</p><p>FTP client logon FTP server success , and download file from FTP server , i can't see any traffic about FTP and</p><p>IP based 10.10.1.150 , i have no ideal why no traffic captured by wireshark , pls help me<br />
</p></div><div id="question-tags" class="tags-container tags">ftp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '12, 23:56</strong></p><img src="https://secure.gravatar.com/avatar/6a04692430076d39add37aad9fcd9887?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="douchin&#39;s gravatar image" /><p>douchin<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="douchin has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-12001" class="comments-container"></div><div id="comment-tools-12001" class="comment-tools"></div><div class="clear"></div><div id="comment-12001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12002"></span>

<div id="answer-container-12002" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12002-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe your "Hub" is not a Hub but a switch. Do you read something like "switching Hub" on that device?</p><p>Did you check these:</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/Ethernet</code><br />
<code>http://wiki.wireshark.org/CaptureSetup/InterferingSoftware</code><br />
</p></blockquote><p>Just to eliminate problems with Wireshark itself: Do you see any FTP traffic, if you download something from the Wireshark PC itself?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '12, 00:41</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-12002" class="comments-container"><span id="12004"></span><div id="comment-12004" class="comment"><div id="post-12004-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much , Kurt , my hub is "Switching Hub" , after replacing it to "Hub" , i get FTP traffic . Thank you again</p></div><div id="comment-12004-info" class="comment-info"><span class="comment-age">(18 Jun '12, 01:32)</span> douchin</div></div><span id="12006"></span><div id="comment-12006" class="comment"><div id="post-12006-score" class="comment-score"></div><div class="comment-text"><p>I converted your answer to a comment. And you might want to accept Kurts answer using the checkmark icon next to it ;-)</p></div><div id="comment-12006-info" class="comment-info"><span class="comment-age">(18 Jun '12, 02:09)</span> Jasper ♦♦</div></div></div><div id="comment-tools-12002" class="comment-tools"></div><div class="clear"></div><div id="comment-12002-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

