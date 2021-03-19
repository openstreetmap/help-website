+++
type = "question"
title = "Can Wireshark show a &quot;Locked View&quot; with message values changing?"
description = '''Hi there, I&#x27;m looking to do some analyses of my car with Wireshark in live capture mode. However, I find it difficult to analyse the data live, even when using filters.  I was wondering if it would be possible to &quot;lock the view&quot; in wireshark so that I e.g. specify 10 message IDs that I want to &quot;stay...'''
date = "2017-05-10T14:20:00Z"
lastmod = "2017-05-10T21:57:00Z"
weight = 61345
keywords = [ "capture", "live", "wireshark", "data", "view" ]
aliases = [ "/questions/61345" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Can Wireshark show a "Locked View" with message values changing?](/questions/61345/can-wireshark-show-a-locked-view-with-message-values-changing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61345-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I'm looking to do some analyses of my car with Wireshark in live capture mode. However, I find it difficult to analyse the data live, even when using filters.</p><p>I was wondering if it would be possible to "lock the view" in wireshark so that I e.g. specify 10 message IDs that I want to "stay in place" on my screen, while allowing the values of these IDs to change? I.e. one message ID could relate to vehicle speed and it would constantly be the top message in the interface - but the value would change as the speed changes.</p><p>Does this already exist? If not, is it possible to code this up?</p><p>Thank you, Martin</p></div><div id="question-tags" class="tags-container tags">capture live wireshark data view</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '17, 14:20</strong></p><img src="https://secure.gravatar.com/avatar/bb505f6832bb10125678c300fff66aae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mfcss&#39;s gravatar image" /><p>mfcss<br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mfcss has no accepted answers">0%</span></p></div></div><div id="comments-container-61345" class="comments-container"></div><div id="comment-tools-61345" class="comment-tools"></div><div class="clear"></div><div id="comment-61345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61349"></span>

<div id="answer-container-61349" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61349-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Does this already exist?</p></blockquote><p>No.</p><blockquote><p>If not, is it possible to code this up?</p></blockquote><p>It would probably be <em>extremely</em> difficult to make the packet list work that way.</p><p>However, it would probably be not too hard to write a tap for your protocol that could be given a list of message IDs and displays the values corresponding to those message IDs, updating them as new packets arrive.</p><p>See <a href="https://wiki.wireshark.org/Lua/Taps">this page on writing taps in Lua</a> and <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=doc/README.tapping">the README.tapping document</a>. At least for writing a tap in C++, you'll probably need to read the Qt documentation as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '17, 21:57</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-61349" class="comments-container"></div><div id="comment-tools-61349" class="comment-tools"></div><div class="clear"></div><div id="comment-61349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

