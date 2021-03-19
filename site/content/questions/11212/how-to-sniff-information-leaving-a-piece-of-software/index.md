+++
type = "question"
title = "How to sniff information leaving a piece of software."
description = '''I need to streamline a process for a client. Currently he has a bit of software which extracts products from a supplier website which he then manually imports into his website to sell. Once the sale of the product is done on the client&#x27;s site though, he needs to update the software which then update...'''
date = "2012-05-22T06:26:00Z"
lastmod = "2012-05-22T07:57:00Z"
weight = 11212
keywords = [ "sniffing" ]
aliases = [ "/questions/11212" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to sniff information leaving a piece of software.](/questions/11212/how-to-sniff-information-leaving-a-piece-of-software)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11212-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to streamline a process for a client. Currently he has a bit of software which extracts products from a supplier website which he then manually imports into his website to sell. Once the sale of the product is done on the client's site though, he needs to update the software which then updates the supplier website. Very clunky. There is also no API in this software to integrate more seamlessly.</p><p>I need to figure out how to "sniff" the information sent out from this application to supplier site in order to replicate the process, thereby bypassing the software in order for it to be more seamless.</p><p>I've been told that Wireshark might be able to help with this but it is not for novices. Is there someone who can help with this?</p><p>Many thanks</p></div><div id="question-tags" class="tags-container tags">sniffing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '12, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/d18266484dd68e0e729ebc2bce79249b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sixfootjames&#39;s gravatar image" /><p>sixfootjames<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sixfootjames has no accepted answers">0%</span></p></div></div><div id="comments-container-11212" class="comments-container"></div><div id="comment-tools-11212" class="comment-tools"></div><div class="clear"></div><div id="comment-11212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11216"></span>

<div id="answer-container-11216" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11216-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Install Wireshark on the system that does the supplier web site update (I think it should be O.K. to do it this way for your purpose). Then start Wireshark with this capture filter</p><blockquote><p><code>Capture -&gt; Options -&gt; Capture Filter</code><br />
<code>host x.x.x.x</code></p></blockquote><p>where x.x.x.x is the ip address of the supplier web site. Then let the software perform the update. Stop the capture process in Wireshark (Capture -&gt; Stop) and analyze the HTTP communication between the two hosts. It's best to start with this display filter</p><blockquote><p><code>http.request</code><br />
</p></blockquote><p>This will show only HTTP Requests (GET / POST). Select the first displayed line and right-click it. Then select "Follow TCP Stream". That will give you the whole communication in clear text. Within that you will find the client request and the servers answer. You should be able to use that information to biuld your own update client. Repeat that step with the next line, until you find the required information.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '12, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 May '12, 08:02</p></div></div><div id="comments-container-11216" class="comments-container"></div><div id="comment-tools-11216" class="comment-tools"></div><div class="clear"></div><div id="comment-11216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

