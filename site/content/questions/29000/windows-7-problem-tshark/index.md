+++
type = "question"
title = "windows 7 problem tshark"
description = '''Hi I had the current version of Wireshark1.10.2 on my laptop (Mac Os) and desktop (windows 7)  I tried this script in terminal and it is working on Mac Os, but whenever I try it in Windows 7 command terminal, I get this error:  tshark: Invalid -o flag &quot;column.format:&#x27;No.,%m,&quot; Why it is working in Ma...'''
date = "2014-01-17T11:46:00Z"
lastmod = "2014-01-17T12:07:00Z"
weight = 29000
keywords = [ "windows7", "tshark" ]
aliases = [ "/questions/29000" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [windows 7 problem tshark](/questions/29000/windows-7-problem-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29000-score" class="post-score" title="current number of votes">0</div><span id="post-29000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I had the current version of Wireshark1.10.2 on my laptop (Mac Os) and desktop (windows 7) I tried this script in terminal and it is working on Mac Os, but whenever I try it in Windows 7 command terminal, I get this error:</p><p><strong>tshark: Invalid -o flag "column.format:'No.,%m,"</strong></p><p>Why it is working in Mac os but not in windows !!!!!</p><p>Please Help me :)</p><p>tshark -Y "ip" -o column.format:'"No.","%m", "full time", "%Yt","src ip", "%us","des ip","%ud", "lenght", "%L","transfered byte", "%B","protocol","%p","srcmac","%uhs","destmac","%uhd","sourceport", "%uS", "destport", "%uD", "Info", "%i"' -r test.pcap &gt;test.txt</p><p><strong>tshark: Invalid -o flag "column.format:'No.,%m,"</strong></p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '14, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/a76f3e9f7708742d5869cf5353337891?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Payam365&#39;s gravatar image" /><p><span>Payam365</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Payam365 has no accepted answers">0%</span></p></div></div><div id="comments-container-29000" class="comments-container"></div><div id="comment-tools-29000" class="comment-tools"></div><div class="clear"></div><div id="comment-29000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29001"></span>

<div id="answer-container-29001" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29001-score" class="post-score" title="current number of votes">0</div><span id="post-29001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Payam365 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is quoting. You need to escape all the quotes using <code>\"</code> except for the outermost quotes. The development version of <code>tshark</code> adds a <code>-G column-formats</code> option that, besides listing all available column formats, provides the following example at the end of the output:</p><p><code> For example, to print Wireshark's default columns with tshark:</code></p><code></code><p><code>tshark.exe -o "gui.column.format:\"No.\",\"%m\",\"Time\",\"%t\",\"Source\",\"%s\",\"Destination\",\"%d\",\"Protocol\",\"%p\",\"Length\",\"%L\",\"Info\",\"%i\""</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '14, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-29001" class="comments-container"></div><div id="comment-tools-29001" class="comment-tools"></div><div class="clear"></div><div id="comment-29001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

