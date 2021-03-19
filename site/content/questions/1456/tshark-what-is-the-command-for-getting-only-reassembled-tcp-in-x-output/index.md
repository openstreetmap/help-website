+++
type = "question"
title = "tshark: What is the command for getting  only &quot;Reassembled TCP&quot; in -x output"
description = '''Assume Windows, if I used  tshark -r file.pcap -R &quot;tcp.stream eq xxx&quot; -x according to the documentation I get &quot;hex and ASCII dump of the packet data after printing the summary or details&quot;. Looking at the output, I am only interested in Reassembled TCP section of -x output. Is there a field in wiresh...'''
date = "2010-12-22T13:58:00Z"
lastmod = "2010-12-27T08:26:00Z"
weight = 1456
keywords = [ "ascii", "hex", "-x", "data" ]
aliases = [ "/questions/1456" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tshark: What is the command for getting only "Reassembled TCP" in -x output](/questions/1456/tshark-what-is-the-command-for-getting-only-reassembled-tcp-in-x-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1456-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Assume Windows, if I used</p><p>tshark -r file.pcap -R "tcp.stream eq xxx" -x</p><p>according to the documentation I get "hex and ASCII dump of the packet data after printing the summary or details". Looking at the output, I am only interested in Reassembled TCP section of -x output. Is there a field in wireshark or a command to output only that section? Thanks for your help!<br />
</p></div><div id="question-tags" class="tags-container tags">ascii hex -x data</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '10, 13:58</strong></p><img src="https://secure.gravatar.com/avatar/64f007f3459dbfd425cd4f57393b2295?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="averageguy&#39;s gravatar image" /><p>averageguy<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="averageguy has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-1456" class="comments-container"><span id="1457"></span><div id="comment-1457" class="comment"><div id="post-1457-score" class="comment-score"></div><div class="comment-text"><p>A better way of asking this question would be how do I get the data of a reconstructed tcp stream.</p></div><div id="comment-1457-info" class="comment-info"><span class="comment-age">(22 Dec '10, 14:35)</span> averageguy</div></div></div><div id="comment-tools-1456" class="comment-tools"></div><div class="clear"></div><div id="comment-1456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1466"></span>

<div id="answer-container-1466" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1466-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no way?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '10, 21:13</strong></p><img src="https://secure.gravatar.com/avatar/64f007f3459dbfd425cd4f57393b2295?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="averageguy&#39;s gravatar image" /><p>averageguy<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="averageguy has no accepted answers">0%</span></p></div></div><div id="comments-container-1466" class="comments-container"></div><div id="comment-tools-1466" class="comment-tools"></div><div class="clear"></div><div id="comment-1466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1490"></span>

<div id="answer-container-1490" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1490-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Can this be done with rawshark?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '10, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/64f007f3459dbfd425cd4f57393b2295?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="averageguy&#39;s gravatar image" /><p>averageguy<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="averageguy has no accepted answers">0%</span></p></div></div><div id="comments-container-1490" class="comments-container"></div><div id="comment-tools-1490" class="comment-tools"></div><div class="clear"></div><div id="comment-1490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

