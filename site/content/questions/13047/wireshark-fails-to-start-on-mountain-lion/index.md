+++
type = "question"
title = "Wireshark fails to start on Mountain Lion"
description = '''I get the following when I try and run wireshark after running xquartz: bash-3.2$ /Applications/Wireshark.app/Contents/MacOS/Wireshark dyld: Symbol not found: _iconv  Referenced from: /usr/lib/libcups.2.dylib  Expected in: /Applications/Wireshark.app/Contents/Resources/lib/libiconv.2.dylib  in /usr/...'''
date = "2012-07-26T21:07:00Z"
lastmod = "2012-09-13T11:52:00Z"
weight = 13047
keywords = [ "mountainlion" ]
aliases = [ "/questions/13047" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark fails to start on Mountain Lion](/questions/13047/wireshark-fails-to-start-on-mountain-lion)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13047-score" class="post-score" title="current number of votes">0</div><span id="post-13047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I get the following when I try and run wireshark after running xquartz:</p><p>bash-3.2$ /Applications/Wireshark.app/Contents/MacOS/Wireshark dyld: Symbol not found: _iconv Referenced from: /usr/lib/libcups.2.dylib Expected in: /Applications/Wireshark.app/Contents/Resources/lib/libiconv.2.dylib in /usr/lib/libcups.2.dylib bash-3.2$</p><p>Any takers??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mountainlion" rel="tag" title="see questions tagged &#39;mountainlion&#39;">mountainlion</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '12, 21:07</strong></p><img src="https://secure.gravatar.com/avatar/e5a241194af8593cc5a5a3e030aff832?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thebruge&#39;s gravatar image" /><p><span>thebruge</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thebruge has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted <strong>13 Sep '12, 11:47</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-13047" class="comments-container"></div><div id="comment-tools-13047" class="comment-tools"></div><div class="clear"></div><div id="comment-13047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14249"></span>

<div id="answer-container-14249" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14249-score" class="post-score" title="current number of votes">0</div><span id="post-14249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What version of Wireshark is that? I installed 1.8.2 on a Mountain Lion (virtual) machine, and it doesn't <em>have</em> <code>/Applications/Wireshark.app/Contents/Resources/lib/libiconv.2.dylib</code>. Mountain Lion <em>does</em> have <code>/usr/lib/libiconv.2.dylib</code> and, at least according to <code>otool -L /usr/lib/libcups.2.dylib</code>, that's where libcups expects to find <code>iconv</code>.</p><p>Try dragging Wireshark to the Trash and re-installing the Snow Leopard 64-bit version (rather than the Leopard 32-bit version; as you're running Mountain Lion, you have a 64-bit machine).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '12, 11:52</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-14249" class="comments-container"></div><div id="comment-tools-14249" class="comment-tools"></div><div class="clear"></div><div id="comment-14249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

