+++
type = "question"
title = "The smoking gun?"
description = '''Two weeks ago, users started reporting issues with one of our Sun Oracle 7410 file servers. Opening a file on the server or downloading to a workstation tops out at speeds around 700 KB/s - 2.5 MB/s on a 1G link. There are no drops or discards on any switch interfaces in the path, Wireshark doesn&#x27;t ...'''
date = "2014-08-18T06:32:00Z"
lastmod = "2014-08-18T06:42:00Z"
weight = 35535
keywords = [ "delay", "transfer", "sun" ]
aliases = [ "/questions/35535" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [The smoking gun?](/questions/35535/the-smoking-gun)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35535-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Two weeks ago, users started reporting issues with one of our Sun Oracle 7410 file servers. Opening a file on the server or downloading to a workstation tops out at speeds around 700 KB/s - 2.5 MB/s on a 1G link. There are no drops or discards on any switch interfaces in the path, Wireshark doesn't show any TCP Retransmissions, and there are multiple instances of an ACK from the server followed by a delay before sending the next packet, like so:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/delay_22.PNG" alt="alt text" /></p><p>This makes me fairly positive that the server is the source of the problem, not the network. The server admins claim innocence. Is a delay like this proof-positive of a server issue, or does it warrant more troubleshooting from the network side?</p></div><div id="question-tags" class="tags-container tags">delay transfer sun</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '14, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/e0cb4422f173754fdb30ceb8523c6533?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="reklov77&#39;s gravatar image" /><p>reklov77<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="reklov77 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-35535" class="comments-container"></div><div id="comment-tools-35535" class="comment-tools"></div><div class="clear"></div><div id="comment-35535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35536"></span>

<div id="answer-container-35536" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35536-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's a little hard to say from just a screenshot, but it looks like the client is sending a new read request in No. 21578, which gets ACKed in about 2 milliseconds (meaning "I've received your request"). After that it takes 10 seconds to start sending actual data, which is an eternity in networks.</p><p>If this trace was taken next to the server you have text book application delay (because the Stack ACKed nice and fast), but it takes ages for actual data to flow. If the trace was taken at the client you need to take another capture at the server to verify this behavior (and exclude freak network device behavior).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '14, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35536" class="comments-container"><span id="35537"></span><div id="comment-35537" class="comment"><div id="post-35537-score" class="comment-score"></div><div class="comment-text"><p>This trace was taken from the client. A SPAN capture on the server interface shows similar delays. Cloudshark is blocked at work (file sharing) so I can't upload a full capture.</p></div><div id="comment-35537-info" class="comment-info"><span class="comment-age">(18 Aug '14, 06:52)</span> reklov77</div></div><span id="35538"></span><div id="comment-35538" class="comment"><div id="post-35538-score" class="comment-score"></div><div class="comment-text"><p>If you want you can send me a sample (only if there is no confidential stuff in the trace) to [email protected] But if the capture at the server shows similar delays you've got the smoking gun. SMB service delay on the server.</p></div><div id="comment-35538-info" class="comment-info"><span class="comment-age">(18 Aug '14, 07:02)</span> Jasper ♦♦</div></div></div><div id="comment-tools-35536" class="comment-tools"></div><div class="clear"></div><div id="comment-35536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

