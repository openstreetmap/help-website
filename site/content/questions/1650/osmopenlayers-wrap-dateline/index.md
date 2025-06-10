+++
type = "question"
title = "OSM/Openlayers - wrap dateline"
description = '''How do you wrap the dateline in OpenLayers with OSM data like they do on the main openstreetmap.org map? I can&#x27;t seem to get wrapDateLine to work with OpenLayers.Layer.OSM? Is there another way?'''
date = "2010-11-26T15:51:00Z"
lastmod = "2010-11-27T14:39:00Z"
weight = 1650
keywords = [ "wrap", "dateline", "wrapdateline" ]
aliases = [ "/questions/1650" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OSM/Openlayers - wrap dateline](/questions/1650/osmopenlayers-wrap-dateline)

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
<span id="post-1650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1650-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do you wrap the dateline in OpenLayers with OSM data like they do on the main <a href="http://openstreetmap.org">openstreetmap.org</a> map?</p>
<p>I can't seem to get wrapDateLine to work with OpenLayers.Layer.OSM?</p>
<p>Is there another way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wrap" rel="tag" title="see questions tagged &#39;wrap&#39;">wrap</span> <span class="post-tag tag-link-dateline" rel="tag" title="see questions tagged &#39;dateline&#39;">dateline</span> <span class="post-tag tag-link-wrapdateline" rel="tag" title="see questions tagged &#39;wrapdateline&#39;">wrapdateline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Nov '10, 15:51</strong></p>
<img src="https://secure.gravatar.com/avatar/fbb15843641ffaf1c2259cc7ebb4735c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maw269&#39;s gravatar image" />
<p><span>maw269</span><br />
<span class="score" title="115 reputation points">115</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maw269 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1650" class="comments-container">
&#10;</div>
<div id="comment-tools-1650" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1650-form-container" class="comment-form-container">
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

<span id="1655"></span>

<div id="answer-container-1655" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1655-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="maw269 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Seems to be "wrapDateLine: true". Maybe you also need the "displayOutsideMaxExtent: true".</p>
<p>Here's the actual code <a href="http://git.openstreetmap.org/rails.git/blob/HEAD:/public/javascripts/map.js#l38">as in the repo</a> :</p>
<pre><code>   var mapnik = new OpenLayers.Layer.OSM.Mapnik(i18n(&quot;javascripts.map.base.mapnik&quot;), {
      keyid: &quot;mapnik&quot;,
      displayOutsideMaxExtent: true,
      wrapDateLine: true,
      layerCode: &quot;M&quot;
   });</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Nov '10, 14:39</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-1655" class="comments-container">
&#10;</div>
<div id="comment-tools-1655" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1655-form-container" class="comment-form-container">
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

