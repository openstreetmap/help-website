+++
type = "question"
title = "Dumpcap as a service"
description = '''I am looking to run dumpcap as a service. I tried using sc create but the service doesn&#x27;t start.'''
date = "2014-12-22T13:24:00Z"
lastmod = "2014-12-22T13:27:00Z"
weight = 38665
keywords = [ "dumpcap" ]
aliases = [ "/questions/38665" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dumpcap as a service](/questions/38665/dumpcap-as-a-service)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38665-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking to run dumpcap as a service. I tried using sc create but the service doesn't start.</p></div><div id="question-tags" class="tags-container tags">dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '14, 13:24</strong></p><img src="https://secure.gravatar.com/avatar/b826fc435a80f6b2fe75d4bf4789022a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wireshark_r&#39;s gravatar image" /><p>wireshark_r<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wireshark_r has no accepted answers">0%</span></p></div></div><div id="comments-container-38665" class="comments-container"><span id="38667"></span><div id="comment-38667" class="comment"><div id="post-38667-score" class="comment-score"></div><div class="comment-text"><p>Do you have a specific end goal that you're trying to reach by running it as a service? If you need to run long captures in automation, there are several useful arguments within the dumpcap binary which can be combined with cron to make it service-like depending on what you're trying to do.</p></div><div id="comment-38667-info" class="comment-info"><span class="comment-age">(22 Dec '14, 14:23)</span> Quadratic</div></div></div><div id="comment-tools-38665" class="comment-tools"></div><div class="clear"></div><div id="comment-38665-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38666"></span>

<div id="answer-container-38666" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38666-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>dumpcap is not intended to run as a service. Maybe you can use the RunAsService project on Sourceforge to trick it into working though:</p><p><a href="http://sourceforge.net/projects/runasservice/">http://sourceforge.net/projects/runasservice/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '14, 13:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-38666" class="comments-container"></div><div id="comment-tools-38666" class="comment-tools"></div><div class="clear"></div><div id="comment-38666-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

