+++
type = "question"
title = "NMAKE : fatal error U1077: &#x27;sed&#x27; : return code &#x27;0x1&#x27;"
description = '''I am unable to build wireshark from the released source. I found a few references to this error but none were resolved. The source is version 1.4.4. Please help.  A verify tools command generates the following:   Checking for required applications:  cl: /cygdrive/c/Program Files/Microsoft Visual Stu...'''
date = "2011-12-15T09:25:00Z"
lastmod = "2012-01-26T12:39:00Z"
weight = 7991
keywords = [ "sed" ]
aliases = [ "/questions/7991" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [NMAKE : fatal error U1077: 'sed' : return code '0x1'](/questions/7991/nmake-fatal-error-u1077-sed-return-code-0x1)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7991-score" class="post-score" title="current number of votes">0</div><span id="post-7991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am unable to build wireshark from the released source. I found a few references to this error but none were resolved. The source is version 1.4.4. Please help.</p><p>A verify tools command generates the following:<br />
</p><blockquote><p>Checking for required applications:<br />
cl: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/BIN/cl<br />
link: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/BIN/link<br />
nmake: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/BIN/nmake<br />
mt: /cygdrive/c/Program Files/Microsoft SDKs/Windows/v6.1/bin/mt<br />
bash: /usr/bin/bash<br />
bison: /usr/bin/bison<br />
flex: /usr/bin/flex<br />
env: /usr/bin/env<br />
grep: /usr/bin/grep<br />
/usr/bin/find: /usr/bin/find<br />
perl: /cygdrive/c/perl/bin/perl<br />
C:Python27python.exe: /cygdrive/c/Python27/python.exe<br />
sed: /cygdrive/x/SW/GARMIN/sed<br />
unzip: /usr/bin/unzip<br />
wget: /usr/bin/wget</p></blockquote><p>Here's the error generated from "nmake -f Makefile.nmake all"<br />
</p><blockquote><p>The system cannot execute the specified program.<br />
NMAKE : fatal error U1077: 'sed' : return code '0x1'</p></blockquote></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sed" rel="tag" title="see questions tagged &#39;sed&#39;">sed</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '11, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/76cdf137f5239bfbe6e10e28b7f3b56c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="simply_blue&#39;s gravatar image" /><p><span>simply_blue</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="simply_blue has one accepted answer">100%</span> </br></br></p></div></div><div id="comments-container-7991" class="comments-container"></div><div id="comment-tools-7991" class="comment-tools"></div><div class="clear"></div><div id="comment-7991-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8001"></span>

<div id="answer-container-8001" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8001-score" class="post-score" title="current number of votes">1</div><span id="post-8001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="simply_blue has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try putting your Cygwin first in your Windows PATH before calling <code>nmake</code>. For example:</p><pre><code>C:\wireshark_src&gt; set PATH=c:\cygwin\bin;%PATH%
C:\wireshark_src&gt; nmake -f Makefile</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '11, 15:31</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span> </br></br></p></div></div><div id="comments-container-8001" class="comments-container"><span id="8039"></span><div id="comment-8039" class="comment"><div id="post-8039-score" class="comment-score"></div><div class="comment-text"><p>That seems to have resolved this issue. Thanks! (although, now the build stops at a linking stage)</p></div><div id="comment-8039-info" class="comment-info"><span class="comment-age">(19 Dec '11, 07:04)</span> <span class="comment-user userinfo">simply_blue</span></div></div><span id="8041"></span><div id="comment-8041" class="comment"><div id="post-8041-score" class="comment-score"></div><div class="comment-text"><p>Also for anyone else who hits this issue, you want to set cygwin at the beginning of the path before you run vcvars32.bat</p></div><div id="comment-8041-info" class="comment-info"><span class="comment-age">(19 Dec '11, 07:40)</span> <span class="comment-user userinfo">simply_blue</span></div></div><span id="8628"></span><div id="comment-8628" class="comment"><div id="post-8628-score" class="comment-score"></div><div class="comment-text"><p>I think this question can be closed but I'm too new to do so.</p></div><div id="comment-8628-info" class="comment-info"><span class="comment-age">(26 Jan '12, 11:59)</span> <span class="comment-user userinfo">simply_blue</span></div></div><span id="8630"></span><div id="comment-8630" class="comment"><div id="post-8630-score" class="comment-score"></div><div class="comment-text"><p>@simply_blue if this suggestion fixed your problem, you can mark it as the accepted answer by clicking the checkmark outline underneath the voting buttons. This will mark the question as resolved. There is no need to close the question, as the Q&amp;A format works differently from a forum.</p></div><div id="comment-8630-info" class="comment-info"><span class="comment-age">(26 Jan '12, 12:06)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="8631"></span><div id="comment-8631" class="comment"><div id="post-8631-score" class="comment-score"></div><div class="comment-text"><p>@multipleinterfaces Thanks I was trying to figure out how to do so but i figured I didn't have enough karma yet.</p></div><div id="comment-8631-info" class="comment-info"><span class="comment-age">(26 Jan '12, 12:39)</span> <span class="comment-user userinfo">simply_blue</span></div></div></div><div id="comment-tools-8001" class="comment-tools"></div><div class="clear"></div><div id="comment-8001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7993"></span>

<div id="answer-container-7993" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7993-score" class="post-score" title="current number of votes">2</div><span id="post-7993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>sed: /cygdrive/x/SW/GARMIN/sed</code> ????? expected <code>/usr/bin/sed</code></p><p>Something wrong with your path ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '11, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Dec '11, 09:55</strong> </span></p></div></div><div id="comments-container-7993" class="comments-container"><span id="7994"></span><div id="comment-7994" class="comment"><div id="post-7994-score" class="comment-score"></div><div class="comment-text"><p>That directory is included in the path. I can use sed from the command line (cmd.exe not bash) successfully with other commands. Would it help if I tried to point it to a local install instead of the network drive?</p><p>http://seclists.org/wireshark/2010/Dec/5 This guy had the same error with /usr/bin/sed</p></div><div id="comment-7994-info" class="comment-info"><span class="comment-age">(15 Dec '11, 10:28)</span> <span class="comment-user userinfo">simply_blue</span></div></div><span id="7995"></span><div id="comment-7995" class="comment"><div id="post-7995-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Would it help if I tried to point it to a local install instead of the network drive?</p></blockquote><p>Yes</p><p>Your <em>bash</em> (not cmd) path is somehow setup so that the weird sed is found first when looking for sed.</p><p>(I'm assuming that the GARMIN/sed is something "not sed").</p><p>What is your path from the Bash prompt ?</p></div><div id="comment-7995-info" class="comment-info"><span class="comment-age">(15 Dec '11, 10:33)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="7996"></span><div id="comment-7996" class="comment"><div id="post-7996-score" class="comment-score"></div><div class="comment-text"><p>The path from cmd/bash differs only by /usr/local/bin:/usr/bin: being included at the beginning of the bash path. The network drive is included in both.</p><p>My understanding, from the developer's guide, is that commands like "nmake -f Makefile.nmake all" should be run from cmd not bash. Which path would the tool verification command use?</p><p>Is it possible to remove the X drive from the path used by bash but not the cmd path?</p></div><div id="comment-7996-info" class="comment-info"><span class="comment-age">(15 Dec '11, 12:37)</span> <span class="comment-user userinfo">simply_blue</span></div></div><span id="7997"></span><div id="comment-7997" class="comment"><div id="post-7997-score" class="comment-score">1</div><div class="comment-text"><p>That sounds like the network drive is in your windows path which is then being picked up by bash.</p><p>You'll need to fix the path being used in your cmd prompt before calling nmake.</p></div><div id="comment-7997-info" class="comment-info"><span class="comment-age">(15 Dec '11, 12:54)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-7993" class="comment-tools"></div><div class="clear"></div><div id="comment-7993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

