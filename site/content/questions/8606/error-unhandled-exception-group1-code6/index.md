+++
type = "question"
title = "Error: Unhandled Exception (group=1, code=6)?"
description = '''I am trying to dissect the captured pcap header using libwireshark.so, but when i call  epan_dissect_init(&amp;amp;edt,true,true); epan_dissect_run();  I see this error: Error: Unhandled Exception (group=1, code=6)  Why?'''
date = "2012-01-25T09:14:00Z"
lastmod = "2012-01-30T09:59:00Z"
weight = 8606
keywords = [ "development", "exception" ]
aliases = [ "/questions/8606" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Error: Unhandled Exception (group=1, code=6)?](/questions/8606/error-unhandled-exception-group1-code6)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8606-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to dissect the captured pcap header using libwireshark.so, but when i call</p><pre><code>epan_dissect_init(&amp;edt,true,true);
epan_dissect_run();</code></pre><p>I see this error:</p><pre><code>Error: Unhandled Exception (group=1, code=6)</code></pre><p>Why?</p></div><div id="question-tags" class="tags-container tags">development exception</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '12, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p>Sanny_D<br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jan '12, 20:09</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-8606" class="comments-container"></div><div id="comment-tools-8606" class="comment-tools"></div><div class="clear"></div><div id="comment-8606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="8705"></span>

<div id="answer-container-8705" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8705-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>thanks guys!</p><p>there was some problem in initializing the epan</p><p>after fixing that now its working :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '12, 09:59</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p>Sanny_D<br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div></div><div id="comments-container-8705" class="comments-container"></div><div id="comment-tools-8705" class="comment-tools"></div><div class="clear"></div><div id="comment-8705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8610"></span>

<div id="answer-container-8610" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8610-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>As I said earlier:</p><p>" ....you are basically on your own if you are trying to use libwireshark directly. :-)</p><p>At the very least you need to be quite comfortable using a debugger to trace through the code to see why you are getting the error."</p><p>In this case, something caused an Exception (trap) and there was no code to 'handle' the exception.</p><p>I would use a debugger to step through the code following the call to <code>epan_dissect_run()</code> to see where the exception occurs.</p><p>You probably don't need to worry too much how exceptions work; You just need to find the place in the code which caused the exception.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '12, 11:48</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-8610" class="comments-container"></div><div id="comment-tools-8610" class="comment-tools"></div><div class="clear"></div><div id="comment-8610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8614"></span>

<div id="answer-container-8614" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8614-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>It means a dissector failed to allocate memory (see code 6's definition below)...</p><p>The exception group value is always 1, and the exception codes are defined here (based on <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/exceptions.h?revision=35277&amp;view=markup">epan/exceptions.h</a>):</p><table data-border="1"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="header"><th>Code</th><th>Description</th></tr><tr class="odd"><td>1</td><td><code>BoundsError</code><p><br />
Index is out of range.<br />
<br />
An attempt was made to read past the end of a buffer.<br />
This generally means that the capture was done with a "slice"<br />
length or "snapshot" length less than the maximum packet size,<br />
and a link-layer packet was cut short by that, so not all of the<br />
data in the link-layer packet was available.</p></td></tr><tr class="even"><td>2</td><td><code>ReportedBoundsError</code><p><br />
Index is beyond reported length (not cap_len).<br />
<br />
An attempt was made to read past the logical end of a buffer. This<br />
differs from a BoundsError in that the parent protocol established a<br />
limit past which this dissector should not process in the buffer and that<br />
limit was exceeded.<br />
This generally means that the packet is invalid, i.e. whatever<br />
code constructed the packet and put it on the wire didn't put enough<br />
data into it. It is therefore currently reported as a "Malformed<br />
packet".<br />
<br />
However, it also happens in some cases where the packet was fragmented<br />
and the fragments weren't reassembled. We need to add another length<br />
field to a tvbuff, so that "length of the packet from the link layer"<br />
and "length of the packet were it fully reassembled" are different,<br />
and going past the first of those without going past the second would<br />
throw a different exception, which would be reported as an "Unreassembled<br />
packet" rather than a "Malformed packet".</p></td></tr><tr class="odd"><td>3</td><td><code>TypeError</code><p><br />
During display-filter parsing</p></td></tr><tr class="even"><td>4</td><td><code>DissectorError</code><p><br />
A bug was detected in a dissector.<br />
<br />
DO NOT throw this with <code>THROW()</code>; that means that no details about<br />
the dissector error will be reported. (Instead, the message will<br />
blame you for not providing details.)<br />
<br />
Instead, use the <code>DISSECTOR_ASSERT()</code>, etc. macros in epan/proto.h.</p></td></tr><tr class="odd"><td>5</td><td><code>ScsiBoundsError</code><p><br />
Index is out of range.<br />
<br />
An attempt was made to read past the end of a buffer.<br />
<br />
This error is specific to SCSI data transfers where for some CDBs<br />
it is normal that the data PDU might be short.<br />
I.e. ReportLuns initially called with allocation_length=8, just enough<br />
to get the "size" of lun list back after which the initiator will<br />
reissue the command with an allocation_length that is big enough.</p></td></tr><tr class="even"><td>6</td><td><code>OutOfMemoryError</code><p><br />
Running out of memory.<br />
<br />
A dissector tried to allocate memory but that failed.</p></td></tr></tbody></table></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '12, 19:59</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span> </br></br></p></div></div><div id="comments-container-8614" class="comments-container"><span id="8626"></span><div id="comment-8626" class="comment"><div id="post-8626-score" class="comment-score"></div><div class="comment-text"><p>Thanks ppl!</p><p>i tried to fix it.. but all in vain.. what exactly is the problem? is it related to the OS i am using or the amount of virtual memory i have?</p><p>how to get rid of this error.. any help :-/</p><p>thanks|</p></div><div id="comment-8626-info" class="comment-info"><span class="comment-age">(26 Jan '12, 10:30)</span> Sanny_D</div></div><span id="8642"></span><div id="comment-8642" class="comment"><div id="post-8642-score" class="comment-score"></div><div class="comment-text"><p>Go with Bill's suggestion, and step through your code with a debugger.</p></div><div id="comment-8642-info" class="comment-info"><span class="comment-age">(26 Jan '12, 18:29)</span> helloworld</div></div></div><div id="comment-tools-8614" class="comment-tools"></div><div class="clear"></div><div id="comment-8614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

