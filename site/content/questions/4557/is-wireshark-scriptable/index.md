+++
type = "question"
title = "is wireshark scriptable?"
description = '''hello i have a simple question i need to import many big pcap files were talking about 200GB+  and i would like to write a script to make wireshark import the separate 500Mb Files and merge them into 1 big file for analyzing? is this possible? and if yeah how ? or where can i find anything about the...'''
date = "2011-06-14T02:16:00Z"
lastmod = "2011-06-14T02:54:00Z"
weight = 4557
keywords = [ "merge", "gb", "analysis", "script" ]
aliases = [ "/questions/4557" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [is wireshark scriptable?](/questions/4557/is-wireshark-scriptable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4557-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello i have a simple question</p><p>i need to import many big pcap files were talking about 200GB+ and i would like to write a script to make wireshark import the separate 500Mb Files and merge them into 1 big file for analyzing? is this possible? and if yeah how ? or where can i find anything about the scripting functions?</p><p>thanks in advanced</p></div><div id="question-tags" class="tags-container tags">merge gb analysis script</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '11, 02:16</strong></p><img src="https://secure.gravatar.com/avatar/8f973182882130ed5ab2bb1ebd5e1ea4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="g33n&#39;s gravatar image" /><p>g33n<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="g33n has no accepted answers">0%</span></p></div></div><div id="comments-container-4557" class="comments-container"></div><div id="comment-tools-4557" class="comment-tools"></div><div class="clear"></div><div id="comment-4557-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4559"></span>

<div id="answer-container-4559" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4559-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are several command line tools available to manipulate capture files, have a look at <a href="http://www.wireshark.org/docs/wsug_html_chunked/AppTools.html">the User's Guide</a>.</p><p>On the other hand, feeding Wireshark 500MB files, let alone 200GB files would crush it under <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">memory constraints</a>.</p><p>If you need to analyze data sets like this, <a href="http://www.riverbed.com/us/products/cascade/cascade_pilot.php">CACE^H^H^H^HRiverbed Cascade Pilot Software</a> is more for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '11, 02:54</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4559" class="comments-container"><span id="4563"></span><div id="comment-4563" class="comment"><div id="post-4563-score" class="comment-score"></div><div class="comment-text"><p>thank you for this quick anwser i will try the trial of cascade and if it works well ill buy it thanks alot</p></div><div id="comment-4563-info" class="comment-info"><span class="comment-age">(14 Jun '11, 05:42)</span> g33n</div></div></div><div id="comment-tools-4559" class="comment-tools"></div><div class="clear"></div><div id="comment-4559-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

