+++
type = "question"
title = "What does large delta time tells?"
description = '''I have quite a lot of high delta times from receiving multicast. What does it mean in general? How did the delta time calculated? '''
date = "2013-01-02T18:42:00Z"
lastmod = "2013-01-02T19:56:00Z"
weight = 17405
keywords = [ "multicast" ]
aliases = [ "/questions/17405" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What does large delta time tells?](/questions/17405/what-does-large-delta-time-tells)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17405-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have quite a lot of high delta times from receiving multicast. What does it mean in general? How did the delta time calculated?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/crazy_deltatime.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">multicast</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jan '13, 18:42</strong></p><img src="https://secure.gravatar.com/avatar/eaebacafc90c2a4a4e75f053e3c16432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bryanevil&#39;s gravatar image" /><p>bryanevil<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bryanevil has no accepted answers">0%</span></p></img></div></div><div id="comments-container-17405" class="comments-container"></div><div id="comment-tools-17405" class="comment-tools"></div><div class="clear"></div><div id="comment-17405-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17407"></span>

<div id="answer-container-17407" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17407-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The "delta time" is exactly whatever you originally created the column to be:</p><p>If you created the column it using Edit ! Preferences | Columns and selected "Delta Time", the time is the "Time delta from previous captured frame".</p><p>If you sort the frames by "No." the difference between the time for a frame and the time for the previous frame should be equal to the Delta Time.</p><p>A "high delta time" just means that at times frames were received at a low rate.</p><p>Again, if you sort by the "No." column and then look at one of the frames with a high delta time, you should see that the frame was received after not receiveing any frames for the "delta time" interval.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '13, 19:56</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jan '13, 20:01</p></div></div><div id="comments-container-17407" class="comments-container"><span id="17442"></span><div id="comment-17442" class="comment"><div id="post-17442-score" class="comment-score"></div><div class="comment-text"><p>And be sure to pay attention to which delta time you choose. There are a few (self explanatory) so just pay attention.</p></div><div id="comment-17442-info" class="comment-info"><span class="comment-age">(04 Jan '13, 07:38)</span> hansangb</div></div></div><div id="comment-tools-17407" class="comment-tools"></div><div class="clear"></div><div id="comment-17407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

