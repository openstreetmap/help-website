+++
type = "question"
title = "Get enclosing borders"
description = '''Can I use Overpass-API to get all administrative entities enclosing (partially or completely) an object. i.e. I have a wood like Sarghai (https://www.openstreetmap.org/way/475130161) and I want to know that it lies at least partially within a national park (Nationalpark Harz) and Harz (LK Goslar) ad...'''
date = "2020-04-08T10:37:00Z"
lastmod = "2020-04-08T20:01:00Z"
weight = 74052
keywords = [ "overpass", "admin_boundary" ]
aliases = [ "/questions/74052" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Get enclosing borders](/questions/74052/get-enclosing-borders)

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
<span id="post-74052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74052-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can I use Overpass-API to get all administrative entities enclosing (partially or completely) an object. i.e. I have a wood like Sarghai (<a href="https://www.openstreetmap.org/way/475130161)">https://www.openstreetmap.org/way/475130161)</a> and I want to know that it lies at least partially within a national park (Nationalpark Harz) and Harz (LK Goslar) administrative boundaries and lower saxony. Best case would be a Overpass-API script where I can give a Node, Way or Relation and receive all enclosing administrative entities.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '20, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/7ef3a3c25492438c9f0e5a548a36fa07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ogmios&#39;s gravatar image" />
<p><span>Ogmios</span><br />
<span class="score" title="766 reputation points">766</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ogmios has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-74052" class="comments-container">
<span id="74056"></span>
<div id="comment-74056" class="comment">
<div id="post-74056-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Have a read up of 'is_in'</p>
</div>
<div id="comment-74056-info" class="comment-info">
<span class="comment-age">(08 Apr '20, 12:04)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="74064"></span>
<div id="comment-74064" class="comment">
<div id="post-74064-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks DaveF, that was helpful. I just have to figure out how to use a node/way/rel instead of a coordinate but so far it works well:</p>
<p>[out:csv(::id, name)][timeout:25]; ( is_in(51.70785, 10.45692)-&gt;.a; / <em>* boundary=national_park = Nationalpark * boundary=protected_area = Naturschutzgebiet * boundary=administrative = Landrkeise, Länder etc.</em> / area.a ["boundary"~"national_park|protected_area"] -&gt;.b;</p>
<p>area.a ["boundary"="administrative"] ["admin_level"!="2"] -&gt;.c;</p>
<p>rel(pivot.b)-&gt;.b; rel(pivot.c)-&gt;.c; ); .b out geom; .c out geom;</p>
</div>
<div id="comment-74064-info" class="comment-info">
<span class="comment-age">(08 Apr '20, 17:47)</span> <span class="comment-user userinfo">Ogmios</span>
</div>
</div>
</div>
<div id="comment-tools-74052" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74052-form-container" class="comment-form-container">
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

<span id="74065"></span>

<div id="answer-container-74065" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74065-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ogmios has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>// All boundaries enclosing an entity (forest)
way(475130161);
out geom;
(._;&gt;;);
is_in;
rel(pivot)[boundary];
out geom;</code></pre>
<p><a href="https://overpass-turbo.eu/s/SAZ">https://overpass-turbo.eu/s/SAZ</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '20, 18:05</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Apr '20, 18:23</strong> </span></p>
</div>
</div>
<div id="comments-container-74065" class="comments-container">
<span id="74068"></span>
<div id="comment-74068" class="comment">
<div id="post-74068-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great, thanks.</p>
</div>
<div id="comment-74068-info" class="comment-info">
<span class="comment-age">(08 Apr '20, 20:01)</span> <span class="comment-user userinfo">Ogmios</span>
</div>
</div>
</div>
<div id="comment-tools-74065" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74065-form-container" class="comment-form-container">
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

