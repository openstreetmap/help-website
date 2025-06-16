+++
type = "question"
title = "Having trouble getting osm data with overpass query"
description = '''Hello all,  I am trying to do an overpass query to show which streets had sidewalk tags added in 2016 in Portland, Oregon, USA. This query returns visible data in https://overpass-turbo.eu/, but when I try to export raw data, or use the same query from the command line, the .osm file that is created...'''
date = "2016-08-06T01:01:00Z"
lastmod = "2016-08-09T20:16:00Z"
weight = 51271
keywords = [ "overpass" ]
aliases = [ "/questions/51271" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Having trouble getting osm data with overpass query](/questions/51271/having-trouble-getting-osm-data-with-overpass-query)

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
<span id="post-51271-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51271-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51271-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all,</p>
<p>I am trying to do an overpass query to show which streets had sidewalk tags added in 2016 in Portland, Oregon, USA. This query returns visible data in <a href="https://overpass-turbo.eu/,">https://overpass-turbo.eu/,</a> but when I try to export raw data, or use the same query from the command line, the .osm file that is created will not open in JOSM (message says "No data found in file..." I think I must be having some trouble with recursion?</p>
<p>Here is the query, with a small test bounding box:</p>
<pre><code>[timeout:300][diff:&quot;2016-01-01T00:00:00Z&quot;,&quot;2016-08-01T00:00:00Z&quot;];
(way[&quot;highway&quot;~&quot;primary|secondary|tertiary|trunk|service|residential|primary_link|secondary_link|tertiary_link|unclassified&quot;][&quot;sidewalk&quot;~&quot;.&quot;](45.5,-122.72,45.52,-122.7);
&gt;;
);
out meta;</code></pre>
<p>Any help would be very much appreciated! FYI, I want the raw OSM data so I can use it to create a time lapse visualization with <a href="http://prabhasp.github.io/OSMTimeLapseR/">http://prabhasp.github.io/OSMTimeLapseR/</a></p>
<p>Thank you!</p>
<p>Madeline</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Aug '16, 01:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a99958ffb04613a8ca73e65f3d76c2d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mosteele&#39;s gravatar image" />
<p><span>mosteele</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mosteele has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Aug '16, 01:03</strong> </span></p>
</div>
</div>
<div id="comments-container-51271" class="comments-container">
&#10;</div>
<div id="comment-tools-51271" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51271-form-container" class="comment-form-container">
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

<span id="51274"></span>

<div id="answer-container-51274" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51274-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51274-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51274-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>By using the 'diff' setting you're asking for a so called augmented diff format. There are some apps like achavi which can visualize this format. JOSM for sure is not amongst them and it really has no clue about it. That's why you get the message about no data being found in JOSM.</p>
<p>Long story short, use [date:...] as often as needed to get data at some given point in time instead. You will receive the usual osm xml format JOSM will also be happy with.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '16, 06:32</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Aug '16, 06:42</strong> </span></p>
</div>
</div>
<div id="comments-container-51274" class="comments-container">
<span id="51307"></span>
<div id="comment-51307" class="comment">
<div id="post-51307-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much, this helps! However, I am still struggling with the query. Do you think that the best approach is to do a subtraction (as in <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Difference)">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Difference)</a> between one set created with the old date (using "[date:...") and one created with the new date? I'm having trouble with this since it seems like the ["date:"] parameter, like the ["timeout:"] parameter, is meant to be set only once for the whole query, at the top.</p>
<p>I suppose another approach would be to try to convert the diff file to OSM using <a href="https://wiki.openstreetmap.org/wiki/Osmconvert">OSMConvert</a> .</p>
<p>Any further pointers you could give me would be mush appreciated. A link to a working example of a query with two different dates (but not using "diff:") would be particularly valuable.</p>
<p>Thanks again,</p>
<p>Madeline</p>
</div>
<div id="comment-51307-info" class="comment-info">
<span class="comment-age">(08 Aug '16, 18:10)</span> <span class="comment-user userinfo">mosteele</span>
</div>
</div>
<span id="51308"></span>
<div id="comment-51308" class="comment">
<div id="post-51308-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><code>[date: ...]</code> is indeed meant to be a global setting for the query, i.e. you can only set it once and get all data which was available back then. <code>difference</code> does not work across different <code>[date: ...]</code> settings.</p>
<p>My idea was to simply run several different queries with different <code>[date: ..]</code> settings and get a series of snapshots for different points in time. Store each query result in a different file, like osm-portland-2015-01, 2015-02, 2015-03.osm, etc. Wouldn't that be exactly what you need to feed into OSMTimeLapseR?</p>
<p>Please note that <code>[diff: ...]</code> will only provide the difference between the first and the last timestamp. If there are multiple changes to an object during that timeframe, you will not get a full history containing all intermittent versions this way!</p>
</div>
<div id="comment-51308-info" class="comment-info">
<span class="comment-age">(08 Aug '16, 19:44)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="51318"></span>
<div id="comment-51318" class="comment">
<div id="post-51318-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the clarification on the [date:...] setting. Actually, if I understand it correctly, OSMTimeLapseR takes a single OSM file and animates it based on the date of last edit. Multiple time slices files could be used to create visualizations using a number of other techniques, though.</p>
<p>I think I've alighted on a different approach that will work. I'll just write a query that pulls streets with sidewalk tags that were edited by the people involved in the current effort. I think this should be close enough for what I need.</p>
<p>Thanks again for taking the time to help! It's much appreciated!</p>
<p>Madeline</p>
</div>
<div id="comment-51318-info" class="comment-info">
<span class="comment-age">(09 Aug '16, 19:45)</span> <span class="comment-user userinfo">mosteele</span>
</div>
</div>
<span id="51319"></span>
<div id="comment-51319" class="comment">
<div id="post-51319-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your feedback. A pure 'date of last edit' approach might be a bit skewed by trivial edits occurring at a later point in time. When filtering based on the names, you should probably also cross check if there were some later (e.g. QA) fixes by mappers unrelated to your project. Otherwise, parts of your effort will not show up in the result.</p>
<p>Also, I've never really heard of OSMTimeLapseR before. To bring everyone up to speed, a few introductory words on what kind of data you're expecting would have been really helpful. Maybe next time... ;)</p>
</div>
<div id="comment-51319-info" class="comment-info">
<span class="comment-age">(09 Aug '16, 20:16)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-51274" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51274-form-container" class="comment-form-container">
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

