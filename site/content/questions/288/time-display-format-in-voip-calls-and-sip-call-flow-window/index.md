+++
type = "question"
title = "Time display format in VoIP calls (and SIP Call Flow) window"
description = '''Hello WireShark.org, I have a question about time display format using in Wireshark. I prefer to use &quot;Time of day&quot; format, but &quot;VoIP calls&quot; analyser window and &quot;Graph Analyse&quot; Call Flow window do not support this time format, it always use time &quot;Since beginning of capture&quot;. It is very inconvenient -...'''
date = "2010-09-23T02:37:00Z"
lastmod = "2010-10-06T16:16:00Z"
weight = 288
keywords = [ "graph", "sip", "voip", "time" ]
aliases = [ "/questions/288" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Time display format in VoIP calls (and SIP Call Flow) window](/questions/288/time-display-format-in-voip-calls-and-sip-call-flow-window)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-288-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello WireShark.org,</p><p>I have a question about time display format using in Wireshark. I prefer to use "Time of day" format, but "VoIP calls" analyser window and "Graph Analyse" Call Flow window do not support this time format, it always use time "Since beginning of capture". It is very inconvenient - when comparing long captures of VoIP activity from different NICs, for example. Or when debuging VoIP from long files, which are captured for a few days, etc.</p><p>Is it possible that the "VoIP calls" analyser window and "Graph Analyse" Call Flow window to legacy time display format from main window?</p><p>Thank you!</p><p>Best regards, Ramil Khankildiev</p></div><div id="question-tags" class="tags-container tags">graph sip voip time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '10, 02:37</strong></p><img src="https://secure.gravatar.com/avatar/2119680c7389540f94e106ee20ccfcf5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nreal&#39;s gravatar image" /><p>nreal<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nreal has no accepted answers">0%</span></p></div></div><div id="comments-container-288" class="comments-container"></div><div id="comment-tools-288" class="comment-tools"></div><div class="clear"></div><div id="comment-288-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="290"></span>

<div id="answer-container-290" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-290-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's a good enhancement request. Currently this is not possible, but the data is available internally, so it all comes down to creating the desired presentation in the GUI.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '10, 03:45</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-290" class="comments-container"><span id="301"></span><div id="comment-301" class="comment"><div id="post-301-score" class="comment-score">1</div><div class="comment-text"><p>Thank you, it would be great. By the way, the RTP Player also uses time "Since beginning of capture". Fix'em all! :)</p></div><div id="comment-301-info" class="comment-info"><span class="comment-age">(23 Sep '10, 09:37)</span> nreal</div></div></div><div id="comment-tools-290" class="comment-tools"></div><div class="clear"></div><div id="comment-290-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="450"></span>

<div id="answer-container-450" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-450-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not only is it a good enhancement request, it's a request that's already been made: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1293" title="Bug 1293">Bug 1293</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '10, 16:16</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Oct '10, 16:16</p></div></div><div id="comments-container-450" class="comments-container"></div><div id="comment-tools-450" class="comment-tools"></div><div class="clear"></div><div id="comment-450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

