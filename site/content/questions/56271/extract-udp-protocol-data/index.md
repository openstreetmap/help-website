+++
type = "question"
title = "Extract UDP protocol data"
description = '''Hello, on my ethernet port i am receving UDP data, i wanted to extract/captured that data and want to use for some other application. Can anyone guide me how to extrack string of UDP data, in detail. '''
date = "2016-10-09T22:06:00Z"
lastmod = "2016-10-10T06:19:00Z"
weight = 56271
keywords = [ "damaniaa" ]
aliases = [ "/questions/56271" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract UDP protocol data](/questions/56271/extract-udp-protocol-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56271-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56271-score" class="post-score" title="current number of votes">0</div><span id="post-56271-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>on my ethernet port i am receving UDP data, i wanted to extract/captured that data and want to use for some other application.</p><p>Can anyone guide me how to extrack string of UDP data, in detail.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-damaniaa" rel="tag" title="see questions tagged &#39;damaniaa&#39;">damaniaa</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '16, 22:06</strong></p><img src="https://secure.gravatar.com/avatar/05adc6a546b937f54f8cfe46c5a25346?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="damaniaa&#39;s gravatar image" /><p><span>damaniaa</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="damaniaa has no accepted answers">0%</span></p></div></div><div id="comments-container-56271" class="comments-container"></div><div id="comment-tools-56271" class="comment-tools"></div><div class="clear"></div><div id="comment-56271-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56275"></span>

<div id="answer-container-56275" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56275-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56275-score" class="post-score" title="current number of votes">0</div><span id="post-56275-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><pre><code># cat &lt; /dev/udp/127.0.0.1/&lt;port&gt; | &lt;other application&gt;</code></pre><p>This is for a Bash prompt. Otherwise you'll need to give more context.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '16, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-56275" class="comments-container"><span id="56276"></span><div id="comment-56276" class="comment"><div id="post-56276-score" class="comment-score"></div><div class="comment-text"><p>hi, thanks for your answer. but i couldnt understood your solution</p></div><div id="comment-56276-info" class="comment-info"><span class="comment-age">(10 Oct '16, 03:12)</span> <span class="comment-user userinfo">damaniaa</span></div></div><span id="56279"></span><div id="comment-56279" class="comment"><div id="post-56279-score" class="comment-score"></div><div class="comment-text"><p>The reason might be because your question itself is hard to understand. You haven't specified what exactly you want to do with the data, whether you mean a particular UDP stream or any UDP packet which happens to arrive to your network card..., so <span>@Jaap</span> has given you a correct answer which may, however, be useless for your purpose.</p><p>The part to the left from the <code>|</code> sign converts the payload of the UDP packets into a byte stream, and if the application to the right can read binary streams on its <code>STDIN</code>, it can read that stream. And it works on Linux and possibly also OS X.</p><p>If you wanted something else, say it clearly.</p></div><div id="comment-56279-info" class="comment-info"><span class="comment-age">(10 Oct '16, 04:32)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="56280"></span><div id="comment-56280" class="comment"><div id="post-56280-score" class="comment-score"></div><div class="comment-text"><p>My answer was just bait; correct, but likely useless. As <span>@sindy</span> said: specify your setup, in detail, so there can be guidance, in detail.</p></div><div id="comment-56280-info" class="comment-info"><span class="comment-age">(10 Oct '16, 06:19)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-56275" class="comment-tools"></div><div class="clear"></div><div id="comment-56275-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

