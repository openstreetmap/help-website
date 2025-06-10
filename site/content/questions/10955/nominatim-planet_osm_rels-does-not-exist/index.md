+++
type = "question"
title = "Nominatim: planet_osm_rels does not exist"
description = '''Hi, i&#x27;m doing a setup.php -all for a full planet.pbf, after all steps without errors(aparently) when i exec --index option appears this errors: what&#x27;s the meaning of these errors?  Starting rank 25  Done 19 in 0 @ 19.000000 per second - ETA (seconds): 2187.684326 Done 210 in 1 @ 210.000000 per secon...'''
date = "2012-03-03T02:27:00Z"
lastmod = "2012-05-02T18:58:00Z"
weight = 10955
keywords = [ "nominatim", "installation", "install" ]
aliases = [ "/questions/10955" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim: planet_osm_rels does not exist](/questions/10955/nominatim-planet_osm_rels-does-not-exist)

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
<span id="post-10955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10955-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>i'm doing a setup.php -all for a full planet.pbf, after all steps without errors(aparently) when i exec --index option appears this errors:</p>
<p>what's the meaning of these errors?</p>
<hr />
<p>Starting rank 25 Done 19 in 0 @ 19.000000 per second - ETA (seconds): 2187.684326</p>
<p>Done 210 in 1 @ 210.000000 per second - ETA (seconds): 197.023804</p>
<p>Done 258 in 1 @ 258.000000 per second - ETA (seconds): 160.182175</p>
<p>index_placex: UPDATE failed: ERROR: relation "planet_osm_rels" does not exist</p>
<p>LINE 1: select * from planet_osm_rels where parts @&gt; ARRAY[NEW.osm_i... ^ QUERY: select * from planet_osm_rels where parts @&gt; ARRAY[NEW.osm_id::integer] and members @&gt; ARRAY['n'||NEW.osm_id]</p>
<p>CONTEXT: PL/pgSQL function "placex_update" line 112 at FOR over SELECT rows</p>
<p>index_placex: UPDATE failed: ERROR: relation "planet_osm_rels" does not exist</p>
<p>LINE 1: select * from planet_osm_rels where parts @&gt; ARRAY[NEW.osm_i...</p>
<p>.... ... .... same error</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Mar '12, 02:27</strong></p>
<img src="https://secure.gravatar.com/avatar/9c330cb7225d0a8d2f82a7438b76b608?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="luup2k&#39;s gravatar image" />
<p><span>luup2k</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="luup2k has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Mar '12, 09:00</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-10955" class="comments-container">
<span id="10957"></span>
<div id="comment-10957" class="comment">
<div id="post-10957-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i'm using setup.php script</p>
<hr />
<p>passthru($osm2pgsql.' -lsc -O gazetteer -C 9000 --hstore -d '.$aDSNInfo['database'].' '.$aCMDResult['osm-file']);</p>
<hr />
<p><em></em></p>
<em></em>
<p><em>additional: i'm testing with other small country ( belgium.osm.pbf ) and with this country i have other fail... but too in index proceseing and related with planet_osm_</em> tables</p>
<hr />
<p>QUERY: select nodes from planet_osm_ways where id = wayid<br />
CONTEXT: PL/pgSQL function "create_interpolation" line 26 at SQL statement<br />
PL/pgSQL function "placex_update" line 57 at assignment<br />
Done 4 in 50 @ 0.080000 per second - Rank 28 ETA (seconds): 28425.000000<br />
index_placex: UPDATE failed: ERROR: relation "planet_osm_ways" does not exist<br />
LINE 1: select nodes from planet_osm_ways where id = wayid<br />
</p>
<hr />
</div>
<div id="comment-10957-info" class="comment-info">
<span class="comment-age">(03 Mar '12, 09:59)</span> <span class="comment-user userinfo">luup2k</span>
</div>
</div>
</div>
<div id="comment-tools-10955" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10955-form-container" class="comment-form-container">
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

<span id="11082"></span>

<div id="answer-container-11082" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11082-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>These kind of installation problems should better be discussed on one of the developer mailing lists. For Nominatim, you can use either the <a href="http://lists.openstreetmap.org/listinfo/geocoding">geocoding</a> mailing list or the more general <a href="http://lists.openstreetmap.org/listinfo/dev">dev list</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '12, 22:39</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span> </br></br></p>
</div>
</div>
<div id="comments-container-11082" class="comments-container">
<span id="12497"></span>
<div id="comment-12497" class="comment">
<div id="post-12497-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I politely disagree. If you can figure out, it should be here so when other people have the same error, they can google it.</p>
</div>
<div id="comment-12497-info" class="comment-info">
<span class="comment-age">(01 May '12, 23:25)</span> <span class="comment-user userinfo">rafamvc</span>
</div>
</div>
</div>
<div id="comment-tools-11082" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11082-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12509"></span>

<div id="answer-container-12509" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12509-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-12509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I had the same problem. It turns out I was using osm2pgsql provided by my distro and not the one from SVN. Is this your case as well?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 May '12, 18:58</strong></p>
<img src="https://secure.gravatar.com/avatar/e17c2bfaed82349f7a355866ff24e4cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Norm1&#39;s gravatar image" />
<p><span>Norm1</span><br />
<span class="score" title="126 reputation points">126</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Norm1 has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-12509" class="comments-container">
&#10;</div>
<div id="comment-tools-12509" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12509-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

