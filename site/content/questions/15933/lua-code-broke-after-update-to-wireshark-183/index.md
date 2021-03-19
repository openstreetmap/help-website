+++
type = "question"
title = "Lua code broke after update to wireshark 1.8.3"
description = '''http://code.google.com/p/packet-bnetp/issues/detail?id=5 This code worked fine on wireshark 1.4.4 but crashes wireshark after update to 1.8.3.  How to fix it? Why the heck wireshark compelety crashes? Doesn&#x27;t it walidate calls from lua wrapper? It should be too &quot;thin&quot; wrapper. '''
date = "2012-11-15T11:49:00Z"
lastmod = "2012-11-16T13:33:00Z"
weight = 15933
keywords = [ "lua", "crash" ]
aliases = [ "/questions/15933" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Lua code broke after update to wireshark 1.8.3](/questions/15933/lua-code-broke-after-update-to-wireshark-183)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15933-score" class="post-score" title="current number of votes">-3</div><span id="post-15933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><a href="http://code.google.com/p/packet-bnetp/issues/detail?id=5">http://code.google.com/p/packet-bnetp/issues/detail?id=5</a></p><p>This code worked fine on wireshark 1.4.4 but crashes wireshark after update to 1.8.3.</p><ol><li>How to fix it?</li><li>Why the heck wireshark compelety crashes? Doesn't it walidate calls from lua wrapper? It should be too "thin" wrapper.</li></ol></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Nov '12, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/a00c8faaeb8a556d49ded6b3aa1eb51e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xpeh&#39;s gravatar image" /><p><span>xpeh</span><br />
<span class="score" title="-3 reputation points">-3</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xpeh has no accepted answers">0%</span></p></div></div><div id="comments-container-15933" class="comments-container"><span id="15937"></span><div id="comment-15937" class="comment"><div id="post-15937-score" class="comment-score">2</div><div class="comment-text"><p>Nice comment you made on the issue you linked to.</p><p>Wireshark is GPL and the source is freely available for modification and improvement by anyone. Patches for the issue would be gratefully accepted.</p></div><div id="comment-15937-info" class="comment-info"><span class="comment-age">(15 Nov '12, 12:43)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="15940"></span><div id="comment-15940" class="comment"><div id="post-15940-score" class="comment-score"></div><div class="comment-text"><p>GPL is neiter a quality sign nor an attibute of open development. But if you invented it, you may grow beart, stomach and eat dirt from feet.</p><p>Breaking API is bad. Crashing because of function call is bad too. I don't know how it's in C, but in high-level languages it have to be avoided.</p></div><div id="comment-15940-info" class="comment-info"><span class="comment-age">(15 Nov '12, 12:59)</span> <span class="comment-user userinfo">xpeh</span></div></div><span id="15985"></span><div id="comment-15985" class="comment"><div id="post-15985-score" class="comment-score"></div><div class="comment-text"><p>grahamb, you are funny. I don't want to patch an issue which [b]wireshark[/b] caused without any good reason, [b]wireshark team[/b] has to patch it. It's their fault, not ours. Our plugin worked.</p></div><div id="comment-15985-info" class="comment-info"><span class="comment-age">(16 Nov '12, 13:33)</span> <span class="comment-user userinfo">xpeh</span></div></div></div><div id="comment-tools-15933" class="comment-tools"></div><div class="clear"></div><div id="comment-15933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15945"></span>

<div id="answer-container-15945" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15945-score" class="post-score" title="current number of votes">0</div><span id="post-15945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like you also opened a <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7976">bug 7976</a> for this. Suggest sending followups there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Nov '12, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-15945" class="comments-container"></div><div id="comment-tools-15945" class="comment-tools"></div><div class="clear"></div><div id="comment-15945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

