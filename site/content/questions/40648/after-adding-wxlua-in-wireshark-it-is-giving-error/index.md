+++
type = "question"
title = "After adding wxlua in wireshark it is giving error"
description = '''When i have copied wx.dll and lua5.2.dll and lua52.dll in wireshark folder and then i have tried to evaluate simple wxlua syntax require(&quot;wx&quot;). it is giving me error like this  How to fix this error how i can successfully integrate wxlua with wireshark??'''
date = "2015-03-18T02:48:00Z"
lastmod = "2015-03-23T11:44:00Z"
weight = 40648
keywords = [ "lua", "wireshark" ]
aliases = [ "/questions/40648" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [After adding wxlua in wireshark it is giving error](/questions/40648/after-adding-wxlua-in-wireshark-it-is-giving-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40648-score" class="post-score" title="current number of votes">0</div><span id="post-40648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When i have copied wx.dll and lua5.2.dll and lua52.dll in wireshark folder and then i have tried to evaluate simple wxlua syntax require("wx"). it is giving me error like this <img src="https://osqa-ask.wireshark.org/upfiles/wxlua_qsWLWuB.png" alt="alt text" /></p><p>How to fix this error how i can successfully integrate wxlua with wireshark??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Mar '15, 02:48</strong></p><img src="https://secure.gravatar.com/avatar/8efce51fbbf3dbd6c9b9132056f45eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankit&#39;s gravatar image" /><p><span>ankit</span><br />
<span class="score" title="65 reputation points">65</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankit has one accepted answer">25%</span></p></img></div></div><div id="comments-container-40648" class="comments-container"></div><div id="comment-tools-40648" class="comment-tools"></div><div class="clear"></div><div id="comment-40648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40650"></span>

<div id="answer-container-40650" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40650-score" class="post-score" title="current number of votes">0</div><span id="post-40650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That type of error is sometimes due to a 32\64 bit mismatch. Are you sure that Wireshark and wxLua are the same architecture?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Mar '15, 03:41</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-40650" class="comments-container"><span id="40770"></span><div id="comment-40770" class="comment"><div id="post-40770-score" class="comment-score"></div><div class="comment-text"><p>I am using wireshark version 1.12.4 and wxlua is 2.8.12.3 which is I think follows under same architecture. The problem occurs only in 64 bit version only. When I have tried same exercise in 32 bit wireshark version it was running perfectly</p></div><div id="comment-40770-info" class="comment-info"><span class="comment-age">(22 Mar '15, 20:10)</span> <span class="comment-user userinfo">ankit</span></div></div><span id="40787"></span><div id="comment-40787" class="comment"><div id="post-40787-score" class="comment-score"></div><div class="comment-text"><p>From your results and the lack of an explicit 64 bit version in the wxLua downloads directory I suspect that you do have a 32 bit version of wxLua which won't run with 64 bit Wireshark.</p><p>It would seem that if you must use 64 bit Wireshark and want wxLua, you'll need to build your own 64 bit version of wxLua.</p><p>Note that this really isn't a Wireshark issue, more a wxLua issue.</p></div><div id="comment-40787-info" class="comment-info"><span class="comment-age">(23 Mar '15, 11:44)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-40650" class="comment-tools"></div><div class="clear"></div><div id="comment-40650-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

