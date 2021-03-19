+++
type = "question"
title = "List of protocol codes"
description = '''hello guys. as you know, we can filter traffic for specific protocol with &quot;ip proto &amp;lt;protocol code=&quot;&quot;&amp;gt;&quot; capture filters, as I know, this code for TCP is 6, UDP is 17 and ICMP is 1. now I want the whole list of protocol codes, can any body help me?? thanks.'''
date = "2014-07-11T06:18:00Z"
lastmod = "2014-07-12T07:02:00Z"
weight = 34598
keywords = [ "protocols" ]
aliases = [ "/questions/34598" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [List of protocol codes](/questions/34598/list-of-protocol-codes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34598-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello guys. as you know, we can filter traffic for specific protocol with "ip proto &lt;protocol code=""&gt;" capture filters, as I know, this code for TCP is 6, UDP is 17 and ICMP is 1. now I want the whole list of protocol codes, can any body help me?? thanks.</p></div><div id="question-tags" class="tags-container tags">protocols</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '14, 06:18</strong></p><img src="https://secure.gravatar.com/avatar/db00b14e3649ef46f9c87cb77617ea12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="M_Bazgir&#39;s gravatar image" /><p>M_Bazgir<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="M_Bazgir has no accepted answers">0%</span></p></div></div><div id="comments-container-34598" class="comments-container"></div><div id="comment-tools-34598" class="comment-tools"></div><div class="clear"></div><div id="comment-34598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="34599"></span>

<div id="answer-container-34599" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34599-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You might want to try IANA: <a href="http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml">http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '14, 06:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-34599" class="comments-container"><span id="34600"></span><div id="comment-34600" class="comment"><div id="post-34600-score" class="comment-score"></div><div class="comment-text"><p>That's enough for me. :) Thanks Jasper.</p></div><div id="comment-34600-info" class="comment-info"><span class="comment-age">(11 Jul '14, 06:23)</span> M_Bazgir</div></div></div><div id="comment-tools-34599" class="comment-tools"></div><div class="clear"></div><div id="comment-34599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="34615"></span>

<div id="answer-container-34615" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34615-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can view this currently registered list in Wireshark itself.</p><p>From the menu &gt;&gt; Analyze &gt;&gt; Display Filters...</p><p>A list of the currently registered filters should appear. Now click Expression...</p><p>If you scroll down to (or type) IPv4 and expand its tree you get a list of the currently registered filters for the IPv4 protocol.</p><p>Scroll down to and select ip.proto.</p><p>If you select '==' from the relations menu and click on the specific protocol you're looking to filter by from the 'Predefined Values' menu, the 'protocol code' you are looking for should appear under Value.</p><p>You can now select the filter from here, without having to know the number, by clicking 'okay' and 'apply'. Or you can use the Expression list as a reference for all the filters registered to Wireshark! I find it really useful when one of my coworkers gives me a custom dissector and I don't know the correct syntax for the display filters they registered with Wireshark.</p><p>Jeffrey</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '14, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/e66163b53ebae2cb35d621d806073ea2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jphmiller&#39;s gravatar image" /><p>jphmiller<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jphmiller has no accepted answers">0%</span></p></div></div><div id="comments-container-34615" class="comments-container"></div><div id="comment-tools-34615" class="comment-tools"></div><div class="clear"></div><div id="comment-34615-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

