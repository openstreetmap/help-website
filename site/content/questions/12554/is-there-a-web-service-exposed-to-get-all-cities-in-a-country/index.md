+++
type = "question"
title = "Is there a web service exposed to get all cities in a country"
description = '''Is it possible to get all cities of a country from OSM using a web service? I need this in order to use in a combo box (fill the combo box with city names when user selects a country) Thanks in advance.'''
date = "2012-05-05T10:02:00Z"
lastmod = "2012-05-05T11:17:00Z"
weight = 12554
keywords = [ "cities" ]
aliases = [ "/questions/12554" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a web service exposed to get all cities in a country](/questions/12554/is-there-a-web-service-exposed-to-get-all-cities-in-a-country)

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
<span id="post-12554-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12554-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12554-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to get all cities of a country from OSM using a web service? I need this in order to use in a combo box (fill the combo box with city names when user selects a country) Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-cities" rel="tag" title="see questions tagged &#39;cities&#39;">cities</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 May '12, 10:02</strong></p>
<img src="https://secure.gravatar.com/avatar/8f25d6294309a98aa20ad63a312aa8c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sewdil&#39;s gravatar image" />
<p><span>sewdil</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sewdil has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12554" class="comments-container">
&#10;</div>
<div id="comment-tools-12554" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12554-form-container" class="comment-form-container">
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

<span id="12559"></span>

<div id="answer-container-12559" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12559-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-12559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sewdil has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No. OpenStreetMap has the raw data from which you could extract such a list yourself, but there's no ready-made web service that does that for you.</p>
<p>It is possible to go a little way in your direction with the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a>; this allows you to ask for "all objects tagged <code>place=city</code> within the boundary described by the OpenStreetMap relation with the ID x". This requires that you first find out which relation you are interested in.</p>
<p>Say you wanted to find all cities in Moldova. <a href="http://www.google.com/search?q=openstreetmap+relation+moldova&amp;ie=utf-8&amp;oe=utf-8&amp;client=ubuntu&amp;channel=fs">Google</a> can be used to find out that the relation id you are looking for is 58974. Add 3600000000 to that number and use the following Overpass query:</p>
<pre><code>&lt;query type=&quot;node&quot;&gt;
  &lt;has-kv k=&quot;place&quot; v=&quot;city&quot;/&gt;
  &lt;area-query ref=&quot;3600058974&quot;/&gt;
&lt;/query&gt;
&lt;print mode=&quot;body&quot;/&gt;</code></pre>
<p>This returns the OSM XML for all city nodes in Moldova.</p>
<p>However, requesting such information live from the database every time you need it is a terrible waste of time; you really want to compute such a list ahead of time and then use that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '12, 11:17</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-12559" class="comments-container">
&#10;</div>
<div id="comment-tools-12559" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12559-form-container" class="comment-form-container">
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

