+++
type = "question"
title = "how to capture tcp stream from ip address,,,"
description = '''well i am using wireshark to test security of my project in local host ,,,so i can check it through my ip address ,,,but problem is there is no relevant findings like tcp streams ,,,so that i may check my login pages and signup pages security like if they eay to track ,,,,,what should i do to see my...'''
date = "2015-04-16T07:12:00Z"
lastmod = "2015-04-16T11:59:00Z"
weight = 41488
keywords = [ "ip", "localhost", "tcp" ]
aliases = [ "/questions/41488" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to capture tcp stream from ip address,,,](/questions/41488/how-to-capture-tcp-stream-from-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41488-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>well i am using wireshark to test security of my project in local host ,,,so i can check it through my ip address ,,,but problem is there is no relevant findings like tcp streams ,,,so that i may check my login pages and signup pages security like if they eay to track ,,,,,what should i do to see my password and username in plain text with out security in wireshark.</p></div><div id="question-tags" class="tags-container tags">ip localhost tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '15, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/60b30263659e0d109c15212ea242f96b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rohit%20palampur&#39;s gravatar image" /><p>rohit palampur<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rohit palampur has no accepted answers">0%</span></p></div></div><div id="comments-container-41488" class="comments-container"><span id="41491"></span><div id="comment-41491" class="comment"><div id="post-41491-score" class="comment-score"></div><div class="comment-text"><p>What is your OS and which version and what is your Wireshark version?</p><p>Your question isn't very clear to me, can you rephrase it?</p></div><div id="comment-41491-info" class="comment-info"><span class="comment-age">(16 Apr '15, 11:04)</span> grahamb ♦</div></div></div><div id="comment-tools-41488" class="comment-tools"></div><div class="clear"></div><div id="comment-41488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41494"></span>

<div id="answer-container-41494" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41494-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>well i am using wireshark to test security of my project in <strong>local host</strong> ,,,</p></blockquote><p>If you are trying to capture localhost traffic on Windows, then you won't see anything in Wireshark, because WinPcap (the capturing subsystem on Windows) is unable to capture localhost traffic.</p><blockquote><p>what should i do to see my password and username in plain text with out security in wireshark.</p></blockquote><p>Either run two distinct systems. One client and one server, then try to capture traffic between then, which should work with much problems.</p><p>If you need to run everything on localhost, you'll need a different sniffer!</p><p>Please check the answers to the following question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/11992/can-wireshark-capture-traffic-between-a-browser-and-jboss-both-running-on-localhost">https://ask.wireshark.org/questions/11992/can-wireshark-capture-traffic-between-a-browser-and-jboss-both-running-on-localhost</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '15, 11:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-41494" class="comments-container"><span id="41524"></span><div id="comment-41524" class="comment"><div id="post-41524-score" class="comment-score"></div><div class="comment-text"><p>thanks mr. kurt knochner,i will follow ur advice,currently working on a php project and using mysql server,just wanted to catch the traffic of my login pages if it is secure and encrypted well or not ,,just new at it</p></div><div id="comment-41524-info" class="comment-info"><span class="comment-age">(17 Apr '15, 01:40)</span> rohit palampur</div></div></div><div id="comment-tools-41494" class="comment-tools"></div><div class="clear"></div><div id="comment-41494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

