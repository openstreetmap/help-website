+++
type = "question"
title = "Intercept communication to certain websites"
description = '''Hi, there! I am quite curious about WireShark, and as an experiment, I have programmed a simple application which contacts a specific website, and outputs the contents of that website. My goal is to see if it is possible to use wireshark to:  Detect that my app (or any app at all, no need for specif...'''
date = "2012-06-09T23:11:00Z"
lastmod = "2012-06-10T00:31:00Z"
weight = 11791
keywords = [ "intercept", "http", "wireshark" ]
aliases = [ "/questions/11791" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Intercept communication to certain websites](/questions/11791/intercept-communication-to-certain-websites)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11791-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, there! I am quite curious about WireShark, and as an experiment, I have programmed a simple application which contacts a specific website, and outputs the contents of that website.</p><p>My goal is to see if it is possible to use wireshark to:</p><ol><li>Detect that my app (or any app at all, no need for specificity, only my app will visit this page) is contacting the specific webpage</li><li>Stop the connection</li><li>Send back false data, making my app think that the website returned something that it didn't</li></ol><p>Is this possible at all, and if so, how might I do it?</p><p>Thankyou! :)</p><p>P.S. for clarity, yes, I am looking to specifically intercept and falsify HTTP data transfer to and from a very specific URI on a very specific URL.</p></div><div id="question-tags" class="tags-container tags">intercept http wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '12, 23:11</strong></p><img src="https://secure.gravatar.com/avatar/8f8db8b8e412fc9f724623163227ff1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Flynn&#39;s gravatar image" /><p>Flynn<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Flynn has no accepted answers">0%</span></p></div></div><div id="comments-container-11791" class="comments-container"></div><div id="comment-tools-11791" class="comment-tools"></div><div class="clear"></div><div id="comment-11791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11794"></span>

<div id="answer-container-11794" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11794-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>P.S. for clarity, yes, I am looking to specifically <strong>intercept and falsify HTTP data</strong> transfer to and from a very specific URI on a very specific URL.</p></blockquote><p>Wireshark is a <strong>passive monitoring tool</strong>. It can only read (and analyze) data from the network. There is no option to send data. So, there is no way to do what you want (changing data on the fly).</p><p>A transparent proxy can do that. Please google it.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '12, 00:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jun '12, 00:43</p></div></div><div id="comments-container-11794" class="comments-container"></div><div id="comment-tools-11794" class="comment-tools"></div><div class="clear"></div><div id="comment-11794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

