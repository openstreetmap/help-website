+++
type = "question"
title = "OpenLayers - Control zoom level granularity?"
description = '''Is there a way to control the granularity of the map zoom levels using OpenLayers? That is, my boss keeps complaining that on smaller monitors zoom level 5 is too close (it cuts off part of the state), but zoom level 4 is too wide (it shows a lot of the surrounding map and makes the markers too crow...'''
date = "2012-07-16T19:46:00Z"
lastmod = "2012-07-17T16:28:00Z"
weight = 14324
keywords = [ "zoomlevel", "openstreetmap", "openlayers", "zoom" ]
aliases = [ "/questions/14324" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OpenLayers - Control zoom level granularity?](/questions/14324/openlayers-control-zoom-level-granularity)

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
<span id="post-14324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14324-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to control the granularity of the map zoom levels using OpenLayers? That is, my boss keeps complaining that on smaller monitors zoom level 5 is too close (it cuts off part of the state), but zoom level 4 is too wide (it shows a lot of the surrounding map and makes the markers too crowded). Ideally, I would like to be able to smoothly zoom in to the exact level I want, but even if I could just get one or two more discrete zoom levels in the proper range I would be happy. Is this possible?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '12, 19:46</strong></p>
<img src="https://secure.gravatar.com/avatar/939aca49b44a6c3e73678fd0f7db1a2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ibrewster&#39;s gravatar image" />
<p><span>ibrewster</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ibrewster has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jul '12, 19:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-14324" class="comments-container">
&#10;</div>
<div id="comment-tools-14324" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14324-form-container" class="comment-form-container">
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

<span id="14325"></span>

<div id="answer-container-14325" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14325-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-14325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not sure if this is meant to be an OpenStreetMap question or an OpenLayers question. If it is an OpenLayers question then this is the wrong place to ask; therefore I'll treat it as if you were asking for OSM specifically.</p>
<p>OpenStreetMap data on the OSM tile server is rendered to tiles on the fixed zoom leves that you see. You have two options:</p>
<ul>
<li>interpolate - i.e. take the zoom level 5 tiles and reduce them a bit, or take the zoom level 4 tiles and increase them a bit. This is what the web site <a href="http://www.khtml.org/">http://www.khtml.org/</a> does, where you can select intermediate zoom levels.</li>
<li>render your own map (enter "render map" in the search box above to find details) - if you do that then you can specify exactly which area and size you want and the renderer will do its best to fulfil the request.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '12, 19:55</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-14325" class="comments-container">
&#10;</div>
<div id="comment-tools-14325" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14325-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14340"></span>

<div id="answer-container-14340" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14340-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-14340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Another noddy way of getting a map at half-zoom-level, is to tell your browser to zoom. 'View' menu. Zoom out.</p>
<p>This works with firefox and safari. Not sure about I.E. It amounts to the interpolation technique federik describes, which introduces unpleasant scaling artefacts. In fact because the browser is scaling quickly on-the-fly, it'll not do a particularly nice job of it. It can even result in spurious gridlines appearing (pixel gaps between tiles). In other words this is a completely half-assed solution :-)</p>
<p>Having said that, I've actually found this handy on a number of occasions when trying to get a quick map screenshot (usually for creating cake diagram images) Don't forget to do view -&gt; zoom -&gt; reset afterwards though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '12, 16:28</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-14340" class="comments-container">
&#10;</div>
<div id="comment-tools-14340" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14340-form-container" class="comment-form-container">
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

