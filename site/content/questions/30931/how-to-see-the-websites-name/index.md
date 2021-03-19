+++
type = "question"
title = "How to see the website&#x27;s name?"
description = '''How can I know the name of the websites being surfed through my network using wireshark?'''
date = "2014-03-18T07:06:00Z"
lastmod = "2014-03-20T10:36:00Z"
weight = 30931
keywords = [ "websites" ]
aliases = [ "/questions/30931" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to see the website's name?](/questions/30931/how-to-see-the-websites-name)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30931-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I know the name of the websites being surfed through my network using wireshark?</p></div><div id="question-tags" class="tags-container tags">websites</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Mar '14, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/6e9e3fa1243a0402df6702d2e7c02e0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Coolboy&#39;s gravatar image" /><p>Coolboy<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Coolboy has no accepted answers">0%</span></p></div></div><div id="comments-container-30931" class="comments-container"><span id="30933"></span><div id="comment-30933" class="comment"><div id="post-30933-score" class="comment-score"></div><div class="comment-text"><p>What do you know with "name" ? Do you mean title tags or do you mean hostnames?</p></div><div id="comment-30933-info" class="comment-info"><span class="comment-age">(18 Mar '14, 11:45)</span> CipherSpec</div></div></div><div id="comment-tools-30931" class="comment-tools"></div><div class="clear"></div><div id="comment-30931-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31002"></span>

<div id="answer-container-31002" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31002-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As most Web sites these days use https protocol and the HTTP traffic is encrypted this http.post filter will not be of help in this environment. I would suggest you trace (at least) all DNS responses along with all SYN packets from clients. The filter would look something like this (udp.srcport eq 53 or tcp[13] eq 2).</p><p>This way you can resolve the destination addresses of the servers using the DNS responses you have in the trace. (You need to enable Edit-Preferences-Name Resolution-Network (ip) addresses)<br />
</p><p>You can then filter on all client SYN requests to see where they connect to... <img src="https://osqa-ask.wireshark.org/upfiles/dns_syn.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '14, 10:36</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div></div><div id="comments-container-31002" class="comments-container"></div><div id="comment-tools-31002" class="comment-tools"></div><div class="clear"></div><div id="comment-31002-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30952"></span>

<div id="answer-container-30952" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30952-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use http.host as a display filter or even better create a column for it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '14, 06:58</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-30952" class="comments-container"><span id="30959"></span><div id="comment-30959" class="comment"><div id="post-30959-score" class="comment-score"></div><div class="comment-text"><p>How can I create a display filter or create a column for it?</p></div><div id="comment-30959-info" class="comment-info"><span class="comment-age">(19 Mar '14, 09:08)</span> Coolboy</div></div><span id="30971"></span><div id="comment-30971" class="comment"><div id="post-30971-score" class="comment-score"></div><div class="comment-text"><p>Just type in the filter field http.host and Apply. In the packet details expand Hypertext Transfer Protocol, right click on Host and Apply as a column.</p><p>Or go to Edit - Preferences - User Interface - Columns and add a Custom column with the Field Name http.host</p></div><div id="comment-30971-info" class="comment-info"><span class="comment-age">(19 Mar '14, 13:22)</span> Roland</div></div></div><div id="comment-tools-30952" class="comment-tools"></div><div class="clear"></div><div id="comment-30952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

