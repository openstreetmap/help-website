+++
type = "question"
title = "Nominatim Local Server Queries Not Working?"
description = '''I finished importing all the planet data, search indices are good and all the indexes have been executed successfully. I also ran the script to check that all imports were successful (./utils/check_import_finished.php) and no issues that I can see. The Apache Web service also seems to be up and runn...'''
date = "2020-09-15T21:23:00Z"
lastmod = "2020-09-16T00:32:00Z"
weight = 76647
keywords = [ "nominatim", "openstreetmaps", "api", "geocoding", "geoparsing" ]
aliases = [ "/questions/76647" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim Local Server Queries Not Working?](/questions/76647/nominatim-local-server-queries-not-working)

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
<span id="post-76647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76647-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I finished importing all the planet data, search indices are good and all the indexes have been executed successfully. I also ran the script to check that all imports were successful (./utils/check_import_finished.php) and no issues that I can see. The Apache Web service also seems to be up and running. Now, when I enter an address to query, it doesn't return any search results. It only returns anything if I enter a country name.</p>
<p>Any idea as to what the issue is? Do I need to update the Web Service to sync with the postgres data?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-openstreetmaps" rel="tag" title="see questions tagged &#39;openstreetmaps&#39;">openstreetmaps</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-geoparsing" rel="tag" title="see questions tagged &#39;geoparsing&#39;">geoparsing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Sep '20, 21:23</strong></p>
<img src="https://secure.gravatar.com/avatar/f8dd6d1f5bf765fbbb3001eb3bdf3f60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rirhun&#39;s gravatar image" />
<p><span>rirhun</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rirhun has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Sep '20, 21:24</strong> </span></p>
</div>
</div>
<div id="comments-container-76647" class="comments-container">
&#10;</div>
<div id="comment-tools-76647" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76647-form-container" class="comment-form-container">
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

<span id="76654"></span>

<div id="answer-container-76654" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76654-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rirhun has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Any chance the search index step of the installation ran out of disk space?</p>
<p>That step can be rerun <a href="https://github.com/osm-search/Nominatim/issues/1694">https://github.com/osm-search/Nominatim/issues/1694</a> <code>./utils/setup.php --create-search-indices --create-country-names</code> You can also add <code>--ignore-errors</code> if you get 'relation already exists' warnings. <a href="https://github.com/osm-search/Nominatim/issues/1833">https://github.com/osm-search/Nominatim/issues/1833</a></p>
<p>If it's not a missing index it could be incomplete indices. In that case delete all indices listed in <code>sql/indices.src.sql</code> and <code>sql/indices_search.src.sql</code> first and and run the step above again.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '20, 00:32</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-76654" class="comments-container">
&#10;</div>
<div id="comment-tools-76654" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76654-form-container" class="comment-form-container">
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

