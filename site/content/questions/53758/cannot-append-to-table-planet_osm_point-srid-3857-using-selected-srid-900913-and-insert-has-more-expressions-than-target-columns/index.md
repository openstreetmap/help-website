+++
type = "question"
title = "Cannot append to table planet_osm_point (SRID 3857) using selected SRID 900913, and &quot;INSERT has more expressions than target columns&quot;"
description = '''My openstreetmap database have import the asia.osm.pbf, and the gis database have import the planet-lastest.osm.pbf, when i make an edit on the openstreetmap db by iD editor, and use osmosis command to produce a changes.osc.gz file, then i use the &quot;osm2pgsql --append --slim -H 192.168.1.162 -P 5432 ...'''
date = "2016-12-30T13:57:00Z"
lastmod = "2017-01-02T10:32:00Z"
weight = 53758
keywords = [ "editing", "osm2pgsql" ]
aliases = [ "/questions/53758" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Cannot append to table planet_osm_point (SRID 3857) using selected SRID 900913, and "INSERT has more expressions than target columns"](/questions/53758/cannot-append-to-table-planet_osm_point-srid-3857-using-selected-srid-900913-and-insert-has-more-expressions-than-target-columns)

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
<span id="post-53758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53758-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My openstreetmap database have import the asia.osm.pbf, and the gis database have import the planet-lastest.osm.pbf, when i make an edit on the openstreetmap db by iD editor, and use osmosis command to produce a changes.osc.gz file, then i use the "<strong>osm2pgsql --append --slim -H 192.168.1.162 -P 5432 -d gis -U postgres -C 160 --number-processes 3 changes.osc.gz -e15 -o expire.list</strong>" command to import the changes.osc.gz into gis db, some error occurs, i don't know how to solve it. And i didn't find a solution on the internet, so i ask a question here, hope someone to help me.</p>
<p><img src="/upfiles/error1.png" alt="alt text" /></p>
<p>This error disappears when i add a projection parameter "-E 3857", but other error occurs, the detail error message is:</p>
<pre><code>osm2pgsql SVN version 0.82.0 (64bit id space)
Using projection SRS 3857 (EPSG:3857)
....
failed: ERROR:  INSERT has more expressions than target columns
LINE 1: ...oolean) AS INSERT INTO planet_osm_ways VALUES ($1,$2,$3,$4);
                                                               ^</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '16, 13:57</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jan '17, 10:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-53758" class="comments-container">
<span id="53759"></span>
<div id="comment-53759" class="comment">
<div id="post-53759-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>osm2pgsql's default projection is 900913, but your tables from first (and/or previous) import is in 3087. The simplest way round this is to add a projection parameter "-E 3857". (although 3857 &amp; 900913 are for most purposes identical, PostGIS does not know this)</p>
</div>
<div id="comment-53759-info" class="comment-info">
<span class="comment-age">(30 Dec '16, 15:35)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53758" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53758-form-container" class="comment-form-container">
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

<span id="53796"></span>

<div id="answer-container-53796" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53796-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="yuyy has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It appears that you have downgraded your osm2pgsql version from 0.92 or later to 0.82 after doing the first import. This would explain your initial problem (since 0.92 started using EPSG:3857 as the default, while earlier versions were using EPSG:900913), as well as your follow-on problem (because osm2pgsql 0.82 was using an additional column called "pending" on the database tables that was later removed).</p>
<p>While you found a valid workaround for the projection issue, a workaround for the missing columns would be more cumbersome. (See <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/docs/migrations.md">https://github.com/openstreetmap/osm2pgsql/blob/master/docs/migrations.md</a> for information on migrating osm2pgsql-imported data between versions, but note that 0.82 is so old that it might already warrant the attribute "ancient".)</p>
<p>You should be able to solve your problem by using <strong>the same osm2pgsql version</strong> for the initial import and the subsequent updates.</p>
<p><em>(Hat tip to lonvia and pnorman who told me this on IRC.)</em></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jan '17, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jan '17, 10:17</strong> </span></p>
</div>
</div>
<div id="comments-container-53796" class="comments-container">
&#10;</div>
<div id="comment-tools-53796" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53796-form-container" class="comment-form-container">
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

