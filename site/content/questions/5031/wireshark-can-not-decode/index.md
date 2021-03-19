+++
type = "question"
title = "wireshark can not decode"
description = '''I am tracing s6a messages and on the ula message if the avp1430 shows up more than 3 times wireshark does not decode that part of the message un shows unreassembled packet (exception ocurred)'''
date = "2011-07-13T12:23:00Z"
lastmod = "2011-07-13T15:20:00Z"
weight = 5031
keywords = [ "avp1430" ]
aliases = [ "/questions/5031" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark can not decode](/questions/5031/wireshark-can-not-decode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5031-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am tracing s6a messages and on the ula message if the avp1430 shows up more than 3 times wireshark does not decode that part of the message un shows unreassembled packet (exception ocurred)</p></div><div id="question-tags" class="tags-container tags">avp1430</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '11, 12:23</strong></p><img src="https://secure.gravatar.com/avatar/1a637fd29147289a56de4061210c3d67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GSC&#39;s gravatar image" /><p>GSC<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GSC has no accepted answers">0%</span></p></div></div><div id="comments-container-5031" class="comments-container"></div><div id="comment-tools-5031" class="comment-tools"></div><div class="clear"></div><div id="comment-5031-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5035"></span>

<div id="answer-container-5035" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5035-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What version of Wireshark are you using? 1.6 would be best for LTE stuff. If that's what you are using raise a bug report <a href="https://bugs.wireshark.org/bugzilla/">here</a> attaching a sample trace.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '11, 15:20</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-5035" class="comments-container"><span id="5037"></span><div id="comment-5037" class="comment"><div id="post-5037-score" class="comment-score"></div><div class="comment-text"><p>Reported the <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6116">bug 6116</a>. It seems that it has a restriction on the number of times that avp can repeat or maybe the master avp 1440 (where is breaks) length becomes too big.</p></div><div id="comment-5037-info" class="comment-info"><span class="comment-age">(13 Jul '11, 18:28)</span> GSC</div></div></div><div id="comment-tools-5035" class="comment-tools"></div><div class="clear"></div><div id="comment-5035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

