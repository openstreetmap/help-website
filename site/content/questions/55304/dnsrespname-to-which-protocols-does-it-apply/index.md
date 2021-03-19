+++
type = "question"
title = "dns.resp.name - to which protocols does it apply?"
description = '''Hi there, I&#x27;m writing a program in which I parse a PDML XML file to obtain the domain names of web servers that a program tries to access. I&#x27;m using dns.resp.name for the name attribute in the field tag - i.e. &amp;lt;field name=&quot;dns.resp.name&quot; ...=&quot;&quot;/&amp;gt; - to identify the XML elements which contain th...'''
date = "2016-09-02T11:42:00Z"
lastmod = "2016-09-02T15:35:00Z"
weight = 55304
keywords = [ "pdml", "dns", "filters" ]
aliases = [ "/questions/55304" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [dns.resp.name - to which protocols does it apply?](/questions/55304/dnsrespname-to-which-protocols-does-it-apply)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55304-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I'm writing a program in which I parse a PDML XML file to obtain the domain names of web servers that a program tries to access. I'm using dns.resp.name for the name attribute in the field tag - i.e. &lt;field name="dns.resp.name" ...=""/&gt; - to identify the XML elements which contain the domain names.</p><p>I have found that it is not only the DNS protocol which uses dns.resp.name, but the mDNS protocol too. Just to be sure, do any other protocols use this (and being overly pedantic like I am, could you point me to some documentation somewhere which says so/not)?</p><p>Many thanks in advance, Lobster.</p></div><div id="question-tags" class="tags-container tags">pdml dns filters</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '16, 11:42</strong></p><img src="https://secure.gravatar.com/avatar/05aa98a3a949c17526355a407a7c506e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lobster&#39;s gravatar image" /><p>Lobster<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lobster has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Sep '16, 12:28</p></div></div><div id="comments-container-55304" class="comments-container"></div><div id="comment-tools-55304" class="comment-tools"></div><div class="clear"></div><div id="comment-55304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55310"></span>

<div id="answer-container-55310" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55310-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the dissector source code you can derive that also "Link-local Multicast Name Resolution", LLMNR, uses this same dissector code, so can produce this same field.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '16, 15:35</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-55310" class="comments-container"><span id="56325"></span><div id="comment-56325" class="comment"><div id="post-56325-score" class="comment-score"></div><div class="comment-text"><p>One more sub-question: is it possible for there to be more than one 'num' field within a 'geninfo' protocol section, or more than one 'frame.time_relative' field within a 'frame' protocol section?</p></div><div id="comment-56325-info" class="comment-info"><span class="comment-age">(12 Oct '16, 11:40)</span> Lobster</div></div></div><div id="comment-tools-55310" class="comment-tools"></div><div class="clear"></div><div id="comment-55310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

