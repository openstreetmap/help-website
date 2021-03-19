+++
type = "question"
title = "Multiple concurrent Wireshark sessions"
description = '''Does anyone nkow of a quick and easy way to stop a user accidentally opening multiple Wireshark Sessions on the same box. In our example an admin selected 20 files for deletion but accidentally hit open. 20 Wireshark sessions tried to open at once and the box just halted. A reboot was the only solut...'''
date = "2011-05-27T05:36:00Z"
lastmod = "2011-05-27T15:02:00Z"
weight = 4256
keywords = [ "sessions", "multiple", "wireshark" ]
aliases = [ "/questions/4256" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple concurrent Wireshark sessions](/questions/4256/multiple-concurrent-wireshark-sessions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4256-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does anyone nkow of a quick and easy way to stop a user accidentally opening multiple Wireshark Sessions on the same box. In our example an admin selected 20 files for deletion but accidentally hit open. 20 Wireshark sessions tried to open at once and the box just halted. A reboot was the only solution - how do we prevent that happening again?</p></div><div id="question-tags" class="tags-container tags">sessions multiple wireshark</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '11, 05:36</strong></p><img src="https://secure.gravatar.com/avatar/56e2f6ee15b68dbe44359aae7ce0321f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chalkie&#39;s gravatar image" /><p>Chalkie<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chalkie has no accepted answers">0%</span></p></div></div><div id="comments-container-4256" class="comments-container"></div><div id="comment-tools-4256" class="comment-tools"></div><div class="clear"></div><div id="comment-4256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4262"></span>

<div id="answer-container-4262" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4262-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>One "dirty" way of doing this would be to dissociate wireshark from any file extension so it won't be started with a double click on a file name or accidentally selects "open" in the rightclick list.</p><p>But I guess you will have some user complaints when you do that ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '11, 14:57</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4262" class="comments-container"></div><div id="comment-tools-4262" class="comment-tools"></div><div class="clear"></div><div id="comment-4262-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4263"></span>

<div id="answer-container-4263" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4263-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As far as I know that kind of functionality (checking for "program already running") is something that needs to be coded into the program itself. I'm not sure how fast a thing like that would be added if you'd request it as a feature, but you might still try and ask for it on the bugzilla tracker.</p><p>If you want to mimic that kind of functionality you could write a batch script that is used to run Wireshark instead of calling Wireshark directly. In that script you could write a "lock file" that gets deleted after Wireshark is closed and returns control to the script. If you start a second session the script needs to check if the lock file exists and exit if it does. Problem could be that the lock file might remain on disk if you terminate the script abnormaly, but it would be easy to fix - just delete the lock file manually. Don't forget to make the script the default program when opening capture files, otherwise it will be bypassed by the OS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '11, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4263" class="comments-container"></div><div id="comment-tools-4263" class="comment-tools"></div><div class="clear"></div><div id="comment-4263-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

