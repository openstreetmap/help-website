+++
type = "question"
title = "Rolling window during capture"
description = '''Is it possible to capture packets into a first-in-first-out queue of user-defined duration? It would be extremely handy to leave Wireshark capturing packets unattended - possibly days - until an application crashes. By defining the duration to be n hours, we would have almost n hours to reach the Wi...'''
date = "2016-03-02T16:18:00Z"
lastmod = "2016-03-02T20:34:00Z"
weight = 50691
keywords = [ "capture", "unattended" ]
aliases = [ "/questions/50691" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Rolling window during capture](/questions/50691/rolling-window-during-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50691-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to capture packets into a first-in-first-out queue of user-defined duration?</p><p>It would be extremely handy to leave Wireshark capturing packets unattended - possibly days - until an application crashes. By defining the duration to be <em>n</em> hours, we would have almost <em>n</em> hours to reach the Wireshark workstation and save the capture before losing the failure event.<br />
</p></div><div id="question-tags" class="tags-container tags">capture unattended</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '16, 16:18</strong></p><img src="https://secure.gravatar.com/avatar/02dbd6076edbaea06e027dd9133880dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pbyhistorian&#39;s gravatar image" /><p>pbyhistorian<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pbyhistorian has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-50691" class="comments-container"></div><div id="comment-tools-50691" class="comment-tools"></div><div class="clear"></div><div id="comment-50691-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50693"></span>

<div id="answer-container-50693" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50693-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, the <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureOptions.html">capture options dialog</a> provides several options when capturing, including automatically stopping the capture after a specified duration of time.</p><p>That said, if you intend to capture for days, I wouldn't recommend using Wireshark itself for capturing, but its command-line companion <a href="https://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> tool instead, which is what Wireshark uses under the hood for capturing anyway. The main reasons for using dumpcap instead of Wireshark are for better <a href="https://wiki.wireshark.org/Performance">performance</a> and to avoid <a href="https://wiki.wireshark.org/KnownBugs/OutOfMemory">running out of memory</a>. Dumpcap allows you to specify capture options, just as Wireshark does, including limiting the capture duration using either the <code>-a duration:value</code> or <code>-b duration:value</code> options. Use the one that best suits your needs.</p><p>By the way, for your use case, there doesn't really appear to be any particularly compelling need to stop dumpcap after a specified duration, I don't think. Instead you could configure it to capture forever, making use of the ringbuffer options to avoid any individual files from growing too large, and then only stopping the capture manually whenever you've detected that the application has crashed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '16, 20:34</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-50693" class="comments-container"></div><div id="comment-tools-50693" class="comment-tools"></div><div class="clear"></div><div id="comment-50693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

