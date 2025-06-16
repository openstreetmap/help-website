+++
type = "question"
title = "refining osmfilter to get more out of it"
description = '''hello dear openstreetmap experts  new to the gis-technique: i am workin with the following tools:  this  https://wiki.openstreetmap.org/wiki/DE:Osmconvert  and that https://wiki.openstreetmap.org/wiki/DE:Osmfilter  i get the following example:   wget download.geofabrik.de/openstreetmap/europe/germany....'''
date = "2014-04-14T15:35:00Z"
lastmod = "2014-04-16T21:39:00Z"
weight = 32364
keywords = [ "xml", "osmfilter" ]
aliases = [ "/questions/32364" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [refining osmfilter to get more out of it](/questions/32364/refining-osmfilter-to-get-more-out-of-it)

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
<span id="post-32364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32364-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello dear openstreetmap experts</p>
<p>new to the gis-technique: i am workin with the following tools:</p>
<p>this</p>
<pre><code>https://wiki.openstreetmap.org/wiki/DE:Osmconvert</code></pre>
<p>and that</p>
<pre><code>https://wiki.openstreetmap.org/wiki/DE:Osmfilter</code></pre>
<p>i get the following example: wget download.geofabrik.de/openstreetmap/europe/germany.osm.pbf osmconvert germany.osm.pbf --all-to-nodes -o=germany.o5m osmfilter germany.o5m --keep="amenity=shop or shop=*" -o=shops.o5m osmconvert shops.o5m --csv="<span>@id</span> <span>@lon</span> <span>@lat</span> shop name" --csv-headline -o=shops.csv</p>
<p>that runs fine - now i want to refine:</p>
<p>to get such a result- [made out of xslt]</p>
<pre><code>&lt;node id=&quot;52768810&quot; lat=&quot;48.2044749&quot; lon=&quot;11.3249434&quot; version=&quot;7&quot; changeset=&quot;9490517&quot; user=&quot;wheelmap_visitor&quot; uid=&quot;290680&quot; timestamp=&quot;2013-10-07T20:24:46Z&quot;&gt;
&lt;tag k=&quot;addr:city&quot; v=&quot;Olching&quot; /&gt;
&lt;tag k=&quot;addr:country&quot; v=&quot;DE&quot; /&gt;
&lt;tag k=&quot;addr:housenumber&quot; v=&quot;72&quot; /&gt;
&lt;tag k=&quot;addr:postcode&quot; v=&quot;82140&quot; /&gt;
&lt;tag k=&quot;addr:street&quot; v=&quot;Hauptstraße&quot; /&gt;
&lt;tag k=&quot;amenity&quot; v=&quot;restaurant&quot; /&gt;
&lt;tag k=&quot;cuisine&quot; v=&quot;mexican&quot; /&gt;
&lt;tag k=&quot;email&quot; v=&quot;info@cantina-olching.de&quot; /&gt;
&lt;tag k=&quot;name&quot; v=&quot;La Cantina&quot; /&gt;
&lt;tag k=&quot;opening_hours&quot; v=&quot;Mo-Su 17:00-01:00&quot; /&gt;
&lt;tag k=&quot;phone&quot; v=&quot;+49 (8142) 444393&quot; /&gt;
&lt;tag k=&quot;website&quot; v=&quot;http://www.cantina-olching.com/&quot; /&gt;
&lt;tag k=&quot;wheelchair&quot; v=&quot;no&quot; /&gt;</code></pre>
<p>doable!?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Apr '14, 15:35</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Apr '14, 15:38</strong> </span></p>
</div>
</div>
<div id="comments-container-32364" class="comments-container">
&#10;</div>
<div id="comment-tools-32364" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32364-form-container" class="comment-form-container">
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

<span id="32394"></span>

<div id="answer-container-32394" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32394-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have you tried the simple <code>-o shops.osm</code>?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Apr '14, 21:39</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-32394" class="comments-container">
&#10;</div>
<div id="comment-tools-32394" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32394-form-container" class="comment-form-container">
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

