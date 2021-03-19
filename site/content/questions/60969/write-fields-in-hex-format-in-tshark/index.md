+++
type = "question"
title = "Write fields in hex format in tshark"
description = '''hi. can we print some fields of a packet in hex format in tshark? if we use :  tshark -r nbns.pcap -T fields -e frame.number -e ip.src -V &amp;gt; nbns.txt  the output(nbns.txt) is : 1 192.168.1.9 2 192.168.1.9 3 192.168.1.9 but i want to Write ip address in hex format(below).is it possible? 1 c0 a8 01 ...'''
date = "2017-04-22T05:20:00Z"
lastmod = "2017-04-22T14:55:00Z"
weight = 60969
keywords = [ "tshark" ]
aliases = [ "/questions/60969" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Write fields in hex format in tshark](/questions/60969/write-fields-in-hex-format-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60969-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi. can we print some fields of a packet in hex format in tshark? if we use :</p><blockquote><p>tshark -r nbns.pcap -T fields -e frame.number -e ip.src -V &gt; nbns.txt</p></blockquote><p>the output(nbns.txt) is :</p><p>1 192.168.1.9</p><p>2 192.168.1.9</p><p>3 192.168.1.9</p><p>but i want to Write ip address in hex format(below).is it possible?</p><p>1 c0 a8 01 09</p><p>2 c0 a8 01 09</p><p>3 c0 a8 01 09</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '17, 05:20</strong></p><img src="https://secure.gravatar.com/avatar/28d5dc133c31193058a99892f00a0213?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ghader&#39;s gravatar image" /><p>ghader<br />
<span class="score" title="61 reputation points">61</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ghader has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>wikified 22 Apr '17, 10:23</p></div></div><div id="comments-container-60969" class="comments-container"></div><div id="comment-tools-60969" class="comment-tools"></div><div class="clear"></div><div id="comment-60969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60972"></span>

<div id="answer-container-60972" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60972-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This can probably be optimized, but you can pipe the <code>tshark</code> output to other tools to transform it as you like, for example:</p><pre><code>tshark -r nbns.pcap -T fields -e frame.number -e ip.src | sed &#39;s/\./ /g&#39; | sed &#39;s/\r//g&#39; | xargs printf &#39;%d %02x %02x %02x %02x\n&#39; | tee nbns.txt</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '17, 14:55</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Apr '17, 15:30</p></div></div><div id="comments-container-60972" class="comments-container"><span id="60974"></span><div id="comment-60974" class="comment"><div id="post-60974-score" class="comment-score"></div><div class="comment-text"><p>thanks, but when i run this command in tshark it says: sed in not recognizeds as an internal or external command,operable program or batch file. we use %02x %02x %02x %02x to printf ip address in hex format and know that ip address has 4 byte,but if we dont know fields length, how we can write them in hex format?</p></div><div id="comment-60974-info" class="comment-info"><span class="comment-age">(22 Apr '17, 21:06)</span> ghader</div></div><span id="60975"></span><div id="comment-60975" class="comment"><div id="post-60975-score" class="comment-score">1</div><div class="comment-text"><p>If you're running on Windows, that answer won't work, unless you happen to have UN*X tools such as sed, xargs, and printf installed on your machine (for example, through Cygwin); you'll have to find some other program or programs to transform the output into that format - TShark has no mechanism to produce that output directly.</p></div><div id="comment-60975-info" class="comment-info"><span class="comment-age">(22 Apr '17, 21:13)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-60972" class="comment-tools"></div><div class="clear"></div><div id="comment-60972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

