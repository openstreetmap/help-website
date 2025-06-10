+++
type = "question"
title = "Overpass API: full building address query"
description = '''My bounding box is this: 41.7679,12.2622,41.7732,12.2707 I am trying to extract the full address of all polygons in this bounding box, and at the moment I can only extract the polygons and their ID&#x27;s.  Any idea on how this query should look like? // i thought this is how you &quot;constrain&quot; the query in...'''
date = "2016-07-12T16:19:00Z"
lastmod = "2016-07-12T21:23:00Z"
weight = 50880
keywords = [ "overpass" ]
aliases = [ "/questions/50880" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API: full building address query](/questions/50880/overpass-api-full-building-address-query)

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
<span id="post-50880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50880-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My bounding box is this: 41.7679,12.2622,41.7732,12.2707</p>
<p>I am trying to extract the full address of all polygons in this bounding box, and at the moment I can only extract the polygons and their ID's.</p>
<p>Any idea on how this query should look like?</p>
<pre><code>// i thought this is how you &quot;constrain&quot; the query in a bounding box
way(41.7679,12.2622,41.7732,12.2707);
((
// Query all buildings
  way[building=yes];
// and remove ...
  - 
// all buildings with a tag that doesn&#39;t start with letter &#39;b&#39;
  way[building=yes][~&quot;^[^b].*$&quot;~&quot;.&quot;]; 
); &gt;; );
out;</code></pre>
<p>Any suggestion would be greately appreciated, I couldn't find any sample query to extract the full address of those polygons.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '16, 16:19</strong></p>
<img src="https://secure.gravatar.com/avatar/1cca2aa74a362990b93740123b6059c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MarkAllenLU&#39;s gravatar image" />
<p><span>MarkAllenLU</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MarkAllenLU has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50880" class="comments-container">
<span id="50884"></span>
<div id="comment-50884" class="comment">
<div id="post-50884-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Overpass API is not a geocoder. You might want to look at Nominatim instead for full addresses.</p>
</div>
<div id="comment-50884-info" class="comment-info">
<span class="comment-age">(12 Jul '16, 21:23)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-50880" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50880-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

