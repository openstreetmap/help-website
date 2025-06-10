+++
type = "question"
title = "build tile server manually with Postgres db on a different server"
description = '''I have set up my map tile server and have used the following components:  Mod_tile osm2pgsql postgres Mapnik open street map carto  In my configuration, postgres is on a different server. when I access the /osm_tiles/0/0/0.png, I get a blank square.  I think the data is not being fetched from postgr...'''
date = "2019-02-27T05:28:00Z"
lastmod = "2019-02-27T10:19:00Z"
weight = 68173
keywords = [ "mod_tile", "postgresql", "server", "mapnik", "tileserver" ]
aliases = [ "/questions/68173" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [build tile server manually with Postgres db on a different server](/questions/68173/build-tile-server-manually-with-postgres-db-on-a-different-server)

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
<span id="post-68173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68173-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have set up my map tile server and have used the following components:</p>
<ol>
<li>Mod_tile</li>
<li>osm2pgsql</li>
<li>postgres</li>
<li>Mapnik</li>
<li>open street map carto</li>
</ol>
<p>In my configuration, postgres is on a different server. when I access the /osm_tiles/0/0/0.png, I get a blank square. I think the data is not being fetched from postgres database. How do I tell my server that the postgres db is on another server? I have mentioned the configuration in the osm2pgsql/project.yaml file.</p>
<ol>
<li>Do I need to mention the db details in some other place as well?</li>
<li>Which of tool fetches the tiles from the postgres db to be displayed?</li>
</ol>
<p>P.s I've used this <a href="https://github.com/s6o/aws-osm-rds">link</a> as the setup guide.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Feb '19, 05:28</strong></p>
<img src="https://secure.gravatar.com/avatar/153d30d9d12370c8532371eaaa3593b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vishy91&#39;s gravatar image" />
<p><span>vishy91</span><br />
<span class="score" title="66 reputation points">66</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vishy91 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68173" class="comments-container">
<span id="68174"></span>
<div id="comment-68174" class="comment">
<div id="post-68174-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>crosspost: <a href="https://gis.stackexchange.com/questions/313715/build-tile-server-manually-with-postgres-db-on-a-different-server">https://gis.stackexchange.com/questions/313715/build-tile-server-manually-with-postgres-db-on-a-different-server</a></p>
</div>
<div id="comment-68174-info" class="comment-info">
<span class="comment-age">(27 Feb '19, 09:09)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68173" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68173-form-container" class="comment-form-container">
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

<span id="68175"></span>

<div id="answer-container-68175" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68175-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>project.yaml (in the openstreetmap-carto directory, not in the osm2pgsql directory) is the source of the style description and contains database access information, but when you run renderd it will actually access project.xml (cf. your renderd.conf which will likely point to that). Your project.xml will still contain the old database parameters. To re-generate project.xml, you have to do this:</p>
<pre><code>carto -a 3.0.0 project.yaml &gt; project.xml</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '19, 10:19</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-68175" class="comments-container">
&#10;</div>
<div id="comment-tools-68175" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68175-form-container" class="comment-form-container">
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

