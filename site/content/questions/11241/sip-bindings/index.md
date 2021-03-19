+++
type = "question"
title = "SIP - Bindings"
description = '''What does bindings means in SIP. And what does 1 bindings and 0 bindings refers?'''
date = "2012-05-22T23:02:00Z"
lastmod = "2012-05-23T00:01:00Z"
weight = 11241
keywords = [ "sip_bindings" ]
aliases = [ "/questions/11241" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SIP - Bindings](/questions/11241/sip-bindings)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11241-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What does bindings means in SIP. And what does 1 bindings and 0 bindings refers?</p></div><div id="question-tags" class="tags-container tags">sip_bindings</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '12, 23:02</strong></p><img src="https://secure.gravatar.com/avatar/d819222181814e56dd75394a644cf2ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="devrajk&#39;s gravatar image" /><p>devrajk<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="devrajk has no accepted answers">0%</span></p></div></div><div id="comments-container-11241" class="comments-container"></div><div id="comment-tools-11241" class="comment-tools"></div><div class="clear"></div><div id="comment-11241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11244"></span>

<div id="answer-container-11244" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11244-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>from RFC 3261</p><blockquote><p>The REGISTER messages <strong>associate Bob's SIP or SIPS URI</strong> (sip:[email protected]<a href="http://biloxi.com">biloxi.com</a>) <strong>with the machine</strong> into which he is <strong>currently logged</strong> (conveyed as a SIP or SIPS URI in the Contact header field). The registrar writes this association, <strong>also called a binding</strong>, to a database, called the location service,</p></blockquote><p>Basically bindings are a link between the contact information (SIP URI or tel. number) and the IP address (or FQDN) of the VoIP device. There can be multiple bindings, if there are several contact details (e.g. tel. numbers) and/or multiple VoIP devices (for the same contact information).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '12, 00:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 May '12, 10:10</p></div></div><div id="comments-container-11244" class="comments-container"></div><div id="comment-tools-11244" class="comment-tools"></div><div class="clear"></div><div id="comment-11244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

