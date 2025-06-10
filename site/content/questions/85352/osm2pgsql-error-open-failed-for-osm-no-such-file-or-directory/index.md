+++
type = "question"
title = "osm2pgsql: ERROR: Open failed for &#x27;osm&#x27;: No such file or directory"
description = '''Hello, after compiling osm2pgsql v1.6.0 and all its requirements, I tried to use it. But it did fail with ERROR: Open failed for &#x27;osm&#x27;: No such file or directory. where could I find out about the file or directory? osm2pgsql --slim -d gis -C 1600 -H uslamvm3.gre.hpecorp.net -P 5432 --number-process ...'''
date = "2022-08-16T00:25:00Z"
lastmod = "2022-08-21T13:35:00Z"
weight = 85352
keywords = [ "failed" ]
aliases = [ "/questions/85352" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql: ERROR: Open failed for 'osm': No such file or directory](/questions/85352/osm2pgsql-error-open-failed-for-osm-no-such-file-or-directory)

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
<span id="post-85352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85352-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-85352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>after compiling osm2pgsql v1.6.0 and all its requirements, I tried to use it. But it did fail with <strong><em>ERROR: Open failed for 'osm': No such file or directory</em></strong>. where could I find out about the file or directory?</p>
<p>osm2pgsql --slim -d gis -C 1600 -H uslamvm3.gre.hpecorp.net -P 5432 --number-process 1 -G --hstore --tag-transform-script ./openstreetmap-carto.lua -S ./openstreetmap-carto.style --log-level=debug -v ./data/gcc-states-140101.osm.pbf 2022-08-16 00:46:32 osm2pgsql version 1.6.0 (1.6.0-244-g65d0d27) Password: 2022-08-16 00:46:34 [0] Database version: 12.11 2022-08-16 00:46:34 [0] PostGIS version: 3.1 2022-08-16 00:46:34 [0] Reading file: osm 2022-08-16 00:46:34 [0] Reading file: ./data/gcc-states-140101.osm.pbf 2022-08-16 00:46:34 [0] Started pool with 1 threads. 2022-08-16 00:46:34 [0] Mid: pgsql, cache=1600 2022-08-16 00:46:34 [0] Setting up table 'planet_osm_nodes' 2022-08-16 00:46:34 [0] Setting up table 'planet_osm_ways' 2022-08-16 00:46:34 [0] Setting up table 'planet_osm_rels' 2022-08-16 00:46:34 [0] Using projection SRS 3857 (Spherical Mercator) 2022-08-16 00:46:34 [0] Using lua based tag transformations with script ./openstreetmap-carto.lua 2022-08-16 00:46:34 [0] Setting up table 'planet_osm_point' 2022-08-16 00:46:34 [0] Setting up table 'planet_osm_line' 2022-08-16 00:46:34 [0] Setting up table 'planet_osm_polygon' 2022-08-16 00:46:34 [0] Setting up table 'planet_osm_roads' 2022-08-16 00:46:34 [0] ERROR: Open failed for 'osm': No such file or directory</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-failed" rel="tag" title="see questions tagged &#39;failed&#39;">failed</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '22, 00:25</strong></p>
<img src="https://secure.gravatar.com/avatar/cfc1c707b366ad757397920866cb6819?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HoangA&#39;s gravatar image" />
<p><span>HoangA</span><br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HoangA has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85352" class="comments-container">
<span id="85372"></span>
<div id="comment-85372" class="comment">
<div id="post-85372-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have no idea what is happening: the same command on my own osm2pgsql install complains about the file name " ERROR: Open failed for './data/gcc-states-140101.osm.pbf': The system cannot find the file specified." as I would expect.</p>
</div>
<div id="comment-85372-info" class="comment-info">
<span class="comment-age">(18 Aug '22, 10:45)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-85352" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85352-form-container" class="comment-form-container">
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

<span id="85364"></span>

<div id="answer-container-85364" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85364-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I did check all the input files, and they do exist.</p>
<p>looking at code, I do see this error only in:</p>
<p>contrib/libosmium/include/osmium/io/detail/read_write.hpp:</p>
<p>throw std::system_error{errno, std::system_category(), std::string("<strong><em>Open failed for</em></strong> '") + filename + "'"};</p>
<p>but I don't understand why user "osm" is view as file ..</p>
<p>the function "open_for_writing" is called by function in <em>contrib/libosmium/include/osmium/io/writer.hpp</em>:</p>
<p>std::unique_ptr&lt;osmium::io::compressor&gt; compressor = <strong>CompressionFactory::instance().create_compressor</strong>(file.compression(), osmium::io::detail::open_for_writing(<strong><em>m_file.filename()</em></strong>, options.allow_overwrite), options.sync);</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '22, 00:35</strong></p>
<img src="https://secure.gravatar.com/avatar/cfc1c707b366ad757397920866cb6819?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HoangA&#39;s gravatar image" />
<p><span>HoangA</span><br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HoangA has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Aug '22, 00:37</strong> </span></p>
</div>
</div>
<div id="comments-container-85364" class="comments-container">
&#10;</div>
<div id="comment-tools-85364" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85364-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85381"></span>

<div id="answer-container-85381" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85381-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>the error is due to -W... see <a href="https://stackoverflow.com/questions/44552054/osm2pgsql-error-trying-to-import-osm-to-postgis-on-aws">osm2pgsql-error-trying-to-import-osm-to-postgis-on-aws</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '22, 14:23</strong></p>
<img src="https://secure.gravatar.com/avatar/cfc1c707b366ad757397920866cb6819?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HoangA&#39;s gravatar image" />
<p><span>HoangA</span><br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HoangA has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Aug '22, 14:24</strong> </span></p>
</div>
</div>
<div id="comments-container-85381" class="comments-container">
<span id="85384"></span>
<div id="comment-85384" class="comment">
<div id="post-85384-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There was no -W in your original query. It really helps if you provide an accurate command line.</p>
</div>
<div id="comment-85384-info" class="comment-info">
<span class="comment-age">(21 Aug '22, 13:35)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-85381" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85381-form-container" class="comment-form-container">
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

