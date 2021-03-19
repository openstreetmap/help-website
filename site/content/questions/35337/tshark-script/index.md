+++
type = "question"
title = "TShark script"
description = '''Hi All, I have used wireshark but not tshark. Is it possible with tshark to capture the barcodes from a USB reader, and send them as raw TCP to a IP address? Would this be difficult to script? Cheers in advance, -Al'''
date = "2014-08-08T17:36:00Z"
lastmod = "2014-08-10T06:48:00Z"
weight = 35337
keywords = [ "raw", "barcode", "tshark", "tcp", "usb" ]
aliases = [ "/questions/35337" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TShark script](/questions/35337/tshark-script)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35337-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I have used wireshark but not tshark.</p><p>Is it possible with tshark to capture the barcodes from a USB reader, and send them as raw TCP to a IP address?</p><p>Would this be difficult to script?</p><p>Cheers in advance,</p><p>-Al</p></div><div id="question-tags" class="tags-container tags">raw barcode tshark tcp usb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '14, 17:36</strong></p><img src="https://secure.gravatar.com/avatar/4c867c7e03c8a62c9dc21a2db19d79c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bigalnz&#39;s gravatar image" /><p>bigalnz<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bigalnz has no accepted answers">0%</span></p></div></div><div id="comments-container-35337" class="comments-container"></div><div id="comment-tools-35337" class="comment-tools"></div><div class="clear"></div><div id="comment-35337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35369"></span>

<div id="answer-container-35369" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35369-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I <strong>have used wireshark</strong> but not tshark. Is it <strong>possible with tshark to capture the barcodes from a USB</strong> reader,</p></blockquote><p>If you are able to do that with Wireshark (sounds like, according to your comments), you can do it with tshark as well. In that case, I'll need more information about how you did it with Wireshark. As soon as you post that information, I can (possibly) 'translate' it into a way to do the same with tshark.</p><blockquote><p>and send them as raw TCP to a IP address?<br />
Would this be difficult to script?</p></blockquote><p><strong>sending data</strong> does not work with tshark, so you'll have to write a script that is able to send data via TCP or use netcat or similar tools.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '14, 06:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Aug '14, 09:20</p></div></div><div id="comments-container-35369" class="comments-container"></div><div id="comment-tools-35369" class="comment-tools"></div><div class="clear"></div><div id="comment-35369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

