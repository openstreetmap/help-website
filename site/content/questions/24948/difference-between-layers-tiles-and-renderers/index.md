+++
type = "question"
title = "Difference between layers, tiles and renderers"
description = '''Hi there As I am having a bit of an issue with those three terms, I was wondering if anyone could have a go at clearly and concisely explaining what Layers, Tiles and Renderers are? Cheers!'''
date = "2013-08-06T04:42:00Z"
lastmod = "2013-08-06T22:53:00Z"
weight = 24948
keywords = [ "definition", "layer", "tiles", "renderer" ]
aliases = [ "/questions/24948" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Difference between layers, tiles and renderers](/questions/24948/difference-between-layers-tiles-and-renderers)

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
<span id="post-24948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24948-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there</p>
<p>As I am having a bit of an issue with those three terms, I was wondering if anyone could have a go at clearly and concisely explaining what Layers, Tiles and Renderers are?</p>
<p>Cheers!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-definition" rel="tag" title="see questions tagged &#39;definition&#39;">definition</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-renderer" rel="tag" title="see questions tagged &#39;renderer&#39;">renderer</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Aug '13, 04:42</strong></p>
<img src="https://secure.gravatar.com/avatar/19c111f5c672fdb25353073c835f6a38?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephane-guillou&#39;s gravatar image" />
<p><span>stephane-gui...</span><br />
<span class="score" title="585 reputation points">585</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephane-guillou has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24948" class="comments-container">
<span id="24954"></span>
<div id="comment-24954" class="comment">
<div id="post-24954-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Thanks Andy! If you put those comments in an answer and expand on the layer part, you might get the best answer tick ;)</p>
</div>
<div id="comment-24954-info" class="comment-info">
<span class="comment-age">(06 Aug '13, 06:07)</span> <span class="comment-user userinfo">stephane-gui...</span>
</div>
</div>
</div>
<div id="comment-tools-24948" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24948-form-container" class="comment-form-container">
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

<span id="24973"></span>

<div id="answer-container-24973" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24973-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-24973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="stephane-guillou has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>assuming "Layers" means "Layers on the main OSM website" (from your comment, you may add this to your question) and assuming all of that question is about the <a href="https://www.openstreetmap.org/">OSM.org website</a>:</p>
<ul>
<li><em><span>layers</span></em> (if talking about different maps / map styles) are made of …</li>
<li><em><span>tiles</span></em> (square bitmap graphics -typically 256×256 pixels- images displayed in a grid arrangement to show a map) are produced by …</li>
<li>… <em><span>renderers</span></em> (software that outputs e.g. a visual map from raw geospatial data -our OSM data- as input)</li>
</ul>
<p>Layers usually/basically mean something overlayed on something else e.g. the <span>data layer</span> or <span>notes markers</span> over a base map. If there would only be different maps to switch between I would think that "layers" is not a good description but "map style switcher" would be.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '13, 12:19</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Aug '13, 12:32</strong> </span></p>
</div>
</div>
<div id="comments-container-24973" class="comments-container">
&#10;</div>
<div id="comment-tools-24973" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24973-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24959"></span>

<div id="answer-container-24959" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24959-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Layers are used to separate ways on different levels. Is the road over or under the rail line? Do the cross roads have a junction node, so you may turn there, or is it a bridge. This is important for drawing the map and routing, could I turn left or right or only go straight on? Layers are also the backgrounds in the editors such as out of copyright maps, others maps we can use and aerial all of which we can trace from or use to assist us in our edits. <a href="https://wiki.openstreetmap.org/wiki/Osmarender/Layers">https://wiki.openstreetmap.org/wiki/Osmarender/Layers</a> maybe better link <a href="https://wiki.openstreetmap.org/wiki/Layer">https://wiki.openstreetmap.org/wiki/Layer</a> Tiles are squares of map. Each Tile consists of four tiles. Each of those Tiles consists of four Tiles and so on for the 20 or so levels of zoom. each level shows more detail. This is done to speed up the availability of maps on screen. <a href="https://wiki.openstreetmap.org/wiki/Tiles">https://wiki.openstreetmap.org/wiki/Tiles</a> Rendering is the drawing of a map from a set of data. These renderings are a bit like artistic styles of painters. They are also made for particular users so a drivers map would concentrate on roads and motorways and show towns and road numbers. A hiker would maybe want footpaths, contours, woods, rivers and maybe campsites. <a href="https://wiki.openstreetmap.org/wiki/Renderers">https://wiki.openstreetmap.org/wiki/Renderers</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '13, 06:18</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Aug '13, 15:33</strong> </span></p>
</div>
</div>
<div id="comments-container-24959" class="comments-container">
<span id="24960"></span>
<div id="comment-24960" class="comment">
<div id="post-24960-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So I guess the word "Layers" on the main OSM website is misused?</p>
</div>
<div id="comment-24960-info" class="comment-info">
<span class="comment-age">(06 Aug '13, 06:22)</span> <span class="comment-user userinfo">stephane-gui...</span>
</div>
</div>
<span id="25007"></span>
<div id="comment-25007" class="comment">
<div id="post-25007-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I count three types of layers:- they are (1) The map layers on the map page. (2) The level layers of rivers, tunnels,roads, bridges and others. used by the renderers to decide which is shown above or below. (3) The choices of background layer we choose from when editing such as GPX traces,out of copyright maps, permitted maps, and allowed aerial sources which are layered under the data of the osm database, but separate from it, which is extremely useful when editing.</p>
</div>
<div id="comment-25007-info" class="comment-info">
<span class="comment-age">(06 Aug '13, 22:53)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-24959" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24959-form-container" class="comment-form-container">
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

