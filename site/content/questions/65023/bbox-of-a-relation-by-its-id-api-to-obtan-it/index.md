+++
type = "question"
title = "BBOX of a relation by its ID, API to obtan it"
description = '''I have the ID of the relation, and I need a API that returns its boundary box. Example: the relation 298204, openstreetmap.org/relation/298204... Where its boundary box?  PS: I need BBOX in standard format (ex. to use in Overpass).'''
date = "2018-07-30T16:48:00Z"
lastmod = "2018-07-30T23:47:00Z"
weight = 65023
keywords = [ "bbox", "relations" ]
aliases = [ "/questions/65023" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [BBOX of a relation by its ID, API to obtan it](/questions/65023/bbox-of-a-relation-by-its-id-api-to-obtan-it)

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
<span id="post-65023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65023-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have the ID of the relation, and I need a API that returns its boundary box.</p>
<p>Example: the relation 298204, <a href="https://www.openstreetmap.org/relation/298204"><code>openstreetmap.org/relation/298204</code></a>... Where its boundary box?</p>
<p>PS: I need BBOX in standard format (ex. to use in Overpass).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '18, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/6963015ca2c3146e2a2a348b7fcb793b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppKrauss&#39;s gravatar image" />
<p><span>ppKrauss</span><br />
<span class="score" title="95 reputation points">95</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppKrauss has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jul '18, 18:34</strong> </span></p>
</div>
</div>
<div id="comments-container-65023" class="comments-container">
<span id="65025"></span>
<div id="comment-65025" class="comment">
<div id="post-65025-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you know the relation ID, you can use this straight in Overpass. Are you trying to find all places within (in this case) São Paulo</p>
</div>
<div id="comment-65025-info" class="comment-info">
<span class="comment-age">(30 Jul '18, 17:16)</span> <span class="comment-user userinfo">andrewblack</span>
</div>
</div>
<span id="65028"></span>
<div id="comment-65028" class="comment">
<div id="post-65028-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/9571/andrewblack"></a><a href="https://help.openstreetmap.org/users/9571/andrewblack">@andrewblack</a>, thanks. Well, the question was oriented to BBOX but will be welcome an extra "how to use relation ID with overpass" (instead BBOX, as spatial mask to the query).</p>
</div>
<div id="comment-65028-info" class="comment-info">
<span class="comment-age">(30 Jul '18, 18:38)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
</div>
<div id="comment-tools-65023" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65023-form-container" class="comment-form-container">
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

<span id="65035"></span>

<div id="answer-container-65035" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65035-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ppKrauss has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<h1 id="finding-the-bounding-box">Finding the bounding box</h1>
<pre><code>relation   (298204) ;
out  bb ;</code></pre>
<p>gives the information you want (but not quite in the right format. A bit if editing will get it.</p>
<pre><code>bounds minlat=&quot;-25.4832679&quot; minlon=&quot;-53.1090000&quot; maxlat=&quot;-19.7823272&quot; maxlon=&quot;-44.1610000&quot;</code></pre>
<h1 id="using-a-relation-within-overpass">Using a relation within Overpass</h1>
<p>Assuming you want to do the query mentioned in <a href="/questions/65020/best-way-to-retrieve-a-csv-table-from-overpass">Best way to retrieve a CSV table from Overpass</a> , the following query uses the area defined by the relation, rather than a bounding box.</p>
<pre><code>[out:csv(::id,::user,::type,wikidata,name,place, boundary)] ;
relation   (298204) -&gt; .c ;
.c map_to_area -&gt; .myarea ;
( 
  node (area.myarea)  [place] [wikidata] ;
  relation  (area.myarea) [boundary] [wikidata];  
);
out meta ;</code></pre>
<p>In a bit more detail</p>
<ul>
<li>Load the relation into set <strong>c</strong></li>
<li>Create an area from set c.</li>
<li>run the query - <strong>(area.myarea)</strong> restricts it to this area</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jul '18, 23:47</strong></p>
<img src="https://secure.gravatar.com/avatar/ba18d96cf193429ae1a16c30828ef58d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andrewblack&#39;s gravatar image" />
<p><span>andrewblack</span><br />
<span class="score" title="365 reputation points">365</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andrewblack has 4 accepted answers">57%</span></p>
</div>
</div>
<div id="comments-container-65035" class="comments-container">
&#10;</div>
<div id="comment-tools-65035" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65035-form-container" class="comment-form-container">
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

