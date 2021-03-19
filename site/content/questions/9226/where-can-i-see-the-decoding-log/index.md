+++
type = "question"
title = "where can i see the decoding log"
description = '''I download the wireshark source-code and install it on ubuntu. Now i&#x27;d like to see the log when decoding such as: RTMPT_DEBUG(&quot;Segment: cdir=%d seq=%d-%d&#92;n&quot;, cdir, seq, seq+remain-1). where can i find the log file? (i&#x27;ve enable the macro of DEBUG_RTMPT and compile/re-install). Thanks'''
date = "2012-02-26T18:21:00Z"
lastmod = "2012-02-27T13:47:00Z"
weight = 9226
keywords = [ "log" ]
aliases = [ "/questions/9226" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [where can i see the decoding log](/questions/9226/where-can-i-see-the-decoding-log)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9226-score" class="post-score" title="current number of votes">0</div><span id="post-9226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I download the wireshark source-code and install it on ubuntu. Now i'd like to see the log when decoding such as: RTMPT_DEBUG("Segment: cdir=%d seq=%d-%d\n", cdir, seq, seq+remain-1). where can i find the log file? (i've enable the macro of DEBUG_RTMPT and compile/re-install). Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-log" rel="tag" title="see questions tagged &#39;log&#39;">log</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '12, 18:21</strong></p><img src="https://secure.gravatar.com/avatar/4fcce4e0a1968119d1b4305823054fa0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mumulinp&#39;s gravatar image" /><p><span>mumulinp</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mumulinp has no accepted answers">0%</span></p></div></div><div id="comments-container-9226" class="comments-container"></div><div id="comment-tools-9226" class="comment-tools"></div><div class="clear"></div><div id="comment-9226-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9258"></span>

<div id="answer-container-9258" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9258-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9258-score" class="post-score" title="current number of votes">0</div><span id="post-9258-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Look at the <code>RTMPT_DEBUG</code> macro. It either expands to <code>rtmpt_debug</code> or to a bit of a hack that results in nothing being printed. <code>rtmpt_debug()</code> uses <code>vprintf()</code>, which prints to the standard output, so the "log file" is wherever Wireshark's or TShark's standard output goes. If you run Wireshark in a terminal, then, unless you redirect its standard output, it'll show up on your terminal; your terminal is probably an <code>xterm</code> or <code>Konsole</code> or <code>gnome-terminal</code> or other such terminal-emulator program; it might have scrolling enabled, so you can see more than one screenful of output.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '12, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9258" class="comments-container"></div><div id="comment-tools-9258" class="comment-tools"></div><div class="clear"></div><div id="comment-9258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

