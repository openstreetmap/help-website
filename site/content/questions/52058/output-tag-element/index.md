+++
type = "question"
title = "output tag element"
description = '''I currently have a query that is outputting shops (nodes &amp;amp; ways) and the area ids they belong in. I also have a list of the areas details in the second step. Since some of the areas have the same ids, I also need to output the admin_level in each for each of the areas in the first query, so that...'''
date = "2016-09-15T14:49:00Z"
lastmod = "2016-09-15T14:49:00Z"
weight = 52058
keywords = [ "overpass", "export", "tags" ]
aliases = [ "/questions/52058" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [output tag element](/questions/52058/output-tag-element)

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
<span id="post-52058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52058-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I currently have a query that is outputting shops (nodes &amp; ways) and the area ids they belong in. I also have a list of the areas details in the second step. Since some of the areas have the same ids, I also need to output the admin_level in each for each of the areas in the first query, so that I can tie them up to the areas in the second query. Does anyone know what I need to add to</p>
<p><code>out ids;</code></p>
<p>to get the admin level?</p>
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
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Sep '16, 14:49</strong></p>
<img src="https://secure.gravatar.com/avatar/688fe2a76a5d3843e2030260215159d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scass&#39;s gravatar image" />
<p><span>scass</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scass has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52058" class="comments-container">
&#10;</div>
<div id="comment-tools-52058" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52058-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

