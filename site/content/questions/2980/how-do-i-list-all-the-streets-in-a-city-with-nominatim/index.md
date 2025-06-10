+++
type = "question"
title = "How do I list all the streets in a city with nominatim?"
description = '''I&#x27;d like to list the names of every streets in a given city (from OSM data). How can I do that? I&#x27;ve tried with nominatim a query like: http://nominatim.openstreetmap.org/search?q=residentials%20in%20delft,netherlands But it returns an empty result (while if I look for &quot;pubs&quot;, it works fine). Using ...'''
date = "2011-02-12T11:29:00Z"
lastmod = "2014-01-24T18:25:00Z"
weight = 2980
keywords = [ "query", "nominatim", "street", "name" ]
aliases = [ "/questions/2980" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I list all the streets in a city with nominatim?](/questions/2980/how-do-i-list-all-the-streets-in-a-city-with-nominatim)

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
<span id="post-2980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2980-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-2980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to list the names of every streets in a given city (from OSM data). How can I do that?</p>
<p>I've tried with nominatim a query like: <a href="http://nominatim.openstreetmap.org/search?q=residentials%20in%20delft,netherlands">http://nominatim.openstreetmap.org/search?q=residentials%20in%20delft,netherlands</a></p>
<p>But it returns an empty result (while if I look for "pubs", it works fine). Using the details.php, I see that nominatim can list them: <a href="http://open.mapquestapi.com/nominatim/v1/details.php?place_id=7227120">http://open.mapquestapi.com/nominatim/v1/details.php?place_id=7227120</a></p>
<p>I'm working around using Xapi and a bounding box, but that works kind of ok only if the city is not surrounded too closely by other cities. Example of such a query: <a href="http://azure.openstreetmap.org/xapi/api/0.6/*%5Bhighway=residential%5D%5Bbbox=2.8634295463562,49.2131958007812,2.936068534807,49.2601203918457%5D">http://azure.openstreetmap.org/xapi/api/0.6/*[highway=residential][bbox=2.8634295463562,49.2131958007812,2.936068534807,49.2601203918457]</a></p>
<p>Can anyone suggest me a way to get it working via nominatim?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '11, 11:29</strong></p>
<img src="https://secure.gravatar.com/avatar/eea25ff6647bea6fd95feb3afdcac3b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="%C3%89ric%20Piel&#39;s gravatar image" />
<p><span>Éric Piel</span><br />
<span class="score" title="116 reputation points">116</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Éric Piel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2980" class="comments-container">
&#10;</div>
<div id="comment-tools-2980" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2980-form-container" class="comment-form-container">
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

<span id="3132"></span>

<div id="answer-container-3132" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3132-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-3132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to do it regularly for lots of cities this is the way:</p>
<ol>
<li><a href="http://dev.openstreetmap.org/~bretth/osmosis-build/osmosis-latest.zip">download osmosis</a> (and perhaps <a href="http://osmembrane.de">osmembrane</a> which is a beta GUI for osmosis)</li>
<li>download your country extract <a href="http://download.geofabrik.de/osm/europe/">netherlands.osm.pbf</a> (~430MB)</li>
<li>create a <a href="http://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format">polygon file parseable</a> by osmois (see <a href="http://trac.openstreetmap.org/browser/applications/utils/osm-extract/polygons/osm2poly.pl">osm2polygon</a>)</li>
<li>run osmosis with the polygon and extract all ways that have the tags name=* and highway=residential
<ol>
<li><a href="http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#--way-key_.28--wk.29">way-key</a> name,highway</li>
<li><a href="http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#--tag-filter_.28--tf.29">tag filter</a> reject-node, reject-relation</li>
</ol></li>
</ol>
<p>Then just filter out all the names in the resulting OSM xml file match all lines containing <code>k="name" v="</code> this can be done in many ways. Parsing Sweden (~70MB) with osmosis takes about 16 seconds on a 4 year old desktop machine..</p>
<p>This is my osmosis line without poly file</p>
<pre><code>osmosis-0.38/bin/osmosis --read-pbf file=sweden.osm.pbf  \
--bounding-box left=17.8 right=18.16 top=59.45 bottom=59.27 \
--way-key keyList=highway \
--way-key keyList=name \
--tag-filter reject-nodes \
--tag-filter reject-relations \
--write-xml Stockholm-names.osm</code></pre>
<p>Then I run:</p>
<pre><code>sed -n &#39;s/.*k=&quot;name&quot; v=&quot;//;T;s|&quot;/&gt;||;p&#39; Stockholm-names.osm |sort -u</code></pre>
<p><strong>Creating a Polygon file</strong></p>
<p>With Josm I created the a .osm file like this,</p>
<pre><code>&lt;?xml version=&#39;1.0&#39; encoding=&#39;UTF-8&#39;?&gt;
&lt;osm version=&#39;0.6&#39; generator=&#39;JOSM&#39;&gt;
  &lt;bounds minlat=&#39;59.323463999999994&#39; minlon=&#39;18.0798161&#39; maxlat=&#39;59.323715799999995&#39; maxlon=&#39;18.0805349&#39; origin=&#39;CGImap 0.0.2&#39; /&gt;
  &lt;bounds minlat=&#39;59.323463999999994&#39; minlon=&#39;18.0798161&#39; maxlat=&#39;59.323715799999995&#39; maxlon=&#39;18.0805349&#39; origin=&#39;OpenStreetMap server&#39; /&gt;
  &lt;node id=&#39;-28&#39; visible=&#39;true&#39; lat=&#39;59.30925658&#39; lon=&#39;18.044743&#39; /&gt;
  &lt;node id=&#39;-26&#39; visible=&#39;true&#39; lat=&#39;59.31157127&#39; lon=&#39;18.035956&#39; /&gt;
  &lt;node id=&#39;-24&#39; visible=&#39;true&#39; lat=&#39;59.31533231&#39; lon=&#39;18.025752&#39; /&gt;
  &lt;node id=&#39;-22&#39; visible=&#39;true&#39; lat=&#39;59.31779123&#39; lon=&#39;18.026035&#39; /&gt;
  &lt;node id=&#39;-20&#39; visible=&#39;true&#39; lat=&#39;59.31938219&#39; lon=&#39;18.028019&#39; /&gt;
  &lt;node id=&#39;-18&#39; visible=&#39;true&#39; lat=&#39;59.32024996&#39; lon=&#39;18.037940&#39; /&gt;
  &lt;node id=&#39;-16&#39; visible=&#39;true&#39; lat=&#39;59.32256391&#39; lon=&#39;18.048995&#39; /&gt;
  &lt;node id=&#39;-14&#39; visible=&#39;true&#39; lat=&#39;59.32184082&#39; lon=&#39;18.068552&#39; /&gt;
  &lt;node id=&#39;-12&#39; visible=&#39;true&#39; lat=&#39;59.31865904&#39; lon=&#39;18.086693&#39; /&gt;
  &lt;node id=&#39;-10&#39; visible=&#39;true&#39; lat=&#39;59.31692339&#39; lon=&#39;18.108802&#39; /&gt;
  &lt;node id=&#39;-8&#39; visible=&#39;true&#39; lat=&#39;59.31157127&#39; lon=&#39;18.103133&#39; /&gt;
  &lt;node id=&#39;-6&#39; visible=&#39;true&#39; lat=&#39;59.30621830&#39; lon=&#39;18.098881&#39; /&gt;
  &lt;node id=&#39;-4&#39; visible=&#39;true&#39; lat=&#39;59.30260096&#39; lon=&#39;18.077056&#39; /&gt;
  &lt;node id=&#39;-2&#39; visible=&#39;true&#39; lat=&#39;59.30274566&#39; lon=&#39;18.068552&#39; /&gt;
  &lt;node id=&#39;-1&#39; visible=&#39;true&#39; lat=&#39;59.30549486&#39; lon=&#39;18.058065&#39; /&gt;
  &lt;way id=&#39;-3&#39; action=&#39;modify&#39; visible=&#39;true&#39;&gt;
    &lt;nd ref=&#39;-1&#39; /&gt;
    &lt;nd ref=&#39;-2&#39; /&gt;
    &lt;nd ref=&#39;-4&#39; /&gt;
    &lt;nd ref=&#39;-6&#39; /&gt;
    &lt;nd ref=&#39;-8&#39; /&gt;
    &lt;nd ref=&#39;-10&#39; /&gt;
    &lt;nd ref=&#39;-12&#39; /&gt;
    &lt;nd ref=&#39;-14&#39; /&gt;
    &lt;nd ref=&#39;-16&#39; /&gt;
    &lt;nd ref=&#39;-18&#39; /&gt;
    &lt;nd ref=&#39;-20&#39; /&gt;
    &lt;nd ref=&#39;-22&#39; /&gt;
    &lt;nd ref=&#39;-24&#39; /&gt;
    &lt;nd ref=&#39;-26&#39; /&gt;
    &lt;nd ref=&#39;-28&#39; /&gt;
    &lt;nd ref=&#39;-1&#39; /&gt;
    &lt;tag k=&#39;polygon_file&#39; v=&#39;sodermalm&#39; /&gt;
    &lt;tag k=&#39;polygon_id&#39; v=&#39;1&#39; /&gt;
  &lt;/way&gt;
&lt;/osm&gt;</code></pre>
<p>With <a href="http://trac.openstreetmap.org/export/25346/applications/utils/osm-extract/polygons/osm2poly.pl">perl osm2poly.pl &lt;sodermalm_poly.osm&gt;sodermalm.poly</a> I got this:</p>
<pre><code>sodermalm
1
   1.805807E+01   5.930549E+01
   1.806855E+01   5.930275E+01
   1.807706E+01   5.930260E+01
   1.809888E+01   5.930622E+01
   1.810313E+01   5.931157E+01
   1.810880E+01   5.931692E+01
   1.808669E+01   5.931866E+01
   1.806855E+01   5.932184E+01
   1.804900E+01   5.932256E+01
   1.803794E+01   5.932025E+01
   1.802802E+01   5.931938E+01
   1.802604E+01   5.931779E+01
   1.802575E+01   5.931533E+01
   1.803596E+01   5.931157E+01
   1.804474E+01   5.930926E+01
   1.805807E+01   5.930549E+01
END
END</code></pre>
<p>Then I ran osmosis:</p>
<pre><code>osmosis-0.38/bin/osmosis --read-pbf file=sweden.osm.pbf  \
-bounding-polygon file=osmosis-0.38/sodermalm.poly \
--way-key keyList=highway \
--way-key keyList=name \
--tag-filter reject-nodes \
--tag-filter reject-relations \
--write-xml Stockholm-names.osm</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '11, 13:57</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Feb '11, 14:27</strong> </span></p>
</div>
</div>
<div id="comments-container-3132" class="comments-container">
<span id="25710"></span>
<div id="comment-25710" class="comment">
<div id="post-25710-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've been gathering poly files for cities at <a href="https://github.com/JamesChevalier/cities">https://github.com/JamesChevalier/cities</a> The method that I go through to create the poly files is in the readme file (displayed at the bottom of the page).</p>
</div>
<div id="comment-25710-info" class="comment-info">
<span class="comment-age">(24 Aug '13, 03:04)</span> <span class="comment-user userinfo">JamesChevalier</span>
</div>
</div>
</div>
<div id="comment-tools-3132" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3132-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3055"></span>

<div id="answer-container-3055" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3055-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-3055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim is designed to be a geocoding and reverse geocoding system rather than a general method of downloading data from OpenStreetMap and as such only a limited number of 'special' phrases work - normally restricted to points of interest. That said there will shortly be a downloadable version of the nominatim data set available which you could filter yourself for this information. Please watch for anouncements on the <span>geocoding mailing list</span>.</p>
<p>In the mean time you can download a suitable OSM file (either from xapi, or a planet extract or even the full planet file) and filter it using the bounding-polygon option of <span>Osmosis</span>. You may be able to download the polygon from OSM, in other cases you will have to draw it yourself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Feb '11, 09:32</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Feb '11, 09:33</strong> </span></p>
</div>
</div>
<div id="comments-container-3055" class="comments-container">
<span id="30191"></span>
<div id="comment-30191" class="comment">
<div id="post-30191-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You mention 'You may be able to download the polygon from OSM' ... Where (when they exist) are those available?</p>
</div>
<div id="comment-30191-info" class="comment-info">
<span class="comment-age">(24 Jan '14, 18:25)</span> <span class="comment-user userinfo">JamesChevalier</span>
</div>
</div>
</div>
<div id="comment-tools-3055" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3055-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3077"></span>

<div id="answer-container-3077" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3077-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-3077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should also take a look at <a href="http://maposmatic.org/">http://maposmatic.org/</a> , which does pretty much what you are looking for and allows you to download either a rendered version or the raw data. They explain how they did it in the "about" page, and the tool they wrote is available. It requires that you have a local installation of OSM tools and database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Feb '11, 15:02</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Feb '11, 15:09</strong> </span></p>
</div>
</div>
<div id="comments-container-3077" class="comments-container">
&#10;</div>
<div id="comment-tools-3077" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3077-form-container" class="comment-form-container">
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

