+++
type = "question"
title = "How to best feed packets to Wireshark from e.g. CAN"
description = '''Hi all, We have a logger that streams CAN bus messages from e.g. a CAR via a C program and a pipe into Wireshark. This works great, though we are experiencing some packet loss, in some cases significant. Right now the C code handles one byte at a time, incl. testing what type of byte it is and then ...'''
date = "2017-05-13T08:23:00Z"
lastmod = "2017-05-15T03:53:00Z"
weight = 61383
keywords = [ "pipe", "data", "packet", "wireshark" ]
aliases = [ "/questions/61383" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to best feed packets to Wireshark from e.g. CAN](/questions/61383/how-to-best-feed-packets-to-wireshark-from-eg-can)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61383-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>We have a logger that streams CAN bus messages from e.g. a CAR via a C program and a pipe into Wireshark. This works great, though we are experiencing some packet loss, in some cases significant.</p><p>Right now the C code handles one byte at a time, incl. testing what type of byte it is and then handling it accordingly. This is most likely the cause of losses as we miss packets that are close together.</p><p>Is there a best practice for how to handle this "packet feeding" into Wireshark? Would it e.g. be better to create a "buffer array" of incoming bytes, then handle these via another function to avoid the loss - or is there another generally applied best practice?</p><p>Thank you.</p><p>Best, Martin</p></div><div id="question-tags" class="tags-container tags">pipe data packet wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '17, 08:23</strong></p><img src="https://secure.gravatar.com/avatar/bb505f6832bb10125678c300fff66aae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mfcss&#39;s gravatar image" /><p>mfcss<br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mfcss has no accepted answers">0%</span></p></div></div><div id="comments-container-61383" class="comments-container"></div><div id="comment-tools-61383" class="comment-tools"></div><div class="clear"></div><div id="comment-61383-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61403"></span>

<div id="answer-container-61403" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61403-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The development version of Wireshark supports a mechanism known as Extcap that allows applications external to Wireshark to provide traffic to Wireshark.</p><p>See <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=doc/README.extcap;h=f1e27ce01c14fbc305406f2e44b867a7cc5b6e08;hb=HEAD">README.extcap</a>, the Wiki <a href="https://wiki.wireshark.org/Development/Extcap">Extcap development page</a> (somewhat out of date) and the <a href="https://www.wireshark.org/docs/man-pages/extcap.html">extcap man page</a> that discusses the arguments supplied to extcap applications for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '17, 03:53</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-61403" class="comments-container"></div><div id="comment-tools-61403" class="comment-tools"></div><div class="clear"></div><div id="comment-61403-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

