+++
type = "question"
title = "Can not filter SSL traffic."
description = '''Hi.  I&#x27;ve started a simple client/server application using SSL. Both, client and service, were built using Java. The SSL functionality was provided by JSSE, and the server is listening on port number 7070.   Despite of existence of a SSL filter, I can not view any SSL traffic when I use it. I am sur...'''
date = "2011-09-12T13:51:00Z"
lastmod = "2011-09-12T14:17:00Z"
weight = 6296
keywords = [ "ssl" ]
aliases = [ "/questions/6296" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can not filter SSL traffic.](/questions/6296/can-not-filter-ssl-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6296-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I've started a simple client/server application using SSL. Both, client and service, were built using Java. The SSL functionality was provided by JSSE, and the server is listening on port number 7070. Despite of existence of a SSL filter, I can not view any SSL traffic when I use it. I am sure there is no errors on applications. Everything I can see is the certificates being sent over the network, but just when I use a TCP filter on stream.<br />
Any explanation?</p></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '11, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/f9f4feeb18f4ac637adcc5afafe84cd3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hwsilva&#39;s gravatar image" /><p>hwsilva<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hwsilva has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-6296" class="comments-container"></div><div id="comment-tools-6296" class="comment-tools"></div><div class="clear"></div><div id="comment-6296-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6297"></span>

<div id="answer-container-6297" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6297-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since you are running SSL on a non-standard port, you will have to tell Wireshark that traffic on port 7070 should be dissected as SSL. You can do this with "Analyze -&gt; Decode as..." (also available in the right-click menus).</p><p>In "Decode As...", choose port 7070 and select SSL as the protocol to use for that port and click on OK.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '11, 14:17</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6297" class="comments-container"></div><div id="comment-tools-6297" class="comment-tools"></div><div class="clear"></div><div id="comment-6297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

