+++
type = "question"
title = "Extract all hydropower stations or dams along one river"
description = '''I am looking for a way to get all hydropower stations or dams that are along a given river via Overpass turbo. Something like the following but for a given river instead of a given country: [out:json][timeout:25]; {{geocodeArea:Sweden}}-&amp;gt;.searchArea; ( node[&quot;power&quot;=&quot;plant&quot;][&quot;plant:source&quot;=hydro](...'''
date = "2021-06-02T21:00:00Z"
lastmod = "2021-06-14T21:06:00Z"
weight = 80395
keywords = [ "overpass" ]
aliases = [ "/questions/80395" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Extract all hydropower stations or dams along one river](/questions/80395/extract-all-hydropower-stations-or-dams-along-one-river)

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
<span id="post-80395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80395-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am looking for a way to get <strong>all hydropower stations or dams</strong> that are <strong>along a given river</strong> via Overpass turbo. Something like the following but for a given river instead of a given country:</p>
<pre><code>[out:json][timeout:25];
{{geocodeArea:Sweden}}-&gt;.searchArea;
(
node[&quot;power&quot;=&quot;plant&quot;][&quot;plant:source&quot;=hydro](area.searchArea);
way[&quot;power&quot;=&quot;plant&quot;][&quot;plant:source&quot;=hydro](area.searchArea);
relation[&quot;power&quot;=&quot;plant&quot;][&quot;plant:source&quot;=hydro](area.searchArea);
);
out center;</code></pre>
<p>For example, for all hydropower stations or dams along Luleälven (<a href="https://www.openstreetmap.org/relation/6974663).">https://www.openstreetmap.org/relation/6974663).</a> Perhaps it is possible to generate a search area that covers the river, e.g. extending the center of the river bed by 200 m on each side of the river. Or by using a search area that is defined to be "near" the river (most hydropower stations are on the river, but sometimes, they can be besides it, e.g. when the original river bed is bypassing the power station). Perhaps one could even use a search line instead of a search area.</p>
<p><strong>Thanks</strong> for all hints!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '21, 21:00</strong></p>
<img src="https://secure.gravatar.com/avatar/ffb12f7c2548687764b2de9e4562d2d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="G%C3%A5seborg&#39;s gravatar image" />
<p><span>Gåseborg</span><br />
<span class="score" title="311 reputation points">311</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gåseborg has 4 accepted answers">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jun '21, 22:08</strong> </span></p>
</div>
</div>
<div id="comments-container-80395" class="comments-container">
&#10;</div>
<div id="comment-tools-80395" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80395-form-container" class="comment-form-container">
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

<span id="80396"></span>

<div id="answer-container-80396" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80396-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Gåseborg has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>'around' is the command you're looking for.</p>
<pre><code>{{geocodeArea:Sweden}};
rel[name=&quot;Luleälven&quot;]-&gt;.river;
.river out geom;
nwr(around.river:50)[power=plant][&quot;plant:source&quot;=hydro](area);
out center;</code></pre>
<p>I've set the value to 50m, you may need to increase that, but it'll take longer to run &amp; may return erroneous results.</p>
<p>FYI use 'nwr'; it saves a lot of typing</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '21, 00:01</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jun '21, 00:03</strong> </span></p>
</div>
</div>
<div id="comments-container-80396" class="comments-container">
<span id="80397"></span>
<div id="comment-80397" class="comment">
<div id="post-80397-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This works perfectly! Thanks also for the hint on 'nwr' which I was not aware of :)</p>
</div>
<div id="comment-80397-info" class="comment-info">
<span class="comment-age">(03 Jun '21, 09:23)</span> <span class="comment-user userinfo">Gåseborg</span>
</div>
</div>
<span id="80576"></span>
<div id="comment-80576" class="comment">
<div id="post-80576-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/1532/davef">@DaveF</a>: One more detail, the river in the example gets water from many smaller rivers. I tried including the largest one of those ("Lilla Luleälven") by changing the second line in your answer to (rel[name="Luleälven"];rel[name="Lilla Luleälven"];)-&gt;.river; As a result, the outline of both rivers is shown correct in Overpass turbo, but it cannot find any stations any longer. Could you even give me a hint on how to get this done correcly? That would be great! Perhaps there even is a way to specify just the main river but adding an additional argument to include all mapped tributaries. Thanks in advance!</p>
</div>
<div id="comment-80576-info" class="comment-info">
<span class="comment-age">(14 Jun '21, 21:06)</span> <span class="comment-user userinfo">Gåseborg</span>
</div>
</div>
</div>
<div id="comment-tools-80396" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80396-form-container" class="comment-form-container">
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

