+++
type = "question"
title = "Searching for Text in a Pcap from a Blog DTD XHTML 1.0"
description = '''I have been noticing that when I sniff traffic from blogs, that I cannot seem to be able to read the text on the main blog page as it shows up as all garbled when you follow the tcp stream in Wireshark. For instance, you would see something like. 14949 ...............W.%.&amp;gt;.}..ge..63......p..........'''
date = "2012-07-24T05:26:00Z"
lastmod = "2013-05-01T11:25:00Z"
weight = 12954
keywords = [ "text", "blogs", "pcap" ]
aliases = [ "/questions/12954" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Searching for Text in a Pcap from a Blog DTD XHTML 1.0](/questions/12954/searching-for-text-in-a-pcap-from-a-blog-dtd-xhtml-10)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12954-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been noticing that when I sniff traffic from blogs, that I cannot seem to be able to read the text on the main blog page as it shows up as all garbled when you follow the tcp stream in Wireshark. For instance, you would see something like.</p><p>14949</p><p>...............W.%.&gt;.}[email protected])\M...w..-....0%2]#Y.=.-#sy....._./......Qs...dd0:Y.A....=.}.}....{......x...u.......'..d..........'..g.....N...uZ6y.WeZ..?.jo...Vm.y...qq1..9.......</p><p>Instead of text on the blog. I cannot search any of the text on the blog via ASCII/Unicode or Hex within this garbled mess.</p><p>When I export the file out via HTTP Objects and look at it in a text editor it looks just like you would expect it to be with the HTML source code. Is there a way to make Wireshark show me the HTML source code of blog sites without having to extract out the main page every time?<br />
</p></div><div id="question-tags" class="tags-container tags">text blogs pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '12, 05:26</strong></p><img src="https://secure.gravatar.com/avatar/00554dd290f9d95df515fdda7cb04859?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WSHKNeezy&#39;s gravatar image" /><p>WSHKNeezy<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WSHKNeezy has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-12954" class="comments-container"></div><div id="comment-tools-12954" class="comment-tools"></div><div class="clear"></div><div id="comment-12954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12955"></span>

<div id="answer-container-12955" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12955-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Most certainly the webserver used gzip compression for the content (HTTP response header: <code>Content-Encoding: gzip</code>). "Follow TCP Stream" does <strong>NOT uncompress</strong> the content, as that is not implemented. If you save the HTTP objects, uncompressing is implemented.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '12, 05:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jul '12, 12:15</p></div></div><div id="comments-container-12955" class="comments-container"></div><div id="comment-tools-12955" class="comment-tools"></div><div class="clear"></div><div id="comment-12955-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20880"></span>

<div id="answer-container-20880" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20880-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sadly, wireshark's capabilities in working with compressed TCP streams are quite limited. I recommend using tcpflow, which will reassemble all of the TCP streams and decompressed those that are compressed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '13, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/a355f7a3b3404b578af95e47cd274cc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bhh&#39;s gravatar image" /><p>bhh<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bhh has no accepted answers">0%</span></p></div></div><div id="comments-container-20880" class="comments-container"></div><div id="comment-tools-20880" class="comment-tools"></div><div class="clear"></div><div id="comment-20880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

