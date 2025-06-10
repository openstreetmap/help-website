+++
type = "question"
title = "Postgis Plugin: geometry name lookup failed for table"
description = '''I have a table name erpAssets which has column name Region of type polygon. it contains entries of points also like (-79.4609576808001,43.9726680183837)). I have written query which convert these points to geometry which is used by mapnick to generate tiles. ( SELECT replace(concat(concat(&#x27;POINT&#x27;,co...'''
date = "2014-05-15T07:18:00Z"
lastmod = "2014-05-15T07:18:00Z"
weight = 33192
keywords = [ "osm", "mapnik", "postgis" ]
aliases = [ "/questions/33192" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Postgis Plugin: geometry name lookup failed for table](/questions/33192/postgis-plugin-geometry-name-lookup-failed-for-table)

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
<span id="post-33192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33192-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a table name erpAssets which has column name Region of type polygon. it contains entries of points also like (-79.4609576808001,43.9726680183837)).</p>
<p>I have written query which convert these points to geometry which is used by mapnick to generate tiles.</p>
<p>( SELECT replace(concat(concat('POINT',concat(trim(TRAILING ')'FROM concat('(',trim(LEADING '(' FROM region::TEXT)::TEXT) ),')')),''),',',' ') as data from "erpAssets" where parent=326815) as foo<br />
) as points</p>
<p>My osm.xml file is as follows:</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;!DOCTYPE Map [
&lt;!ENTITY % entities SYSTEM &quot;inc/entities.xml.inc&quot;&gt;
%entities;
]&gt;
&lt;Map background-color=&quot;#bb0000&quot; srs=&quot;&amp;srs900913;&quot; minimum-version=&quot;2.0.0&quot;&gt;
  &amp;fontset-settings;
 &lt;Style name=&quot;theme_park&quot;&gt;
     &lt;Rule&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/alpinehut.p.16.png&quot;
&#10;      /&gt;
&#10;    &lt;/Rule&gt;
&#10;&lt;/Style&gt;
&#10;&amp;layer-shapefiles;
&lt;Layer name=&quot;theme_park&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;theme_park&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
        (SELECT ST_GeomFromText(data)
FROM
(
SELECT replace(concat(concat(&#39;POINT&#39;,concat(trim(TRAILING &#39;)&#39;FROM  concat(&#39;(&#39;,trim(LEADING &#39;(&#39; FROM region::TEXT)::TEXT) ),&#39;)&#39;)),&#39;&#39;),&#39;,&#39;,&#39; &#39;) as data
 from &quot;erpAssets&quot; where parent=326815) as foo       
        ) as points
&#10;      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;/Map&gt;</code></pre>
<p>Tiles are not generated and i am getting error on console as follows: Postgis Plugin: geometry name lookup failed for table '"erpassets"'. Please manually provide the 'geometry_field' parameter or add an entry in the geometry_columns for '"erpassets"'.</p>
<p>I have converted region column into geometry by aliasing then why i am not getting points on map?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 May '14, 07:18</strong></p>
<img src="https://secure.gravatar.com/avatar/9dbb1f1efa6ecf79ac9f2a97845e9ccc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Muneem&#39;s gravatar image" />
<p><span>Muneem</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Muneem has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-33192" class="comments-container">
&#10;</div>
<div id="comment-tools-33192" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33192-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

