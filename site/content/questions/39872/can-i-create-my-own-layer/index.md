+++
type = "question"
title = "can i create my own layer?"
description = '''Hi. I want to have an overview of schools in a specific area (the municipality of Lyngby-Taarbæk, Denmark). If I use Google Maps (which I by all means wish to avoid), I can create my own map showing exactly the POI I need. I don&#x27;t mind mind sharing my map of these POI. Is there a way that doesn&#x27;t in...'''
date = "2014-12-28T09:38:00Z"
lastmod = "2014-12-28T15:21:00Z"
weight = 39872
keywords = [ "map", "layer", "own", "poi" ]
aliases = [ "/questions/39872" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [can i create my own layer?](/questions/39872/can-i-create-my-own-layer)

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
<span id="post-39872-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39872-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-39872-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi.</p>
<p>I want to have an overview of schools in a specific area (the municipality of Lyngby-Taarbæk, Denmark). If I use Google Maps (which I by all means wish to avoid), I can create my own map showing exactly the POI I need. I don't mind mind sharing my map of these POI. Is there a way that doesn't include installing and figuring out new software?</p>
<p>With regards</p>
<p>Jacob</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-own" rel="tag" title="see questions tagged &#39;own&#39;">own</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Dec '14, 09:38</strong></p>
<img src="https://secure.gravatar.com/avatar/38340bc84ae9ec2176e69970d1feca4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jacobbahn&#39;s gravatar image" />
<p><span>Jacobbahn</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jacobbahn has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-39872" class="comments-container">
<span id="39880"></span>
<div id="comment-39880" class="comment">
<div id="post-39880-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the answer. That worked very well. I ran in to two issues though:</p>
<p>1) Some schools of that municipality is apparently not listed. Can I (easily) do that my self?</p>
<p>2) I would appreciate that the names of the schools would show up next to the spot on the map. Is there a simple way?</p>
</div>
<div id="comment-39880-info" class="comment-info">
<span class="comment-age">(28 Dec '14, 11:42)</span> <span class="comment-user userinfo">Jacobbahn</span>
</div>
</div>
</div>
<div id="comment-tools-39872" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39872-form-container" class="comment-form-container">
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

<span id="39888"></span>

<div id="answer-container-39888" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39888-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-39888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jacobbahn has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To answer all of your questions in one go:</p>
<p>Use <a href="http://overpass-turbo.eu/s/6If">this Overpass Query</a>:</p>
<pre><code>[out:json][timeout:25];area(3602183062)-&gt;.searchArea;(node[&quot;amenity&quot;=&quot;school&quot;](area.searchArea);way[&quot;amenity&quot;=&quot;school&quot;](area.searchArea);relation[&quot;amenity&quot;=&quot;school&quot;](area.searchArea););out body center;&gt;;out skel qt;
{{style:
    way[amenity] {
      text: name;
    }
&#10;    node[amenity] {
      text: name;
    }
&#10;   relation[amenity] {
      text: name;
    }
&#10;}}</code></pre>
<p>It returns not only schools represented by nodes, but also those represented by ways or relations. The names get displayed by the little Mapcss at the end of the query.</p>
<p>The Vej (or Way) refers to the OSM object that is used to represent the object. It has nothing to do with the physical "street" object on which one drives.</p>
<p>Frederik's query only asked for schools represented by a node, so some of the schools you mention did not appear the answer, as they are represented by (closed) ways.</p>
<p>The query I link to uses a slightly different syntax. This is the new standard language of Overpass, but the XML-format in Frederik's answer is still supported.</p>
<p>Editing is pretty simple. First you have to make an account on openstreetmap.org. Then you see an edit button above the map openstreetmap.org. Follow the tutorial offered by the iD tutorial. You could also read <a href="http://learnosm.org/en/">LearnOSM</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Dec '14, 13:29</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jan '15, 06:29</strong> </span></p>
</div>
</div>
<div id="comments-container-39888" class="comments-container">
<span id="39893"></span>
<div id="comment-39893" class="comment">
<div id="post-39893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For a beginner, I would highly recommend to start with overpass turbo wizard. It automatically does all the magic for you, i.e. no need to learn anything new.</p>
<p>Just type: <code>amenity=school in "Lyngby-Taarbæk Kommune"</code> in the wizard dialog on overpass-turbo.eu. You can read all about the wizard here:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Overpass_turbo/Wizard">http://wiki.openstreetmap.org/wiki/Overpass_turbo/Wizard</a></p>
<p>It's super simple to use. Just give it a try.</p>
</div>
<div id="comment-39893-info" class="comment-info">
<span class="comment-age">(28 Dec '14, 15:21)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-39888" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39888-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="39879"></span>

<div id="answer-container-39879" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39879-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-39879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a query tool that you can use to find the objects in question. It is called "Overpass API" and can be conveniently accessed through the <a href="http://overpass-turbo.eu">Overpass Turbo</a> web site. Using Overpass to find the schools in Lyngby-Taarbæk requires that you first identify the OSM relation ID of that municipality - <a href="http://www.openstreetmap.org/relation/2183062">2183062</a> - and then add 3600000000 to that number to use it in an Overpass query like so:</p>
<pre><code>&lt;osm-script output=&quot;json&quot;&gt;
  &lt;query type=&quot;node&quot;&gt;
    &lt;has-kv k=&quot;amenity&quot; v=&quot;school&quot;/&gt;
    &lt;area-query ref=&quot;3602183062&quot;/&gt;
  &lt;/query&gt;
  &lt;print mode=&quot;body&quot;/&gt;  
&lt;/osm-script&gt;</code></pre>
<p><a href="http://overpass-turbo.eu/s/6I3">(See it in action directly on Overpass Turbo.)</a></p>
<p>You can influence the look of the result within certain limits, see <a href="http://wiki.openstreetmap.org/wiki/Overpass_turbo/MapCSS.">http://wiki.openstreetmap.org/wiki/Overpass_turbo/MapCSS.</a> If you want more control over the look of the map, you should have a look at the <a href="http://umap.openstreetmap.fr">UMap service</a> which lets you draw stuff on the map and edit it. You can even export the query results from the above Overpass query and import them into UMap for editing, or <a href="http://www.mappa-mercia.org/2014/09/creating-an-always-up-to-date-map.html">directly link UMap and Overpass</a> - but then of course you can't manually edit the result.</p>
<p><a href="http://umap.openstreetmap.fr/de/map/anonymous-edit/24805%3At9FlEAJk6Nau1L-oEMLgok1ElII">(Example for an editable UMap with the above data.)</a></p>
<p>(answer edited to include comments by escada and mmd, thanks!)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Dec '14, 11:17</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Dec '14, 21:23</strong> </span></p>
</div>
</div>
<div id="comments-container-39879" class="comments-container">
&#10;</div>
<div id="comment-tools-39879" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39879-form-container" class="comment-form-container">
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

