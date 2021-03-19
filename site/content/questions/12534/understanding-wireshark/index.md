+++
type = "question"
title = "Understanding wireshark"
description = '''I am new to Wireshark and I am needing help with navigating through it. How do I lfind the IP and MAC address of the suspect system, the DNS server, the default gateway, and the DHCP server. How do I find the vendor of the suspect network card. How do I extract a web page and a graphic file from wir...'''
date = "2012-07-09T12:42:00Z"
lastmod = "2012-07-09T14:59:00Z"
weight = 12534
keywords = [ "suspect", "system" ]
aliases = [ "/questions/12534" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Understanding wireshark](/questions/12534/understanding-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12534-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to Wireshark and I am needing help with navigating through it. How do I lfind the IP and MAC address of the suspect system, the DNS server, the default gateway, and the DHCP server. How do I find the vendor of the suspect network card. How do I extract a web page and a graphic file from wire shark. How do I find the computer name of the suspect system. And last how do I find which protocols used the most. I tried to find help online and I could not find what I am looking for so I am trying this route.</p><p>Thanks in Advance</p></div><div id="question-tags" class="tags-container tags">suspect system</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '12, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/49fa20257072052df246d3c91e7c4355?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jennifer26m&#39;s gravatar image" /><p>jennifer26m<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jennifer26m has no accepted answers">0%</span></p></div></div><div id="comments-container-12534" class="comments-container"></div><div id="comment-tools-12534" class="comment-tools"></div><div class="clear"></div><div id="comment-12534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="12536"></span>

<div id="answer-container-12536" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12536-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This sounds like another homework assignment to me (which would mean you should better try to find out yourself). There's tons of help on the Wireshark home page, including tutorials, videos, a Wiki etc.</p><p>If it isn't a homework assignment: can you specify more details about the so called "suspect system"? Why is it a suspect system, and what kind of trace data do you have?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '12, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-12536" class="comments-container"><span id="12537"></span><div id="comment-12537" class="comment"><div id="post-12537-score" class="comment-score">1</div><div class="comment-text"><p>Its an intro to wireshark for a college course. I don't want answers I want to know how to navigate through wireshark to be able to answer these questions. I have been looking all through wireshark and online but I cant find any type of help that i am looking for</p></div><div id="comment-12537-info" class="comment-info"><span class="comment-age">(09 Jul '12, 14:16)</span> jennifer32c</div></div><span id="12541"></span><div id="comment-12541" class="comment"><div id="post-12541-score" class="comment-score"></div><div class="comment-text"><p>Okay, fair enough. In that case you might want to start asking questions one at a time and tell us where you're stuck.</p><p>Finding IP addresses and MAC addresses is quite easy if you take a look at the statistics menu, especially the "Endpoint" and "Conversation" statistics. It will give you an overview of what addresses there are in a capture.</p><p>If you need to identify a certain system doing something suspicious you'd first need to know what suspicious is. Then use display filters to isolate the suspicious communication and use the packet detail pane to investigate further details.</p></div><div id="comment-12541-info" class="comment-info"><span class="comment-age">(09 Jul '12, 16:20)</span> Jasper ♦♦</div></div></div><div id="comment-tools-12536" class="comment-tools"></div><div class="clear"></div><div id="comment-12536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12538"></span>

<div id="answer-container-12538" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12538-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Lots of information is on the <a href="http://www.wireshark.org/docs/">documentation page</a>. The "Introduction to Wireshark" video should answer some of the questions. You also may be interested in the protocol hierarchy and exporting objects features within Wireshark; more details will be in the user guide. It's still hard to give pointers on a "suspect system" without a definition for one. Maybe some of the "network mysteries" videos at the link below will be of help in suggested a process to repeat.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '12, 14:45</strong></p><img src="https://secure.gravatar.com/avatar/da397b10ce6b1b4fcc25764ce0c9e35a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rickg421&#39;s gravatar image" /><p>rickg421<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rickg421 has no accepted answers">0%</span></p></div></div><div id="comments-container-12538" class="comments-container"></div><div id="comment-tools-12538" class="comment-tools"></div><div class="clear"></div><div id="comment-12538-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12539"></span>

<div id="answer-container-12539" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12539-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I don't want answers I want to know how to navigate through wireshark to be able to answer these questions.</p></blockquote><p>Watch the following videos (including others on youtube) and you will be enlighted ;-)</p><blockquote><p><code>http://www.youtube.com/watch?v=NHLTa29iovU</code><br />
<code>http://www.youtube.com/watch?v=pk4OfsxxB4g&amp;feature=related</code><br />
<code>http://wiresharkdownloads.riverbed.com/video/wireshark/introduction-to-wireshark/</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '12, 14:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jul '12, 15:02</p></div></div><div id="comments-container-12539" class="comments-container"></div><div id="comment-tools-12539" class="comment-tools"></div><div class="clear"></div><div id="comment-12539-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

