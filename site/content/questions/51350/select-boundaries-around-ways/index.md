+++
type = "question"
title = "select boundaries around ways"
description = '''EDIT: using overpass-turbo I have been looking for all shop=alcohol in Poland and finding their respective administration boundaries since the addresses are seldom complete. So far I have this; [out:json][timeout:3000];  {{geocodeArea:Poland}}-&amp;gt;.searchArea;  node[shop=&quot;alcohol&quot;](area.searchArea)-...'''
date = "2016-08-11T15:25:00Z"
lastmod = "2016-08-11T15:58:00Z"
weight = 51350
keywords = [ "ways", "extract", "admin_boundary" ]
aliases = [ "/questions/51350" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [select boundaries around ways](/questions/51350/select-boundaries-around-ways)

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
<span id="post-51350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51350-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>EDIT: using overpass-turbo</strong></p>
<p>I have been looking for all shop=alcohol in Poland and finding their respective administration boundaries since the addresses are seldom complete.</p>
<p>So far I have this;</p>
<pre><code>[out:json][timeout:3000];
&#10;{{geocodeArea:Poland}}-&gt;.searchArea;
&#10;node[shop=&quot;alcohol&quot;](area.searchArea)-&gt;.posts;
&#10;foreach.posts(
  out;
  is_in;
  area._[admin_level~&quot;[467]&quot;];
  out ids;
);
&#10;// collect area details in 2nd step
.posts is_in;
area._[admin_level~&quot;[467]&quot;];
out;</code></pre>
<p>which is almost a direct copy from this post <a href="/questions/35976/add-reverse-geocoding-information-to-the-overpass-resulting-set">https://help.openstreetmap.org/questions/35976/add-reverse-geocoding-information-to-the-overpass-resulting-set</a></p>
<p>however I also need to add ways, since many of the shops have been charted that way. Therefore I tried the following;</p>
<pre><code>[out:json][timeout:3000];
&#10;{{geocodeArea:Poland}}-&gt;.searchArea;
&#10;node[shop=&quot;alcohol&quot;](area.searchArea)-&gt;.posts;
way[shop=&quot;alcohol&quot;](area.searchArea)-&gt;.posts;
&#10;foreach.posts(
  out;
  is_in;
  area._[admin_level~&quot;[467]&quot;];
  out ids;
);
&#10;// collect area details in 2nd step
.posts is_in;
area._[admin_level~&quot;[467]&quot;];
out;</code></pre>
<p>However this bugs out and the auto help, well...doesn't.</p>
<p>Anyone?</p>
<p>Thanks in advance;</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Aug '16, 15:25</strong></p>
<img src="https://secure.gravatar.com/avatar/688fe2a76a5d3843e2030260215159d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scass&#39;s gravatar image" />
<p><span>scass</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scass has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Aug '16, 15:41</strong> </span></p>
</div>
</div>
<div id="comments-container-51350" class="comments-container">
&#10;</div>
<div id="comment-tools-51350" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51350-form-container" class="comment-form-container">
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

<span id="51351"></span>

<div id="answer-container-51351" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51351-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="scass has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are basically two issues in your second query:</p>
<ol>
<li>Inputset union is needed to store all nodes and ways in .posts</li>
<li><code>is_in;</code> does only work on nodes, that's why an additional recursion step is needed as well to turn ways into their respective nodes - namely (<code>._;&gt;;);</code> and <code>(.posts;&gt;;);</code> in the query below.</li>
</ol>
<p>Here's how the query should look like:</p>
<pre><code>[out:json][timeout:3000];
&#10;{{geocodeArea:Poland}}-&gt;.searchArea;
&#10;(node[shop=&quot;alcohol&quot;](area.searchArea);
 way[shop=&quot;alcohol&quot;](area.searchArea);)-&gt;.posts;
&#10;foreach.posts(
  out center;
  (._;&gt;;);
  is_in;
  area._[admin_level~&quot;[467]&quot;];
  out ids;
);
&#10;// collect area details in 2nd step
(.posts;&gt;;);
is_in;
area._[admin_level~&quot;[467]&quot;];
out;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '16, 15:52</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Aug '16, 15:55</strong> </span></p>
</div>
</div>
<div id="comments-container-51351" class="comments-container">
<span id="51352"></span>
<div id="comment-51352" class="comment">
<div id="post-51352-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>this appears to work perfectly, i'm going to have to read into recursion syntax.</p>
<p>Thanks for your help</p>
</div>
<div id="comment-51352-info" class="comment-info">
<span class="comment-age">(11 Aug '16, 15:58)</span> <span class="comment-user userinfo">scass</span>
</div>
</div>
</div>
<div id="comment-tools-51351" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51351-form-container" class="comment-form-container">
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

