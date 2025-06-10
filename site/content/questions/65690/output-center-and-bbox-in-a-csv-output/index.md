+++
type = "question"
title = "Output Center and BBOX in a CSV output"
description = '''I am using something as the code below, but need something as ::center of the relations (the ::lat and ::lon are only for nodes) and ::bbox.... What the syntax this kind of output? [out:csv(::id,::type,wikidata,place, boundary,::center,::bbox)] ; relation (298285) -&amp;gt; .c ; .c map_to_area -&amp;gt; .my...'''
date = "2018-09-02T15:40:00Z"
lastmod = "2018-09-03T01:59:00Z"
weight = 65690
keywords = [ "overpass" ]
aliases = [ "/questions/65690" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Output Center and BBOX in a CSV output](/questions/65690/output-center-and-bbox-in-a-csv-output)

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
<span id="post-65690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65690-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using something as the code below, but need something as <code>::center</code> of the <em>relations</em> (the <code>::lat</code> and <code>::lon</code> are only for <em>nodes</em>) and <code>::bbox</code>.... What the syntax this kind of output?</p>
<pre><code>[out:csv(::id,::type,wikidata,place, boundary,::center,::bbox)] ;
relation   (298285) -&gt; .c ;
.c map_to_area -&gt; .myarea ;
( 
  node (area.myarea)  [place] [wikidata] ;
  relation  (area.myarea) [boundary] [wikidata];  
);
out meta ;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '18, 15:40</strong></p>
<img src="https://secure.gravatar.com/avatar/6963015ca2c3146e2a2a348b7fcb793b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppKrauss&#39;s gravatar image" />
<p><span>ppKrauss</span><br />
<span class="score" title="95 reputation points">95</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppKrauss has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65690" class="comments-container">
&#10;</div>
<div id="comment-tools-65690" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65690-form-container" class="comment-form-container">
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

<span id="65691"></span>

<div id="answer-container-65691" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65691-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://overpass-turbo.eu/s/Bzw">Just use <code>out center</code></a> to get the <code>::lat</code> and <code>::lon</code> for the relation centers.</p>
<pre><code>[out:csv(::id,::type,::lat,::lon,wikidata,place, boundary)] ;
area(3600298285)-&gt; .myarea ;
( 
  node (area.myarea)  [place] [wikidata] ;
  relation  (area.myarea) [boundary] [wikidata];  
);
out center meta;</code></pre>
<p>I don't know if there is a way to get a bbox in csv output.</p>
<p>(<a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_area_.28area.29">There's info in the docs about directly looking up areas based on the OSM id they are generated from</a>)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '18, 16:10</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-65691" class="comments-container">
<span id="65692"></span>
<div id="comment-65692" class="comment">
<div id="post-65692-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, 50% of the answer (!)... If there are no manner to obtain BBOX, the answer will be 100%, so accepted. Lets wait some comment about existence of BBOX solution.</p>
</div>
<div id="comment-65692-info" class="comment-info">
<span class="comment-age">(02 Sep '18, 16:46)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
<span id="65693"></span>
<div id="comment-65693" class="comment">
<div id="post-65693-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You could do a separate query to get the bounds. <a href="http://overpass-turbo.eu/s/Bzz">http://overpass-turbo.eu/s/Bzz</a></p>
<p>(of course for nodes it doesn't return anything)</p>
<p>But I don't think there is any way to access the bounds using csv fields.</p>
</div>
<div id="comment-65693-info" class="comment-info">
<span class="comment-age">(02 Sep '18, 17:46)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="65702"></span>
<div id="comment-65702" class="comment">
<div id="post-65702-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, yes, I must to change my goal, from CSV to JSON, that is the solution for any output...</p>
</div>
<div id="comment-65702-info" class="comment-info">
<span class="comment-age">(03 Sep '18, 01:59)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
</div>
<div id="comment-tools-65691" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65691-form-container" class="comment-form-container">
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

