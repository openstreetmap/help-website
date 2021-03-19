+++
type = "question"
title = "Cannot build Wireshark installer for Win10 (Visual Studio 2013)"
description = '''Hi, When trying to follow the next step for Win64 (Windows10, VS 2013)  2.2.15. Optional: Create a Wireshark Installer (from 2.2. Win32/64: Step-by-Step Guide)  I am experiencing the following error:  MSBUILD : error MSB1009: Project file does not exist.  Switch: nsis_package_prep.vcxproj Can you pl...'''
date = "2016-07-07T00:42:00Z"
lastmod = "2016-07-07T04:25:00Z"
weight = 53880
keywords = [ "nsis", "vs2013", "win64" ]
aliases = [ "/questions/53880" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Cannot build Wireshark installer for Win10 (Visual Studio 2013)](/questions/53880/cannot-build-wireshark-installer-for-win10-visual-studio-2013)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53880-score" class="post-score" title="current number of votes">0</div><span id="post-53880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, When trying to follow the next step for Win64 (Windows10, VS 2013) <strong>2.2.15. Optional: Create a Wireshark Installer (from 2.2. Win32/64: Step-by-Step Guide)</strong> I am experiencing the following error: MSBUILD : error MSB1009: Project file does not exist. Switch: nsis_package_prep.vcxproj Can you please help? Thanks, Bella</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nsis" rel="tag" title="see questions tagged &#39;nsis&#39;">nsis</span> <span class="post-tag tag-link-vs2013" rel="tag" title="see questions tagged &#39;vs2013&#39;">vs2013</span> <span class="post-tag tag-link-win64" rel="tag" title="see questions tagged &#39;win64&#39;">win64</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '16, 00:42</strong></p><img src="https://secure.gravatar.com/avatar/9e15553cdb8784b68cd492baaa00e5c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BellaS&#39;s gravatar image" /><p><span>BellaS</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BellaS has no accepted answers">0%</span></p></div></div><div id="comments-container-53880" class="comments-container"></div><div id="comment-tools-53880" class="comment-tools"></div><div class="clear"></div><div id="comment-53880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53890"></span>

<div id="answer-container-53890" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53890-score" class="post-score" title="current number of votes">2</div><span id="post-53890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="BellaS has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think there's a note missing from the Developers Guide. If you installed nsis <strong>after</strong> generating the configuration using CMake, then CMake won't have created the nsis projects as nsis wasn't around at the time.</p><p>Try re-running your CMake generation step.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '16, 03:13</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53890" class="comments-container"><span id="53894"></span><div id="comment-53894" class="comment"><div id="post-53894-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much! Works perfect now :)</p></div><div id="comment-53894-info" class="comment-info"><span class="comment-age">(07 Jul '16, 03:49)</span> <span class="comment-user userinfo">BellaS</span></div></div><span id="53897"></span><div id="comment-53897" class="comment"><div id="post-53897-score" class="comment-score">1</div><div class="comment-text"><p><span>@Bellas</span></p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-53897-info" class="comment-info"><span class="comment-age">(07 Jul '16, 04:22)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="53898"></span><div id="comment-53898" class="comment"><div id="post-53898-score" class="comment-score"></div><div class="comment-text"><p>Done, thank you</p></div><div id="comment-53898-info" class="comment-info"><span class="comment-age">(07 Jul '16, 04:25)</span> <span class="comment-user userinfo">BellaS</span></div></div></div><div id="comment-tools-53890" class="comment-tools"></div><div class="clear"></div><div id="comment-53890-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

