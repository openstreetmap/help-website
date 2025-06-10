+++
type = "question"
title = "Find the boundary streets of a suburb"
description = '''A simple query can find the streets inside the boundary of a suburb. [out:csv(&quot;name&quot;;false)] [bbox:-33.9480172,151.1107534,-33.8594833,151.2207935]; area[name=&quot;Beaconsfield&quot;]; way(area)[highway][name]; out; Beaconsfield Lane, Collins Street, Connolly Lane, McConville Lane, O&#x27;Connor Lane, Queen Stree...'''
date = "2020-08-28T14:15:00Z"
lastmod = "2020-08-29T09:48:00Z"
weight = 76339
keywords = [ "suburbs", "boundary", "streets", "boundary_streets" ]
aliases = [ "/questions/76339" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Find the boundary streets of a suburb](/questions/76339/find-the-boundary-streets-of-a-suburb)

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
<span id="post-76339-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76339-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76339-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A simple query can find the streets inside the boundary of a suburb.</p>
<p>[out:csv("name";false)] [bbox:-33.9480172,151.1107534,-33.8594833,151.2207935]; area[name="Beaconsfield"]; way(area)[highway][name]; out;</p>
<p>Beaconsfield Lane, Collins Street, Connolly Lane, McConville Lane, O'Connor Lane, Queen Street, Reserve Street, Victoria Lane, Victoria Street</p>
<p>In areas (cities) with multiple suburbs, the boundaries are usually streets and these are not included in queries for finding streets in suburbs. Their presence may be only visible by looking at a map or making a query via a bounding box or by making a boundary query as below.</p>
<p>Such streets can thus be listed in queries such as: [out:json][timeout:25] [bbox:-33.9480172,151.1107534,-33.8594833,151.2207935]; rel[name=Beaconsfield]; (._;&gt;;); out;</p>
<p>The streets are readily extracted from the complex output with a simple bash script. However, how can the above Overpass query be modifed/extended/replaced to just supply the streets on the boundary of the suburb without resorting to bash scripts? - Beaconsfield Street, Botany Road, Johnson Street, O'Riordan Street, Reserve Street, William Street</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-suburbs" rel="tag" title="see questions tagged &#39;suburbs&#39;">suburbs</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-streets" rel="tag" title="see questions tagged &#39;streets&#39;">streets</span> <span class="post-tag tag-link-boundary_streets" rel="tag" title="see questions tagged &#39;boundary_streets&#39;">boundary_streets</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Aug '20, 14:15</strong></p>
<img src="https://secure.gravatar.com/avatar/c5e89b8b037b23165056f8722eb83dd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorylila&#39;s gravatar image" />
<p><span>rorylila</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorylila has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76339" class="comments-container">
<span id="76342"></span>
<div id="comment-76342" class="comment">
<div id="post-76342-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think if you try the first part on areas with named paths it will probably return the path names too.</p>
<p>But then I've always recoiled in horror whenever I've tried to look at the Overpass documentation, so you probably shouldn't listen to me.</p>
</div>
<div id="comment-76342-info" class="comment-info">
<span class="comment-age">(28 Aug '20, 17:32)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-76339" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76339-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="76345"></span>

<div id="answer-container-76345" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76345-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The first bit of code in your output repeats some names as some of the ways are split in several places. Assuming this is OK, then a bit of experimentation gives a modification of your second snippet to:</p>
<p><code>[out:csv("name";false)][timeout:25] [bbox:-33.9480172,151.1107534,-33.8594833,151.2207935]; rel[name=Beaconsfield]; (._;&gt;;); way._; out;</code></p>
<p>I think this would also return the names of rivers or streams that are used as boundaries, so an additional filter may be required if you're planning on looking at other suburbs too. It also won't be useful if for some reason one of the boundary lines is actually an independent way that happens to share nodes with a road etc.</p>
<p>To get both the outer and inner ways in one go:</p>
<p><code>[out:csv("name";false)] [bbox:-33.9480172,151.1107534,-33.8594833,151.2207935]; area[name="Beaconsfield"]; way(area)[highway][name] -&gt; .b; rel[name=Beaconsfield] -&gt; .a; (.a &gt;; .a ; .b; .b &gt; ; )-&gt; ._; way._; out;</code></p>
<p>Again, this has the same repetition where ways are split, so depending on your use case you may need to use a script to clean up the output anyway.</p>
<p>The above snippets were cobbled together from your question and the information <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL">here</a>. There's probably a much more elegant way to do this that I'm unaware of.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '20, 00:39</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Aug '20, 00:40</strong> </span></p>
</div>
</div>
<div id="comments-container-76345" class="comments-container">
<span id="76346"></span>
<div id="comment-76346" class="comment">
<div id="post-76346-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the help. a) I do want to use the query over many suburbs. I do this already to find streets within suburb boundaries but that omits boundary streets. b) The second suggestion introduces unwanted streets from inside the boundary. c) Rivers etc should be able to be avoided by somehow using `highway' attributes as part of the query. Unfortunately, I am 'unskilled' and to me, the documentation is still quite opaque.</p>
</div>
<div id="comment-76346-info" class="comment-info">
<span class="comment-age">(29 Aug '20, 08:40)</span> <span class="comment-user userinfo">rorylila</span>
</div>
</div>
</div>
<div id="comment-tools-76345" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76345-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76347"></span>

<div id="answer-container-76347" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76347-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The following seems to produce reasonably 'clean' output but still needs a bash sort. I guess there is no way around that. The admin_level is introduced because there are at least two overlapping administrative boundaries in the area of concern with the same name (Sydney) but different admin_levels. Highway is introduced to hopefully ignore other types of boundaries - rivers have been suggested.That is yet to be tested.</p>
<p>Script:</p>
<p>[out:csv("name";"false")] [bbox:-33.9480172,151.1107534,-33.8594833,151.2207935]; rel[name=Beaconsfield] [boundary=administrative] [admin_level=10]; (.<em>;&gt;;); way.</em>[highway][name]; out;</p>
<p>Beaconsfield Street William Street Johnson Street Botany Road Botany Road Botany Road Botany Road Botany Road O'Riordan Street Reserve Street</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '20, 09:48</strong></p>
<img src="https://secure.gravatar.com/avatar/c5e89b8b037b23165056f8722eb83dd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorylila&#39;s gravatar image" />
<p><span>rorylila</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorylila has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76347" class="comments-container">
&#10;</div>
<div id="comment-tools-76347" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76347-form-container" class="comment-form-container">
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

