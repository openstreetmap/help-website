+++
type = "question"
title = "gathering the information of schools - with overpass-api"
description = '''i want to gather results with a search-request - suggested by the wiki.-page  btw see the central ressource for the tag-system http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dschool on overpass-api we can run this - as request for node, builiding and relaion: &amp;lt;!-- This query looks for nodes, way...'''
date = "2014-06-21T07:23:00Z"
lastmod = "2014-06-21T12:09:00Z"
weight = 34206
keywords = [ "xml", "overpass", "php", "osm", "josm" ]
aliases = [ "/questions/34206" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [gathering the information of schools - with overpass-api](/questions/34206/gathering-the-information-of-schools-with-overpass-api)

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
<span id="post-34206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34206-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i want to gather results with a search-request - suggested by the wiki.-page</p>
<p>btw see the central ressource for the tag-system <a href="http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dschool">http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dschool</a></p>
<p>on overpass-api we can run this - as request for node, builiding and relaion:</p>
<pre><code>&lt;!--
This query looks for nodes, ways and relations 
with the given key/value combination.
Choose your region and hit the Run button above!
--&gt;
&lt;osm-script output=&quot;json&quot; timeout=&quot;25&quot;&gt;
  &lt;!-- gather results --&gt;
  &lt;union&gt;
    &lt;!-- query part for: “building=school” --&gt;
    &lt;query type=&quot;node&quot;&gt;
      &lt;has-kv k=&quot;building&quot; v=&quot;school&quot;/&gt;
      &lt;bbox-query {{bbox}}/&gt;
    &lt;/query&gt;
    &lt;query type=&quot;way&quot;&gt;
      &lt;has-kv k=&quot;building&quot; v=&quot;school&quot;/&gt;
      &lt;bbox-query {{bbox}}/&gt;
    &lt;/query&gt;
    &lt;query type=&quot;relation&quot;&gt;
      &lt;has-kv k=&quot;building&quot; v=&quot;school&quot;/&gt;
      &lt;bbox-query {{bbox}}/&gt;
    &lt;/query&gt;
  &lt;/union&gt;
  &lt;!-- print results --&gt;
  &lt;print mode=&quot;body&quot;/&gt;
  &lt;recurse type=&quot;down&quot;/&gt;
  &lt;print mode=&quot;skeleton&quot; order=&quot;quadtile&quot;/&gt;
&lt;/osm-script&gt;</code></pre>
<p>btw - this above code does not function - and this below also not. what is wrong here?</p>
<pre><code>This query looks for nodes, ways and relations 
with the given key/value combination.
Choose your region and hit the Run button above!
--&gt;
&lt;osm-script output=&quot;json&quot; timeout=&quot;25&quot;&gt;
  &lt;!-- gather results --&gt;
  &lt;union&gt;
    &lt;!-- query part for: “building=school” --&gt;
    &lt;query type=&quot;node&quot;&gt;
      &lt;has-kv k=&quot;building&quot; v=&quot;school&quot;/&gt;
      &lt;bbox-query {51.5557914,0.2118915,51.5673083,0.2369398}/&gt;
    &lt;/query&gt;
  &lt;!-- print results --&gt;
  &lt;print mode=&quot;body&quot;/&gt;
  &lt;recurse type=&quot;down&quot;/&gt;
  &lt;print mode=&quot;skeleton&quot; order=&quot;quadtile&quot;/&gt;
&lt;/osm-script&gt;</code></pre>
<p>why does this not run smoothly?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jun '14, 07:23</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34206" class="comments-container">
&#10;</div>
<div id="comment-tools-34206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34206-form-container" class="comment-form-container">
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

<span id="34207"></span>

<div id="answer-container-34207" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34207-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The first query runs fine, see the <a href="http://overpass-turbo.eu/s/3OC">result on overpass turbo</a>.</p>
<p>The second query is broken. The bbox element has the wrong syntax and the union is not closed. I fixed it for you. See the <a href="http://overpass-turbo.eu/s/3OI">result on overpass turbo</a>, the fixed query is:</p>
<pre><code>&lt;osm-script output=&quot;json&quot; timeout=&quot;25&quot;&gt;
  &lt;!-- gather results --&gt;
  &lt;union&gt;
    &lt;!-- query part for: “building=school” --&gt;
    &lt;query type=&quot;node&quot;&gt;
      &lt;has-kv k=&quot;building&quot; v=&quot;school&quot;/&gt;
      &lt;bbox-query e=&quot;51.5557914&quot; s=&quot;0.2118915&quot; w=&quot;51.5673083&quot; n=&quot;0.2369398&quot;/&gt;
    &lt;/query&gt;
  &lt;/union&gt;
  &lt;!-- print results --&gt;
  &lt;print mode=&quot;body&quot;/&gt;
  &lt;recurse type=&quot;down&quot;/&gt;
  &lt;print mode=&quot;skeleton&quot; order=&quot;quadtile&quot;/&gt;
&lt;/osm-script&gt;</code></pre>
<p>Try to use overpass turbo when constructing queries. It will show you a graphical representation of the results and syntax errors can be spotted easily.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '14, 08:25</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-34207" class="comments-container">
<span id="34211"></span>
<div id="comment-34211" class="comment">
<div id="post-34211-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello dear scai - many thanks for the help - all is greatly apprediated. thx again - have agreat weekend ;-)</p>
</div>
<div id="comment-34211-info" class="comment-info">
<span class="comment-age">(21 Jun '14, 12:02)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
<span id="34213"></span>
<div id="comment-34213" class="comment">
<div id="post-34213-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please accept answers (by clicking on the checkmark) if they answer your questions. So far you have a lot of questions but didn't accept a single answer.</p>
</div>
<div id="comment-34213-info" class="comment-info">
<span class="comment-age">(21 Jun '14, 12:09)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-34207" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34207-form-container" class="comment-form-container">
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

