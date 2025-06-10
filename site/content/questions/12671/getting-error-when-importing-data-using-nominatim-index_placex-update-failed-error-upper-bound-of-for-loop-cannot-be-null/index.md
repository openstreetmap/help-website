+++
type = "question"
title = "Getting error when importing data using Nominatim : index_placex: UPDATE failed: ERROR:  upper bound of FOR loop cannot be null"
description = '''I am trying to install a OSM server using Nominatim but I am getting an error like this.  index_placex: UPDATE failed: ERROR: upper bound of FOR loop cannot be null CONTEXT: PL/pgSQL function &quot;get_osm_rel_members&quot; line 6 at FOR with integer loop variable PL/pgSQL function &quot;placex_update&quot; line 302 at...'''
date = "2012-05-12T06:52:00Z"
lastmod = "2012-05-12T18:37:00Z"
weight = 12671
keywords = [ "nominatim", "osm" ]
aliases = [ "/questions/12671" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting error when importing data using Nominatim : index_placex: UPDATE failed: ERROR: upper bound of FOR loop cannot be null](/questions/12671/getting-error-when-importing-data-using-nominatim-index_placex-update-failed-error-upper-bound-of-for-loop-cannot-be-null)

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
<span id="post-12671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12671-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to install a OSM server using Nominatim but I am getting an error like this.</p>
<p><strong>index_placex: UPDATE failed: ERROR: upper bound of FOR loop cannot be null</strong></p>
<p><strong>CONTEXT: PL/pgSQL function "get_osm_rel_members" line 6 at FOR with integer loop variable</strong></p>
<p><strong>PL/pgSQL function "placex_update" line 302 at FOR over SELECT rows</strong></p>
<p>Does anyone has an idea what it means ?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 May '12, 06:52</strong></p>
<img src="https://secure.gravatar.com/avatar/b6913ae23eed6093317c71235ee3c61e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="reeuv&#39;s gravatar image" />
<p><span>reeuv</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="reeuv has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 May '12, 06:55</strong> </span></p>
</div>
</div>
<div id="comments-container-12671" class="comments-container">
&#10;</div>
<div id="comment-tools-12671" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12671-form-container" class="comment-form-container">
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

<span id="12686"></span>

<div id="answer-container-12686" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12686-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim could not find the members for a relation in the <code>planet_osm_rels</code> table.</p>
<p>This happens most likely because you use an outdated version of osm2pgsql. Get the latest version of <code>osm2pgsql</code> from subversion, recompile it and then redo the complete Nominatim database import.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 May '12, 18:37</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-12686" class="comments-container">
&#10;</div>
<div id="comment-tools-12686" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12686-form-container" class="comment-form-container">
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

