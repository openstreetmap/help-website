+++
type = "question"
title = "Download Libwireshark.dll FIle"
description = '''Hi, I&#x27;m unable to find the libwireshark.dll. I want to wrtie a C# program that can access the wireshark bluetooth data from kismet in windows'''
date = "2014-09-26T00:41:00Z"
lastmod = "2014-09-26T02:31:00Z"
weight = 36623
keywords = [ "c#", "libwireshark", "library", "wireshark" ]
aliases = [ "/questions/36623" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Download Libwireshark.dll FIle](/questions/36623/download-libwiresharkdll-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36623-score" class="post-score" title="current number of votes">0</div><span id="post-36623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm unable to find the libwireshark.dll.</p><p>I want to wrtie a C# program that can access the wireshark bluetooth data from kismet in windows</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-c#" rel="tag" title="see questions tagged &#39;c#&#39;">c#</span> <span class="post-tag tag-link-libwireshark" rel="tag" title="see questions tagged &#39;libwireshark&#39;">libwireshark</span> <span class="post-tag tag-link-library" rel="tag" title="see questions tagged &#39;library&#39;">library</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '14, 00:41</strong></p><img src="https://secure.gravatar.com/avatar/d1fba3d75c7af8dc47876eede9fb1191?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erarijit&#39;s gravatar image" /><p><span>erarijit</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erarijit has no accepted answers">0%</span></p></div></div><div id="comments-container-36623" class="comments-container"></div><div id="comment-tools-36623" class="comment-tools"></div><div class="clear"></div><div id="comment-36623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="36628"></span>

<div id="answer-container-36628" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36628-score" class="post-score" title="current number of votes">1</div><span id="post-36628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="erarijit has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think it's available on its own, only as part of a Wireshark installer, so grab one of those and install Wireshark.</p><p>Note that using libwireshark outside of Wireshark itself is quite a tricky task as it's not the intended role of the dll.</p><p>Also note that libwireshark is mainly for parsing data, it doesn't capture data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '14, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-36628" class="comments-container"><span id="36629"></span><div id="comment-36629" class="comment"><div id="post-36629-score" class="comment-score"></div><div class="comment-text"><p>Hi Thanks,</p><p>for the response, I want to parse data itself already grabbed, do you have any example for the same?</p></div><div id="comment-36629-info" class="comment-info"><span class="comment-age">(26 Sep '14, 02:12)</span> <span class="comment-user userinfo">erarijit</span></div></div><span id="36631"></span><div id="comment-36631" class="comment"><div id="post-36631-score" class="comment-score"></div><div class="comment-text"><p>There's nothing I know of in the Wireshark community as all those folks use Wireshark, not libwireshark. Looks like you'll have to search elsewhere.</p></div><div id="comment-36631-info" class="comment-info"><span class="comment-age">(26 Sep '14, 02:31)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-36628" class="comment-tools"></div><div class="clear"></div><div id="comment-36628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36627"></span>

<div id="answer-container-36627" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36627-score" class="post-score" title="current number of votes">1</div><span id="post-36627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You will have to download the installer and instal Wireshark then you can copy the dll from the install directory. I have no idea if the .dll is usable stand alone or not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '14, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-36627" class="comments-container"><span id="36630"></span><div id="comment-36630" class="comment"><div id="post-36630-score" class="comment-score"></div><div class="comment-text"><p>Hi Thanks,</p><p>for the response, I want to parse data itself already grabbed, do you have any example for the same?</p></div><div id="comment-36630-info" class="comment-info"><span class="comment-age">(26 Sep '14, 02:12)</span> <span class="comment-user userinfo">erarijit</span></div></div></div><div id="comment-tools-36627" class="comment-tools"></div><div class="clear"></div><div id="comment-36627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

