+++
type = "question"
title = "retransmissions issue"
description = '''https://www.cloudshark.org/captures/14bcc5d9a146 In the above link, i have a capture of a client access a server, and i am seeing retransmissions. I check the network and the port that the user is connected to, but there are no errors on the port or the network to the server, but the pattern of the ...'''
date = "2013-08-21T20:42:00Z"
lastmod = "2013-08-21T21:53:00Z"
weight = 23936
keywords = [ "cliret_issues" ]
aliases = [ "/questions/23936" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [retransmissions issue](/questions/23936/retransmissions-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23936-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><a href="https://www.cloudshark.org/captures/14bcc5d9a146">https://www.cloudshark.org/captures/14bcc5d9a146</a></p><p>In the above link, i have a capture of a client access a server, and i am seeing retransmissions. I check the network and the port that the user is connected to, but there are no errors on the port or the network to the server, but the pattern of the retransmission all begin up at a file that the client cannot find, so it retransmit for the file, needless to say, the user connection to the email server is slow and access to other server are slow. Can one or you very smart people look at the trace and give me some advice, I have tried everything I know to figure this out, trying to give the and answer Thanks in advance blessing</p><p>P.S the trace was taken on th client computer if that helps. there are some zero windows, I am sure that plays a part in it also.</p></div><div id="question-tags" class="tags-container tags">cliret_issues</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '13, 20:42</strong></p><img src="https://secure.gravatar.com/avatar/530b55f3fcb17b760aabdf113d9318aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ejohnson7&#39;s gravatar image" /><p>ejohnson7<br />
<span class="score" title="11 reputation points">11</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ejohnson7 has no accepted answers">0%</span></p></div></div><div id="comments-container-23936" class="comments-container"></div><div id="comment-tools-23936" class="comment-tools"></div><div class="clear"></div><div id="comment-23936-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23938"></span>

<div id="answer-container-23938" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23938-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>This trace contains duplicate packets. You need to remove those to get rid of the false alarms.</p><pre><code>editcap -d wireshark-plugin-s3pc.2.cap s3pc.nodups.cap
13797 packets seen, 3674 packets skipped with duplicate window of 5 packets.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '13, 21:53</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-23938" class="comments-container"><span id="23963"></span><div id="comment-23963" class="comment"><div id="post-23963-score" class="comment-score"></div><div class="comment-text"><p>This trace contains duplicate packets how do i get rid of the false alarms?</p></div><div id="comment-23963-info" class="comment-info"><span class="comment-age">(22 Aug '13, 07:26)</span> ejohnson7</div></div><span id="23965"></span><div id="comment-23965" class="comment"><div id="post-23965-score" class="comment-score"></div><div class="comment-text"><p>editcap -d wireshark-plugin-s3pc.2.cap s3pc.nodups.cap</p></div><div id="comment-23965-info" class="comment-info"><span class="comment-age">(22 Aug '13, 08:10)</span> mrEEde</div></div><span id="23968"></span><div id="comment-23968" class="comment"><div id="post-23968-score" class="comment-score"></div><div class="comment-text"><p>where is this added to the Wireshark Dir</p></div><div id="comment-23968-info" class="comment-info"><span class="comment-age">(22 Aug '13, 14:39)</span> ejohnson7</div></div><span id="23973"></span><div id="comment-23973" class="comment"><div id="post-23973-score" class="comment-score"></div><div class="comment-text"><p>See Help -&gt; About Wireshark -&gt; Folders -&gt; Program</p><p>If you are running Windows you should add this directory to the PATH Environment Variable</p></div><div id="comment-23973-info" class="comment-info"><span class="comment-age">(23 Aug '13, 03:53)</span> mrEEde</div></div></div><div id="comment-tools-23938" class="comment-tools"></div><div class="clear"></div><div id="comment-23938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

