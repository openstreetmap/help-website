+++
type = "question"
title = "Nominatim Installation Problem - Projection Code Failed"
description = '''Installed Nominatim and received the following error during import of the pbf: CREATE TABLE ALTER TABLE Import Projection code failed to initialise osm2pgsql SVN version 0.80.0 (64bit id space) ERROR: Error executing external command: /home/user/Nominatim/osm2pgsql/osm2pgsql -lsc -O gazetteer --hsto...'''
date = "2012-09-17T19:13:00Z"
lastmod = "2012-09-19T13:23:00Z"
weight = 16175
keywords = [ "code", "failed", "nominatim", "installation", "projection" ]
aliases = [ "/questions/16175" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim Installation Problem - Projection Code Failed](/questions/16175/nominatim-installation-problem-projection-code-failed)

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
<span id="post-16175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16175-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Installed Nominatim and received the following error during import of the pbf:</p>
<p>CREATE TABLE</p>
<p>ALTER TABLE</p>
<p>Import</p>
<p>Projection code failed to initialise</p>
<p>osm2pgsql SVN version 0.80.0 (64bit id space)</p>
<p>ERROR: Error executing external command: /home/user/Nominatim/osm2pgsql/osm2pgsql -lsc -O gazetteer --hstore -C 1059 -d nominatim /home/user/osm_data/central-america.osm.pbf</p>
<p>Not sure if this is the issue or not but I am not importing the planet file just two country files.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-code" rel="tag" title="see questions tagged &#39;code&#39;">code</span> <span class="post-tag tag-link-failed" rel="tag" title="see questions tagged &#39;failed&#39;">failed</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-projection" rel="tag" title="see questions tagged &#39;projection&#39;">projection</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Sep '12, 19:13</strong></p>
<img src="https://secure.gravatar.com/avatar/b412da9024d219e82fc430b7a4e5a02c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mooreja&#39;s gravatar image" />
<p><span>mooreja</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mooreja has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16175" class="comments-container">
&#10;</div>
<div id="comment-tools-16175" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16175-form-container" class="comment-form-container">
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

<span id="16180"></span>

<div id="answer-container-16180" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16180-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A g-search for "Projection code failed to initialise" leads to the page <a href="http://trac.osgeo.org/mapserver/wiki/RenderingOsmData,">http://trac.osgeo.org/mapserver/wiki/RenderingOsmData,</a> which explains:</p>
<pre><code>On windows make sure that PROJ_LIB environment variable is define to the location of your epsg file (In some case the path is: &quot;C:\ms4w\proj\nad&quot;) - else you will get a &quot;Projection code failed to initialise&quot; error.&quot;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '12, 20:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a1156d45a55699715b80fc3cadd0c8d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmehl&#39;s gravatar image" />
<p><span>mmehl</span><br />
<span class="score" title="565 reputation points">565</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmehl has 3 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-16180" class="comments-container">
<span id="16182"></span>
<div id="comment-16182" class="comment">
<div id="post-16182-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Apologies. This isn't a windows environment. I should have put in the environment.</p>
<p>Ubuntu 12.04 server Postgresql 9.1.4 PostGIS 2.01</p>
<p>I followed the latest Nominatim installlation procedures outlined on <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">https://wiki.openstreetmap.org/wiki/Nominatim/Installation</a></p>
</div>
<div id="comment-16182-info" class="comment-info">
<span class="comment-age">(17 Sep '12, 21:05)</span> <span class="comment-user userinfo">mooreja</span>
</div>
</div>
<span id="16186"></span>
<div id="comment-16186" class="comment">
<div id="post-16186-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is "proj-epsg" installed properly?</p>
<p>From the Installation guide:</p>
<blockquote>
<p>There is also a problem with proj-epsg on some platforms, so we manually install it:</p>
<p>wget <a href="ftp://ftp.muug.mb.ca/mirror/fedora/epel/6/x86_64/proj-epsg-4.7.0-1.el6.x86_64.rpm">ftp://ftp.muug.mb.ca/mirror/fedora/epel/6/x86_64/proj-epsg-4.7.0-1.el6.x86_64.rpm</a></p>
<p>rpm -i proj-epsg-4.7.0-1.el6.x86_64.rpm --nodeps</p>
</blockquote>
</div>
<div id="comment-16186-info" class="comment-info">
<span class="comment-age">(17 Sep '12, 21:35)</span> <span class="comment-user userinfo">mmehl</span>
</div>
</div>
<span id="16188"></span>
<div id="comment-16188" class="comment">
<div id="post-16188-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does that problem apply to Ubuntu too? That line's in the Fedora section of the wiki page, and on Ubuntu an alternative to an rpm would be needed.</p>
</div>
<div id="comment-16188-info" class="comment-info">
<span class="comment-age">(17 Sep '12, 22:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="16193"></span>
<div id="comment-16193" class="comment">
<div id="post-16193-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, since that portion of the procedure deals with Fedora/CentOS, and the link is fedora specific, it shouldn't be applicable to an Ubuntu implementation.</p>
</div>
<div id="comment-16193-info" class="comment-info">
<span class="comment-age">(18 Sep '12, 00:56)</span> <span class="comment-user userinfo">mooreja</span>
</div>
</div>
<span id="16225"></span>
<div id="comment-16225" class="comment">
<div id="post-16225-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Update. The error is being caused by the -l in the osm2pgsql -lsc. I can run the script without the -l but I later get SRID erors which I suspect is being caused by this projection failure.</p>
<p>I have read the osm2pgsql man page and have seen the supported projections but am unsure exactly how the -l checks for the projections.</p>
<p>Does anyone have any knowledge of that?</p>
<p>Thanks in advance.</p>
</div>
<div id="comment-16225-info" class="comment-info">
<span class="comment-age">(18 Sep '12, 17:29)</span> <span class="comment-user userinfo">mooreja</span>
</div>
</div>
</div>
<div id="comment-tools-16180" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16180-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16254"></span>

<div id="answer-container-16254" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16254-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Found a discussion about a similar problem at <a href="http://web.archiveorange.com/archive/v/wQWIbp8uENgQyNoCJGQz.">http://web.archiveorange.com/archive/v/wQWIbp8uENgQyNoCJGQz.</a> Even though the discussion happened several years ago the information provided to troubleshoot is still relevant.</p>
<p>In doing some of the troubleshooting listed in this discussion I was able to identify and resolve the problem.</p>
<p>Thanks to Jon Burgess for providing the level of detail that he did in that discussion.</p>
<p>JAM</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Sep '12, 13:23</strong></p>
<img src="https://secure.gravatar.com/avatar/b412da9024d219e82fc430b7a4e5a02c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mooreja&#39;s gravatar image" />
<p><span>mooreja</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mooreja has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Sep '12, 13:25</strong> </span></p>
</div>
</div>
<div id="comments-container-16254" class="comments-container">
&#10;</div>
<div id="comment-tools-16254" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16254-form-container" class="comment-form-container">
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

