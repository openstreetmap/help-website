+++
type = "question"
title = "Mouse Hover Highlight  hex/ascii on GTK?"
description = '''Mouse hover highlight hex to ascii issue.  Of the three window Panes, the &#x27;Packet Bytes&#x27; pane, it used to be that if you hover the mouse over the Hex or binary data, either &#x27;printable text&#x27; or &#x27;value&#x27; whichever one, the mouse would highlight the current location and also it&#x27;s match. so to clarify, b...'''
date = "2017-01-12T20:06:00Z"
lastmod = "2017-01-12T23:55:00Z"
weight = 58715
keywords = [ "hex-ascii", "highlight", "hover", "mouse", "gtk+" ]
aliases = [ "/questions/58715" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Mouse Hover Highlight hex/ascii on GTK?](/questions/58715/mouse-hover-highlight-hexascii-on-gtk)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58715-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Mouse hover highlight hex to ascii issue.</p><p>Of the three window Panes, the 'Packet Bytes' pane, it used to be that if you hover the mouse over the Hex or binary data, either 'printable text' or 'value' whichever one, the mouse would highlight the current location and also it's match. so to clarify, both the printable text (hex/binary) and the value(printable text) would be lit up, wherever the mouse goes.</p><p>This behavior is observed in windows, but not in linux (centos 7, fedora 25).</p><p>Can anybody shed some light into the right direction, where can i start troubleshooting to get this feature on linux?</p><p>Thanks in advance!</p><p>Update: Okay, so does the windows version use QT?</p><p>can this feature be ported over to GTK+ also?? <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11547">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11547</a></p></div><div id="question-tags" class="tags-container tags">hex-ascii highlight hover mouse gtk+</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '17, 20:06</strong></p><img src="https://secure.gravatar.com/avatar/12485589afcbdb073ee7191e38d8836f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cdoyle4785&#39;s gravatar image" /><p>cdoyle4785<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cdoyle4785 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jan '17, 20:07</p></div></div><div id="comments-container-58715" class="comments-container"></div><div id="comment-tools-58715" class="comment-tools"></div><div class="clear"></div><div id="comment-58715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58717"></span>

<div id="answer-container-58717" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58717-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The hover highlighting feature was created for Qt, since that is the interface toolkit <a href="https://blog.wireshark.org/2013/10/switching-to-qt/">we are moving towards</a>. Therefore don't expect many, if any, improvements on the GTK interface in Wireshark 2.x. Might as well the Qt variant on your Linux systems.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '17, 23:55</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-58717" class="comments-container"></div><div id="comment-tools-58717" class="comment-tools"></div><div class="clear"></div><div id="comment-58717-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

