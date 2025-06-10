+++
type = "question"
title = "how to identify parts of the same osm_id in planet_osm_polygon?"
description = '''The relation 303702 and many others in the table planet_osm_polygon have same osm_id, so, same ID and no other id (eg. z_order is zero)... There are a column that I not see? How to configure osm2pgsql to add a gid or any complement to add a counter for each &quot;multiple osm_id&quot;?'''
date = "2018-10-05T12:44:00Z"
lastmod = "2018-10-05T15:37:00Z"
weight = 66170
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/66170" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to identify parts of the same osm_id in planet_osm_polygon?](/questions/66170/how-to-identify-parts-of-the-same-osm_id-in-planet_osm_polygon)

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
<span id="post-66170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66170-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The relation <a href="https://www.openstreetmap.org/relation/303702">303702</a> and many others in the table <code>planet_osm_polygon</code> have same <code>osm_id</code>, so, same ID and no other id (eg. <code>z_order</code> is zero)... There are a column that I not see? How to configure <code>osm2pgsql</code> to add a <code>gid</code> or any complement to add a counter for each "multiple osm_id"?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Oct '18, 12:44</strong></p>
<img src="https://secure.gravatar.com/avatar/6963015ca2c3146e2a2a348b7fcb793b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppKrauss&#39;s gravatar image" />
<p><span>ppKrauss</span><br />
<span class="score" title="95 reputation points">95</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppKrauss has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66170" class="comments-container">
&#10;</div>
<div id="comment-tools-66170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66170-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="66171"></span>

<div id="answer-container-66171" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66171-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could use the <code>--multi-geometry</code> flag with osm2pgsql which should get rid of <em>most</em> of these cases (instead, they would all be combined in one record with a multipolygon or multilinestring geometry). Other than that you could follow the standard postgres recommendations of adding an integer column and populating it with a default value that uses a sequence, as explained e.g. in <a href="https://stackoverflow.com/questions/9490014/adding-serial-to-existing-column-in-postgres">https://stackoverflow.com/questions/9490014/adding-serial-to-existing-column-in-postgres</a> - there's no particular osm2pgsql option that would do this for you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Oct '18, 13:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-66171" class="comments-container">
<span id="66174"></span>
<div id="comment-66174" class="comment">
<div id="post-66174-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The <code>--multi-geometry</code> is a good clue, I will test in the next planet-conversion... And will back here with results. If there are no complete solution, my answer below is a workaround using pure SQL and perhaps <code>ALTER TABLE</code> (adding UNIQUE clause to index it) enhance performance.</p>
</div>
<div id="comment-66174-info" class="comment-info">
<span class="comment-age">(05 Oct '18, 15:37)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
</div>
<div id="comment-tools-66171" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66171-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66172"></span>

<div id="answer-container-66172" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66172-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If it is the truth, as @FraderikRamm say "there's no particular osm2pgsql option that would do this for you"... The only solution is by SQL,</p>
<pre><code>select osm_id, row_number() OVER (PARTITION BY osm_id) as sub_id 
from planet_osm_polygon</code></pre>
<p>so, now we have a UNIQUE(osm_id,sub_id).</p>
<hr />
<h2 id="complete-solution">Complete solution</h2>
<p>(can be repeated changing table name)</p>
<pre><code>ALTER TABLE planet_osm_polygon ADD COLUMN osm_id2 int;
UPDATE planet_osm_polygon
SET  osm_id2 = sub_id
FROM (
  SELECT osm_id, way, row_number() OVER (PARTITION BY osm_id) as sub_id 
  FROM planet_osm_polygon
) t WHERE t.osm_id=planet_osm_polygon.osm_id AND t.way=planet_osm_polygon.way
;
ALTER TABLE planet_osm_polygon ALTER COLUMN osm_id2 SET NOT NULL;
ALTER TABLE planet_osm_polygon ADD CONSTRAINT osm_uniqids UNIQUE(osm_id,osm_id2);</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Oct '18, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/6963015ca2c3146e2a2a348b7fcb793b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppKrauss&#39;s gravatar image" />
<p><span>ppKrauss</span><br />
<span class="score" title="95 reputation points">95</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppKrauss has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Oct '18, 00:27</strong> </span></p>
</div>
</div>
<div id="comments-container-66172" class="comments-container">
&#10;</div>
<div id="comment-tools-66172" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66172-form-container" class="comment-form-container">
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

