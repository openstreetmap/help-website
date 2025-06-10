+++
type = "question"
title = "Overpass API Interpreter Help"
description = '''I&#x27;m having trouble executing my query using the overpass-api.de API. Error: line 3: parse error: not well-formed (invalid token) My query is the following: &amp;lt;osm-script timeout=&quot;300&quot;&amp;gt;  &amp;lt;id-query {{nominatimArea:Mexico}} into=&quot;area&quot;/&amp;gt;  &amp;lt;union&amp;gt;  &amp;lt;query type=&quot;node&quot;&amp;gt;  &amp;lt;has-kv k...'''
date = "2015-01-02T13:42:00Z"
lastmod = "2015-01-02T14:40:00Z"
weight = 39971
keywords = [ "overpass", "api" ]
aliases = [ "/questions/39971" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass API Interpreter Help](/questions/39971/overpass-api-interpreter-help)

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
<span id="post-39971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39971-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-39971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm having trouble executing my query using the overpass-api.de API.</p>
<p>Error: line 3: parse error: not well-formed (invalid token)</p>
<p>My query is the following:</p>
<pre><code>&lt;osm-script timeout=&quot;300&quot;&gt;
  &lt;id-query {{nominatimArea:Mexico}} into=&quot;area&quot;/&gt;
  &lt;union&gt;
    &lt;query type=&quot;node&quot;&gt;
      &lt;has-kv k=&quot;amenity&quot; v=&quot;parking&quot;/&gt;
      &lt;area-query from=&quot;area&quot;/&gt;
    &lt;/query&gt;
    &lt;query type=&quot;way&quot;&gt;
      &lt;has-kv k=&quot;amenity&quot; v=&quot;parking&quot;/&gt;
      &lt;area-query from=&quot;area&quot;/&gt;
    &lt;/query&gt;
    &lt;query type=&quot;relation&quot;&gt;
      &lt;has-kv k=&quot;amenity&quot; v=&quot;parking&quot;/&gt;
      &lt;area-query from=&quot;area&quot;/&gt;
    &lt;/query&gt;
  &lt;/union&gt;
  &lt;print mode=&quot;body&quot;/&gt;
  &lt;recurse type=&quot;down&quot;/&gt;
  &lt;print mode=&quot;skeleton&quot; order=&quot;quadtile&quot;/&gt;
&lt;/osm-script&gt;</code></pre>
<p>Any suggestions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jan '15, 13:42</strong></p>
<img src="https://secure.gravatar.com/avatar/218b9190a505be909bd7e31c6ec79766?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="turgus&#39;s gravatar image" />
<p><span>turgus</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="turgus has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-39971" class="comments-container">
&#10;</div>
<div id="comment-tools-39971" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39971-form-container" class="comment-form-container">
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

<span id="39974"></span>

<div id="answer-container-39974" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39974-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39974-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-39974-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="turgus has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>{{nominatimArea:Mexico}} is overpass turbo specific (=syntactic sugar). Overpass API (the database backend) has no idea about this, hence the error message you get.</p>
<p>Just paste your query into overpass-turbo.eu and click on Export. What you're probably looking for is the link behind "raw data directly from Overpass API".</p>
<p>Before sending your query to Overpass API, overpass turbo will automatically replace this by</p>
<p>&lt;id-query type="area" ref="3600114686" into="area"/&gt;</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jan '15, 14:25</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jan '15, 14:29</strong> </span></p>
</div>
</div>
<div id="comments-container-39974" class="comments-container">
<span id="39976"></span>
<div id="comment-39976" class="comment">
<div id="post-39976-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Doing that, the second line became: &lt;id-query type="area" ref="3600114686" into="area"/&gt;</p>
<p>Is there anyway I can find out the ref number somehow without overpass turbo doing all the work?</p>
</div>
<div id="comment-39976-info" class="comment-info">
<span class="comment-age">(02 Jan '15, 14:29)</span> <span class="comment-user userinfo">turgus</span>
</div>
</div>
<span id="39977"></span>
<div id="comment-39977" class="comment">
<div id="post-39977-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes, sure, something along those lines:</p>
<p>&lt;query into="area" type="area"&gt; &lt;has-kv k="boundary" v="administrative"/&gt; &lt;has-kv k="ISO3166-1" v="MX"/&gt; &lt;/query&gt;</p>
</div>
<div id="comment-39977-info" class="comment-info">
<span class="comment-age">(02 Jan '15, 14:32)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="39978"></span>
<div id="comment-39978" class="comment">
<div id="post-39978-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a ton!</p>
</div>
<div id="comment-39978-info" class="comment-info">
<span class="comment-age">(02 Jan '15, 14:33)</span> <span class="comment-user userinfo">turgus</span>
</div>
</div>
<span id="39979"></span>
<div id="comment-39979" class="comment">
<div id="post-39979-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>overpass turbo link: <a href="http://overpass-turbo.eu/s/6Nb">http://overpass-turbo.eu/s/6Nb</a></p>
</div>
<div id="comment-39979-info" class="comment-info">
<span class="comment-age">(02 Jan '15, 14:33)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="39980"></span>
<div id="comment-39980" class="comment not_top_scorer">
<div id="post-39980-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, one last question. Let's say I had:</p>
<p>&lt;query into="area" type="area"&gt; &lt;has-kv k="boundary" v="administrative"/&gt; &lt;has-kv k="ISO3166-1" v="US"/&gt; &lt;/query&gt;</p>
<p>and wanted to get only the state Florida from US?</p>
<p>Edit: Nevermind, got it! Thanks again</p>
</div>
<div id="comment-39980-info" class="comment-info">
<span class="comment-age">(02 Jan '15, 14:36)</span> <span class="comment-user userinfo">turgus</span>
</div>
</div>
<span id="39982"></span>
<div id="comment-39982" class="comment">
<div id="post-39982-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Florida's relation (www.openstreetmap.org/relation/162050) is currently tagged as "ISO3166-2"= "US-FL", "admin_level"="4" and "boundary" = "administrative".</p>
<p>So I would probably use &lt;has-kv k="ISO3166-2" v="US-FL"/&gt; along with &lt;has-kv k="boundary" v="administrative"/&gt;</p>
</div>
<div id="comment-39982-info" class="comment-info">
<span class="comment-age">(02 Jan '15, 14:40)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-39974" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-39974-form-container" class="comment-form-container">
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

