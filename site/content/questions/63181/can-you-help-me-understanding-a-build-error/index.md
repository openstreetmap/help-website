+++
type = "question"
title = "Can you help me understanding a build error?"
description = '''Hi, I&#x27;m just trying to build wireshark on a Windows 10 x64 environment from source code available on the website. I do not modify the source code until now. Folllowing the developer&#x27;s guide, i&#x27;m generating the build file at paragraph 2.2.11. the cmake command line return the following error : -- Fou...'''
date = "2017-07-27T08:57:00Z"
lastmod = "2017-07-28T11:24:00Z"
weight = 63181
keywords = [ "windows", "buiding", "x64", "wireshark" ]
aliases = [ "/questions/63181" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can you help me understanding a build error?](/questions/63181/can-you-help-me-understanding-a-build-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63181-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63181-score" class="post-score" title="current number of votes">0</div><span id="post-63181-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm just trying to build wireshark on a Windows 10 x64 environment from source code available on the website. I do not modify the source code until now.</p><p>Folllowing the developer's guide, i'm generating the build file at paragraph 2.2.11.</p><p>the cmake command line return the following error :</p><pre><code>-- Found SBC: C:/Nicolas/Dev/wireshark-win64-libs/sbc-1.3-win64ws/include
-- SBC FOUND
-- SBC includes: C:/Nicolas/Dev/wireshark-win64-libs/sbc-1.3-win64ws/include
-- SBC libs: C:/Nicolas/Dev/wireshark-win64-libs/sbc-1.3-win64ws/lib/sbc.lib
-- Could NOT find SETCAP (missing: SETCAP_EXECUTABLE)
-- SETCAP NOT FOUND
-- Could NOT find SH (missing: SH_EXECUTABLE)
 CMake Error at cmake/modules/FindSH.cmake:29 (message):
  The bash executable (SH_EXECUTABLE-NOTFOUND) isn&#39;t from Cygwin.  Check your
  path
 Call Stack (most recent call first):
  CMakeLists.txt:982 (find_package)-- Found SBC: C:/Nicolas/Dev/wireshark-win64-libs/sbc-1.3-win64ws/include
-- SBC FOUND
-- SBC includes: C:/Nicolas/Dev/wireshark-win64-libs/sbc-1.3-win64ws/include
-- SBC libs: C:/Nicolas/Dev/wireshark-win64-libs/sbc-1.3-win64ws/lib/sbc.lib
-- Could NOT find SETCAP (missing: SETCAP_EXECUTABLE)
-- SETCAP NOT FOUND
-- Could NOT find SH (missing: SH_EXECUTABLE)
 CMake Error at cmake/modules/FindSH.cmake:29 (message):
  The bash executable (SH_EXECUTABLE-NOTFOUND) isn&#39;t from Cygwin.  Check your
  path
 Call Stack (most recent call first):
  CMakeLists.txt:982 (find_package)</code></pre><p>What can generate this error ? What are SETCAP and SH and what do i need to do to correct this error ?</p><p>Thank you for your help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-buiding" rel="tag" title="see questions tagged &#39;buiding&#39;">buiding</span> <span class="post-tag tag-link-x64" rel="tag" title="see questions tagged &#39;x64&#39;">x64</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '17, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/c1fb855837d58eacd2cb682f4e52fd76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob17136&#39;s gravatar image" /><p><span>Bob17136</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob17136 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jul '17, 12:11</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-63181" class="comments-container"></div><div id="comment-tools-63181" class="comment-tools"></div><div class="clear"></div><div id="comment-63181-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63182"></span>

<div id="answer-container-63182" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63182-score" class="post-score" title="current number of votes">0</div><span id="post-63182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Presumably you installed CMake 3.9 (that was just released) and we have an issue with this version related to cygwin path discovery that we need to investigate.</p><p>In the meantime install CMake 3.8.2. It should fix your error (do not forget to clean your cmake build folder first).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '17, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-63182" class="comments-container"><span id="63220"></span><div id="comment-63220" class="comment"><div id="post-63220-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>You're right, cmake 3.9 was installed by default.</p><p>I uninstall it and install cmake 3.8.2.</p><p>Buildins is OK now ! Thank you very much.</p></div><div id="comment-63220-info" class="comment-info"><span class="comment-age">(28 Jul '17, 11:09)</span> <span class="comment-user userinfo">Bob17136</span></div></div><span id="63221"></span><div id="comment-63221" class="comment"><div id="post-63221-score" class="comment-score"></div><div class="comment-text"><p>I've converted your post from an Answer (which it clearly wasn't) to a Comment to Pascal's Answer.</p><p>Please accept Pascal's Answer as the correct one (by clicking the checkmark icon next to it) as doing so marks your Question as usefully answered, helping others who might be interested in the same. No one else that the author of the Question can do that.</p></div><div id="comment-63221-info" class="comment-info"><span class="comment-age">(28 Jul '17, 11:24)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-63182" class="comment-tools"></div><div class="clear"></div><div id="comment-63182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

