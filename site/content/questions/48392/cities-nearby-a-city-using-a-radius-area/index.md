+++
type = "question"
title = "Cities nearby a city using a radius area"
description = '''I would like know how I can get in a json output format the cities around a city. For example: Cities around &quot;London&quot; in 10 km. I read about &quot;around&quot; http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Relative_to_other_elements_.28around.29 And querying about interest poins nearby (like caf...'''
date = "2016-02-28T00:09:00Z"
lastmod = "2016-02-29T13:09:00Z"
weight = 48392
keywords = [ "cities", "radius", "around" ]
aliases = [ "/questions/48392" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cities nearby a city using a radius area](/questions/48392/cities-nearby-a-city-using-a-radius-area)

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
<span id="post-48392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48392-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like know how I can get in a json output format the cities around a city.</p>
<p>For example:</p>
<p>Cities around "London" in 10 km.</p>
<p>I read about "around" http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Relative_to_other_elements_.28around.29</p>
<p>And querying about interest poins nearby (like cafe or bar)</p>
<p><a href="http://stackoverflow.com/questions/16442663/how-to-get-point-of-interest-near-my-point-using-overpass-api">http://stackoverflow.com/questions/16442663/how-to-get-point-of-interest-near-my-point-using-overpass-api</a></p>
<p>But I don't know how I can fetch this.</p>
<p>Could be something like? For example nearby cities in Madrid in 10 km:</p>
<pre><code>[out:json];node(name=&quot;Madrid&quot;)[around:10000];out;</code></pre>
<p>I am trying to achieve this for a PHP script, so I plan use a curl request with the OverPass API.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-cities" rel="tag" title="see questions tagged &#39;cities&#39;">cities</span> <span class="post-tag tag-link-radius" rel="tag" title="see questions tagged &#39;radius&#39;">radius</span> <span class="post-tag tag-link-around" rel="tag" title="see questions tagged &#39;around&#39;">around</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Feb '16, 00:09</strong></p>
<img src="https://secure.gravatar.com/avatar/e705b40159e5ad11fcbc25776403e1cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shakaran&#39;s gravatar image" />
<p><span>shakaran</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shakaran has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48392" class="comments-container">
&#10;</div>
<div id="comment-tools-48392" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48392-form-container" class="comment-form-container">
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

<span id="48413"></span>

<div id="answer-container-48413" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48413-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-48413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When working with Overpass API, it's good to use <a href="http://overpass-turbo.eu/">Overpass turbo</a> (a web-IDE written around Overpass API) to test your queries.</p>
<p>Overpass turbo will also give you error messages</p>
<p>Now, for the actual question. First you need to create the input set of the "around" command (or you need to know the coordinates you want to query around). That depends a bit on the place you want to query. Some names are used for a lot of different places, so finding a good selector for it is crucial</p>
<p>In the example of Madrid, you will see that there are 22 places called Madrid, while there's only one city called Madrid. Compare the following two queries in Overpass Turbo:</p>
<pre><code>node[&quot;place&quot;][&quot;name&quot;=&quot;Madrid&quot;];
out;
&#10;node[&quot;place&quot;=&quot;city&quot;][&quot;name&quot;=&quot;Madrid&quot;];
out;</code></pre>
<p>When you have found a good selector (based on tags or any other criterium Overpass can handle), you need to save that point into a set, let's call the set "center":</p>
<pre><code>node[&quot;place&quot;=&quot;city&quot;][&quot;name&quot;=&quot;Madrid&quot;]-&gt;.center;</code></pre>
<p>Now that you have the central node, you can use the around command to query everything around Madrid, like this:</p>
<pre><code>node[&quot;place&quot;=&quot;city&quot;][&quot;name&quot;=&quot;Madrid&quot;]-&gt;.center;
node(around.center:10000);</code></pre>
<p>But this will query every single object in that area (and will probably be too big for your browser to handle). So then you need to filter the results further with other filters. F.e. related to your query, all places near Madrid (cities are usually further apart than 10km, so that wouldn't yield any results).</p>
<p>So the full query looks like this.</p>
<pre><code>node[&quot;place&quot;=&quot;city&quot;][&quot;name&quot;=&quot;Madrid&quot;]-&gt;.center;
node(around.center:10000)[&quot;place&quot;];
out;</code></pre>
<p>And when you execute the query, you'll see the results: <a href="http://overpass-turbo.eu/s/eHb">http://overpass-turbo.eu/s/eHb</a></p>
<p>When you're finished, you can use one of the export functions of Overpass Turbo to get it formatted as a nice URL (without useless whitespace and with fully escaped special characters).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Feb '16, 13:09</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-48413" class="comments-container">
&#10;</div>
<div id="comment-tools-48413" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48413-form-container" class="comment-form-container">
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

