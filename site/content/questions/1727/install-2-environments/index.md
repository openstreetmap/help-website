+++
type = "question"
title = "Install 2 environments"
description = '''I want to work with version 1.2.1 and 1.3.6 Is it possible to install and work with 2 environments on the same computer?'''
date = "2011-01-13T00:04:00Z"
lastmod = "2011-01-13T11:55:00Z"
weight = 1727
keywords = [ "development", "environment" ]
aliases = [ "/questions/1727" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Install 2 environments](/questions/1727/install-2-environments)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1727-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to work with version 1.2.1 and 1.3.6</p><p>Is it possible to install and work with 2 environments on the same computer?</p></div><div id="question-tags" class="tags-container tags">development environment</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '11, 00:04</strong></p><img src="https://secure.gravatar.com/avatar/878c62d2f87284c01ed450e8df7883a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alrik&#39;s gravatar image" /><p>Alrik<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alrik has no accepted answers">0%</span></p></div></div><div id="comments-container-1727" class="comments-container"></div><div id="comment-tools-1727" class="comment-tools"></div><div class="clear"></div><div id="comment-1727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1738"></span>

<div id="answer-container-1738" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1738-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Certainly.</p><p>Depending upon your needs, you may want to create a separate profile for each Wireshark version and then start whichever version of Wireshark with the -C option to specify the profile to be used....</p><p>Also: 1.2.1 is a rather old version and 1.3.6 is an old development version.</p><p>The current stable version 1.4.3 contains whatever was in 1.3.6 (and additional fixes).</p><p>Why do you need to run both a production and a development version ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '11, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jan '11, 07:11</p></div></div><div id="comments-container-1738" class="comments-container"></div><div id="comment-tools-1738" class="comment-tools"></div><div class="clear"></div><div id="comment-1738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1741"></span>

<div id="answer-container-1741" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1741-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What I usually do is have the main version installed "normally" (the stable version, or the "most stable" to be precise, 1.4.3 is slowly getting there but often I revert to 1.2.x still). And then I install the other (unstable, in my case "bleeding edge") version as a portable app which makes both of them totally independent from each other.</p><p>But I have to agree with Bill, versions 1.2.1 and 1.3.6 are odd choices. You might consider 1.2.14 and 1.4.3 (or 1.5.x if you like "bleeding").</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '11, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1741" class="comments-container"></div><div id="comment-tools-1741" class="comment-tools"></div><div class="clear"></div><div id="comment-1741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

