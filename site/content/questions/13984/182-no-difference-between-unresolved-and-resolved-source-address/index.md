+++
type = "question"
title = "[1.8.2] no difference between unresolved and resolved source address..."
description = '''I&#x27;ve set up my columns to display both unresolved and resolved &#x27;Src/Dest addr&#x27; but Wireshark reflects the changes to the options onto both of the columns i.e. both columns display unresolved or resolved, not one or the other. Before you ask... I&#x27;ve specifically selected the unresolved and resolved f...'''
date = "2012-09-01T12:23:00Z"
lastmod = "2012-09-02T06:49:00Z"
weight = 13984
keywords = [ "resolved", "unresolved", "name" ]
aliases = [ "/questions/13984" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [\[1.8.2\] no difference between unresolved and resolved source address...](/questions/13984/182-no-difference-between-unresolved-and-resolved-source-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13984-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've set up my columns to display both unresolved and resolved 'Src/Dest addr' but Wireshark reflects the changes to the options onto both of the columns i.e. both columns display unresolved or resolved, not one or the other. Before you ask... I've specifically selected the unresolved and resolved field types for both address and port.</p><p>Under the options, if I 'Enable MAC and Transport Name Resolution, the Src/Dest addr (Resolved) columns don't resolve but both 'Src/Dest Port (Resolved)' do resolve and Src/Dest Port (unresolved) stays as unresolved.</p><p>If I 'Enable Network Name Resolution' then the Ports unresolved/resolved columns behave as expected but both the Src/Dest addr (unresolved) columns seem to be effected by the option and are resolved. Essentially, all the columns get resolved regardless if I select them to be unresolved.</p><p>Any ideas anyone?</p></div><div id="question-tags" class="tags-container tags">resolved unresolved name</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Sep '12, 12:23</strong></p><img src="https://secure.gravatar.com/avatar/bb0dd8c140ac683baf24b6438c825c87?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ASGR&#39;s gravatar image" /><p>ASGR<br />
<span class="score" title="20 reputation points">20</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ASGR has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Sep '12, 17:37</p></div></div><div id="comments-container-13984" class="comments-container"></div><div id="comment-tools-13984" class="comment-tools"></div><div class="clear"></div><div id="comment-13984-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13990"></span>

<div id="answer-container-13990" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13990-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a bug, similar to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7546">bug 7546</a>. I added mention of this problem to that bug report, as I'm guessing that it's probably the same bug affecting both.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '12, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-13990" class="comments-container"><span id="13992"></span><div id="comment-13992" class="comment"><div id="post-13992-score" class="comment-score"></div><div class="comment-text"><p>Thought it would head in this direction. Look forward to the fix-er-upper release.</p><p>A.</p></div><div id="comment-13992-info" class="comment-info"><span class="comment-age">(02 Sep '12, 12:22)</span> ASGR</div></div><span id="21750"></span><div id="comment-21750" class="comment"><div id="post-21750-score" class="comment-score">1</div><div class="comment-text"><p>Fixed in revision 49776 which will be included in the next 1.8 release.</p></div><div id="comment-21750-info" class="comment-info"><span class="comment-age">(04 Jun '13, 14:44)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-13990" class="comment-tools"></div><div class="clear"></div><div id="comment-13990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

