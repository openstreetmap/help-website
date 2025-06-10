+++
type = "question"
title = "Help / Aide :OSM postgis query Layers line Point"
description = '''Bonsoir Je suis nouveau ( moins d’un mois ) , pour faire la version courte . - J’ai installé Qgis (pas encore réellement utilisé) - Installé Postgresql (connaissance limite ) - Téléchargé depuis https://download.geofabrik.de/ et intégré avec deux méthodes ogr2ogr et osm2pgsql (bien sur 2 bases ) (re...'''
date = "2018-03-21T21:16:00Z"
lastmod = "2018-03-24T20:12:00Z"
weight = 62770
keywords = [ "postgresql", "points", "osm", "lines", "query" ]
aliases = [ "/questions/62770" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Help / Aide :OSM postgis query Layers line Point](/questions/62770/help-aide-osm-postgis-query-layers-line-point)

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
<span id="post-62770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62770-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Bonsoir</p>
<p>Je suis nouveau ( moins d’un mois ) , pour faire la version courte . - J’ai installé Qgis (pas encore réellement utilisé) - Installé Postgresql (connaissance limite ) - Téléchargé depuis <a href="https://download.geofabrik.de/">https://download.geofabrik.de/</a> et intégré avec deux méthodes ogr2ogr et osm2pgsql (bien sur 2 bases ) (recherche sur le net) . L’idée est de pouvoir extraire une base de donnée (voie/Rue/….) cad planet_osm_line et les associés avec (Localité,Ville,village…) planet_osm_point et de les comparer avec un référentiel pour avoir les candidats (voie/Rue/….) qui ne figurent pas sur OSM C’est ici que j’ai besoin de votre aide. Voici la query simplifié :</p>
<pre><code>SELECT 
    public.planet_osm_line.name,public.planet_osm_line.highway,public.planet_osm_line.boundary,
    public.planet_osm_line.route,public.planet_osm_line.barrier,public.planet_osm_line.osm_id,
    public.planet_osm_point.name, public.planet_osm_point.place,public.planet_osm_point.amenity,
    public.planet_osm_point.osm_id
FROM
  public.planet_osm_line,
   public.planet_osm_point
  where
  ST_Contains(public.planet_osm_line.way,  public.planet_osm_point.way)
  And 
  (public.planet_osm_point.place = &#39;city&#39; OR
   public.planet_osm_point.place = &#39;town&#39; OR
   public.planet_osm_point.place = &#39;village&#39; OR
   public.planet_osm_point.place = &#39;hamlet&#39; OR
   public.planet_osm_point.place = &#39;dwelling&#39;)</code></pre>
<p>Résultat : rien .</p>
<p>Merci d’avance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-points" rel="tag" title="see questions tagged &#39;points&#39;">points</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-lines" rel="tag" title="see questions tagged &#39;lines&#39;">lines</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Mar '18, 21:16</strong></p>
<img src="https://secure.gravatar.com/avatar/ad98d8b056eb0ac971523411f851db1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fox2000&#39;s gravatar image" />
<p><span>Fox2000</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fox2000 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Mar '18, 21:26</strong> </span></p>
</div>
</div>
<div id="comments-container-62770" class="comments-container">
&#10;</div>
<div id="comment-tools-62770" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62770-form-container" class="comment-form-container">
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

<span id="62775"></span>

<div id="answer-container-62775" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62775-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p>Est-ce que <a href="https://cadastre.openstreetmap.fr/fantoir/">https://cadastre.openstreetmap.fr/fantoir/</a> fait déjà ce que tu veux faire?</p>
<p>Sinon, <code>st_contains</code> n'est pas la fonction que tu recherches; tu n'aurais des résultats que si le chemin est accidentellement à cheval sur la frontière d'une commune. Je crois que tu veux quelque chose <code>st_within</code> ou <code>st_intersects</code>, genre:</p>
<p><code>select distinct l.name from planet_osm_line l, planet_osm_polygon g where l.highway is not null and l.name is not null AND ST_Intersects(l.way,g.way) AND g.name LIKE 'Commune';</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '18, 08:17</strong></p>
<img src="https://secure.gravatar.com/avatar/aace33beb0d1a608b0763ac8a2404049?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stereo&#39;s gravatar image" />
<p><span>Stereo</span><br />
<span class="score" title="356 reputation points">356</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stereo has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-62775" class="comments-container">
<span id="62811"></span>
<div id="comment-62811" class="comment">
<div id="post-62811-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Merci beaucoup tu m'aides beaucoup.</p>
</div>
<div id="comment-62811-info" class="comment-info">
<span class="comment-age">(24 Mar '18, 20:12)</span> <span class="comment-user userinfo">Fox2000</span>
</div>
</div>
</div>
<div id="comment-tools-62775" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62775-form-container" class="comment-form-container">
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

