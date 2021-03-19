+++
type = "question"
title = "How to change wireshark temp files&#x27; directory"
description = '''I want to change wireshark &quot;.pcapng&quot; temp files&#x27; directory, how to config or where to modify the source code?'''
date = "2014-01-20T17:09:00Z"
lastmod = "2014-01-21T01:15:00Z"
weight = 29036
keywords = [ "files", "directory", "temp", "wireshark" ]
aliases = [ "/questions/29036" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to change wireshark temp files' directory](/questions/29036/how-to-change-wireshark-temp-files-directory)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29036-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29036-score" class="post-score" title="current number of votes">0</div><span id="post-29036-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to change wireshark ".pcapng" temp files' directory, how to config or where to modify the source code?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-files" rel="tag" title="see questions tagged &#39;files&#39;">files</span> <span class="post-tag tag-link-directory" rel="tag" title="see questions tagged &#39;directory&#39;">directory</span> <span class="post-tag tag-link-temp" rel="tag" title="see questions tagged &#39;temp&#39;">temp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '14, 17:09</strong></p><img src="https://secure.gravatar.com/avatar/13679628c84abac93be65773340d2589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="metamatrix&#39;s gravatar image" /><p><span>metamatrix</span><br />
<span class="score" title="56 reputation points">56</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="metamatrix has one accepted answer">100%</span></p></div></div><div id="comments-container-29036" class="comments-container"></div><div id="comment-tools-29036" class="comment-tools"></div><div class="clear"></div><div id="comment-29036-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29037"></span>

<div id="answer-container-29037" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29037-score" class="post-score" title="current number of votes">1</div><span id="post-29037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="metamatrix has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Presumably you mean the directory in which it writes temporary capture files.</p><p>On UN*X, you can set the TMPDIR environment variable to the directory you want the temporary files (which may be difficult if you're launching it from the GUI rather than the command line); on Windows, you can set the TEMP environment variable.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '14, 17:39</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-29037" class="comments-container"><span id="29042"></span><div id="comment-29042" class="comment"><div id="post-29042-score" class="comment-score"></div><div class="comment-text"><p>I need only wireshark temp files to write in user config directory, without modifying the system temp directory. How to do?</p></div><div id="comment-29042-info" class="comment-info"><span class="comment-age">(20 Jan '14, 21:09)</span> <span class="comment-user userinfo">metamatrix</span></div></div><span id="29045"></span><div id="comment-29045" class="comment"><div id="post-29045-score" class="comment-score"></div><div class="comment-text"><p>Modify the source code by changing the <code>create_tempfile()</code> routine to use a different directory.</p></div><div id="comment-29045-info" class="comment-info"><span class="comment-age">(20 Jan '14, 23:42)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="29047"></span><div id="comment-29047" class="comment"><div id="post-29047-score" class="comment-score"></div><div class="comment-text"><p>Just create a batch file that sets "temp" to whatever you need and runs Wireshark afterwards. That will get you a temporary "temp" path that will be discarded as soon as Wireshark exits. Much easier than a code change :)</p></div><div id="comment-29047-info" class="comment-info"><span class="comment-age">(21 Jan '14, 01:15)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-29037" class="comment-tools"></div><div class="clear"></div><div id="comment-29037-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

