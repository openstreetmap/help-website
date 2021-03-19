+++
type = "question"
title = "Automate Wireshark using perl"
description = '''How can i automate Wireshark using perl script. I need to launch the software, capture for a specified duration and save the packet dissections into a text file using perl script. Is it possible to do so?'''
date = "2014-03-26T23:56:00Z"
lastmod = "2014-03-30T19:16:00Z"
weight = 31211
keywords = [ "automate", "perl" ]
aliases = [ "/questions/31211" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Automate Wireshark using perl](/questions/31211/automate-wireshark-using-perl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31211-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>How can i automate Wireshark using perl script. I need to launch the software, capture for a specified duration and save the packet dissections into a text file using perl script. Is it possible to do so?</p></div><div id="question-tags" class="tags-container tags">automate perl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '14, 23:56</strong></p><img src="https://secure.gravatar.com/avatar/544053d14f5b05c1d48009dcb206ce40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zoikelle&#39;s gravatar image" /><p>zoikelle<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zoikelle has no accepted answers">0%</span></p></div></div><div id="comments-container-31211" class="comments-container"></div><div id="comment-tools-31211" class="comment-tools"></div><div class="clear"></div><div id="comment-31211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="31212"></span>

<div id="answer-container-31212" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31212-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is a command line "version" of Wireshark called <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark</a>, usually installed with the Wireshark suite, that is suitable for use with scripts.</p><p>As to how to use it, well it's exactly the same as <a href="http://www.perlhowto.com/executing_external_commands">calling any other external command</a> from perl.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '14, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-31212" class="comments-container"></div><div id="comment-tools-31212" class="comment-tools"></div><div class="clear"></div><div id="comment-31212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31230"></span>

<div id="answer-container-31230" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31230-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How can i automate Wireshark using perl script.</p></blockquote><p>Take a look at Net::Sharktools.</p><blockquote><p><a href="http://search.cpan.org/dist/Net-Sharktools/">http://search.cpan.org/dist/Net-Sharktools/</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '14, 11:43</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31230" class="comments-container"></div><div id="comment-tools-31230" class="comment-tools"></div><div class="clear"></div><div id="comment-31230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31304"></span>

<div id="answer-container-31304" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31304-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For automated <strong>captures</strong>, I highly recommend using dumpcap rather than wireshark or tshark. The reason is that dumpcap doesn't keep the packets in memory as it writes, so it's far more resource-efficient for automated capture processes. If you want tshark-level intelligence (eg: with Wireshark display filters), I'd still recommend saving first with dumpcap, then running tshark against the file saved by dumpcap.</p><p>If your objective is as simple as you say, a script could be written with just a few lines of code. What I usually do for this is grab the current date/time from Perl's localtime(), use the time as part of a file name, and schedule a dumpcap trace for a duration equal to the frequency that cron reruns the script. Do a 'man dumpcap' (installed with Wireshark) to see the options there for a system call from perl, no modules required.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '14, 19:16</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-31304" class="comments-container"></div><div id="comment-tools-31304" class="comment-tools"></div><div class="clear"></div><div id="comment-31304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

