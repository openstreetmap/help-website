+++
type = "question"
title = "How to import OSM ways, without tags, into PostgreSQL using osm2pgsql?"
description = '''I have a very special problem when importing OSM Data with osm2pgsql. I was searching for days on how to import ways which do not have any tag but which are part of a relation (which itself has tags) into PostgresDB. Take the following way for example: http://www.openstreetmap.org/way/50126690 As yo...'''
date = "2017-04-14T19:30:00Z"
lastmod = "2017-04-14T19:30:00Z"
weight = 55609
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/55609" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to import OSM ways, without tags, into PostgreSQL using osm2pgsql?](/questions/55609/how-to-import-osm-ways-without-tags-into-postgresql-using-osm2pgsql)

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
<span id="post-55609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55609-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a very special problem when importing OSM Data with osm2pgsql. I was searching for days on how to import ways which do not have any tag but which are part of a relation (which itself has tags) into PostgresDB. Take the following way for example: <a href="http://www.openstreetmap.org/way/50126690">http://www.openstreetmap.org/way/50126690</a> As you can see it does not have any tags but is part of the relation <a href="http://www.openstreetmap.org/relation/2">http://www.openstreetmap.org/relation/2</a> … 81/12.3246 which is tagged as a cross country slope. When I import data into postgresql, the way 50126690 is not imported. Even when I use --hstore option which should keep all objects if you believe documentation on <a href="http://www.volkerschatz.com/net/osm/osm2pgsql-usage.htm">http://www.volkerschatz.com/net/osm/osm2pgsql-usage.htm</a> the way will not be imported into planet_osm_line table. My default.style looks like that:</p>
<code> </code>
<h1 id="osmtype-tag-datatype-flags">OsmType Tag DataType Flags</h1>
<p>node,way access text linear node,way addr:housename text linear node,way addr:housenumber text linear node,way addr:interpolation text linear node,way admin_level text linear node,way aerialway text linear node,way aeroway text polygon node,way amenity text polygon node,way area text polygon # hard coded support for area=1/yes =&gt; polygon is in osm2pgsql node,way barrier text linear node,way bicycle text linear node,way brand text linear node,way bridge text linear node,way boundary text linear node,way building text polygon node capital text linear node,way construction text linear node,way covered text linear node,way culvert text linear node,way cutting text linear node,way denomination text linear node,way disused text linear node ele text linear node,way embankment text linear node,way foot text linear node,way generator:source text linear node,way harbour text polygon node,way highway text linear node,way historic text polygon node,way horse text linear node,way intermittent text linear node,way junction text linear node,way landuse text polygon node,way layer text linear node,way leisure text polygon node,way lock text linear node,way man_made text polygon node,way military text polygon node,way motorcar text linear node,way name text linear node,way natural text polygon # natural=coastline tags are discarded by a hard coded rule in osm2pgsql node,way office text polygon node,way oneway text linear node,way operator text linear node,way place text polygon node poi text linear node,way population text linear node,way power text polygon node,way power_source text linear node,way public_transport text polygon node,way railway text linear node,way ref text linear node,way religion text linear node,way route text linear node,way service text linear node,way shop text polygon node,way sport text polygon node,way surface text linear node,way toll text linear node,way tourism text polygon node,way tower:type text linear way tracktype text linear node,way tunnel text linear node,way water text polygon node,way waterway text polygon node,way wetland text polygon node,way width text linear node,way wood text linear node,way z_order int4 linear # This is calculated during import way way_area real linear # This is calculated during import</p>
<h1 id="area-tags">Area tags</h1>
<h1 id="we-dont-make-columns-for-these-tags-but-objects-with-them-are-areas.">We don't make columns for these tags, but objects with them are areas.</h1>
<h1 id="mainly-for-use-with-hstore">Mainly for use with hstore</h1>
<p>way abandoned:aeroway text phstore way abandoned:amenity text phstore way abandoned:building text phstore way abandoned:landuse text phstore way abandoned:power text phstore way area:highway text phstore</p>
<h1 id="deleted-tags">Deleted tags</h1>
<h1 id="these-are-tags-that-are-generally-regarded-as-useless-for-most-rendering.">These are tags that are generally regarded as useless for most rendering.</h1>
<h1 id="most-of-them-are-from-imports-or-intended-as-internal-information-for-mappers">Most of them are from imports or intended as internal information for mappers</h1>
<h1 id="some-of-them-are-automatically-deleted-by-editors.">Some of them are automatically deleted by editors.</h1>
<h1 id="if-you-want-some-of-them-perhaps-for-a-debugging-layer-just-delete-the-lines.">If you want some of them, perhaps for a debugging layer, just delete the lines.</h1>
<h1 id="these-tags-are-used-by-mappers-to-keep-track-of-data.">These tags are used by mappers to keep track of data.</h1>
<h1 id="they-arent-very-useful-for-rendering.">They aren't very useful for rendering.</h1>
<p>node,way note text delete node,way note: <em>text delete node,way source text delete node,way source_ref text delete node,way source:</em> text delete node,way attribution text delete node,way comment text delete node,way fixme text delete</p>
<h1 id="tags-generally-dropped-by-editors-not-otherwise-covered">Tags generally dropped by editors, not otherwise covered</h1>
<p>node,way created_by text delete node,way odbl text delete node,way odbl:note text delete node,way SK53_bulk:load text delete</p>
<h1 id="lots-of-import-tags">Lots of import tags</h1>
<h1 id="tiger-us">TIGER (US)</h1>
<p>node,way tiger:* text delete</p>
<h1 id="nhd-us">NHD (US)</h1>
<h1 id="nhd-has-been-converted-every-way-imaginable">NHD has been converted every way imaginable</h1>
<p>node,way NHD: <em>text delete node,way nhd:</em> text delete</p>
<h1 id="gnis-us">GNIS (US)</h1>
<p>node,way gnis:* text delete</p>
<h1 id="geobase-ca">Geobase (CA)</h1>
<p>node,way geobase:* text delete</p>
<h1 id="nhn-ca">NHN (CA)</h1>
<p>node,way accuracy:meters text delete node,way sub_sea:type text delete node,way waterway:type text delete</p>
<h1 id="ksj2-ja">KSJ2 (JA)</h1>
<h1 id="see-also-noteja-and-source_ref-above">See also note:ja and source_ref above</h1>
<p>node,way KSJ2:* text delete</p>
<h1 id="yahooalps-ja">Yahoo/ALPS (JA)</h1>
<p>node,way yh:* text delete</p>
<h1 id="osak-dk">osak (DK)</h1>
<p>node,way osak:* text delete</p>
<h1 id="kms-dk">kms (DK)</h1>
<p>node,way kms:* text delete</p>
<h1 id="ngbe-es">ngbe (ES)</h1>
<h1 id="see-also-notees-and-sourcefile-above">See also note:es and source:file above</h1>
<p>node,way ngbe:* text delete</p>
<h1 id="naptan-uk">naptan (UK)</h1>
<p>node,way naptan:* text delete</p>
<h1 id="corine-clc-europe">Corine (CLC) (Europe)</h1>
<p>node,way CLC:* text delete</p>
<h1 id="misc">misc</h1>
<p>node,way 3dshapes:ggmodelk text delete node,way AND_nosr_r text delete node,way import text delete node,way it:fvg:* text delete</p>
<h1 id="openpistemap-data-activated">OpenPisteMap data activated</h1>
<p>way piste:lift text linear way piste:lift:occupancy text linear way piste:lift:capacity text linear way piste:lift:duration text linear way piste:type text linear way piste:difficulty text linear way piste:grooming text linear way piste:ref text linear way lit text linear way aerialway:capacity text linear way aerialway:duration text linear way aerialway:heating text linear way aerialway:bubble text linear way aerialway:occupancy text linear node,way information text linear way sac_scale text linear</p>
<h1 id="if-youre-interested-in-bicycle-routes-you-may-want-the-following-fields">If you're interested in bicycle routes, you may want the following fields</h1>
<h1 id="to-make-these-work-you-need-slim-mode-or-the-necessary-data-wont-be-remembered.">To make these work you need slim mode or the necessary data won't be remembered.</h1>
</code>
<p><code>way lcn_ref text linear way rcn_ref text linear way ncn_ref text linear way lcn text linear way rcn text linear way ncn text linear way lwn_ref text linear way rwn_ref text linear way nwn_ref text linear way lwn text linear way rwn text linear way nwn text linear way route_pref_color text linear way route_name text linear way loc_ref text linear way usage text linear </code> Can anybody point me into the right direction on how to import those ways? Thanks for all your help Martin</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Apr '17, 19:30</strong></p>
<img src="https://secure.gravatar.com/avatar/4493ed826d70539d3d239832bc999407?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tourispo&#39;s gravatar image" />
<p><span>tourispo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tourispo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55609" class="comments-container">
&#10;</div>
<div id="comment-tools-55609" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55609-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

