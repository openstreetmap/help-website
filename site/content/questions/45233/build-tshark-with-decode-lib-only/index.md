+++
type = "question"
title = "Build tshark with decode lib only"
description = '''Hi. What options should be used with ./configure to build only console tool (tshark)? Tshark should be able to decode captured packets?'''
date = "2015-08-19T02:59:00Z"
lastmod = "2015-08-19T14:50:00Z"
weight = 45233
keywords = [ "tshark" ]
aliases = [ "/questions/45233" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Build tshark with decode lib only](/questions/45233/build-tshark-with-decode-lib-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45233-score" class="post-score" title="current number of votes">0</div><span id="post-45233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. What options should be used with ./configure to build only console tool (tshark)? Tshark should be able to decode captured packets?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '15, 02:59</strong></p><img src="https://secure.gravatar.com/avatar/4bb5f53b35c799847b0c7415f270ff02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="insekt&#39;s gravatar image" /><p><span>insekt</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="insekt has no accepted answers">0%</span></p></div></div><div id="comments-container-45233" class="comments-container"></div><div id="comment-tools-45233" class="comment-tools"></div><div class="clear"></div><div id="comment-45233-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="45234"></span>

<div id="answer-container-45234" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45234-score" class="post-score" title="current number of votes">1</div><span id="post-45234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Run <code>./configure --help</code> to get all relevant options for your build. In your case, specifically look at options like <code>--disable-wireshark</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '15, 03:48</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-45234" class="comments-container"><span id="45235"></span><div id="comment-45235" class="comment"><div id="post-45235-score" class="comment-score"></div><div class="comment-text"><p>Already looked at it. A lot of options but poor descriptions =( Have to dig into sources to understand, don't want to spent too much time on it. Thought code maintainers can help.</p></div><div id="comment-45235-info" class="comment-info"><span class="comment-age">(19 Aug '15, 03:52)</span> <span class="comment-user userinfo">insekt</span></div></div><span id="45244"></span><div id="comment-45244" class="comment"><div id="post-45244-score" class="comment-score"></div><div class="comment-text"><p>If you expect more help, you should be able to at least provide the steps you've taken so far and your current results. With so little information provided, what do you really expect?</p><p>As for the descriptions of <code>configure --help</code> options, I think they are rather good and for the most part, self-explanatory. If you're having trouble understanding some, then maybe you could inquire about specific options that are causing you confusion. Surely you're not confused by all of them?</p><p><em>don't want to spent too much time on it.</em> Well, if you don't want to spend too much time on it, why should anyone else want to? To quote Jerry Maguire, <em>"Help me [us] help you"</em>.</p></div><div id="comment-45244-info" class="comment-info"><span class="comment-age">(19 Aug '15, 10:03)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-45234" class="comment-tools"></div><div class="clear"></div><div id="comment-45234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45253"></span>

<div id="answer-container-45253" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45253-score" class="post-score" title="current number of votes">0</div><span id="post-45253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, here's a simpler answer:</p><pre><code>./configure --disable-wireshark</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '15, 14:50</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-45253" class="comments-container"></div><div id="comment-tools-45253" class="comment-tools"></div><div class="clear"></div><div id="comment-45253-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

