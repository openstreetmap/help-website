+++
type = "question"
title = "Overpass-API on custom osm postgres database exported as XML"
description = '''Hi everyone, I have an experimental osm postgres database and website api set according to https://github.com/openstreetmap/openstreetmap-website Is there any way I can set the overpass-API to read my own osm postgres db? Issue: https://github.com/drolbr/Overpass-API/issues/624 The contributor impli...'''
date = "2021-06-29T09:32:00Z"
lastmod = "2022-03-31T13:19:00Z"
weight = 80768
keywords = [ "overpassapi", "overpass", "postgresql", "xml", "database" ]
aliases = [ "/questions/80768" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass-API on custom osm postgres database exported as XML](/questions/80768/overpass-api-on-custom-osm-postgres-database-exported-as-xml)

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
<span id="post-80768-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80768-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80768-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone,</p>
<p>I have an experimental osm postgres database and website api set according to</p>
<p><a href="https://github.com/openstreetmap/openstreetmap-website">https://github.com/openstreetmap/openstreetmap-website</a></p>
<p>Is there any way I can set the overpass-API to read my own osm postgres db?</p>
<p>Issue: <a href="https://github.com/drolbr/Overpass-API/issues/624">https://github.com/drolbr/Overpass-API/issues/624</a></p>
<p>The contributor implies that I need to export my database in OSM XML format, is there any instructions on how to achieve that?</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jun '21, 09:32</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd7a49e703fd6a8b30ff44b262ed7ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ubill88&#39;s gravatar image" />
<p><span>ubill88</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ubill88 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80768" class="comments-container">
&#10;</div>
<div id="comment-tools-80768" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80768-form-container" class="comment-form-container">
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

<span id="80769"></span>

<div id="answer-container-80769" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80769-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-80769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You haven't said why you have your own database. If you have your own database because you have non-OSM data in it, then yes, exporting that data in OSM XML and importing into Overpass is the way to go. You would typically use the "osmosis" command line tool with a combination of the <code>--read-apidb</code> and <code>--write-xml</code> flags. See <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.48">https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.48</a> for details.</p>
<p>If you have your own database but it has standard OSM data in it, then of course this makes no sense at all and you would simply feed Overpass OSM data downloaded from any of the usual sources!</p>
<p>Also, consider if you really need Overpass. It might be possible to run any queries that you are interested in on your existing API database with some SQL cleverness, which would save you the - potentially long-running - export-import step.</p>
<p>If your own database is very big and the osmosis export step takes too long, you might consider a special tool to convert an API database dump created with <code>pg_dump</code> into an XML representation: <a href="https://github.com/zerebubuth/planet-dump-ng">https://github.com/zerebubuth/planet-dump-ng</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jun '21, 09:43</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jun '21, 09:49</strong> </span></p>
</div>
</div>
<div id="comments-container-80769" class="comments-container">
<span id="80777"></span>
<div id="comment-80777" class="comment">
<div id="post-80777-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/104/frederik-ramm">@Frederik Ramm</a> ♦ thanks for your reply, I have my own postgres database with standard OSM data in it. There are some custom keys and values stored in my experimental region so I'm trying to create my own Overpass API. According to your reply, I just need to feed Overpass my own OSM data. I'm actually stuck in this part. According to the installation guide: <a href="https://overpass-api.de/no_frills.html">https://overpass-api.de/no_frills.html</a> bin/download_clone.sh --source=<a href="https://dev.overpass-api.de/api_drolbr/">https://dev.overpass-api.de/api_drolbr/</a> --db-dir="db/" --meta=no My question is actually here, how to feed my local osm postgres database to Overpass API? Thank you very much!</p>
</div>
<div id="comment-80777-info" class="comment-info">
<span class="comment-age">(30 Jun '21, 04:16)</span> <span class="comment-user userinfo">ubill88</span>
</div>
</div>
</div>
<div id="comment-tools-80769" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80769-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84050"></span>

<div id="answer-container-84050" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84050-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello <a href="https://help.openstreetmap.org/users/20432/ubill88">@ubill88</a>, I was wondering if you managed to do this ? I am also looking to do something like this. It would be great if you can share the solution.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Mar '22, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/900ddf3c47916230b7cabb3ba07a1371?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Allhad&#39;s gravatar image" />
<p><span>Allhad</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Allhad has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84050" class="comments-container">
&#10;</div>
<div id="comment-tools-84050" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84050-form-container" class="comment-form-container">
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

