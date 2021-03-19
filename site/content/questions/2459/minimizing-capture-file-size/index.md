+++
type = "question"
title = "Minimizing Capture File Size?"
description = '''I&#x27;ve read http://wiki.wireshark.org/KnownBugs/OutOfMemory. But it seems to beg the question of how one can minimize the size of the capture file. All I care about are VOIP &quot;INVITE&quot; packets. I&#x27;ve got a filter set: syslog.msg contains &quot;INVITE sip:&quot; I think it&#x27;s a &quot;Capture&quot; filter... but even though Wi...'''
date = "2011-02-21T13:45:00Z"
lastmod = "2011-02-22T05:27:00Z"
weight = 2459
keywords = [ "memory" ]
aliases = [ "/questions/2459" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Minimizing Capture File Size?](/questions/2459/minimizing-capture-file-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2459-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've read http://wiki.wireshark.org/KnownBugs/OutOfMemory.</p><p>But it seems to beg the question of how one can minimize the size of the capture file.</p><p>All I care about are VOIP "INVITE" packets.</p><p>I've got a filter set: syslog.msg contains "INVITE sip:"</p><p>I <em>think</em> it's a "Capture" filter... but even though WireShark's window is only showing the desired packets (very, very few....) it seems to keep chugging along with the total packets.</p><p>So, bottom line, is there a way to make WireShark use that filter to not even add non-qualifying packets to it's file? That would enable the running of WireShark for very, very long periods of time without running out of memory.</p></div><div id="question-tags" class="tags-container tags">memory</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '11, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/8bde5a113e61480e8111dcc2e49409f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PeteCress&#39;s gravatar image" /><p>PeteCress<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PeteCress has no accepted answers">0%</span></p></div></div><div id="comments-container-2459" class="comments-container"></div><div id="comment-tools-2459" class="comment-tools"></div><div class="clear"></div><div id="comment-2459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2460"></span>

<div id="answer-container-2460" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2460-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The filter <code>syslog.msg contains "INVITE sip:"</code> is <strong>not</strong> a capture filter, it is a display filter. That means that it doesn't filter out packets from getting into the trace, it only hides them from view. Capture filters are specified in the Capture Options dialog, not in the main window. Unfortunately I do not have a capture filter for you that does what you want to do, but maybe someone else can help you with that.</p><p>If nobody can come up with a capture filter you might consider doing a ring buffer capture and running tshark on the files to extract the packets you want every once in a while. That way you can prevent running out of disk space and extract the information you want.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '11, 14:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2460" class="comments-container"></div><div id="comment-tools-2460" class="comment-tools"></div><div class="clear"></div><div id="comment-2460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2474"></span>

<div id="answer-container-2474" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2474-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Check out this page for a reference http://wiki.wireshark.org/CaptureFilters</p><p>Skip down to the line that starts "Capture HTTP Get" - use this sample as a guide.</p><p>To build this filter you'll need a packet capture that contains the kind of packet you're going to be looking for as a reference. In other words, do whatever you've done before and use the display filter you listed above - this should produce a few good representative packets. Click on the packet of interest, in Wireshark's middle frame expand the "Syslog message" tree, and look for the "Message: " line. In there you should see the "INVITE sip:" data, click on it. This should highlight an area of text in Wireshark's 3rd/bottom frame, this is the HEX viewer. You need to note into which HEX locations the characters "INVITE sip:" fall. In the only Syslog sample I have it appears that the syslog message starts in 0030. I ASSume that "INVITE sip:" would be located 0030-003a.</p><p>SO, you can start building the filter from there..</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '11, 05:27</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p>GeonJay<br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-2474" class="comments-container"></div><div id="comment-tools-2474" class="comment-tools"></div><div class="clear"></div><div id="comment-2474-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

