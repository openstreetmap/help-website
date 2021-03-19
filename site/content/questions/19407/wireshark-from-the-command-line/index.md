+++
type = "question"
title = "Wireshark from the command line"
description = '''I tried modifying this for my own purposes: @echo on  set start=0 set /p end= Enter number of 30-minute increments to loop: set filenum=1 set filestart=&quot;c:&#92;tempWScap&#92;result&quot; set fileend=&quot;.pcapng&quot;  :loop if %start%==%end% goto stop set &quot;filestring=%filestart%%filenum%%fileend%&quot; &quot;C:&#92;program files&#92;wire...'''
date = "2013-03-12T14:05:00Z"
lastmod = "2013-03-13T07:44:00Z"
weight = 19407
keywords = [ "commandline", "scripting" ]
aliases = [ "/questions/19407" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark from the command line](/questions/19407/wireshark-from-the-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19407-score" class="post-score" title="current number of votes">0</div><span id="post-19407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried modifying this for my own purposes:</p><pre><code>@echo on

set start=0
set /p end= Enter number of 30-minute increments to loop:
set filenum=1
set filestart=&quot;c:\tempWScap\result&quot;
set fileend=&quot;.pcapng&quot;

:loop
if %start%==%end% goto stop
set &quot;filestring=%filestart%%filenum%%fileend%&quot;
&quot;C:\program files\wireshark\wireshark.exe&quot; -i &quot;\Device\NPF_{5423F6E4-1BC8-4F55-625E-B2F995D893D1}&quot; -a duration:180 -w %filestring% -k
set /a start=%start%+1
set /a filenum=%filenum%+1

PING 127.0.0.1 -n 1800

goto loop

:stop</code></pre><p>This works fine but I want it to quit wireshark after the capture is over. The -Q option does not appear to work. Any suggestions?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-commandline" rel="tag" title="see questions tagged &#39;commandline&#39;">commandline</span> <span class="post-tag tag-link-scripting" rel="tag" title="see questions tagged &#39;scripting&#39;">scripting</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '13, 14:05</strong></p><img src="https://secure.gravatar.com/avatar/f156a63914cee87412f6d4e8c2ecf333?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pdxsfin33&#39;s gravatar image" /><p><span>pdxsfin33</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pdxsfin33 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>12 Mar '13, 15:28</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-19407" class="comments-container"></div><div id="comment-tools-19407" class="comment-tools"></div><div class="clear"></div><div id="comment-19407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19452"></span>

<div id="answer-container-19452" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19452-score" class="post-score" title="current number of votes">0</div><span id="post-19452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What version of Wireshark are you using?</p><p>The -Q option was changed to an environment variable (WIRESHARK_QUIT_AFTER_CAPTURE) in <a href="http://anonsvn.wireshark.org/viewvc/viewvc.cgi?view=rev&amp;revision=38784">r38784</a>. That means version 1.8.0 and later must use that environment variable instead of -Q (see the <a href="https://www.wireshark.org/docs/man-pages/wireshark.html">Wireshark man page</a> for more details).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '13, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-19452" class="comments-container"></div><div id="comment-tools-19452" class="comment-tools"></div><div class="clear"></div><div id="comment-19452-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

