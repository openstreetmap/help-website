+++
type = "question"
title = "&quot;Acid test&quot; capture file for new builds?"
description = '''I&#x27;m building Wireshark 1.4.1 on a new platform, and I&#x27;m wondering if there&#x27;s any sort of &quot;test capture&quot; file that exercises the base dissectors (or some particular subset thereof) as a &quot;build test&quot; sort of thing.  I&#x27;ve thought of using the various sample captures, but I suspect that something better...'''
date = "2010-11-14T19:25:00Z"
lastmod = "2010-11-15T11:57:00Z"
weight = 942
keywords = [ "testing", "build" ]
aliases = [ "/questions/942" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# ["Acid test" capture file for new builds?](/questions/942/acid-test-capture-file-for-new-builds)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-942-score" class="post-score" title="current number of votes">0</div><span id="post-942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm building Wireshark 1.4.1 on a new platform, and I'm wondering if there's any sort of "test capture" file that exercises the base dissectors (or some particular subset thereof) as a "build test" sort of thing.<br />
</p><p>I've thought of using the various sample captures, but I suspect that something better is "out there"...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-testing" rel="tag" title="see questions tagged &#39;testing&#39;">testing</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '10, 19:25</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Nov '10, 19:26</strong> </span></p></div></div><div id="comments-container-942" class="comments-container"></div><div id="comment-tools-942" class="comment-tools"></div><div class="clear"></div><div id="comment-942-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="953"></span>

<div id="answer-container-953" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-953-score" class="post-score" title="current number of votes">1</div><span id="post-953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wesmorgan1 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The way it's currently done is a whole bunch of collected captures, mangled through fuzz-test.sh and feed to the build. That shakes out bugs real nice. You can find the script in the tools directory of the source. Sample captures can be found on the Wiki, and from other sources mentioned there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '10, 23:07</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-953" class="comments-container"><span id="960"></span><div id="comment-960" class="comment"><div id="post-960-score" class="comment-score"></div><div class="comment-text"><p>Excellent! Now testing build against generic Big Honking Captures...thanks!</p></div><div id="comment-960-info" class="comment-info"><span class="comment-age">(15 Nov '10, 11:57)</span> <span class="comment-user userinfo">wesmorgan1</span></div></div></div><div id="comment-tools-953" class="comment-tools"></div><div class="clear"></div><div id="comment-953-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

