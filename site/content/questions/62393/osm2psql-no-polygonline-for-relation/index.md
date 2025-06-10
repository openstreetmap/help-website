+++
type = "question"
title = "Osm2psql no polygon/line for relation"
description = '''So im trying todo some analysize with osm2pgsql From what I read from the documentation I was supposed to call the osm2pgsql command with -G which is what I have done. Now I&#x27;m trying to understand why there are no planet_osm_polygon or planet_osm_line for certain planet_osm_rels. E.g. lets take foll...'''
date = "2018-02-25T16:49:00Z"
lastmod = "2018-05-11T04:20:00Z"
weight = 62393
keywords = [ "postgresql", "osm2pgsql", "postgis", "polygon" ]
aliases = [ "/questions/62393" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Osm2psql no polygon/line for relation](/questions/62393/osm2psql-no-polygonline-for-relation)

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
<span id="post-62393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62393-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So im trying todo some analysize with osm2pgsql</p>
<p>From what I read from the documentation I was supposed to call the osm2pgsql command with -G which is what I have done.</p>
<p>Now I'm trying to understand why there are no planet_osm_polygon or planet_osm_line for certain planet_osm_rels.</p>
<p>E.g. lets take following relation</p>
<pre><code>SELECT * FROM planet_osm_rels WHERE id=6720604
&#10;&quot;id&quot;,&quot;way_off&quot;,&quot;rel_off&quot;,&quot;parts&quot;,&quot;members&quot;,&quot;tags&quot;
6720604,0,74,&quot;{326805364,326805360,94231412,31114639,31114638,31981611,31981635,31114634,558620158,558620159,558620157,558620160,30081284,31114640,558620183,31114633,558620149,31114636,558620152,558620161,558620156,558620151,558620153,326805353,31981645,326805358,326805359,31981639,326805355,558620147,326805350,30081288,326805354,94231410,558620169,558620168,558620167,31096644,558620166,558620170,30081299,558620163,558620162,558620165,100534409,558620150,558620148,31114637,558620164,31977042,54517047,30081290,454328977,326805362,558730585,32009830,558620180,558620181,54255111,186651151,326805357,259267365,558620176,37994264,54517048,326805363,558620177,558620178,558620175,31976982,454328978,23045055,326805361,326805352,3479986,3479881,7981263,7981262,7981261,7981260,7981259,7981257,7981256,7981255,7981254,7981253,7981252,7982581}&quot;,&quot;{r3479986,&quot;&quot;&quot;&quot;,r3479881,&quot;&quot;&quot;&quot;,w326805364,&quot;&quot;&quot;&quot;,w326805360,&quot;&quot;&quot;&quot;,w94231412,&quot;&quot;&quot;&quot;,w31114639,&quot;&quot;&quot;&quot;,w31114638,&quot;&quot;&quot;&quot;,w31981611,&quot;&quot;&quot;&quot;,w31981635,&quot;&quot;&quot;&quot;,w31114634,&quot;&quot;&quot;&quot;,w558620158,&quot;&quot;&quot;&quot;,w558620159,&quot;&quot;&quot;&quot;,w558620157,&quot;&quot;&quot;&quot;,w558620160,&quot;&quot;&quot;&quot;,w30081284,&quot;&quot;&quot;&quot;,w31114640,&quot;&quot;&quot;&quot;,w558620183,&quot;&quot;&quot;&quot;,w31114633,&quot;&quot;&quot;&quot;,w558620149,&quot;&quot;&quot;&quot;,w31114636,&quot;&quot;&quot;&quot;,w558620152,&quot;&quot;&quot;&quot;,w558620161,&quot;&quot;&quot;&quot;,w558620156,&quot;&quot;&quot;&quot;,w558620151,&quot;&quot;&quot;&quot;,w558620153,&quot;&quot;&quot;&quot;,w326805353,&quot;&quot;&quot;&quot;,w31981645,&quot;&quot;&quot;&quot;,w326805358,&quot;&quot;&quot;&quot;,w326805359,&quot;&quot;&quot;&quot;,w31981639,&quot;&quot;&quot;&quot;,w326805355,&quot;&quot;&quot;&quot;,w558620147,&quot;&quot;&quot;&quot;,w326805350,&quot;&quot;&quot;&quot;,w30081288,&quot;&quot;&quot;&quot;,w326805354,&quot;&quot;&quot;&quot;,w94231410,&quot;&quot;&quot;&quot;,w558620169,&quot;&quot;&quot;&quot;,w558620168,&quot;&quot;&quot;&quot;,w558620167,&quot;&quot;&quot;&quot;,w31096644,&quot;&quot;&quot;&quot;,w558620166,&quot;&quot;&quot;&quot;,w558620170,&quot;&quot;&quot;&quot;,w30081299,&quot;&quot;&quot;&quot;,w558620163,&quot;&quot;&quot;&quot;,w558620162,&quot;&quot;&quot;&quot;,w558620165,&quot;&quot;&quot;&quot;,w100534409,&quot;&quot;&quot;&quot;,w558620150,&quot;&quot;&quot;&quot;,w558620148,&quot;&quot;&quot;&quot;,w31114637,&quot;&quot;&quot;&quot;,w558620164,&quot;&quot;&quot;&quot;,w31977042,&quot;&quot;&quot;&quot;,w54517047,&quot;&quot;&quot;&quot;,w30081290,&quot;&quot;&quot;&quot;,w454328977,&quot;&quot;&quot;&quot;,w326805362,&quot;&quot;&quot;&quot;,w558730585,&quot;&quot;&quot;&quot;,w32009830,&quot;&quot;&quot;&quot;,w558620180,&quot;&quot;&quot;&quot;,w558620181,&quot;&quot;&quot;&quot;,w54255111,&quot;&quot;&quot;&quot;,w186651151,&quot;&quot;&quot;&quot;,w326805357,&quot;&quot;&quot;&quot;,w259267365,&quot;&quot;&quot;&quot;,w558620176,&quot;&quot;&quot;&quot;,w37994264,&quot;&quot;&quot;&quot;,w54517048,&quot;&quot;&quot;&quot;,w326805363,&quot;&quot;&quot;&quot;,w558620177,&quot;&quot;&quot;&quot;,w558620178,&quot;&quot;&quot;&quot;,w558620175,&quot;&quot;&quot;&quot;,w31976982,&quot;&quot;&quot;&quot;,w454328978,&quot;&quot;&quot;&quot;,w23045055,&quot;&quot;&quot;&quot;,w326805361,&quot;&quot;&quot;&quot;,w326805352,&quot;&quot;&quot;&quot;,r7981263,&quot;&quot;&quot;&quot;,r7981262,&quot;&quot;&quot;&quot;,r7981261,&quot;&quot;&quot;&quot;,r7981260,&quot;&quot;&quot;&quot;,r7981259,&quot;&quot;&quot;&quot;,r7981257,&quot;&quot;&quot;&quot;,r7981256,&quot;&quot;&quot;&quot;,r7981255,&quot;&quot;&quot;&quot;,r7981254,&quot;&quot;&quot;&quot;,r7981253,&quot;&quot;&quot;&quot;,r7981252,&quot;&quot;&quot;&quot;,r7982581,&quot;&quot;&quot;&quot;}&quot;,&quot;{leisure,ski_resort,name,Savognin,site,piste,type,site}&quot;</code></pre>
<p>For that relation I can't find any corresponding line or polygon.</p>
<p>Do I need to configure my default.style differently?</p>
<p>Or bascially what is the cause why there is no line or polygon and how can I make sure one get's generated. I hope that is possible :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Feb '18, 16:49</strong></p>
<img src="https://secure.gravatar.com/avatar/b59231b2ea01633cc4c5936cd117dc84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gabac&#39;s gravatar image" />
<p><span>gabac</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gabac has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Feb '18, 16:57</strong> </span></p>
</div>
</div>
<div id="comments-container-62393" class="comments-container">
&#10;</div>
<div id="comment-tools-62393" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62393-form-container" class="comment-form-container">
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

<span id="62394"></span>

<div id="answer-container-62394" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62394-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://www.openstreetmap.org/relation/6720604">That relation</a> is a type=site relation. My recollection is that osm2pgsql doesn't process those at all. There's a discussion about the rendering of type=site relations in the standard style <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/2940">here</a> - that links to other issues discussing "what would need to change to render them".</p>
<p>If there's some useful geometry in a type=site relation you could get osm2pgsql to process it by using a lua tag transform. The relevant bits of the one used by OSM's standard style are <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.lua#L308">here</a> and <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.lua#L348">here</a>.</p>
<p>What you'd probably need to do is:</p>
<ul>
<li>Identify a subset of type=site relations with valid geometry</li>
<li>Write a lua tag transform to turn them into something that osm2pgsql will continue to process</li>
<li>Write some style code in your map style to do something useful with the data.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Feb '18, 17:07</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Feb '18, 17:08</strong> </span></p>
</div>
</div>
<div id="comments-container-62394" class="comments-container">
<span id="63420"></span>
<div id="comment-63420" class="comment">
<div id="post-63420-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>exact, osm2pgsqk processes only a part of the "multipolygon" , "boundary" and "route" types. Each tool has its algorithm and others analyze more relation types. Osm_id is negative for a relation.</p>
</div>
<div id="comment-63420-info" class="comment-info">
<span class="comment-age">(11 May '18, 04:20)</span> <span class="comment-user userinfo">AntaC</span>
</div>
</div>
</div>
<div id="comment-tools-62394" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62394-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62395"></span>

<div id="answer-container-62395" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62395-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Osm2pgsql is able to handle routes and multipolygon relations, not sites. From the routes and MPs relations, there is a way to calculate a geometry and put them in the planet_osm_line or_polygon tables, but not for sites.</p>
<p>Of you want to use sites, then you can create yourself a polygon around their member, for example, and insert them into the planet_osm_polygon table. But that's a process I don't think Osm2pgsql can do. Yves</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Feb '18, 17:22</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-62395" class="comments-container">
&#10;</div>
<div id="comment-tools-62395" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62395-form-container" class="comment-form-container">
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

