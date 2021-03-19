+++
type = "question"
title = "Getting compiler error with tools/textify.sh:line50:u2d:command not found"
description = '''Hello,  First of all my question is to how to locate source code for Wireshark release 1.10.7 with Git?  My other question is I just downloaded the source code for Wireshark release 1.10.10 from the download site instead of via Git and tried to make a build as is without any modification and I am ge...'''
date = "2014-10-02T06:57:00Z"
lastmod = "2014-10-03T02:20:00Z"
weight = 36786
keywords = [ "source", "code", "issue", "build", "wireshark" ]
aliases = [ "/questions/36786" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting compiler error with tools/textify.sh:line50:u2d:command not found](/questions/36786/getting-compiler-error-with-toolstextifyshline50u2dcommand-not-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36786-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36786-score" class="post-score" title="current number of votes">0</div><span id="post-36786-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, First of all my question is to how to locate source code for Wireshark release 1.10.7 with Git? My other question is I just downloaded the source code for Wireshark release 1.10.10 from the download site instead of via Git and tried to make a build as is without any modification and I am getting the following error. Not sure I am missing any. I would prefer to obtain the 1.10.7 source code via Git, but did not know how to do so, hence going this route but having issue at the moment with the build. Please suggest. thanks in advance, Muriel</p><pre><code>        bash -o igncr tools/textify.sh &quot;./COPYING&quot; wireshark-gtk2
tools/textify.sh: line 50: u2d: command not found
NMAKE : fatal error U1077: &#39;c:\cygwin\bin\bash.EXE&#39; : return code &#39;0x7f&#39;
Stop.</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span> <span class="post-tag tag-link-code" rel="tag" title="see questions tagged &#39;code&#39;">code</span> <span class="post-tag tag-link-issue" rel="tag" title="see questions tagged &#39;issue&#39;">issue</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '14, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/fe7b8b8f82626427d3ae7d5428f2102d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="christenmu&#39;s gravatar image" /><p><span>christenmu</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="christenmu has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Oct '14, 07:01</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-36786" class="comments-container"></div><div id="comment-tools-36786" class="comment-tools"></div><div class="clear"></div><div id="comment-36786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36787"></span>

<div id="answer-container-36787" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36787-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36787-score" class="post-score" title="current number of votes">1</div><span id="post-36787-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The build error is because your Cygwin installation doesn't have the u2d command. You need to install the dos2unix Cygwin package.</p><p>1.10.7 is tagged in git, so clone the Wireshark repo (<code>git clone https://code.wireshark.org/review/wireshark</code>) and then <code>git checkout tags/v1.10.7</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '14, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-36787" class="comments-container"><span id="36799"></span><div id="comment-36799" class="comment"><div id="post-36799-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I managed to build after reinstalled cygwin with dos2unix included. Also, I think I checked out the v1.10.7 with git checkout branch with ver specified to v1.10.7.</p></div><div id="comment-36799-info" class="comment-info"><span class="comment-age">(02 Oct '14, 11:05)</span> <span class="comment-user userinfo">christenmu</span></div></div><span id="36811"></span><div id="comment-36811" class="comment"><div id="post-36811-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-36811-info" class="comment-info"><span class="comment-age">(03 Oct '14, 02:20)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-36787" class="comment-tools"></div><div class="clear"></div><div id="comment-36787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

