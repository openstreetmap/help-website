+++
type = "question"
title = "Nominatim setup cannot find postgis.sql"
description = '''Upon running the command,  ./Nominatim-2.1/utils/setup.php --osm-file /postgres/OpenStreetMaps/planetfile/north-america-latest.osm.pbf --all --osm2pgsql-cache 18000  the setup ended quickly with the following output.  Create DB Setup DB createlang: language &quot;plpgsql&quot; is already installed in database...'''
date = "2013-10-08T02:01:00Z"
lastmod = "2013-10-08T17:49:00Z"
weight = 27007
keywords = [ "nominatim", "postgis" ]
aliases = [ "/questions/27007" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim setup cannot find postgis.sql](/questions/27007/nominatim-setup-cannot-find-postgissql)

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
<span id="post-27007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27007-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Upon running the command,</p>
<pre><code>./Nominatim-2.1/utils/setup.php --osm-file /postgres/OpenStreetMaps/planetfile/north-america-latest.osm.pbf --all --osm2pgsql-cache 18000</code></pre>
<p>the setup ended quickly with the following output.</p>
<pre><code>Create DB
Setup DB
createlang: language &quot;plpgsql&quot; is already installed in database &quot;nominatim&quot;
WARNING:  =&gt; is deprecated as an operator name
DETAIL:  This name may be disallowed altogether in future versions of PostgreSQL.
CREATE EXTENSION
ERROR: unable to find /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql
unable to find /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql</code></pre>
<p>I know that postgis is installed on my machine, so finding postgis.sql file yielded the following:</p>
<pre><code>/usr/pgsql-9.1/share/contrib/postgis-2.0/postgis.sql
/usr/pgsql-9.1/share/contrib/postgis-1.5/postgis.sql</code></pre>
<p>How can I let Nominatim know where my postgis.sql is? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Oct '13, 02:01</strong></p>
<img src="https://secure.gravatar.com/avatar/61de868d7785f30711497cecbdddf5f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baekacaek&#39;s gravatar image" />
<p><span>baekacaek</span><br />
<span class="score" title="176 reputation points">176</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baekacaek has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27007" class="comments-container">
&#10;</div>
<div id="comment-tools-27007" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27007-form-container" class="comment-form-container">
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

<span id="27012"></span>

<div id="answer-container-27012" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27012-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-27012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="baekacaek has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Add, or create if needed, <code>settings/local.php</code> and add the following lines:</p>
<pre><code>@define(&#39;CONST_Postgis_Version&#39;, &#39;2.0&#39;);
@define(&#39;CONST_Path_Postgresql_Contrib&#39;, &#39;/usr/pgsql-9.1/share/contrib/postgis-2.0&#39;);
@define(&#39;CONST_Path_Postgresql_Postgis&#39;, &#39;/usr/pgsql-9.1/share/contrib/postgis-2.0&#39;);</code></pre>
<p>The second line gives the path to <code>spatial_ref_sys.sql</code> if it isn't in the same folder you may need to alter this.</p>
<p>You will find a number of settings in settings in <code>settings/settings.php</code> that should allow you to customise paths as required.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '13, 12:41</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Oct '13, 12:44</strong> </span></p>
</div>
</div>
<div id="comments-container-27012" class="comments-container">
<span id="27018"></span>
<div id="comment-27018" class="comment">
<div id="post-27018-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks! It somehow flew over my head that this is included in the Nominatim installation wiki.</p>
</div>
<div id="comment-27018-info" class="comment-info">
<span class="comment-age">(08 Oct '13, 17:49)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
</div>
<div id="comment-tools-27012" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27012-form-container" class="comment-form-container">
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

