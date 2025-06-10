+++
type = "question"
title = "extract POIs for a region"
description = '''I am currently working on a list of available hotels in the Republic of Georgia. As the OSM-Database has lots of POIs, is it possible to access this data for that purpose? I would like to run a query to retrieve hotels with addresses, phone numbers and other details that are entered. The coordinates...'''
date = "2012-05-08T12:26:00Z"
lastmod = "2012-05-08T14:17:00Z"
weight = 12608
keywords = [ "query", "pois", "lists", "database" ]
aliases = [ "/questions/12608" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [extract POIs for a region](/questions/12608/extract-pois-for-a-region)

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
<span id="post-12608-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12608-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12608-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am currently working on a list of available hotels in the Republic of Georgia. As the OSM-Database has lots of POIs, is it possible to access this data for that purpose? I would like to run a query to retrieve hotels with addresses, phone numbers and other details that are entered. The coordinates would not matter for my purpose.</p>
<p>The result should be an Excel-file or similar table format.</p>
<p>How can I do this? All help appreciated!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-pois" rel="tag" title="see questions tagged &#39;pois&#39;">pois</span> <span class="post-tag tag-link-lists" rel="tag" title="see questions tagged &#39;lists&#39;">lists</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 May '12, 12:26</strong></p>
<img src="https://secure.gravatar.com/avatar/139902838ec4406143a7d9f286419a52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moszkva%20ter&#39;s gravatar image" />
<p><span>moszkva ter</span><br />
<span class="score" title="2125 reputation points"><span>2.1k</span></span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moszkva ter has 8 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-12608" class="comments-container">
&#10;</div>
<div id="comment-tools-12608" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12608-form-container" class="comment-form-container">
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

<span id="12609"></span>

<div id="answer-container-12609" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12609-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-12609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can get the data in JSON format in two steps from Overpass API:</p>
<p>First, obtain the area by pasting the following request</p>
<pre><code>&lt;osm-script output=&quot;json&quot;&gt;
&#10;&lt;coord-query lat=&quot;42.2&quot; lon=&quot;43.3&quot;/&gt;
&lt;print/&gt;
&#10;&lt;/osm-script&gt;</code></pre>
<p>into the <a href="http://overpass-api.de/query_form.html">Overpass API query form</a>.</p>
<p>From the result, you can read off the area with name "Georgia" that the relevant area id is 3600028699.</p>
<p>Now you can query for the really wanted data, again on <a href="http://overpass-api.de/query_form.html">Overpass API query form</a>:</p>
<pre><code>&lt;osm-script output=&quot;json&quot;&gt;
&#10;&lt;query type=&quot;node&quot;&gt;
  &lt;area-query ref=&quot;3600028699&quot;/&gt;
  &lt;has-kv k=&quot;tourism&quot; v=&quot;hotel&quot;/&gt;
&lt;/query&gt;
&lt;print/&gt;
&lt;area-query ref=&quot;3600028699&quot;/&gt;
&lt;query type=&quot;way&quot;&gt;
  &lt;recurse type=&quot;node-way&quot;/&gt;
  &lt;has-kv k=&quot;tourism&quot; v=&quot;hotel&quot;/&gt;
&lt;/query&gt;
&lt;print/&gt;
&#10;&lt;/osm-script&gt;</code></pre>
<p>This results in a 92 KB big JSON file containing all information about nodes or ways in Georgia tagged with <code>tourism=hotel</code>. If you want additionally hostels, repeat the second step with <code>tourism=hostel</code> and so on.</p>
<p>Note that some elements have addresses and phone numbers and others have not, depending on how they have been mapped in the database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 May '12, 14:17</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 May '12, 14:18</strong> </span></p>
</div>
</div>
<div id="comments-container-12609" class="comments-container">
&#10;</div>
<div id="comment-tools-12609" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12609-form-container" class="comment-form-container">
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

