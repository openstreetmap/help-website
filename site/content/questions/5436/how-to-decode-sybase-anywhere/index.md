+++
type = "question"
title = "How to decode Sybase Anywhere?"
description = '''Hi, I got a trace with Sybase Anywhere traffic inside. The traffic flows through the tcp port 2638. If I configure the TDS dissector for this port the decode return for every packet &quot;Unknown Packet Type: 24&quot;. Is there a way to decode Sybase Anywhere traffic or to configure the TDS dissector? Regards...'''
date = "2011-08-03T06:07:00Z"
lastmod = "2011-08-03T14:33:00Z"
weight = 5436
keywords = [ "tds", "sybase", "anywhere" ]
aliases = [ "/questions/5436" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to decode Sybase Anywhere?](/questions/5436/how-to-decode-sybase-anywhere)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5436-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I got a trace with Sybase Anywhere traffic inside. The traffic flows through the tcp port 2638. If I configure the TDS dissector for this port the decode return for every packet "Unknown Packet Type: 24". Is there a way to decode Sybase Anywhere traffic or to configure the TDS dissector?</p><p>Regards,</p></div><div id="question-tags" class="tags-container tags">tds sybase anywhere</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Aug '11, 06:07</strong></p><img src="https://secure.gravatar.com/avatar/9a9a0fb96be532d17c0a9a9a5117d43a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OPapep&#39;s gravatar image" /><p>OPapep<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OPapep has no accepted answers">0%</span></p></div></div><div id="comments-container-5436" class="comments-container"></div><div id="comment-tools-5436" class="comment-tools"></div><div class="clear"></div><div id="comment-5436-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5454"></span>

<div id="answer-container-5454" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5454-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Either Sybase Anywhere isn't using TDS or it's using a version of TDS that the Wireshark TDS dissector doesn't know about; you'd have to figure out which of those is the case, and, if it's not using TDS, find out what protocol it's using, and see if Wireshark has a dissector for it - if not, you or somebody else will have to write one - or, if it's using TDS, you'll have to find out what was added to TDS and update the Wireshark dissector to support that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '11, 14:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-5454" class="comments-container"></div><div id="comment-tools-5454" class="comment-tools"></div><div class="clear"></div><div id="comment-5454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

