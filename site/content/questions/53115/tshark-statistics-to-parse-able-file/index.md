+++
type = "question"
title = "tshark statistics to parse-able file"
description = '''Hi, Can tshark export statistics to a parse-able format such as comma or tab delimited? Thanks '''
date = "2016-06-01T11:34:00Z"
lastmod = "2016-06-03T20:31:00Z"
weight = 53115
keywords = [ "statistics", "tshark" ]
aliases = [ "/questions/53115" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark statistics to parse-able file](/questions/53115/tshark-statistics-to-parse-able-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53115-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Can tshark export statistics to a parse-able format such as comma or tab delimited?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">statistics tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '16, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/334b3772ba24e093b1c83a07da9e12c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rob%20B&#39;s gravatar image" /><p>Rob B<br />
<span class="score" title="36 reputation points">36</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rob B has no accepted answers">0%</span></p></div></div><div id="comments-container-53115" class="comments-container"></div><div id="comment-tools-53115" class="comment-tools"></div><div class="clear"></div><div id="comment-53115-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53193"></span>

<div id="answer-container-53193" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53193-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It can present row data out of packets in comma-delimited format (using '-T fields -e example.field1 -e example.field2 -E separator=","' for example to print comma-delimited values of example.field1 and example.field2).</p><p>Now, for counters (such as those produced with "-z io,stat," option), it doesn't present it in anything "clean" like a .csv output but it does produce output for which you can write a perl wrapper around it to get it into .csv format.</p><p>Note, there is an active feature request in the Wireshark bugzilla requesting the ability for Tshark to do exactly what you're asking. If you vote for it, that might help? :) <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10759">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10759</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '16, 20:31</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-53193" class="comments-container"></div><div id="comment-tools-53193" class="comment-tools"></div><div class="clear"></div><div id="comment-53193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

