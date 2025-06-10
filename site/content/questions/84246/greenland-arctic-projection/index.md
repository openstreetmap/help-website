+++
type = "question"
title = "Greenland - Arctic projection"
description = '''Hi, I need a map of Greenland as close as possible to the real shape - so not Mercator. Is it possible to toggle the projection in OpenStreetMap to get a Lagrange or Lambert projection? Or ideally a planar Arctic projection? Thanks'''
date = "2022-04-22T17:42:00Z"
lastmod = "2022-04-25T16:56:00Z"
weight = 84246
keywords = [ "arctic", "greenland" ]
aliases = [ "/questions/84246" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Greenland - Arctic projection](/questions/84246/greenland-arctic-projection)

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
<span id="post-84246-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84246-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84246-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I need a map of Greenland as close as possible to the real shape - so not Mercator. Is it possible to toggle the projection in OpenStreetMap to get a Lagrange or Lambert projection? Or ideally a planar Arctic projection?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-arctic" rel="tag" title="see questions tagged &#39;arctic&#39;">arctic</span> <span class="post-tag tag-link-greenland" rel="tag" title="see questions tagged &#39;greenland&#39;">greenland</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '22, 17:42</strong></p>
<img src="https://secure.gravatar.com/avatar/e427a21624df21d22d536d4036508962?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="J%20Mar%C3%A9chal&#39;s gravatar image" />
<p><span>J Maréchal</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="J Maréchal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84246" class="comments-container">
&#10;</div>
<div id="comment-tools-84246" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84246-form-container" class="comment-form-container">
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

<span id="84248"></span>

<div id="answer-container-84248" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84248-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at <a href="http://webmap.arcticconnect.ca/">http://webmap.arcticconnect.ca/</a> - lots of [del]projection options[/del] (Edit: oh wait, in version 2.0 it's only EPSG:3573, version 1.0 had more) for a polar map of the Arctic region.</p>
<p>If you want to build the map yourself, <a href="https://osm2pgsql.org/examples/antarctica/">https://osm2pgsql.org/examples/antarctica/</a> has some guidance (whilst for Antarctica, it could be used for the Artic polar region as well by changing the wanted projection in the workflow), MazDerMind had also built a mapnik stylesheet years ago ( <a href="https://github.com/MaZderMind/mapnik-stylesheets-polar">https://github.com/MaZderMind/mapnik-stylesheets-polar</a> ), the demo is defunct as of now (2022).</p>
<p>With the standard OSM tile layer you can't just toggle the projection as that layer is raster based and the projection defined at production of the layer, so you would either have to build it yourself (see last paragraph) or use a map where this is already done (see first paragraph).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '22, 19:39</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Apr '22, 09:07</strong> </span></p>
</div>
</div>
<div id="comments-container-84248" class="comments-container">
<span id="84268"></span>
<div id="comment-84268" class="comment">
<div id="post-84268-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot</p>
</div>
<div id="comment-84268-info" class="comment-info">
<span class="comment-age">(25 Apr '22, 16:56)</span> <span class="comment-user userinfo">J Maréchal</span>
</div>
</div>
</div>
<div id="comment-tools-84248" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84248-form-container" class="comment-form-container">
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

