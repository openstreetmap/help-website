+++
type = "question"
title = "Do Perl bindings or a Perl Interface to EPAN or tshark exist?"
description = '''With tshark I can output CSV-like (well, tab-separated values) data about capture packages using -T fields and -e. But I&#x27;d like to access these fields directly with Perl, e.g. as a hash or in an object-oriented manner with getters. Does something like this exist? I&#x27;ve looked on CPAN (via https://met...'''
date = "2017-03-30T08:53:00Z"
lastmod = "2017-04-16T13:22:00Z"
weight = 60444
keywords = [ "bindings", "tshark", "epan", "perl" ]
aliases = [ "/questions/60444" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Do Perl bindings or a Perl Interface to EPAN or tshark exist?](/questions/60444/do-perl-bindings-or-a-perl-interface-to-epan-or-tshark-exist)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60444-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>With tshark I can output CSV-like (well, tab-separated values) data about capture packages using <code>-T fields</code> and <code>-e</code>. But I'd like to access these fields directly with Perl, e.g. as a hash or in an object-oriented manner with getters.</p><p>Does something like this exist? I've looked on CPAN (via <a href="https://metacpan.org/)">https://metacpan.org/)</a> and with Duckduckgo using keywords like <code>perl wireshark</code> as well as <code>perl epan</code>.</p></div><div id="question-tags" class="tags-container tags">bindings tshark epan perl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '17, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/7bc15ccf139f5a575652c1a0b61f6d07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="XTaran&#39;s gravatar image" /><p>XTaran<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="XTaran has no accepted answers">0%</span></p></div></div><div id="comments-container-60444" class="comments-container"></div><div id="comment-tools-60444" class="comment-tools"></div><div class="clear"></div><div id="comment-60444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60859"></span>

<div id="answer-container-60859" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60859-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is/was a library called <a href="http://search.cpan.org/~nanis/Net-Sharktools/">Net::Sharktools</a>. However I'm not sure if it works with Wireshark 2.X.</p><p>Another way to go is to use the JSON output of tshark and the JSON perl module.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '17, 13:22</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-60859" class="comments-container"></div><div id="comment-tools-60859" class="comment-tools"></div><div class="clear"></div><div id="comment-60859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

