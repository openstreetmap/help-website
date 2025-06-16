+++
type = "question"
title = "issue starting render"
description = '''Hi Team, I am getting below sql error while stating render. Request you yo help me understand issue and fix for it. Mapnik LOG&amp;gt; 2018-05-22 14:54:15: warning: unable to find face-name &#x27;Unifont Upper Medium&#x27; in FontSet &#x27;fontset-2&#x27; renderd[64780]: An error occurred while loading the map layer &#x27;defau...'''
date = "2018-05-22T12:13:00Z"
lastmod = "2018-05-24T13:36:00Z"
weight = 63612
keywords = [ "render" ]
aliases = [ "/questions/63612" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [issue starting render](/questions/63612/issue-starting-render)

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
<span id="post-63612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63612-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Team,</p>
<p>I am getting below sql error while stating render. Request you yo help me understand issue and fix for it.</p>
<pre><code>Mapnik LOG&gt; 2018-05-22 14:54:15: warning: unable to find face-name &#39;Unifont Upper Medium&#39; in FontSet &#39;fontset-2&#39;
renderd[64780]: An error occurred while loading the map layer &#39;default&#39;: Postgis Plugin: ERROR:  operator does not exist: hstore -&gt; boolean
LINE 6: ...D (tags-&gt;&#39;location&#39; NOT IN (&#39;underground&#39;) OR tags-&gt;&#39;locatio...
                                                             ^
HINT:  No operator matches the given name and argument type(s). You might need to add explicit type casts.
in executeQuery Full sql was: &#39;SELECT * FROM (SELECT
    way,
    COALESCE((
      &#39;highway_&#39; || (CASE WHEN highway IN (&#39;residential&#39;, &#39;unclassified&#39;, &#39;pedestrian&#39;, &#39;service&#39;, &#39;footway&#39;, &#39;cycleway&#39;, &#39;track&#39;, &#39;path&#39;, &#39;platform&#39;) THEN highway ELSE NULL END)),
      (&#39;railway_&#39; || (CASE WHEN (railway IN (&#39;platform&#39;)
                      AND (tags-&gt;&#39;location&#39; NOT IN (&#39;underground&#39;) OR tags-&gt;&#39;location&#39; IS NULL)
                      AND (tunnel NOT IN (&#39;yes&#39;, &#39;building_passage&#39;) OR tunnel IS NULL)
                      AND (covered NOT IN (&#39;yes&#39;) OR covered IS NULL))
                      THEN railway ELSE NULL END))
    ) AS feature
  FROM planet_osm_polygon
  WHERE highway IN (&#39;residential&#39;, &#39;unclassified&#39;, &#39;pedestrian&#39;, &#39;service&#39;, &#39;footway&#39;, &#39;track&#39;, &#39;path&#39;, &#39;platform&#39;)
    OR (railway IN (&#39;platform&#39;)
        AND (tags-&gt;&#39;location&#39; NOT IN (&#39;underground&#39;) OR tags-&gt;&#39;location&#39; IS NULL)
        AND (tunnel NOT IN (&#39;yes&#39;, &#39;building_passage&#39;) OR tunnel IS NULL)
        AND (covered NOT IN (&#39;yes&#39;) OR covered IS NULL))
  ORDER BY COALESCE(layer,0), way_area DESC
) AS highway_area_casing LIMIT 0&#39;
  encountered during parsing of layer &#39;highway-area-casing&#39; in Layer of &#39;/root/src/openstreetmap-carto/mapnik.xml&#39;
renderd[64780]: An error occurred while loading the map layer &#39;default&#39;: Postgis Plugin: ERROR:  operator does not exist: hstore -&gt; boolean
LINE 6: ...D (tags-&gt;&#39;location&#39; NOT IN (&#39;underground&#39;) OR tags-&gt;&#39;locatio...
                                                             ^
HINT:  No operator matches the given name and argument type(s). You might need to add explicit type casts.
in executeQuery Full sql was: &#39;SELECT * FROM (SELECT
    way,
    COALESCE((
      &#39;highway_&#39; || (CASE WHEN highway IN (&#39;residential&#39;, &#39;unclassified&#39;, &#39;pedestrian&#39;, &#39;service&#39;, &#39;footway&#39;, &#39;cycleway&#39;, &#39;track&#39;, &#39;path&#39;, &#39;platform&#39;) THEN highway ELSE NULL END)),
      (&#39;railway_&#39; || (CASE WHEN (railway IN (&#39;platform&#39;)
                      AND (tags-&gt;&#39;location&#39; NOT IN (&#39;underground&#39;) OR tags-&gt;&#39;location&#39; IS NULL)
                      AND (tunnel NOT IN (&#39;yes&#39;, &#39;building_passage&#39;) OR tunnel IS NULL)
                      AND (covered NOT IN (&#39;yes&#39;) OR covered IS NULL))
                      THEN railway ELSE NULL END))
    ) AS feature
  FROM planet_osm_polygon
  WHERE highway IN (&#39;residential&#39;, &#39;unclassified&#39;, &#39;pedestrian&#39;, &#39;service&#39;, &#39;footway&#39;, &#39;track&#39;, &#39;path&#39;, &#39;platform&#39;)
    OR (railway IN (&#39;platform&#39;)
        AND (tags-&gt;&#39;location&#39; NOT IN (&#39;underground&#39;) OR tags-&gt;&#39;location&#39; IS NULL)
        AND (tunnel NOT IN (&#39;yes&#39;, &#39;building_passage&#39;) OR tunnel IS NULL)
        AND (covered NOT IN (&#39;yes&#39;) OR covered IS NULL))
  ORDER BY COALESCE(layer,0), way_area DESC
) AS highway_area_casing LIMIT 0&#39;
  encountered during parsing of layer &#39;highway-area-casing&#39; in Layer of &#39;/root/src/openstreetmap-carto/mapnik.xml&#39;
renderd[64780]: An error occurred while loading the map layer &#39;default&#39;: Postgis Plugin: ERROR:  operator does not exist: hstore -&gt; boolean
LINE 6: ...D (tags-&gt;&#39;location&#39; NOT IN (&#39;underground&#39;) OR tags-&gt;&#39;locatio...
                                                             ^
HINT:  No operator matches the given name and argument type(s). You might need to add explicit type casts.
in executeQuery Full sql was: &#39;SELECT * FROM (SELECT
    way,
    COALESCE((
      &#39;highway_&#39; || (CASE WHEN highway IN (&#39;residential&#39;, &#39;unclassified&#39;, &#39;pedestrian&#39;, &#39;service&#39;, &#39;footway&#39;, &#39;cycleway&#39;, &#39;track&#39;, &#39;path&#39;, &#39;platform&#39;) THEN highway ELSE NULL END)),
      (&#39;railway_&#39; || (CASE WHEN (railway IN (&#39;platform&#39;)
                      AND (tags-&gt;&#39;location&#39; NOT IN (&#39;underground&#39;) OR tags-&gt;&#39;location&#39; IS NULL)
                      AND (tunnel NOT IN (&#39;yes&#39;, &#39;building_passage&#39;) OR tunnel IS NULL)
                      AND (covered NOT IN (&#39;yes&#39;) OR covered IS NULL))
                      THEN railway ELSE NULL END))
    ) AS feature
  FROM planet_osm_polygon
  WHERE highway IN (&#39;residential&#39;, &#39;unclassified&#39;, &#39;pedestrian&#39;, &#39;service&#39;, &#39;footway&#39;, &#39;track&#39;, &#39;path&#39;, &#39;platform&#39;)
    OR (railway IN (&#39;platform&#39;)
        AND (tags-&gt;&#39;location&#39; NOT IN (&#39;underground&#39;) OR tags-&gt;&#39;location&#39; IS NULL)
        AND (tunnel NOT IN (&#39;yes&#39;, &#39;building_passage&#39;) OR tunnel IS NULL)
        AND (covered NOT IN (&#39;yes&#39;) OR covered IS NULL))
  ORDER BY COALESCE(layer,0), way_area DESC
) AS highway_area_casing LIMIT 0&#39;
  encountered during parsing of layer &#39;highway-area-casing&#39; in Layer of &#39;/root/src/openstreetmap-carto/mapnik.xml&#39;
renderd[64780]: An error occurred while loading the map layer &#39;default&#39;: Postgis Plugin: ERROR:  operator does not exist: hstore -&gt; boolean
LINE 6: ...D (tags-&gt;&#39;location&#39; NOT IN (&#39;underground&#39;) OR tags-&gt;&#39;locatio...
                                                             ^
HINT:  No operator matches the given name and argument type(s). You might need to add explicit type casts.
in executeQuery Full sql was: &#39;SELECT * FROM (SELECT
    way,
    COALESCE((
      &#39;highway_&#39; || (CASE WHEN highway IN (&#39;residential&#39;, &#39;unclassified&#39;, &#39;pedestrian&#39;, &#39;service&#39;, &#39;footway&#39;, &#39;cycleway&#39;, &#39;track&#39;, &#39;path&#39;, &#39;platform&#39;) THEN highway ELSE NULL END)),
      (&#39;railway_&#39; || (CASE WHEN (railway IN (&#39;platform&#39;)
                      AND (tags-&gt;&#39;location&#39; NOT IN (&#39;underground&#39;) OR tags-&gt;&#39;location&#39; IS NULL)
                      AND (tunnel NOT IN (&#39;yes&#39;, &#39;building_passage&#39;) OR tunnel IS NULL)
                      AND (covered NOT IN (&#39;yes&#39;) OR covered IS NULL))
                      THEN railway ELSE NULL END))
    ) AS feature
  FROM planet_osm_polygon
  WHERE highway IN (&#39;residential&#39;, &#39;unclassified&#39;, &#39;pedestrian&#39;, &#39;service&#39;, &#39;footway&#39;, &#39;track&#39;, &#39;path&#39;, &#39;platform&#39;)
    OR (railway IN (&#39;platform&#39;)
        AND (tags-&gt;&#39;location&#39; NOT IN (&#39;underground&#39;) OR tags-&gt;&#39;location&#39; IS NULL)
        AND (tunnel NOT IN (&#39;yes&#39;, &#39;building_passage&#39;) OR tunnel IS NULL)
        AND (covered NOT IN (&#39;yes&#39;) OR covered IS NULL))
  ORDER BY COALESCE(layer,0), way_area DESC
) AS highway_area_casing LIMIT 0&#39;
  encountered during parsing of layer &#39;highway-area-casing&#39; in Layer of &#39;/root/src/openstreetmap-carto/mapnik.xml&#39;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-render" rel="tag" title="see questions tagged &#39;render&#39;">render</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 May '18, 12:13</strong></p>
<img src="https://secure.gravatar.com/avatar/1c8154cf6e206c8009a6901c7b2661e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jiten19851985&#39;s gravatar image" />
<p><span>jiten19851985</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jiten19851985 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 May '18, 08:16</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-63612" class="comments-container">
<span id="63629"></span>
<div id="comment-63629" class="comment">
<div id="post-63629-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This snapshot may help</p>
<p><img src="/upfiles/mapsrv.PNG" alt="alt text" /></p>
</div>
<div id="comment-63629-info" class="comment-info">
<span class="comment-age">(23 May '18, 07:50)</span> <span class="comment-user userinfo">jiten19851985</span>
</div>
</div>
<span id="63639"></span>
<div id="comment-63639" class="comment">
<div id="post-63639-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><img src="/upfiles/hstore.PNG" alt="alt text" /></p>
</div>
<div id="comment-63639-info" class="comment-info">
<span class="comment-age">(23 May '18, 09:36)</span> <span class="comment-user userinfo">jiten19851985</span>
</div>
</div>
</div>
<div id="comment-tools-63612" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63612-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="63682"></span>

<div id="answer-container-63682" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63682-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jiten19851985 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I wrote this code and I was testing it on Ubuntu 18.04 without problems. In the past we had some problems with database compatibility:</p>
<p><a href="https://github.com/gravitystorm/openstreetmap-carto/pull/3078">https://github.com/gravitystorm/openstreetmap-carto/pull/3078</a></p>
<p>I'm not familiar with databases, so please open the ticket here:</p>
<p><a href="https://github.com/gravitystorm/openstreetmap-carto/issues">https://github.com/gravitystorm/openstreetmap-carto/issues</a></p>
<p>If you find the right solution, I will test it on my setup and merge the code as soon as possible.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '18, 11:32</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</img>
</div>
</div>
<div id="comments-container-63682" class="comments-container">
<span id="63688"></span>
<div id="comment-63688" class="comment">
<div id="post-63688-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hi,</p>
<p>upgraded postgres to 9.5 and all ok now. Thanks a lot your help on this.</p>
<p>Thanks</p>
</div>
<div id="comment-63688-info" class="comment-info">
<span class="comment-age">(24 May '18, 13:35)</span> <span class="comment-user userinfo">jiten19851985</span>
</div>
</div>
</div>
<div id="comment-tools-63682" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63682-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63630"></span>

<div id="answer-container-63630" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63630-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect that the style that you're using requires hstore and you haven't created it. See <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> where it says "<code>CREATE EXTENSION hstore;</code>".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '18, 08:18</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</img>
</div>
</div>
<div id="comments-container-63630" class="comments-container">
<span id="63638"></span>
<div id="comment-63638" class="comment">
<div id="post-63638-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hstore is there in the DB gis</p>
<p>gis=# gis=# gis=# \dx List of installed extensions Name | Version | Schema | Description ---------+---------+------------+--------------------------------------------------------------------- hstore | 1.1 | public | data type for storing sets of (key, value) pairs plpgsql | 1.0 | pg_catalog | PL/pgSQL procedural language postgis | 2.0.7 | public | PostGIS geometry, geography, and raster spatial types and functions (3 rows)</p>
<p>gis=#</p>
</div>
<div id="comment-63638-info" class="comment-info">
<span class="comment-age">(23 May '18, 09:35)</span> <span class="comment-user userinfo">jiten19851985</span>
</div>
</div>
<span id="63640"></span>
<div id="comment-63640" class="comment">
<div id="post-63640-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We'd probably need a bit more information about how you got to where you are? What was installed, and on what OS? Did you update from a previous version (perhaps you've got two versions of postgres/postgis, one with hstore, one without)?</p>
</div>
<div id="comment-63640-info" class="comment-info">
<span class="comment-age">(23 May '18, 09:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63647"></span>
<div id="comment-63647" class="comment">
<div id="post-63647-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>this is a fresh installation on RHEL 7.4 by following steps from below two links.</p>
<p><a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a> <a href="https://www.keisan.io/knowledgebase/centos-7-open-street-map-tile-server">https://www.keisan.io/knowledgebase/centos-7-open-street-map-tile-server</a></p>
<p>below is the version of postgres * postgis</p>
<p>[root@mapsrv ~]# rpm -qa | grep postg postgresql-devel-9.2.23-3.el7_4.x86_64 postgresql-9.2.23-3.el7_4.x86_64 postgis-utils-2.0.7-1.el7.x86_64 postgresql-server-9.2.23-3.el7_4.x86_64 postgis-docs-2.0.7-1.el7.x86_64 postgresql-contrib-9.2.23-3.el7_4.x86_64 postgis-debuginfo-2.0.7-1.el7.x86_64 postgresql-libs-9.2.23-3.el7_4.x86_64 postgis-2.0.7-1.el7.x86_64 [root@mapsrv ~]#</p>
</div>
<div id="comment-63647-info" class="comment-info">
<span class="comment-age">(23 May '18, 11:37)</span> <span class="comment-user userinfo">jiten19851985</span>
</div>
</div>
<span id="63648"></span>
<div id="comment-63648" class="comment">
<div id="post-63648-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You've got further than me on Centos then :)</p>
<p>(I couldn't get Mapnik to build cleanly there)</p>
</div>
<div id="comment-63648-info" class="comment-info">
<span class="comment-age">(23 May '18, 11:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63649"></span>
<div id="comment-63649" class="comment not_top_scorer">
<div id="post-63649-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I had a hard time installing mapnik but was able to install it finally. now I am stuck at this issue. :(</p>
</div>
<div id="comment-63649-info" class="comment-info">
<span class="comment-age">(23 May '18, 11:48)</span> <span class="comment-user userinfo">jiten19851985</span>
</div>
</div>
<span id="63674"></span>
<div id="comment-63674" class="comment not_top_scorer">
<div id="post-63674-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Team,</p>
<p>I am still facing the issue, any help on this much appreciated.</p>
<p>Thanks</p>
</div>
<div id="comment-63674-info" class="comment-info">
<span class="comment-age">(24 May '18, 09:17)</span> <span class="comment-user userinfo">jiten19851985</span>
</div>
</div>
<span id="63679"></span>
<div id="comment-63679" class="comment not_top_scorer">
<div id="post-63679-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's hardly surprising that no-one has looked at this again in the last 21 hours :)</p>
<p>As you have discovered, there isn't an "out of the box" solution on Redhat-based distributions. There are for Ubuntu (the last 2 long term support releases have good support). Other options might include Docker (though I'd personally think twice before running that in production; and you're not removing the Ubuntu dependancy there, just hiding it).</p>
</div>
<div id="comment-63679-info" class="comment-info">
<span class="comment-age">(24 May '18, 10:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63680"></span>
<div id="comment-63680" class="comment">
<div id="post-63680-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This error is clearly a PostgreSQL one. Follow standard methods to resolve queries which generate errors on any DB package (i.e., take the actual query, run it in isolation vs the db, break it down to isolate the offending clause, review the DDL of tables/views used in the query, etc.) Also avoid posting large screeds of error messages here, they arent particularly readable).</p>
</div>
<div id="comment-63680-info" class="comment-info">
<span class="comment-age">(24 May '18, 11:29)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="63689"></span>
<div id="comment-63689" class="comment not_top_scorer">
<div id="post-63689-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Guys,</p>
<p>Thanks for your help</p>
</div>
<div id="comment-63689-info" class="comment-info">
<span class="comment-age">(24 May '18, 13:36)</span> <span class="comment-user userinfo">jiten19851985</span>
</div>
</div>
</div>
<div id="comment-tools-63630" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-63630-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63615"></span>

<div id="answer-container-63615" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63615-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your pasted message is hardly legible. The problem might be helped by putting parentheses around any occurrence of <code>tags-&gt;'something'</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 May '18, 13:59</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-63615" class="comments-container">
&#10;</div>
<div id="comment-tools-63615" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63615-form-container" class="comment-form-container">
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

