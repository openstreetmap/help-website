+++
type = "question"
title = "OSM to Shapefile question"
description = '''Hello, I am asking what I realize is technical question about shapefiles rather than OSM but I hope you will excuse me. For what it is worth, I am a newbie but really think I will be involved in OSM for a while, so it won&#x27;t be a lost cause to help me: I think I will contribute back. Anyway: I have d...'''
date = "2012-03-13T11:50:00Z"
lastmod = "2012-03-14T09:20:00Z"
weight = 11160
keywords = [ "shapefile", "tagging", "database" ]
aliases = [ "/questions/11160" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM to Shapefile question](/questions/11160/osm-to-shapefile-question)

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
<span id="post-11160-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11160-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11160-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am asking what I realize is technical question about shapefiles rather than OSM but I hope you will excuse me. For what it is worth, I am a newbie but really think I will be involved in OSM for a while, so it won't be a lost cause to help me: I think I will contribute back.</p>
<p>Anyway: I have downloaded shapefiles from both cloudmade and geofabrik. I have also downloaded OSM files and converted them.</p>
<p>My problem: all the shapefiles have different dbase structures. For example, Cloudmade is nice and neat with four columns and missing a lot of tag information. QGIS saves shapefiles with anywhere from four columns to twenty columns so far, with the tags column having a variety of information such as "bicycle"="yes","hiking"="yes","information"="map","internet_access"="terminal". Some of this information is duplicated in a separate column: e.g. tags list parking/fees/surface... and the column amenity lists 'parking'.</p>
<p>This means that I have to parse this data somewhere else. Which means that I not only have to write a parser (ot at least a macro) but it would have to deal with unknowns each time. What is wierd is that the program I am using, NetLogo (for the moment), is oddly sucessful in dealing with some of the data - unfortunatly I don't have details on how this data is handled in order to solve it. However I would like to move forward having the data side solved and then deal with issues on the programming side.</p>
<p>So what I am looking for is:</p>
<ul>
<li>An explanation of why the converters give such different results (or is it the same result and I am just missing the conversion schema?).</li>
<li>Ideas for how to filter the data if I download direct from OSM. (If I missed that please don't jump on me, I am sorry but all I've seen is the very nice export option. I haven't found any options.)</li>
<li>Any ideas for a program to handle the data in order to convert it post download? I have been using QGIS so far but I am a newbie pretty much at everything and can't get QGIS to present just the data I want. I would be happy enough to do the work manually and seperate layers at the QGIS stage but the information is scattered in the 'tags' line and I can't seem to get at it.</li>
</ul>
<p>I realize this is only partially a OSM question, but any help would be appreciated.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Mar '12, 11:50</strong></p>
<img src="https://secure.gravatar.com/avatar/318bba37886c22b0902ca444ee5796d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jake%20cimilo&#39;s gravatar image" />
<p><span>jake cimilo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jake cimilo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11160" class="comments-container">
&#10;</div>
<div id="comment-tools-11160" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11160-form-container" class="comment-form-container">
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

<span id="11161"></span>

<div id="answer-container-11161" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11161-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The shapefile format has a lot of limitations, so it is not possible to create a shapefile with all the information from OSM, so when you convert you have to decide what to include.</p>
<p>You don't describe what data you actually need, so it is hard to say for sure what is the best solution for you. If you need more than just simple shapes, you might be better off importing the planet file (or one of the extracts from <a href="http://download.geofabrik.de/">Geofabrik</a> or <a href="http://downloads.cloudmade.com/">Cloudmade</a>) into a PostGIS database.</p>
<p>Again depending on your needs, there are several ways to do that. Some of the options are: <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">Osm2pgsql</a>, <a href="https://wiki.openstreetmap.org/wiki/Imposm">Imposm</a> and <a href="https://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a></p>
<p>With Osmosis, PostgreSQL and PostGIS you can do something like this:</p>
<p>Create a PostGIS and hstore enabled database and setup the <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#PostGIS_Tasks_.28Snapshot_Schema.29">pgsnapshot schema</a>, use Osmosis to import the data:</p>
<pre><code>osmosis --read-pbf file=denmark.osm.pbf outPipe.0=1 --write-pgsql database=osm user=XXX password=XXX inPipe.0=1</code></pre>
<p>Then create and index new qid columns to make QGIS happy:</p>
<pre><code>CREATE SEQUENCE nodes_qid_seq;
ALTER TABLE nodes ADD COLUMN qid integer NOT NULL DEFAULT nextval(&#39;nodes_qid_seq&#39;);
CREATE UNIQUE INDEX nodes_qid ON nodes (qid ASC NULLS LAST);
ALTER TABLE nodes ADD CONSTRAINT unique_nodes_qid UNIQUE (qid);
&#10;CREATE SEQUENCE ways_qid_seq;
ALTER TABLE ways ADD COLUMN qid integer NOT NULL DEFAULT nextval(&#39;ways_qid_seq&#39;);
CREATE UNIQUE INDEX ways_qid ON ways (qid ASC NULLS LAST);
ALTER TABLE ways ADD CONSTRAINT unique_ways_qid UNIQUE (qid);</code></pre>
<p>When you use the pgsnapshot schema, all the tags are stored in a hstore column. To make it easier to work with from QGIS, you can create views like this:</p>
<pre><code>CREATE OR REPLACE VIEW &quot;Amenities&quot; AS 
  SELECT nodes.qid, nodes.tags -&gt; &#39;amenity&#39; AS amenity, nodes.tags -&gt; &#39;leisure&#39; AS leisure, 
    nodes.tags -&gt; &#39;sport&#39; AS sport, nodes.tags -&gt; &#39;tourism&#39; AS tourism, nodes.geom
  FROM nodes
  WHERE nodes.tags ? &#39;amenity&#39; OR nodes.tags ? &#39;leisure&#39; OR nodes.tags ? &#39;sport&#39; OR nodes.tags ? &#39;tourism&#39;
UNION ALL 
  SELECT ways.qid, ways.tags -&gt; &#39;amenity&#39; AS amenity, ways.tags -&gt; &#39;leisure&#39; AS leisure, 
    ways.tags -&gt; &#39;sport&#39; AS sport, ways.tags -&gt; &#39;tourism&#39; AS tourism, ways.linestring AS geom
  FROM ways
  WHERE ways.tags ? &#39;amenity&#39; OR ways.tags ? &#39;leisure&#39; OR ways.tags ? &#39;sport&#39; OR ways.tags ? &#39;tourism&#39;;
&#10;CREATE OR REPLACE VIEW &quot;Roads&quot; AS 
  SELECT w.qid, w.tags -&gt; &#39;highway&#39; AS highway, w.tags -&gt; &#39;foot&#39; AS foot, w.tags -&gt; &#39;bicycle&#39; AS bicycle, 
    w.tags -&gt; &#39;tracktype&#39; AS tracktype, w.tags -&gt; &#39;access&#39; AS access, w.tags -&gt; &#39;surface&#39; AS surface, 
    w.tags -&gt; &#39;sac_scale&#39; AS sac_scale, w.tags -&gt; &#39;mtb:scale&#39; AS mtb_scale, w.linestring
  FROM ways w
  WHERE w.tags ? &#39;highway&#39; OR w.tags ? &#39;foot&#39; OR w.tags ? &#39;bicycle&#39; OR w.tags ? &#39;tracktype&#39; OR 
    w.tags ? &#39;access&#39; OR w.tags ? &#39;surface&#39; OR w.tags ? &#39;sac_scale&#39; OR w.tags ? &#39;mtb:scale&#39;;
&#10;CREATE OR REPLACE VIEW &quot;Walkable&quot; AS 
  SELECT &quot;Roads&quot;.qid, &quot;Roads&quot;.highway, &quot;Roads&quot;.foot, &quot;Roads&quot;.bicycle, &quot;Roads&quot;.tracktype, &quot;Roads&quot;.access, 
    &quot;Roads&quot;.surface, &quot;Roads&quot;.sac_scale, &quot;Roads&quot;.mtb_scale, &quot;Roads&quot;.linestring
    FROM &quot;Roads&quot;
  WHERE COALESCE(&quot;Roads&quot;.foot, &#39;empty&#39;) &lt;&gt; &#39;no&#39; AND 
    (COALESCE(&quot;Roads&quot;.access, &#39;empty&#39;) &lt;&gt; ALL (ARRAY[&#39;private&#39;, &#39;no&#39;, &#39;restricted&#39;, &#39;emergency&#39;])) AND 
    (COALESCE(&quot;Roads&quot;.highway, &#39;empty&#39;) &lt;&gt; ALL (ARRAY[&#39;primary&#39;, &#39;cycleway&#39;, &#39;trunk&#39;, &#39;motorway&#39;, &#39;primary_link&#39;, &#39;trunk_link&#39;, &#39;motorway_link&#39;, &#39;motorway_junction&#39;]));</code></pre>
<p>Then in QGIS, you can add the Amenities and Walkable views as PostGIS layers.</p>
<p>You should change the views to use your own classifications.</p>
<p>You can also use osm2pgsql and change the import style to create a schema that matches your needs.</p>
<p>There are no fixed rules for how anything should be tagged in OSM, so your biggest task is probably identifying what tag/value combinations you should use to make your classifications.</p>
<p>You can start by looking at some of these keys and especially their link to <a href="http://taginfo.openstreetmap.org">taginfo</a> on the right side of the page - the "values" tab can give you an idea about values you should consider:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Key:highway">highway</a>, <a href="https://wiki.openstreetmap.org/wiki/Key:foot">foot</a>, <a href="https://wiki.openstreetmap.org/wiki/Key:bicycle">bicycle</a>, <a href="https://wiki.openstreetmap.org/wiki/Key:tracktype">tracktype</a>, <a href="https://wiki.openstreetmap.org/wiki/Key:surface">surface</a>, <a href="https://wiki.openstreetmap.org/wiki/Key:access">access</a>, <a href="https://wiki.openstreetmap.org/wiki/Key:mtb:scale">mtb:scale</a> and <a href="https://wiki.openstreetmap.org/wiki/Key:sac_scale">sac_scale</a>.</p>
<p>/Jais</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '12, 12:37</strong></p>
<img src="https://secure.gravatar.com/avatar/b9a8b8a3b1418b4b0bb41041555b18a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dymo12&#39;s gravatar image" />
<p><span>Dymo12</span><br />
<span class="score" title="796 reputation points">796</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dymo12 has 2 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Mar '12, 20:12</strong> </span></p>
</div>
</div>
<div id="comments-container-11161" class="comments-container">
<span id="11162"></span>
<div id="comment-11162" class="comment">
<div id="post-11162-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would like to do that. Eventually I will get to the point where I am storing the various layers I need, including the ones I generate, in an external database. For the moment, I wanted the .dbf file to hold just certain layers.</p>
<p>For example, I would like to have separate shapefiles with:</p>
<ul>
<li>Highways but with the capability to show which roads are hikeable and bikeable.</li>
<li>Paths that can be shown to be bikeable by various degrees, mountainbikable, walkable, hikable, climbable.</li>
<li>Amenities but broken out seperately: gas stations, parking, toilets, bars, restaurants, hotels, etc.</li>
<li>natural parks, recreation sites, camping, etc.</li>
</ul>
<p>To take the first example, bikeable roads have a tag: "bicycle"="yes". All the .dbf files I have right now just list that tag in a text record with all the other tags that apply to that feature. If the tags were separated or if I could download them in a way that the .dbf file showed a column "bicycle" and a column "level" (for 1 to 5 or which ever standard is used, then I could sort the roads using those columns, e.g. "highways" with "bicycle"="yes" and "level"&lt;"3".</p>
<p>I admit that my reason is just that my system has built in ways to do this which I prefer over writing my own script. But if I am running hundreds of agents and hundreds of scenarios, I prefer having the data presorted... aye, which i guess is what i will have to do.</p>
<p>Still, if you know an answer without me having to code something, I would appreciate it.</p>
<p>Thanks</p>
</div>
<div id="comment-11162-info" class="comment-info">
<span class="comment-age">(13 Mar '12, 13:17)</span> <span class="comment-user userinfo">jake cimilo</span>
</div>
</div>
<span id="11168"></span>
<div id="comment-11168" class="comment">
<div id="post-11168-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you aware that QGIS can load OSM files directly (through its OSM plugin) ? This may cause problems if your data use <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">multipolygons</a> but would be enough for simple OSM elements (ways, nodes).</p>
</div>
<div id="comment-11168-info" class="comment-info">
<span class="comment-age">(13 Mar '12, 14:55)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="11175"></span>
<div id="comment-11175" class="comment">
<div id="post-11175-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think it is difficult to get the level of detail you want without some coding/scripting, but it is not that hard and it also makes it easier for you to keep you data updated. I have added some examples to my answer.</p>
</div>
<div id="comment-11175-info" class="comment-info">
<span class="comment-age">(13 Mar '12, 20:12)</span> <span class="comment-user userinfo">Dymo12</span>
</div>
</div>
<span id="11186"></span>
<div id="comment-11186" class="comment">
<div id="post-11186-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Dymo12 - thanks.</p>
<p>I have a lot of sorting out of my project to do before I attempt any of your suggestions - the guts of it is cognitive models of people and OSM is just the playground they will eventually use. For the moment, I can 'fake' a playground without sorting the OSM data and i need to do further work on the cogntiive model rather than the playground.</p>
<p>However, I will come back to this because I really like OSM, I even like that "There are no fixed rules for how anything should be tagged in OSM" - I much rpefer a flexible system even at the cost of having to learn how to code. When I get back to it, I will post what happened and how I succeeded. : )</p>
</div>
<div id="comment-11186-info" class="comment-info">
<span class="comment-age">(14 Mar '12, 09:20)</span> <span class="comment-user userinfo">jake cimilo</span>
</div>
</div>
</div>
<div id="comment-tools-11161" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11161-form-container" class="comment-form-container">
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

