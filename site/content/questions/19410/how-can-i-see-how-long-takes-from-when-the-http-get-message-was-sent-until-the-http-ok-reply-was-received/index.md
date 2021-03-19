+++
type = "question"
title = "How can I see how long takes from when the HTTP GET message was sent until the HTTP OK  reply was received"
description = '''Thank you for your help'''
date = "2013-03-12T20:50:00Z"
lastmod = "2013-03-21T06:23:00Z"
weight = 19410
keywords = [ "capture", "http", "packet" ]
aliases = [ "/questions/19410" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How can I see how long takes from when the HTTP GET message was sent until the HTTP OK reply was received](/questions/19410/how-can-i-see-how-long-takes-from-when-the-http-get-message-was-sent-until-the-http-ok-reply-was-received)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19410-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Thank you for your help</p></div><div id="question-tags" class="tags-container tags">capture http packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '13, 20:50</strong></p><img src="https://secure.gravatar.com/avatar/728a19ed04290cbdb9cec210b71fb1bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feierqi&#39;s gravatar image" /><p>feierqi<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feierqi has no accepted answers">0%</span></p></div></div><div id="comments-container-19410" class="comments-container"></div><div id="comment-tools-19410" class="comment-tools"></div><div class="clear"></div><div id="comment-19410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="19412"></span>

<div id="answer-container-19412" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19412-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Set your time display format to "Seconds Since Beginning of Capture." (View &gt; Time Display Format &gt; Seconds Since Beginning of Capture.) In the Packet List pane, right-click on the packet with the GET request, and select "Set Time Reference." You will see "*REF*" in the Time column.</p><p>Now select the packet with the reply. The value in the Time column is the elapsed time between those two packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '13, 21:32</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-19412" class="comments-container"></div><div id="comment-tools-19412" class="comment-tools"></div><div class="clear"></div><div id="comment-19412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19451"></span>

<div id="answer-container-19451" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19451-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Or use the latest development version of Wireshark (a buildbot build or the recently-released 1.9.1): with that Wireshark will calculate these things for you (thanks to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8287">bug 8287</a>).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '13, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-19451" class="comments-container"></div><div id="comment-tools-19451" class="comment-tools"></div><div class="clear"></div><div id="comment-19451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19705"></span>

<div id="answer-container-19705" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19705-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hey, Use Jmeter.. Its a good tool for any HTTP XML/JSON testes.. Automation is easy once you learn it</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '13, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/2fd4419ad615504ce0ad00bcbc0a0cd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kaasi&#39;s gravatar image" /><p>Kaasi<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kaasi has no accepted answers">0%</span></p></div></div><div id="comments-container-19705" class="comments-container"></div><div id="comment-tools-19705" class="comment-tools"></div><div class="clear"></div><div id="comment-19705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

