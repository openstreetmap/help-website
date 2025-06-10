+++
type = "question"
title = "Question about referencing Historic US Routes."
description = '''I would like to tag all officially recognized or signed US Highways as the following: ref=Hist US XX or ref=US XX Hist The reason being it would show up on the main map. I&#x27;m refraining from doing so for the most part in fear it might be against the guidelines and rules. That&#x27;s why I&#x27;m asking here if...'''
date = "2018-10-04T01:45:00Z"
lastmod = "2018-10-10T08:37:00Z"
weight = 66149
keywords = [ "route", "historic", "ref" ]
aliases = [ "/questions/66149" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Question about referencing Historic US Routes.](/questions/66149/question-about-referencing-historic-us-routes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66149-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66149-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66149-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to tag all officially recognized or signed US Highways as the following:<br />
<strong>ref=Hist US XX</strong> or <strong>ref=US XX Hist</strong><br />
The reason being it would show up on the main map. I'm refraining from doing so for the most part in fear it might be against the guidelines and rules. That's why I'm asking here if I can have permission to do this? Thank you in advance for any answer, yes or no.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-historic" rel="tag" title="see questions tagged &#39;historic&#39;">historic</span> <span class="post-tag tag-link-ref" rel="tag" title="see questions tagged &#39;ref&#39;">ref</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '18, 01:45</strong></p>
<img src="https://secure.gravatar.com/avatar/2886620a210afb37a1979495f990d121?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MatthewAndersonUS80&#39;s gravatar image" />
<p><span>MatthewAnder...</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MatthewAndersonUS80 has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-66149" class="comments-container">
&#10;</div>
<div id="comment-tools-66149" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66149-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="66151"></span>

<div id="answer-container-66151" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66151-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MatthewAndersonUS80 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Bad idea. Two main reasons the first being that ref is for the current reference not a historical one. Second one is that there are already ways to tag those and I've seen it used in my area for historic US-66, US-99, US-101 and US-80.</p>
<p>For instance, in the Claremont/Pomona area of the greater LA metroplex Foothill Boulevard has:</p>
<pre><code>ref=&quot;CA 66&quot;
old_ref=&quot;US 66 (Old US 99)&quot;</code></pre>
<p>East of San Diego I see an section of what was once US 80 with the following tags:</p>
<pre><code>ref=&quot;S1&quot;
old_ref=&quot;US 80&quot;
name=&quot;Old Highway 80&quot;</code></pre>
<p>Please don't override a current state highway reference like "CA 66" or county highway reference like "S1" with incorrect data so that "it would show up on the main map". That is vandalism at worst and "tagging for the renderer" at best, neither of which are considered good things in OSM.</p>
<p>But if you want a map that shows the historic route segments (where they still exist) it looks like you can render a map that uses the old_ref= <em>tags in preference to the ref=</em> tags where they exist.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '18, 03:26</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-66151" class="comments-container">
<span id="66152"></span>
<div id="comment-66152" class="comment">
<div id="post-66152-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the reply. I'm glad I asked before doing that.</p>
<p>Also, how can I render a map like that? I've been trying to find ways to do it for a good while now.</p>
</div>
<div id="comment-66152-info" class="comment-info">
<span class="comment-age">(04 Oct '18, 03:51)</span> <span class="comment-user userinfo">MatthewAnder...</span>
</div>
</div>
<span id="66153"></span>
<div id="comment-66153" class="comment">
<div id="post-66153-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am not the best to recommend how to render your own map as my one effort in that was back when mapnik and mapnik XML was the only real option. From what I've read, there are apparently a number of ways to approach that now but I don't know the relative merits or difficulty or even all the possibilities.</p>
</div>
<div id="comment-66153-info" class="comment-info">
<span class="comment-age">(04 Oct '18, 03:58)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="66192"></span>
<div id="comment-66192" class="comment">
<div id="post-66192-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>US Historic routes are still signed routes, just of a recreational nature. ref=US Historic XX is perfectly valid (though I'd put it at the end of the ref tag, and consider the ref tag to be obsolete).</p>
</div>
<div id="comment-66192-info" class="comment-info">
<span class="comment-age">(06 Oct '18, 15:47)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="66260"></span>
<div id="comment-66260" class="comment">
<div id="post-66260-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Re "how can I render a map like that?" the easiest way is probably to manipulate the tags in a lua script and use a map style of your choice (such as the standard one).</p>
<p>That way, the map style just sees a "ref" tag - it doesn't realise that it was originally something like "old_ref". An example snippet of lua to "pretend something is something else" is <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/style.lua#L1056">here</a>.</p>
</div>
<div id="comment-66260-info" class="comment-info">
<span class="comment-age">(10 Oct '18, 08:37)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66151" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66151-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

