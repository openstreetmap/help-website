+++
type = "question"
title = "How to match node place=city to appropriate relation boundary=administrative"
description = '''My question is about processing raw OSM data from .osm.pbf exports. Please don&#x27;t point me to any online tools, nominatim, or overpass queries. I have list of Nodes that represent cities in all Europe, for example node for Wrocław has ID of 418392093 I&#x27;d like to select from .osm.pbf relation that rep...'''
date = "2018-08-10T17:37:00Z"
lastmod = "2018-08-10T22:10:00Z"
weight = 65255
keywords = [ "boundaries", "cities", "osm", "pbf" ]
aliases = [ "/questions/65255" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to match node place=city to appropriate relation boundary=administrative](/questions/65255/how-to-match-node-placecity-to-appropriate-relation-boundaryadministrative)

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
<span id="post-65255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65255-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-65255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My question is about processing raw OSM data from .osm.pbf exports.</p>
<p><em>Please don't point me to any online tools, nominatim, or overpass queries.</em></p>
<p>I have list of Nodes that represent cities in all Europe, for example node for Wrocław has ID of <a href="https://www.openstreetmap.org/node/418392093">418392093</a></p>
<p>I'd like to select from .osm.pbf relation that represents boundary of this city. Fortunately, <code>boundary=administrative</code> <a href="https://www.openstreetmap.org/relation/2805690">Relation</a> has Wrocław's ID listed as <code>admin_centre</code>. <em>Unfortunately</em> Wrocław is also listed as <code>admin_centre</code> of the region it is in (<a href="https://www.openstreetmap.org/relation/224457">Dolnośląskie voivodeship</a>).</p>
<p><strong>How can I know for sure which boundary relation matches which city node?</strong></p>
<p>Subquestions:</p>
<ol>
<li>If the answer is "you can use name", is it reliable method? Does boundary has <strong>always</strong> the same name as node?</li>
<li>If the answer is "select boundary with highest admin level", is it reliable as well? What if subregion has the same admin centre?</li>
<li>If there isn't "official" method of doing so, why? It seems an important use case to know boundary of any city.</li>
</ol>
<p>Raw data for Relation for administrative boundary of Wrocław <strong>city</strong> looks like this:</p>
<pre><code>  {
    &quot;ID&quot;: 2805690,
    &quot;Members&quot;: {
      &quot;admin_centre&quot;: [
        418392093
      ],
      &quot;outer&quot;: [
        52452667,
        ...
        443264980
      ],
      &quot;subarea&quot;: [
        2341621,
        ...
        2318980
      ]
    },
    &quot;Tags&quot;: {
      &quot;admin_level&quot;: &quot;8&quot;,
      &quot;boundary&quot;: &quot;administrative&quot;,
      &quot;name&quot;: &quot;Wrocław&quot;,
      ...
      &quot;name:szl&quot;: &quot;Wrocłow&quot;,
      &quot;old_name:eo&quot;: &quot;Breslaŭo&quot;,
      &quot;old_name:pl&quot;: &quot;Wratislaw&quot;,
      &quot;type&quot;: &quot;boundary&quot;,
      &quot;wikidata&quot;: &quot;Q1799&quot;,
      &quot;wikipedia&quot;: &quot;pl:Wrocław&quot;
    }
  },</code></pre>
<p>Raw data for Relation for administrative boundary of a <strong>region</strong> Wrocław is in looks like this:</p>
<pre><code> {
    &quot;ID&quot;: 224457,
    &quot;Members&quot;: {
      &quot;admin_centre&quot;: [
        418392093
      ],
      &quot;label&quot;: [
        505025705
      ],
      &quot;outer&quot;: [
        175469910,
        ...
        176467203
      ],
      &quot;subarea&quot;: [
        451266,
        ...
        451516
      ]
    },
    &quot;Tags&quot;: {
      &quot;ISO3166-2&quot;: &quot;PL-DS&quot;,
      &quot;admin_level&quot;: &quot;4&quot;,
      &quot;alt_name:en&quot;: &quot;Lower Silesian Province&quot;,
      &quot;boundary&quot;: &quot;administrative&quot;,
      &quot;int_name&quot;: &quot;wojewodztwo dolnoslaskie&quot;,
      &quot;license_plate_code&quot;: &quot;D&quot;,
      &quot;loc_name&quot;: &quot;Dolnośląskie&quot;,
      &quot;long_name:fr&quot;: &quot;Voïvodie de Basse-Silésie&quot;,
      &quot;name&quot;: &quot;województwo dolnośląskie&quot;,
      &quot;name:ar&quot;: &quot;محافظة سيلزيا السفلى&quot;,
      ...
      &quot;name:zh&quot;: &quot;下西里西亚省&quot;,
      &quot;population&quot;: &quot;1970217&quot;,
      &quot;ref&quot;: &quot;DS&quot;,
      &quot;short_name&quot;: &quot;dolnośląskie&quot;,
      &quot;source:population&quot;: &quot;Bank Danych Lokalnych - stan na dzień 31.12.2016&quot;,
      &quot;teryt:terc&quot;: &quot;02&quot;,
      &quot;type&quot;: &quot;boundary&quot;,
      &quot;wikidata&quot;: &quot;Q54150&quot;,
      &quot;wikipedia&quot;: &quot;pl:Województwo dolnośląskie&quot;
    }
  },</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-cities" rel="tag" title="see questions tagged &#39;cities&#39;">cities</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Aug '18, 17:37</strong></p>
<img src="https://secure.gravatar.com/avatar/306b63b79c78a1b67e1789790ad2db86?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sheerun&#39;s gravatar image" />
<p><span>sheerun</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sheerun has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Aug '18, 17:38</strong> </span></p>
</div>
</div>
<div id="comments-container-65255" class="comments-container">
<span id="65259"></span>
<div id="comment-65259" class="comment">
<div id="post-65259-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>At a minimum you need to create geographical objects from your PBF. It so happens Nominatim &amp; Overpass are by far and away the easiest options. You cant process relationships in geodata without turning into geographies. A short answer is process into PostGIS with osm2pgsql and write suitable queries there: the downside is that you lose some explict relationships between city nodes &amp; boundary relations: however as there is no guarantee that these exist consistently you still have to solve the problem.</p>
</div>
<div id="comment-65259-info" class="comment-info">
<span class="comment-age">(10 Aug '18, 22:10)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65255" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65255-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

