+++
type = "question"
title = "Capture telnet username and password"
description = '''Hello, I am trying to get wireshark to capture my telnet session to a cisco switch. I have the capture but can&#x27;t seem to work out how to display the username and password as it is sent in clear text, where should I be looking? Thanks'''
date = "2010-09-17T03:17:00Z"
lastmod = "2012-03-29T12:26:00Z"
weight = 166
keywords = [ "telnet" ]
aliases = [ "/questions/166" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Capture telnet username and password](/questions/166/capture-telnet-username-and-password)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-166-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to get wireshark to capture my telnet session to a cisco switch. I have the capture but can't seem to work out how to display the username and password as it is sent in clear text, where should I be looking?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">telnet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '10, 03:17</strong></p><img src="https://secure.gravatar.com/avatar/1e995183e5891465732f36982ead7799?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gonzouk&#39;s gravatar image" /><p>Gonzouk<br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gonzouk has 2 accepted answers">100%</span></p></div></div><div id="comments-container-166" class="comments-container"></div><div id="comment-tools-166" class="comment-tools"></div><div class="clear"></div><div id="comment-166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="171"></span>

<div id="answer-container-171" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-171-score" class="post-score" title="current number of votes">-1</div></div></td><td><div class="item-right"><div class="answer-body"><p>OMG! that is amazing, thanks very much, shows everything.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '10, 05:11</strong></p><img src="https://secure.gravatar.com/avatar/1e995183e5891465732f36982ead7799?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gonzouk&#39;s gravatar image" /><p>Gonzouk<br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gonzouk has 2 accepted answers">100%</span></p></div></div><div id="comments-container-171" class="comments-container"><span id="173"></span><div id="comment-173" class="comment"><div id="post-173-score" class="comment-score">2</div><div class="comment-text"><p>The idea of the Q&amp;A site is to use the "accept" for the answer that actually does have the answer to the question. That way, people are able to find the answer quickly. You can use the "add new comment" to uhmm... add a comment like you put in your "answer" ;-)</p></div><div id="comment-173-info" class="comment-info"><span class="comment-age">(17 Sep '10, 05:22)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-171" class="comment-tools"></div><div class="clear"></div><div id="comment-171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="167"></span>

<div id="answer-container-167" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-167-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Telnet sends characters one by one, that's why you don't see the username/password straight away. But with "Follow TCP Stream", wireshark will put all data together and you will be able to see the username/password. Just rightclick on a packet of the telnet session and choose: "Follow TCP Stream".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '10, 03:49</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-167" class="comments-container"></div><div id="comment-tools-167" class="comment-tools"></div><div class="clear"></div><div id="comment-167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9845"></span>

<div id="answer-container-9845" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9845-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First You have to create a span Port.. i.e a port that get's all the frames passing through the switch.(if you exactly know how the switch work's you'll know what this mean's) and then install the analyzer onto that SPAN port and start sniffing.. you will get the user name and password.. Just follow the TCP Stream you'll get it.. Thanks</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '12, 12:26</strong></p><img src="https://secure.gravatar.com/avatar/785a9d6dec30b389e9ba54639b58dcb0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sibiraj&#39;s gravatar image" /><p>Sibiraj<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sibiraj has no accepted answers">0%</span></p></div></div><div id="comments-container-9845" class="comments-container"></div><div id="comment-tools-9845" class="comment-tools"></div><div class="clear"></div><div id="comment-9845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

