+++
type = "question"
title = "Error generate ws.css in VS2013 build of Wireshark 2.0.5"
description = '''Hi, I open wireshark-2.0.5 VS2013 project (ALL_BUILD.vcxproj) and rebuild it in Debug configuration. During the build I receive the following output error message: Generating ws.css 4&amp;gt; Error copying file (if different) from &quot;D:/Development/wireshark/docbook/ws.css&quot; to &quot;D:/Development/wireshark/do...'''
date = "2016-09-18T05:55:00Z"
lastmod = "2016-09-19T04:28:00Z"
weight = 55623
keywords = [ "windows", "build" ]
aliases = [ "/questions/55623" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error generate ws.css in VS2013 build of Wireshark 2.0.5](/questions/55623/error-generate-wscss-in-vs2013-build-of-wireshark-205)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55623-score" class="post-score" title="current number of votes">0</div><span id="post-55623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I open wireshark-2.0.5 VS2013 project (ALL_BUILD.vcxproj) and rebuild it in Debug configuration. During the build I receive the following output error message:</p><pre><code>Generating ws.css
4&gt;  Error copying file (if different) from &quot;D:/Development/wireshark/docbook/ws.css&quot; to &quot;D:/Development/wireshark/docbook/ws.css&quot;.
4&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1.</code></pre><p>How do I solve this issue? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '16, 05:55</strong></p><img src="https://secure.gravatar.com/avatar/cec45aa9ba9dd4c242a57075ce4157af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ITCO&#39;s gravatar image" /><p><span>ITCO</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ITCO has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Sep '16, 08:39</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-55623" class="comments-container"></div><div id="comment-tools-55623" class="comment-tools"></div><div class="clear"></div><div id="comment-55623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55628"></span>

<div id="answer-container-55628" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55628-score" class="post-score" title="current number of votes">0</div><span id="post-55628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The build seems to be attempting to copy the file onto itself. Are you attempting to build in-tree, i.e. in the sources directory? Is so, that isn't supported.</p><p>What was the CMake command line you used?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '16, 08:52</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-55628" class="comments-container"><span id="55629"></span><div id="comment-55629" class="comment"><div id="post-55629-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick answer, I understand the problem and as you've suggested I build the solution in the Wireshark source tree. So I need to build it in another. Thanks.</p></div><div id="comment-55629-info" class="comment-info"><span class="comment-age">(18 Sep '16, 09:46)</span> <span class="comment-user userinfo">ITCO</span></div></div><span id="55630"></span><div id="comment-55630" class="comment"><div id="post-55630-score" class="comment-score"></div><div class="comment-text"><p>Please follow the Developers Guide, Section 2.2.10.2:</p><blockquote>Create and change to the correct build directory. CMake is best used in an out-of-tree build configuration where the build is done in a separate directory to the source tree, leaving the source tree in a pristine state. 32 and 64 bit builds require a separate build directory. Create (if required) and change to the appropriate build directory.</blockquote><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-55630-info" class="comment-info"><span class="comment-age">(18 Sep '16, 09:56)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="55644"></span><div id="comment-55644" class="comment"><div id="post-55644-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>It worked without errors: ========== Rebuild All: 66 succeeded, 0 failed, 13 skipped ========== Thank You, Itamar.</p></div><div id="comment-55644-info" class="comment-info"><span class="comment-age">(19 Sep '16, 04:28)</span> <span class="comment-user userinfo">ITCO</span></div></div></div><div id="comment-tools-55628" class="comment-tools"></div><div class="clear"></div><div id="comment-55628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

