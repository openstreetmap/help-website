+++
type = "question"
title = "which schema/tools to use"
description = '''Hi, I would like to have a local server for two purposes: geocoding/reverse geocoding, as well as api-like queries. It seems that Nominatim is good for the first purpose, while osmosis will be a tool that can serve the second purpose. From what I&#x27;ve seen so far, Nominatim uses osm2pgsql to load the ...'''
date = "2014-01-02T15:51:00Z"
lastmod = "2014-01-02T18:05:00Z"
weight = 29549
keywords = [ "nominatim", "postgresql", "osm2pgsql", "osmosis", "schema" ]
aliases = [ "/questions/29549" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [which schema/tools to use](/questions/29549/which-schematools-to-use)

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
<span id="post-29549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29549-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I would like to have a local server for two purposes: geocoding/reverse geocoding, as well as api-like queries.</p>
<p>It seems that Nominatim is good for the first purpose, while osmosis will be a tool that can serve the second purpose.</p>
<p>From what I've seen so far, Nominatim uses osm2pgsql to load the data, and the schema is different than the one osmosis can read.</p>
<p>Is there a solution for this or do I need to keep two copies of the data in two different schemas?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-schema" rel="tag" title="see questions tagged &#39;schema&#39;">schema</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jan '14, 15:51</strong></p>
<img src="https://secure.gravatar.com/avatar/84ebb95a07dd884e34f0170b07b1d652?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RazAlon&#39;s gravatar image" />
<p><span>RazAlon</span><br />
<span class="score" title="61 reputation points">61</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RazAlon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29549" class="comments-container">
&#10;</div>
<div id="comment-tools-29549" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29549-form-container" class="comment-form-container">
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

<span id="29553"></span>

<div id="answer-container-29553" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29553-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim/osm2pgsql does keep a significant portion of the original data in the so-called "slim mode tables" in the PostgreSQL data base - queries like "I want way #1234 and all its tags and nodes" can (almost) be satisfied from that if you're willing to write a little glue code in a scripting language of your choice. What it doesn't usually keep is the user name and time of last modification, or the version number, and it will also throw away some tags, but depending on exactly how "api-like" you need it, maybe it's enough.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jan '14, 16:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-29553" class="comments-container">
<span id="29556"></span>
<div id="comment-29556" class="comment">
<div id="post-29556-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Frederik.</p>
<p>I don't really care about versions and modifications, just the raw geo data.</p>
<p>I would like to use queries like "give me everything within a bbox" or "give me all ways within a bbox with amenity university or college"</p>
<p>Would such similar queries be possible with Nominatim?</p>
<p>Is there any other alternative for such queries (other than using osmosis to write and read)?</p>
<p>Looking at the tables created by osm2pgsql I guess the columns show which tags are kept, is this correct?</p>
<p>Raz</p>
</div>
<div id="comment-29556-info" class="comment-info">
<span class="comment-age">(02 Jan '14, 18:05)</span> <span class="comment-user userinfo">RazAlon</span>
</div>
</div>
</div>
<div id="comment-tools-29553" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29553-form-container" class="comment-form-container">
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

