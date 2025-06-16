+++
type = "question"
title = "OSM data import error into nominatim"
description = '''Hi everybody! I have been trying, for days now, to import a set of osm data into nominatim. These data have been manually generated using the JOSM tool. The import seems to work smoothly, but, at the end I get the following output: Stopping table: planet_osm_rels Building index on table: planet_osm_...'''
date = "2016-05-26T10:12:00Z"
lastmod = "2016-05-31T02:21:00Z"
weight = 49835
keywords = [ "import", "nominatim", "error" ]
aliases = [ "/questions/49835" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM data import error into nominatim](/questions/49835/osm-data-import-error-into-nominatim)

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
<span id="post-49835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49835-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everybody!</p>
<p>I have been trying, for days now, to import a set of osm data into nominatim. These data have been manually generated using the JOSM tool. The import seems to work smoothly, but, at the end I get the following output:</p>
<pre><code>Stopping table: planet_osm_rels
Building index on table: planet_osm_rels
Stopping table: planet_osm_ways
Stopped table: planet_osm_ways in 0s
Stopping table: planet_osm_nodes
Stopped table: planet_osm_nodes in 0s
Stopped table: planet_osm_rels in 0s
node cache: stored: 7(100.00%), storage efficiency: 0.68% (dense blocks: 1, sparse nodes: 0), hit rate: -nan%
&#10;Osm2pgsql took 0s overall
ERROR: No Data
No Data</code></pre>
<p>And, in the end, nothing is imported even though it seems.</p>
<p>A small sample of the data I am trying to import:</p>
<pre><code>&lt;node id=&#39;-9149&#39; visible=&#39;true&#39; lat=&#39;51.8386&#39; lon=&#39;4.9578&#39;&gt;
   &lt;tag k=&#39;electrical_capacity&#39; v=&#39;12h&#39; /&gt;
   &lt;tag k=&#39;general_state&#39; v=&#39;normal&#39; /&gt;
   &lt;tag k=&#39;name&#39; v=&#39;Beatrixziekenhuis&#39; /&gt;
   &lt;tag k=&#39;number_of_men&#39; v=&#39;1500&#39; /&gt;
   &lt;tag k=&#39;resource_availability&#39; v=&#39;HIGH&#39; /&gt;
   &lt;tag k=&#39;state&#39; v=&#39;1&#39; /&gt;
   &lt;tag k=&#39;telecom_availability&#39; v=&#39;TRUE&#39; /&gt;
   &lt;tag k=&#39;type&#39; v=&#39;hospital&#39; /&gt;
&lt;/node&gt;
&lt;node id=&#39;-9202&#39;  visible=&#39;true&#39; lat=&#39;51.8456942144&#39; lon=&#39;4.95328903198&#39; /&gt;
&lt;node id=&#39;-9203&#39;  visible=&#39;true&#39; lat=&#39;51.83503500628&#39; lon=&#39;4.94672298431&#39; /&gt;
&lt;node id=&#39;-9204&#39;  visible=&#39;true&#39; lat=&#39;51.83020836571&#39; lon=&#39;4.96204376221&#39; /&gt;
&lt;node id=&#39;-9205&#39;  visible=&#39;true&#39; lat=&#39;51.83697082115&#39; lon=&#39;4.97406005859&#39; /&gt;
&lt;node id=&#39;-9206&#39;  visible=&#39;true&#39; lat=&#39;51.84625096935&#39; lon=&#39;4.97860908508&#39; /&gt;
&lt;node id=&#39;-9207&#39;  visible=&#39;true&#39; lat=&#39;51.8456942144&#39; lon=&#39;4.95328903198&#39; /&gt;
&#10;&lt;way id=&#39;-9208&#39; visible=&#39;true&#39;&gt;
  &lt;nd ref=&#39;-9202&#39; /&gt;
  &lt;nd ref=&#39;-9203&#39; /&gt;
  &lt;nd ref=&#39;-9204&#39; /&gt;
  &lt;nd ref=&#39;-9205&#39; /&gt;
  &lt;nd ref=&#39;-9206&#39; /&gt;
  &lt;nd ref=&#39;-9207&#39; /&gt;
  &lt;tag k=&#39;electricity_availability&#39; v=&#39;TRUE&#39; /&gt;
  &lt;tag k=&#39;flood_vulnerability&#39; v=&#39;350&#39; /&gt;
  &lt;tag k=&#39;general_state&#39; v=&#39;normal&#39; /&gt;
  &lt;tag k=&#39;name&#39; v=&#39;Gorinchem&#39; /&gt;
  &lt;tag k=&#39;number_of_men&#39; v=&#39;1000&#39; /&gt;
  &lt;tag k=&#39;state&#39; v=&#39;1&#39; /&gt;
  &lt;tag k=&#39;telecom_availability&#39; v=&#39;TRUE&#39; /&gt;
  &lt;tag k=&#39;type&#39; v=&#39;residentialarea&#39; /&gt;
  &lt;tag k=&#39;water_availability&#39; v=&#39;TRUE&#39; /&gt;
&lt;/way&gt;</code></pre>
<p>Any suggestions ? Anyone ever encountered this same issue ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 May '16, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/dc400b116300e713442e10b6d3c1dfe4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GabBurnout&#39;s gravatar image" />
<p><span>GabBurnout</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GabBurnout has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 May '16, 22:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-49835" class="comments-container">
<span id="49836"></span>
<div id="comment-49836" class="comment">
<div id="post-49836-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Forgot to mention, I am trying to import the data using Nominatim.</p>
<p>Thanks again</p>
</div>
<div id="comment-49836-info" class="comment-info">
<span class="comment-age">(26 May '16, 10:17)</span> <span class="comment-user userinfo">GabBurnout</span>
</div>
</div>
<span id="49837"></span>
<div id="comment-49837" class="comment">
<div id="post-49837-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd compare what's in your data with what's in some data that you can import successfully. I'd specifically look at what enclosing XML tags are in there.</p>
</div>
<div id="comment-49837-info" class="comment-info">
<span class="comment-age">(26 May '16, 10:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="49839"></span>
<div id="comment-49839" class="comment">
<div id="post-49839-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank for your answer,</p>
<p>Have tried to remove all the tags, leaving only the name, but the problem persists.</p>
</div>
<div id="comment-49839-info" class="comment-info">
<span class="comment-age">(26 May '16, 10:30)</span> <span class="comment-user userinfo">GabBurnout</span>
</div>
</div>
<span id="49840"></span>
<div id="comment-49840" class="comment">
<div id="post-49840-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did the data that you were able to import from some other source have "only the name" in it? If not, try a (small) Nominatim import of some other data, and look at the tags in that.</p>
</div>
<div id="comment-49840-info" class="comment-info">
<span class="comment-age">(26 May '16, 10:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="49842"></span>
<div id="comment-49842" class="comment">
<div id="post-49842-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I used a group of tags directly from the Faroe-islands downloaded from Geofabrik.</p>
<p>Now something is imported. Finally!</p>
<p>It seems to be a tags-related problem.</p>
<p>Where is a list of supported tags for an osm data that Nominatim does not complain about ? And that can be used for searching operations ?</p>
<p>Thanks again</p>
</div>
<div id="comment-49842-info" class="comment-info">
<span class="comment-age">(26 May '16, 11:20)</span> <span class="comment-user userinfo">GabBurnout</span>
</div>
</div>
</div>
<div id="comment-tools-49835" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49835-form-container" class="comment-form-container">
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

<span id="49841"></span>

<div id="answer-container-49841" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49841-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim doesn't index everything with a name (or ref) tag. It looks for places, streets and similar tag combinations. For some tags it uses a positive list of desired values, for others a negative list. That happens in the file output_gazetteer.cpp.</p>
<p><a href="https://github.com/openstreetmap/osm2pgsql/blob/d0af11f267a202c7c1961c2061d121c726d8db3a/output-gazetteer.cpp">https://github.com/openstreetmap/osm2pgsql/blob/d0af11f267a202c7c1961c2061d121c726d8db3a/output-gazetteer.cpp</a></p>
<p>You can either change the logic in the process_tags method to treat all electrical lines like places. Or add a tag place=locality to all your data before importing. <a href="https://wiki.openstreetmap.org/wiki/Key:place">https://wiki.openstreetmap.org/wiki/Key:place</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 May '16, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-49841" class="comments-container">
<span id="49870"></span>
<div id="comment-49870" class="comment">
<div id="post-49870-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>thanks for you reply. I played a bit around with tags, and finally managed to get something, the import was successful, and also some research operation works.</p>
<p>Still, it's not how I want yet. I want to have a node representing an hospital, in a specific city (e.g. Gorinchem) in a specific country.</p>
<p>This is the node, in the osm file, that I am using:</p>
<pre><code>&lt;node id=&#39;-9149&#39; visible=&#39;true&#39; lat=&#39;51.8386&#39; lon=&#39;4.9578&#39;&gt;
&lt;tag k=&quot;is_in&quot; v=&quot;Gorinchem, The Netherlands&quot;/&gt;
&lt;tag k=&quot;amenity&quot; v=&quot;hospital&quot;/&gt;
&lt;tag k=&quot;building&quot; v=&quot;yes&quot;/&gt;
    &lt;tag k=&#39;name&#39; v=&#39;Beatrixziekenhuis&#39; /&gt;
&lt;tag k=&#39;addr:city&#39; v=&#39;Gorinchem&#39; /&gt;
&lt;tag k=&#39;addr:country&#39; v=&#39;NL&#39; /&gt;
&lt;tag k=&quot;addr:street&quot; v=&quot;Banneweg&quot;/&gt;
&lt;tag k=&quot;addr:postcode&quot; v=&quot;4204AA&quot;/&gt;
&lt;tag k=&quot;addr:housenumber&quot; v=&quot;57&quot;/&gt;
 &lt;/node&gt;</code></pre>
<p>I also added information relative to the specific address.</p>
<p>Basically, I want to be able to perform a research operation that could return me the hospital present in that city, or in that country.</p>
<p>As far as I know the query should be:</p>
<pre><code>  q=The+Netherlands[hospitals]</code></pre>
<p>What am I missing in that node ?</p>
<p>Thanks</p>
</div>
<div id="comment-49870-info" class="comment-info">
<span class="comment-age">(27 May '16, 15:22)</span> <span class="comment-user userinfo">GabBurnout</span>
</div>
</div>
<span id="49920"></span>
<div id="comment-49920" class="comment">
<div id="post-49920-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you import the city and country as well? The is_in key is a hint but the place still needs to exist in the Nominatim database to create a hierarchy.</p>
<p>The query format looks good</p>
<p><a href="http://nominatim.openstreetmap.org/search.php?q=the+nederlands+%5Bhospitals%5D">http://nominatim.openstreetmap.org/search.php?q=the+nederlands+%5Bhospitals%5D</a></p>
<p>Here's a list of all 'special phrases' that can be added to those square brackets. <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases">https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases</a> after you ran the <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation#Add_special_phrases">https://wiki.openstreetmap.org/wiki/Nominatim/Installation#Add_special_phrases</a> step of the installation.</p>
</div>
<div id="comment-49920-info" class="comment-info">
<span class="comment-age">(31 May '16, 02:21)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-49841" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49841-form-container" class="comment-form-container">
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

