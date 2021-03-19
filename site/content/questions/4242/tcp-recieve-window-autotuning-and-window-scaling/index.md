+++
type = "question"
title = "TCP Recieve Window Autotuning and window scaling"
description = '''Hey guys, i am currently running into issues with the rwin autotuning feature since MS Vista. Here are the key facts which make me get headaches: Microsoft has documented autotuning levels for Vista, default being &quot;normal&quot;, others being &quot;restricted&quot; or &quot;experimental&quot; e.g. I was not able to find the ...'''
date = "2011-05-26T02:57:00Z"
lastmod = "2011-05-26T02:57:00Z"
weight = 4242
keywords = [ "rwin", "vista", "ws", "windows7", "tcp" ]
aliases = [ "/questions/4242" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Recieve Window Autotuning and window scaling](/questions/4242/tcp-recieve-window-autotuning-and-window-scaling)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4242-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys,</p><p>i am currently running into issues with the rwin autotuning feature since MS Vista. Here are the key facts which make me get headaches:</p><p>Microsoft has documented autotuning levels for Vista, default being "normal", others being "restricted" or "experimental" e.g. I was not able to find the same docs for Win7 stack, so i supposed(!!) it was the same which popped up to be not so right in the meantime...</p><hr /><p><em>First Part of the question:</em></p><p>While those levels exist in both Vista and Win7, the advertised WS factor during session initiation is different on both systems. Vista sticks to the ng-stack docs with WS=8 being default and going to e.g. 14 in experimental. The Win7 machines always keep WS=4 and i don't find docs about a change in Win7's TCP Stack.... anyone have an explanation (important: need links quoting the answer like TCP/IP Implementation Docs or CableGuy Article...)</p><p><em>Second Part of the question:</em></p><p>I have seen Vista machines advertising window sizes of way over 2^16 because of window scaling, even on 100MB links... now in labs I have a physical Vista machine, which ALWAYS maxes its rwin at 2^16, no matter which WS it uses, even with WS=14, rwin is starting at 3 and rises to 4 but never over it. I tried on 100M and Gigabit Links to test if there is a speed derived limit, which exists if you disable autotuning for example, but no difference. -&gt; Does anyone know where this is coming from - did MS Patch s.th. into their ng-stack explaining this behaviour or did I miss some important update on MS's TCP Implementation ?</p><p><em>Third Part of the question:</em> Anyone with details about TCP window scaling heuristics, especially what triggers the OS to override the default autotuning-level on a per application base?</p><p>Any help as always highly appreciated. Thanks in advance!!</p></div><div id="question-tags" class="tags-container tags">rwin vista ws windows7 tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '11, 02:57</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Sep '11, 08:49</p></div></div><div id="comments-container-4242" class="comments-container"><span id="4276"></span><div id="comment-4276" class="comment"><div id="post-4276-score" class="comment-score"></div><div class="comment-text"><p>Any ideas if the advertised receive window is related to the round trip time?</p></div><div id="comment-4276-info" class="comment-info"><span class="comment-age">(29 May '11, 02:36)</span> packethunter</div></div><span id="4278"></span><div id="comment-4278" class="comment"><div id="post-4278-score" class="comment-score"></div><div class="comment-text"><p>Not at all, though I would have expected this because of the bandwidth*delay product, where MS somewhere stated they would address calculation of optimal rwin within Window scaling... obviously doesn't work</p></div><div id="comment-4278-info" class="comment-info"><span class="comment-age">(29 May '11, 05:33)</span> Landi</div></div><span id="6126"></span><div id="comment-6126" class="comment"><div id="post-6126-score" class="comment-score"></div><div class="comment-text"><p><em>push</em> Any TCP heroes around ?</p></div><div id="comment-6126-info" class="comment-info"><span class="comment-age">(06 Sep '11, 08:47)</span> Landi</div></div></div><div id="comment-tools-4242" class="comment-tools"></div><div class="clear"></div><div id="comment-4242-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

