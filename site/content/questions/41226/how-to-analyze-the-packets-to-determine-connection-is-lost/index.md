+++
type = "question"
title = "How to analyze the packets to determine connection is lost?"
description = '''I apologize for my lack of fluency in the English language. Example situation, I&#x27;m downloading software or video. Then I unplug the RJ-45 connector to show a loss of connection during the download process is executed. The problem is, I do not know to explain the matter by input capture data as shown...'''
date = "2015-04-06T10:18:00Z"
lastmod = "2015-04-08T04:43:00Z"
weight = 41226
keywords = [ "disconnection" ]
aliases = [ "/questions/41226" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to analyze the packets to determine connection is lost?](/questions/41226/how-to-analyze-the-packets-to-determine-connection-is-lost)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41226-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I apologize for my lack of fluency in the English language. Example situation, I'm downloading software or video. Then I unplug the RJ-45 connector to show a loss of connection during the download process is executed. The problem is, I do not know to explain the matter by input capture data as shown.</p></div><div id="question-tags" class="tags-container tags">disconnection</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '15, 10:18</strong></p><img src="https://secure.gravatar.com/avatar/7795f1e292fddb93d08bd1a8796bf7df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Unknown&#39;s gravatar image" /><p>Unknown<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Unknown has no accepted answers">0%</span></p></div></div><div id="comments-container-41226" class="comments-container"></div><div id="comment-tools-41226" class="comment-tools"></div><div class="clear"></div><div id="comment-41226-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41277"></span>

<div id="answer-container-41277" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41277-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is not meant to handle or process issues at the physical layer (which is what you do when you pull the RJ-45 connector). Only from the datalink layer and up Wireshark can show you relevant information. In this case Wireshark will just report to you that the interface went down and capture was aborted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '15, 04:43</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-41277" class="comments-container"></div><div id="comment-tools-41277" class="comment-tools"></div><div class="clear"></div><div id="comment-41277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

