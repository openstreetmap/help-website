+++
type = "question"
title = "variable inside overpass query"
description = '''How can I pass a variable inside a overpass-turbo query?  Typically (with Spyder) the query would be: query = &quot;&quot;&quot;[out:json][timeout:25]; //gather results (// query part for: “university”  way[&#x27;name&#x27;=&#x27;Cape Peninsula University of Technology (Bellville Campus)&#x27;]; );//print results out body; &amp;gt;; out ...'''
date = "2021-07-12T19:09:00Z"
lastmod = "2021-07-15T20:44:00Z"
weight = 80935
keywords = [ "overpass-turbo" ]
aliases = [ "/questions/80935" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [variable inside overpass query](/questions/80935/variable-inside-overpass-query)

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
<span id="post-80935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80935-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I pass a variable inside a overpass-turbo query? Typically (with Spyder) the query would be:</p>
<pre><code>query = &quot;&quot;&quot;[out:json][timeout:25];
//gather results
(// query part for: “university”
 way[&#39;name&#39;=&#39;Cape Peninsula University of Technology (Bellville Campus)&#39;];
);//print results
out body;
&gt;;
out skel qt;&quot;&quot;&quot;
url = &quot;http://overpass-api.de/api/interpreter&quot;
r = requests.get(url, params={&#39;data&#39;: query})
area = osm2geojson.json2geojson(r.json())</code></pre>
<p>I want to read a parameter from a basic json and pass it to the query. Something like:</p>
<pre><code>jparams = json.load(open(&#39;params.json&#39;))
&#10;query = &quot;&quot;&quot;[out:json][timeout:25];
//gather results
(// query part for: “university”
way[&#39;name&#39;=jparams[&#39;read-variable&#39;]];
);//print results
out body;
&gt;;
out skel qt;&quot;&quot;&quot;
url = &quot;http://overpass-api.de/api/interpreter&quot;
r = requests.get(url, params={&#39;data&#39;: query})
area = osm2geojson.json2geojson(r.json())</code></pre>
<p>How would I do this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '21, 19:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a235da08f7d6877654b16dfe832aed66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arkriger&#39;s gravatar image" />
<p><span>arkriger</span><br />
<span class="score" title="155 reputation points">155</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arkriger has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80935" class="comments-container">
&#10;</div>
<div id="comment-tools-80935" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80935-form-container" class="comment-form-container">
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

<span id="80937"></span>

<div id="answer-container-80937" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80937-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="arkriger has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You want some variation of Python's string format: <a href="https://docs.python.org/3/library/stdtypes.html#str.format">https://docs.python.org/3/library/stdtypes.html#str.format</a></p>
<p>The code will be similar to this:</p>
<pre><code>query = &quot;&quot;&quot;[out:json][timeout:25];
//gather results
(// query part for: “university”
way[&#39;name&#39;=&#39;{}&#39;];
);//print results
out body;
&gt;;
out skel qt;&quot;&quot;&quot;.format(jparams[&#39;variable&#39;])</code></pre>
<p>There's lots of flexibility in exactly how you put it all together, using a named placeholder, f strings (which are closer to your example probably), and on and on.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '21, 21:32</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-80937" class="comments-container">
<span id="80986"></span>
<div id="comment-80986" class="comment">
<div id="post-80986-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://github.com/AdrianKriger/osm_LoD1_3DCityModel">result</a>. infinitely more effective. Thank you.</p>
</div>
<div id="comment-80986-info" class="comment-info">
<span class="comment-age">(15 Jul '21, 20:44)</span> <span class="comment-user userinfo">arkriger</span>
</div>
</div>
</div>
<div id="comment-tools-80937" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80937-form-container" class="comment-form-container">
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

