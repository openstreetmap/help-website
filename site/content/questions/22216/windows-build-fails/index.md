+++
type = "question"
title = "windows build fails"
description = '''Can anybody help me... I cannot build wireshark. This error message allways apears: bash -o igncr tool/textify.sh &quot;./COPYING&quot; wireshark-gtk2 tools/textify.sh: line 50: u2d: command not found NMAKE : faral error U1077: &#x27;c:&#92;cygwin&#92;bin&#92;bash.EXE&#x27; : return code &#x27;0x7f&#x27;  I have Win7 and use MSVS2010. Any o...'''
date = "2013-06-20T23:05:00Z"
lastmod = "2013-06-28T02:34:00Z"
weight = 22216
keywords = [ "windows", "failure", "build", "error" ]
aliases = [ "/questions/22216" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [windows build fails](/questions/22216/windows-build-fails)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22216-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22216-score" class="post-score" title="current number of votes">0</div><span id="post-22216-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can anybody help me...</p><p>I cannot build wireshark. This error message allways apears:</p><pre><code>bash -o igncr tool/textify.sh &quot;./COPYING&quot; wireshark-gtk2
tools/textify.sh: line 50: u2d: command not found
NMAKE : faral error U1077: &#39;c:\cygwin\bin\bash.EXE&#39; : return code &#39;0x7f&#39;</code></pre><p>I have Win7 and use MSVS2010. Any other mistakes are not known. Hope you guys can help me...</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-failure" rel="tag" title="see questions tagged &#39;failure&#39;">failure</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '13, 23:05</strong></p><img src="https://secure.gravatar.com/avatar/29dda1a3f1a92e1755318de9e31696c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marko1988&#39;s gravatar image" /><p><span>Marko1988</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marko1988 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Jun '13, 02:35</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-22216" class="comments-container"><span id="22217"></span><div id="comment-22217" class="comment"><div id="post-22217-score" class="comment-score"></div><div class="comment-text"><p>I could avoid this error message by commenting out all command lines with the textify command in the Makefile.nmake file. I think this is quite acceptable, for a quick solution. Because it's a matter of readme, help, ... -files. But anyway, this is a problem which should be avoided. Any ideas?</p></div><div id="comment-22217-info" class="comment-info"><span class="comment-age">(21 Jun '13, 01:18)</span> <span class="comment-user userinfo">Marko1988</span></div></div></div><div id="comment-tools-22216" class="comment-tools"></div><div class="clear"></div><div id="comment-22216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22222"></span>

<div id="answer-container-22222" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22222-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22222-score" class="post-score" title="current number of votes">6</div><span id="post-22222-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to install an additional component of Cygwin, the <code>Utils/dos2unix</code> package. Run the Cygwin <code>setup.exe</code> and find the package using the search box and then install it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '13, 07:01</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-22222" class="comments-container"><span id="22445"></span><div id="comment-22445" class="comment"><div id="post-22445-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much!</p></div><div id="comment-22445-info" class="comment-info"><span class="comment-age">(28 Jun '13, 02:29)</span> <span class="comment-user userinfo">Marko1988</span></div></div><span id="22446"></span><div id="comment-22446" class="comment"><div id="post-22446-score" class="comment-score"></div><div class="comment-text"><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-22446-info" class="comment-info"><span class="comment-age">(28 Jun '13, 02:34)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-22222" class="comment-tools"></div><div class="clear"></div><div id="comment-22222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

