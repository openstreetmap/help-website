+++
type = "question"
title = "Memorial queries with other conditions"
description = '''Hello, perhaps a simple question as I&#x27;m new to the coding here: I&#x27;m looking to build a query to search for memorials/monuments that contains a term like &quot;synagoge&quot; or &quot;ehemalige Synagoge&quot; (Case insesitive search)  So not an actual Synagoge itself, but a memorial to a former &#x27;synagoge&#x27; that may be in...'''
date = "2022-12-03T21:20:00Z"
lastmod = "2022-12-05T12:13:00Z"
weight = 86298
keywords = [ "memorials" ]
aliases = [ "/questions/86298" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Memorial queries with other conditions](/questions/86298/memorial-queries-with-other-conditions)

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
<span id="post-86298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86298-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, perhaps a simple question as I'm new to the coding here:</p>
<p>I'm looking to build a query to search for memorials/monuments that contains a term like "synagoge" or "ehemalige Synagoge" (Case insesitive search) So not an actual Synagoge itself, but a memorial to a former 'synagoge' that may be in the title, or the inscription of the plaque. Looking for a query to run in overpass that will allow me to only search monuments/memorials by adding a keyword (in this case looking for monuments to former synagogues in Germany)</p>
<p>Would like to apply this query to a number of texts for descriptions/inscriptions of memorials in Germany.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-memorials" rel="tag" title="see questions tagged &#39;memorials&#39;">memorials</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Dec '22, 21:20</strong></p>
<img src="https://secure.gravatar.com/avatar/3c5725d189f1abc0bf3d5a98e4176c94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shaughi&#39;s gravatar image" />
<p><span>shaughi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shaughi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86298" class="comments-container">
&#10;</div>
<div id="comment-tools-86298" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86298-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="86300"></span>

<div id="answer-container-86300" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86300-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As a starter I tried the following overpass query:</p>
<pre><code>[out:json][timeout:25];
// fetch area “Berlin” to search in
{{geocodeArea:Berlin}}-&gt;.searchArea;
// gather results
(
 node[&quot;historic&quot;=&quot;memorial&quot;][&quot;description&quot;~&quot;synagoge&quot;,i](area.searchArea);
 way[&quot;historic&quot;=&quot;memorial&quot;][&quot;description&quot;~&quot;synagoge&quot;,i](area.searchArea);
 relation[&quot;historic&quot;=&quot;memorial&quot;][&quot;description&quot;~&quot;synagoge&quot;,i](area.searchArea);
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>see: <a href="http://overpass-turbo.eu/s/1oFM">http://overpass-turbo.eu/s/1oFM</a></p>
<p>Now this query relies on the word "Synagoge" (case insensitive) being used in the description tag, so it won't find an object where there is no "Synagoge in the description tag.</p>
<p>So I tried a second query, this time checking for the inscription tag finding some more places:</p>
<pre><code>[out:json][timeout:25];
// fetch area “Berlin” to search in
{{geocodeArea:Berlin}}-&gt;.searchArea;
// gather results
(
node[&quot;historic&quot;=&quot;memorial&quot;][&quot;inscription&quot;~&quot;synagoge&quot;,i](area.searchArea);
way[&quot;historic&quot;=&quot;memorial&quot;][&quot;inscription&quot;~&quot;synagoge&quot;,i](area.searchArea);
relation[&quot;historic&quot;=&quot;memorial&quot;][&quot;inscription&quot;~&quot;synagoge&quot;,i](area.searchArea);
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>see: <a href="http://overpass-turbo.eu/s/1oFP">http://overpass-turbo.eu/s/1oFP</a></p>
<p>Edit: Ok, found a way to combine those two searches, a UNION in Overpass QL (maybe there is a better way but this works) - so searching for objects that are tagged as historic=memorial and have the word Synagoge (case insensitive) either in description or inscription (or in both):</p>
<pre><code>[out:json][timeout:25];
// fetch area “Berlin” to search in
{{geocodeArea:Berlin}}-&gt;.searchArea;
// gather results
(
node[&quot;historic&quot;=&quot;memorial&quot;][&quot;description&quot;~&quot;synagoge&quot;,i](area.searchArea);
node[&quot;historic&quot;=&quot;memorial&quot;][&quot;inscription&quot;~&quot;synagoge&quot;,i](area.searchArea);
way[&quot;historic&quot;=&quot;memorial&quot;][&quot;description&quot;~&quot;synagoge&quot;,i](area.searchArea);
way[&quot;historic&quot;=&quot;memorial&quot;][&quot;inscription&quot;~&quot;synagoge&quot;,i](area.searchArea);
relation[&quot;historic&quot;=&quot;memorial&quot;][&quot;description&quot;~&quot;synagoge&quot;,i](area.searchArea);
relation[&quot;historic&quot;=&quot;memorial&quot;][&quot;inscription&quot;~&quot;synagoge&quot;,i](area.searchArea);
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>see: <a href="https://overpass-turbo.eu/s/1oFU">https://overpass-turbo.eu/s/1oFU</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Dec '22, 09:22</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Dec '22, 09:47</strong> </span></p>
</div>
</div>
<div id="comments-container-86300" class="comments-container">
&#10;</div>
<div id="comment-tools-86300" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86300-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86302"></span>

<div id="answer-container-86302" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86302-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks! I think this does it. The only addition would be to search the name as some are listed very simply. Wiesbaden, for example produces this result</p>
<pre><code>[out:json][timeout:25];</code></pre>
<p>// fetch area “Wiesbaden” to search in {{geocodeArea:Wiesbaden}}-&gt;.searchArea; // gather results ( node["historic"="memorial"]<a href="area.searchArea">"description"~"synagoge",i</a>; node["historic"="memorial"]<a href="area.searchArea">"inscription"~"synagoge",i</a>; node["historic"="memorial"]<a href="area.searchArea">"name"~"synagoge",i</a>; way["historic"="memorial"]<a href="area.searchArea">"description"~"synagoge",i</a>; way["historic"="memorial"]<a href="area.searchArea">"inscription"~"synagoge",i</a>; way["historic"="memorial"]<a href="area.searchArea">"name"~"synagoge",i</a>; relation["historic"="memorial"]<a href="area.searchArea">"description"~"synagoge",i</a>; relation["historic"="memorial"]<a href="area.searchArea">"inscription"~"synagoge",i</a>; relation["historic"="memorial"]<a href="area.searchArea">"name"~"synagoge",i</a>; ); // print results out body;</p>
<blockquote>
<p>; out skel qt;</p>
</blockquote>
<p><a href="https://overpass-turbo.eu/s/1oGj">https://overpass-turbo.eu/s/1oGj</a></p>
<p><em>Or is the name search not the right way to go here</em>? When I try to change the geocodeArea to a larger region, like Berlin or Hessen, I get a time out error. Ultimately, I'd like to run this query for the entire country of Germany.</p>
<p>Thanks again for the help!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Dec '22, 11:59</strong></p>
<img src="https://secure.gravatar.com/avatar/3c5725d189f1abc0bf3d5a98e4176c94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shaughi&#39;s gravatar image" />
<p><span>shaughi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shaughi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86302" class="comments-container">
&#10;</div>
<div id="comment-tools-86302" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86302-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86303"></span>

<div id="answer-container-86303" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86303-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86303-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86303-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Note: Increased the timeout and was able to query larger area. ! Let me know if the name search is the right way to go, but it appear to work!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Dec '22, 12:13</strong></p>
<img src="https://secure.gravatar.com/avatar/3c5725d189f1abc0bf3d5a98e4176c94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shaughi&#39;s gravatar image" />
<p><span>shaughi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shaughi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86303" class="comments-container">
&#10;</div>
<div id="comment-tools-86303" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86303-form-container" class="comment-form-container">
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

