+++
type = "question"
title = "Required parameter &#x27;type&#x27; is missing"
description = '''Error-Message: Traceback (most recent call last):   File &quot;C:&#92;0A&#92;9&#92;run_python.py&quot;, line 3, in &amp;lt;module&amp;gt;  execfile(r&quot;C:&#92;0A&#92;9&#92;generate_image.py&quot;)   File &quot;C:&#92;0A&#92;9&#92;generate_image.py&quot;, line 42, in &amp;lt;module&amp;gt;  mapnik.load_map(m,mapfile) RuntimeError: Could not create datasource. Required parameter...'''
date = "2012-03-26T14:13:00Z"
lastmod = "2015-06-10T13:32:00Z"
weight = 11504
keywords = [ "rendering", "layer", "type", "parameters", "mapnik" ]
aliases = [ "/questions/11504" ]
osqa_answers = 6
osqa_accepted = true
+++

<div class="headNormal">

# [Required parameter 'type' is missing](/questions/11504/required-parameter-type-is-missing)

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
<span id="post-11504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11504-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Error-Message:</p>
<pre><code>Traceback (most recent call last):   
 File &quot;C:\0A\9\run_python.py&quot;, line 3, in &lt;module&gt;
    execfile(r&quot;C:\0A\9\generate_image.py&quot;) 
 File &quot;C:\0A\9\generate_image.py&quot;, line 42, in &lt;module&gt;
    mapnik.load_map(m,mapfile) RuntimeError: Could not create datasource. Required parameter &#39;type&#39; is missing (encountered during parsing of layer &#39;landuse_overlay&#39; in map &#39;osm.xml&#39;)</code></pre>
<hr />
<p>XML-Stylesheet: osm.xml</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;!DOCTYPE Map [
&lt;!ENTITY % entities SYSTEM &quot;inc/entities.xml.inc&quot;&gt;
%entities;
]&gt;
&lt;Map background-color=&quot;#b5d0d0&quot; srs=&quot;&amp;srs900913;&quot; minimum-version=&quot;2.0.0&quot;&gt;
  &amp;fontset-settings;
&lt;Style name=&quot;turning_circle-casing&quot;&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;Filter&gt;[int_tc_type]=&#39;tertiary&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-tert-casing.18.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;Filter&gt;[int_tc_type]=&#39;residential&#39; or [int_tc_type]=&#39;unclassified&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-uncl-casing.14.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;Filter&gt;[int_tc_type]=&#39;living_street&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-uncl-fill.14.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom16;
      &lt;Filter&gt;[int_tc_type]=&#39;residential&#39; or [int_tc_type]=&#39;unclassified&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-uncl-casing.18.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom16;
      &lt;Filter&gt;[int_tc_type]=&#39;service&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-uncl-casing.14.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom16;
      &lt;Filter&gt;[int_tc_type]=&#39;living_street&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-uncl-fill.18.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom17;
      &lt;Filter&gt;[int_tc_type]=&#39;tertiary&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-tert-casing.24.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom17;
      &lt;Filter&gt;[int_tc_type]=&#39;residential&#39; or [int_tc_type]=&#39;unclassified&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-uncl-casing.24.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom17;
      &lt;Filter&gt;[int_tc_type]=&#39;service&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-uncl-casing.16.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom17;
      &lt;Filter&gt;[int_tc_type]=&#39;living_street&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-uncl-fill.24.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;turning_circle-fill&quot;&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;Filter&gt;[int_tc_type]=&#39;tertiary&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-tert-fill.16.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;Filter&gt;[int_tc_type]=&#39;residential&#39; or [int_tc_type]=&#39;unclassified&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-uncl-fill.12.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;Filter&gt;[int_tc_type]=&#39;living_street&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-livs-fill.12.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom16;
      &lt;Filter&gt;[int_tc_type]=&#39;residential&#39; or [int_tc_type]=&#39;unclassified&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-uncl-fill.16.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom16;
      &lt;Filter&gt;[int_tc_type]=&#39;service&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-uncl-fill.12.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom16;
      &lt;Filter&gt;[int_tc_type]=&#39;living_street&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-livs-fill.16.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom17;
      &lt;Filter&gt;[int_tc_type]=&#39;tertiary&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-tert-fill.22.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom17;
      &lt;Filter&gt;[int_tc_type]=&#39;residential&#39; or [int_tc_type]=&#39;unclassified&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-uncl-fill.22.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom17;
      &lt;Filter&gt;[int_tc_type]=&#39;service&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-uncl-fill.14.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom17;
      &lt;Filter&gt;[int_tc_type]=&#39;living_street&#39;&lt;/Filter&gt;
      &lt;PointSymbolizer file=&quot;&amp;symbols;/turning_circle-livs-fill.22.png&quot; allow-overlap=&quot;true&quot; ignore-placement=&quot;true&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;highway-area-casing&quot;&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway]=&#39;unclassified&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;#999&quot; stroke-width=&quot;1&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39; or [highway]=&#39;service&#39; or [highway]=&#39;footway&#39; or [highway]=&#39;path&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;grey&quot; stroke-width=&quot;1&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;#996600&quot; stroke-width=&quot;2&quot;/&gt;
   &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;platform&#39; or [railway] = &#39;platform&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;grey&quot; stroke-width=&quot;2&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;highway-area-fill&quot;&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;living_street&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;PolygonSymbolizer fill=&quot;#ccc&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway]=&#39;unclassified&#39; or [highway]=&#39;service&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;PolygonSymbolizer fill=&quot;#fff&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39; or [highway]=&#39;footway&#39; or [highway]=&#39;path&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;PolygonSymbolizer fill=&quot;#ededed&quot;/&gt;
   &lt;/Rule&gt;   
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;PolygonSymbolizer fill=&quot;#dfcc66&quot;/&gt;
   &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;platform&#39; or [railway] = &#39;platform&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;PolygonSymbolizer gamma=&quot;.65&quot; fill=&quot;#bbbbbb&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[aeroway] = &#39;runway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom11;
      &lt;PolygonSymbolizer fill=&quot;#bbc&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[aeroway] = &#39;taxiway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &lt;PolygonSymbolizer fill=&quot;#bbc&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[aeroway] = &#39;helipad&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;PolygonSymbolizer fill=&quot;#bbc&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;landuse_overlay&quot;&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom10;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[landuse]=&#39;military&#39;&lt;/Filter&gt;
      &lt;PolygonPatternSymbolizer file=&quot;&amp;symbols;/military_red_hz2.png&quot; /&gt;
      &lt;LineSymbolizer stroke=&quot;#f55&quot; stroke-width=&quot;3&quot; stroke-opacity=&quot;0.329&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[leisure] = &#39;nature_reserve&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom10;
      &amp;minscale_zoom13;
      &lt;PolygonPatternSymbolizer file=&quot;&amp;symbols;/nature_reserve5.png&quot; /&gt;
      &lt;LineSymbolizer stroke=&quot;#6c3&quot; stroke-width=&quot;0.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[leisure] = &#39;nature_reserve&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;PolygonPatternSymbolizer file=&quot;&amp;symbols;/nature_reserve6.png&quot; /&gt;
      &lt;LineSymbolizer stroke=&quot;#6c3&quot; stroke-width=&quot;1&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;area-text&quot;&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[way_area] &amp;gt;= 150000&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#000033&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;20&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[way_area] &amp;gt;= 80000 and [way_area] &amp;lt; 150000&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#000033&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;20&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[way_area] &amp;gt;= 20000 and [way_area] &amp;lt; 80000&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#000033&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;20&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[way_area] &amp;lt; 20000&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#000033&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;20&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;highway-junctions&quot;&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom11;
      &amp;minscale_zoom11;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#6666ff&quot; minimum-distance=&quot;2&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;12&quot;&gt;[ref]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom14;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#6666ff&quot; minimum-distance=&quot;2&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;12&quot;&gt;[ref]&lt;/TextSymbolizer&gt;
      &lt;TextSymbolizer size=&quot;8&quot; fill=&quot;#6666ff&quot; dy=&quot;-8&quot; minimum-distance=&quot;2&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;2&quot; wrap-character=&quot;;&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom15;
      &lt;TextSymbolizer size=&quot;12&quot; fill=&quot;#6666ff&quot; minimum-distance=&quot;2&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;12&quot;&gt;[ref]&lt;/TextSymbolizer&gt;
      &lt;TextSymbolizer size=&quot;11&quot; fill=&quot;#6666ff&quot; dy=&quot;-10&quot; minimum-distance=&quot;2&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;2&quot; wrap-character=&quot;;&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;text&quot;&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[place] = &#39;island&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom18;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#000&quot; dy=&quot;0&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;0&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[amenity]=&#39;pub&#39; or [amenity]=&#39;restaurant&#39; or [amenity]=&#39;cafe&#39; or [amenity]=&#39;fast_food&#39; or [amenity]=&#39;biergarten&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#734a08&quot; dy=&quot;9&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;34&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[amenity]=&#39;bar&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#734a08&quot; dy=&quot;11&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;0&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[amenity]=&#39;library&#39; or [amenity]=&#39;theatre&#39; or [amenity]=&#39;courthouse&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#734a08&quot; dy=&quot;12&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;0&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[amenity]=&#39;cinema&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#734a08&quot; dy=&quot;14&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;0&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[amenity]=&#39;parking&#39; and ([access] = &#39;public&#39; or not [access] != &#39;&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#0066ff&quot; dy=&quot;9&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;34&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[amenity]=&#39;parking&#39; and ([access] != &#39;&#39; and not [access] = &#39;public&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#66ccaf&quot; dy=&quot;9&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;34&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
     &lt;Rule&gt;
      &lt;Filter&gt;[amenity] = &#39;police&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#734a08&quot; dy=&quot;10&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;30&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[amenity] = &#39;fire_station&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#734a08&quot; dy=&quot;9&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;30&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
     &lt;Rule&gt;
      &lt;Filter&gt;[amenity] = &#39;place_of_worship&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#000033&quot; dy=&quot;11&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;30&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[natural] = &#39;wood&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#000&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;2&quot; wrap-width=&quot;10&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[natural] = &#39;peak&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;brown&quot; dy=&quot;5&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[natural] = &#39;peak&#39; and not [name] != &#39;&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;brown&quot; dy=&quot;6&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; placement=&quot;interior&quot;&gt;[ele]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[natural] = &#39;peak&#39; and [name] != &#39;&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;brown&quot; dy=&quot;18&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; placement=&quot;interior&quot;&gt;[ele]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[natural] = &#39;volcano&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;brown&quot; dy=&quot;5&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[natural] = &#39;volcano&#39; and not [name] != &#39;&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;brown&quot; dy=&quot;6&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; placement=&quot;interior&quot;&gt;[ele]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[natural] = &#39;volcano&#39; and [name] != &#39;&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;brown&quot; dy=&quot;16&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; placement=&quot;interior&quot;&gt;[ele]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[natural] = &#39;cave_entrance&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;brown&quot; dy=&quot;9&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;20&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[historic] = &#39;memorial&#39; or [historic]=&#39;archaeological_site&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;brown&quot; dy=&quot;12&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;20&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[natural] = &#39;water&#39; or [natural] = &#39;lake&#39; or [landuse] = &#39;reservoir&#39; or [landuse] = &#39;basin&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#6699cc&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;20&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;([leisure] != &#39;&#39; or [landuse] != &#39;&#39;) and [point] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#000&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;2&quot; wrap-width=&quot;10&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[natural] = &#39;bay&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#6699cc&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;20&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[natural] = &#39;spring&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;TextSymbolizer size=&quot;8&quot; fill=&quot;#6699cc&quot; dy=&quot;10&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;20&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tourism] = &#39;alpine_hut&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#6699cc&quot; dy=&quot;10&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tourism] = &#39;alpine_hut&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;TextSymbolizer size=&quot;8&quot; fill=&quot;#6699cc&quot; dy=&quot;22&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; placement=&quot;interior&quot;&gt;[ele]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[amenity]=&#39;shelter&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#6699cc&quot; dy=&quot;10&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
      &lt;TextSymbolizer size=&quot;8&quot; fill=&quot;#6699cc&quot; dy=&quot;22&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; placement=&quot;interior&quot;&gt;[ele]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[amenity] = &#39;bank&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;black&quot; dy=&quot;9&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;0&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tourism] = &#39;hotel&#39; or [tourism]=&#39;hostel&#39; or [tourism]=&#39;chalet&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#0066ff&quot; dy=&quot;11&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;0&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[amenity] = &#39;embassy&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#0066ff&quot; dy=&quot;8&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;0&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tourism]=&#39;guest_house&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;8&quot; fill=&quot;#0066ff&quot; dy=&quot;9&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;0&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tourism]=&#39;bed_and_breakfast&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;8&quot; fill=&quot;#0066ff&quot; dy=&quot;7&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;0&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[amenity] = &#39;fuel&#39; or [amenity]=&#39;bus_station&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#0066ff&quot; dy=&quot;9&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;0&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tourism] = &#39;camp_site&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#0066ff&quot; dy=&quot;15&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;70&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tourism] = &#39;caravan_site&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#0066ff&quot; dy=&quot;19&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;70&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[waterway] = &#39;lock&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#0066ff&quot; dy=&quot;10&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;70&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[leisure] = &#39;marina&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;TextSymbolizer size=&quot;8&quot; fill=&quot;blue&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;30&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[leisure] = &#39;marina&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;blue&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;30&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tourism] = &#39;theme_park&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom15;
      &lt;TextSymbolizer size=&quot;8&quot; fill=&quot;#734a08&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;30&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tourism] = &#39;theme_park&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#734a08&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;30&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tourism]=&#39;museum&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#734a08&quot; dy=&quot;10&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;0&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[amenity]=&#39;prison&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#734a08&quot; dy=&quot;16&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;0&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tourism] = &#39;attraction&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#660033&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;2&quot; wrap-width=&quot;10&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[amenity] = &#39;university&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#000033&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;16&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[amenity] = &#39;school&#39; or [amenity] = &#39;college&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#000033&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;14&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[amenity] = &#39;kindergarten&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;TextSymbolizer size=&quot;8&quot; fill=&quot;#000033&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;14&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[man_made] = &#39;lighthouse&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#000033&quot; dy=&quot;16&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;2&quot; wrap-width=&quot;12&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[man_made] = &#39;windmill&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#734a08&quot; dy=&quot;12&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;20&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[amenity] = &#39;hospital&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;TextSymbolizer size=&quot;8&quot; fill=&quot;#da0092&quot; dy=&quot;10&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;2&quot; wrap-width=&quot;24&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[amenity] = &#39;pharmacy&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;8&quot; fill=&quot;#da0092&quot; dy=&quot;9&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;12&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[shop]=&#39;bakery&#39; or [shop]=&#39;clothes&#39; or [shop]=&#39;fashion&#39; or [shop]=&#39;convenience&#39; or [shop]=&#39;doityourself&#39; or [shop]=&#39;hairdresser&#39; or [shop]=&#39;butcher&#39; or [shop]=&#39;car&#39; or [shop]=&#39;car_repair&#39; or [shop]=&#39;bicycle&#39; or [shop]=&#39;florist&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;8&quot; fill=&quot;#939&quot; dy=&quot;9&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;12&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[shop]=&#39;supermarket&#39; or [shop]=&#39;department_store&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#939&quot; dy=&quot;9&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;20&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[military] = &#39;danger_area&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;pink&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;10&quot; placement=&quot;interior&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[aeroway] = &#39;gate&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#aa66cc&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;10&quot; placement=&quot;interior&quot;&gt;[ref]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;tunnels-casing&quot;&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway]=&#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke=&quot;#506077&quot; stroke-width=&quot;3&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway]=&#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;#506077&quot; stroke-width=&quot;6.5&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway]=&#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke=&quot;#506077&quot; stroke-width=&quot;10&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway]=&#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke=&quot;#506077&quot; stroke-width=&quot;13&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway] = &#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke=&quot;#477147&quot; stroke-width=&quot;4&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway] = &#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;#477147&quot; stroke-width=&quot;8&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
     &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway] = &#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke=&quot;#477147&quot; stroke-width=&quot;11&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
     &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway] = &#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke=&quot;#477147&quot; stroke-width=&quot;14&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway] = &#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke=&quot;#8d4346&quot; stroke-width=&quot;4&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway] = &#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;#8d4346&quot; stroke-width=&quot;8&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway] = &#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke=&quot;#8d4346&quot; stroke-width=&quot;11&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway] = &#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke=&quot;#8d4346&quot; stroke-width=&quot;14&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; or [highway] = &#39;secondary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke=&quot;#a37b48&quot; stroke-width=&quot;4&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; or [highway] = &#39;secondary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;#a37b48&quot; stroke-width=&quot;10&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; or [highway] = &#39;secondary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke=&quot;#a37b48&quot; stroke-width=&quot;12&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; or [highway] = &#39;secondary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke=&quot;#a37b48&quot; stroke-width=&quot;17&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; or [highway]=&#39;tertiary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke=&quot;#999&quot; stroke-width=&quot;6&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; or [highway]=&#39;tertiary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;#999&quot; stroke-width=&quot;7.5&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke=&quot;#999&quot; stroke-width=&quot;3&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;#999&quot; stroke-width=&quot;4.5&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke=&quot;#999&quot; stroke-width=&quot;8&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke=&quot;#999&quot; stroke-width=&quot;11&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; or [highway]=&#39;tertiary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke=&quot;#999&quot; stroke-width=&quot;11&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; or [highway]=&#39;tertiary_link&#39; or [highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke=&quot;#999&quot; stroke-width=&quot;16&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;tunnels-fill&quot;&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway]=&#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#d6dfea&quot; stroke-width=&quot;2&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway] = &#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#d6dfea&quot; stroke-width=&quot;5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway] = &#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#d6dfea&quot; stroke-width=&quot;8.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway] = &#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#d6dfea&quot; stroke-width=&quot;11&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway] = &#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#cdeacd&quot; stroke-width=&quot;2.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway] = &#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#cdeacd&quot; stroke-width=&quot;6.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;    
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway] = &#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#cdeacd&quot; stroke-width=&quot;9&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway] = &#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#cdeacd&quot; stroke-width=&quot;12&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway] = &#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#f4c3c4&quot; stroke-width=&quot;2.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway] = &#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#f4c3c4&quot; stroke-width=&quot;6.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway] = &#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#f4c3c4&quot; stroke-width=&quot;9&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway] = &#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#f4c3c4&quot; stroke-width=&quot;12&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; or [highway] = &#39;secondary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fee0b8&quot; stroke-width=&quot;2&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; or [highway] = &#39;secondary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fee0b8&quot; stroke-width=&quot;8&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; or [highway] = &#39;secondary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fee0b8&quot; stroke-width=&quot;10&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; or [highway] = &#39;secondary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fee0b8&quot; stroke-width=&quot;14&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; or [highway]=&#39;tertiary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffc&quot; stroke-width=&quot;5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; or [highway]=&#39;tertiary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffc&quot; stroke-width=&quot;6.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fff&quot; stroke-width=&quot;2&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fff&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; or [highway]=&#39;tertiary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffc&quot; stroke-width=&quot;9.4&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; or [highway]=&#39;tertiary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffc&quot; stroke-width=&quot;13&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fff&quot; stroke-width=&quot;6.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fff&quot; stroke-width=&quot;9.4&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fff&quot; stroke-width=&quot;13&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;minor-roads-casing-links&quot;&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway]=&#39;raceway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;pink&quot; stroke-width=&quot;1.2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway]=&#39;raceway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;pink&quot; stroke-width=&quot;4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway]=&#39;raceway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;pink&quot; stroke-width=&quot;7&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway]=&#39;motorway_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#506077&quot; stroke-width=&quot;1.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway]=&#39;motorway_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#506077&quot; stroke-width=&quot;4.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway]=&#39;motorway_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#506077&quot; stroke-width=&quot;8&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway]=&#39;motorway_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#506077&quot; stroke-width=&quot;11&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
     &lt;Filter&gt;[highway] = &#39;trunk_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#477147&quot; stroke-width=&quot;3&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
     &lt;Filter&gt;[highway] = &#39;trunk_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#477147&quot; stroke-width=&quot;7.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
     &lt;Filter&gt;[highway] = &#39;trunk_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#477147&quot; stroke-width=&quot;11.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
     &lt;Filter&gt;[highway] = &#39;trunk_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#477147&quot; stroke-width=&quot;16&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;      
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#8d4346&quot; stroke-width=&quot;3&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;      
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#8d4346&quot; stroke-width=&quot;7.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;      
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#8d4346&quot; stroke-width=&quot;11.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;      
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#8d4346&quot; stroke-width=&quot;16&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a37b48&quot; stroke-width=&quot;2.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a37b48&quot; stroke-width=&quot;8.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a37b48&quot; stroke-width=&quot;11.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a37b48&quot; stroke-width=&quot;16&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary_link&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#bbb&quot; stroke-width=&quot;6&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary_link&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#bbb&quot; stroke-width=&quot;7.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary_link&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#bbb&quot; stroke-width=&quot;11&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary_link&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#bbb&quot; stroke-width=&quot;16&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;minor-roads-casing&quot;&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#506077&quot; stroke-width=&quot;3&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
     &lt;Filter&gt;[highway] = &#39;trunk&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#477147&quot; stroke-width=&quot;3&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;      
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#8d4346&quot; stroke-width=&quot;3&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a37b48&quot; stroke-width=&quot;2.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#506077&quot; stroke-width=&quot;6.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
     &lt;Filter&gt;[highway] = &#39;trunk&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#477147&quot; stroke-width=&quot;7.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;      
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#8d4346&quot; stroke-width=&quot;7.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a37b48&quot; stroke-width=&quot;8.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#506077&quot; stroke-width=&quot;10&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
     &lt;Filter&gt;[highway] = &#39;trunk&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#477147&quot; stroke-width=&quot;11.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;      
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#8d4346&quot; stroke-width=&quot;11.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a37b48&quot; stroke-width=&quot;11.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#506077&quot; stroke-width=&quot;13&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
     &lt;Filter&gt;[highway] = &#39;trunk&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#477147&quot; stroke-width=&quot;16&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;      
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#8d4346&quot; stroke-width=&quot;16&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a37b48&quot; stroke-width=&quot;16&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#bbb&quot; stroke-width=&quot;6&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;([highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;) and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#999&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#bbb&quot; stroke-width=&quot;7.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;([highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;) and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#999&quot; stroke-width=&quot;4.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;([highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;) and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#bbb&quot; stroke-width=&quot;8&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;([highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;) and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#bbb&quot; stroke-width=&quot;11&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#bbb&quot; stroke-width=&quot;11&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;([highway] = &#39;tertiary&#39; or [highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;) and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#bbb&quot; stroke-width=&quot;16&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;service&#39; and not ([service]=&#39;INT-minor&#39; or [tunnel]=&#39;yes&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#999&quot; stroke-width=&quot;2.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;service&#39; and [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke=&quot;#999&quot; stroke-width=&quot;2.5&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;service&#39; and not ([service]=&#39;INT-minor&#39; or [tunnel]=&#39;yes&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#999&quot; stroke-width=&quot;7&quot; stroke-linecap=&quot;round&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;service&#39; and [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke=&quot;#999&quot; stroke-width=&quot;7&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;service&#39; and [service]=&#39;INT-minor&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#999&quot; stroke-width=&quot;4&quot; stroke-linecap=&quot;round&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;grey&quot; stroke-width=&quot;2&quot; stroke-linecap=&quot;round&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39; and [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke=&quot;grey&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;grey&quot; stroke-width=&quot;3.6&quot; stroke-linecap=&quot;round&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39; and [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;grey&quot; stroke-width=&quot;3.6&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;grey&quot; stroke-width=&quot;6.5&quot; stroke-linecap=&quot;round&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39; and [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke=&quot;grey&quot; stroke-width=&quot;6.5&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;grey&quot; stroke-width=&quot;9&quot; stroke-linecap=&quot;round&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39; and [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;LineSymbolizer stroke=&quot;grey&quot; stroke-width=&quot;9&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;living_street&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;2.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;living_street&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;4&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;living_street&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;6&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;living_street&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;9&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;living_street&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;14.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;minor-roads-fill-links&quot;&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway]=&#39;motorway_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke=&quot;#809bc0&quot; stroke-width=&quot;0.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#809bc0&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#809bc0&quot; stroke-width=&quot;6.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#809bc0&quot; stroke-width=&quot;9&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a9dba9&quot; stroke-width=&quot;2.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a9dba9&quot; stroke-width=&quot;7&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a9dba9&quot; stroke-width=&quot;11&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a9dba9&quot; stroke-width=&quot;15.5&quot; stroke-linecap=&quot;round&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ec989a&quot; stroke-width=&quot;2.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ec989a&quot; stroke-width=&quot;7&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ec989a&quot; stroke-width=&quot;11&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary_link&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ec989a&quot; stroke-width=&quot;15.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary_link&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fed7a5&quot; stroke-width=&quot;2&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary_link&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fed7a5&quot; stroke-width=&quot;8&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary_link&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fed7a5&quot; stroke-width=&quot;11&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary_link&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fed7a5&quot; stroke-width=&quot;15.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary_link&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffffb3&quot; stroke-width=&quot;4.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary_link&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffffb3&quot; stroke-width=&quot;6&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary_link&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffffb3&quot; stroke-width=&quot;9.4&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary_link&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffffb3&quot; stroke-width=&quot;13&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;minor-roads-fill&quot;&gt; 
    &lt;Rule&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and not [construction] != &#39;&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#9cc&quot; stroke-width=&quot;2&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and ([construction]=&#39;motorway&#39; or [construction]=&#39;motorway_link&#39;)&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#809bc0&quot; stroke-width=&quot;2&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and ([construction]=&#39;trunk&#39; or [construction]=&#39;trunk_link&#39;)&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#a9dba9&quot; stroke-width=&quot;2&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and ([construction]=&#39;primary&#39; or [construction]=&#39;primary_link&#39;)&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#ec989a&quot; stroke-width=&quot;2&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and ([construction]=&#39;secondary&#39; or [construction]=&#39;secondary_link&#39;)&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#fed7a5&quot; stroke-width=&quot;2&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom15;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and not [construction] != &#39;&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#9cc&quot; stroke-width=&quot;4&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;3.5&quot; stroke-dasharray=&quot;6,4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom15;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and ([construction]=&#39;motorway&#39; or [construction]=&#39;motorway_link&#39;)&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#809bc0&quot; stroke-width=&quot;4&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;3.5&quot; stroke-dasharray=&quot;6,4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom15;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and ([construction]=&#39;trunk&#39; or [construction]=&#39;trunk_link&#39;)&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#a9dba9&quot; stroke-width=&quot;4&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;3.5&quot; stroke-dasharray=&quot;6,4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom15;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and ([construction]=&#39;primary&#39; or [construction]=&#39;primary_link&#39;)&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#ec989a&quot; stroke-width=&quot;4&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;3.5&quot; stroke-dasharray=&quot;6,4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom15;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and ([construction]=&#39;secondary&#39; or [construction]=&#39;secondary_link&#39;)&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#fed7a5&quot; stroke-width=&quot;4&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;3.5&quot; stroke-dasharray=&quot;6,4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom15;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and ([construction]=&#39;tertiary&#39; or [construction]=&#39;tertiary_link&#39;)&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#ffffb3&quot; stroke-width=&quot;4&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;3.5&quot; stroke-dasharray=&quot;6,4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom15;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and ([construction]=&#39;residential&#39; or [construction]=&#39;unclassified&#39; or [construction]=&#39;living_street&#39;)&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#aaa&quot; stroke-width=&quot;4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3.5&quot; stroke-dasharray=&quot;6,4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom15;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and [construction]=&#39;service&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#aaa&quot; stroke-width=&quot;2.5&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;6,4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom18;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and not [construction] != &#39;&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#9cc&quot; stroke-width=&quot;8&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;7&quot; stroke-dasharray=&quot;8,6&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom18;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and ([construction]=&#39;motorway&#39; or [construction]=&#39;motorway_link&#39;)&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#809bc0&quot; stroke-width=&quot;8&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;7&quot; stroke-dasharray=&quot;8,6&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom18;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and ([construction]=&#39;trunk&#39; or [construction]=&#39;trunk_link&#39;)&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#a9dba9&quot; stroke-width=&quot;8&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;7&quot; stroke-dasharray=&quot;8,6&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom18;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and ([construction]=&#39;primary&#39; or [construction]=&#39;primary_link&#39;)&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#ec989a&quot; stroke-width=&quot;8&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;7&quot; stroke-dasharray=&quot;8,6&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom18;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and ([construction]=&#39;secondary&#39; or [construction]=&#39;secondary_link&#39;)&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#fed7a5&quot; stroke-width=&quot;8&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;7&quot; stroke-dasharray=&quot;8,6&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom18;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and ([construction]=&#39;tertiary&#39; or [construction]=&#39;tertiary_link&#39;)&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#ffffb3&quot; stroke-width=&quot;8&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;7&quot; stroke-dasharray=&quot;8,6&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom18;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and ([construction]=&#39;residential&#39; or [construction]=&#39;unclassified&#39; or [construction]=&#39;living_street&#39;)&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#aaa&quot; stroke-width=&quot;8&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;7&quot; stroke-dasharray=&quot;8,6&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom18;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and [construction]=&#39;service&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#aaa&quot; stroke-width=&quot;7&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;6&quot; stroke-dasharray=&quot;8,6&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom18;
      &lt;Filter&gt;([highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;) and [construction]=&#39;cycleway&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot; stroke-opacity=&quot;0.4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#69f&quot; stroke-width=&quot;1.2&quot; stroke-dasharray=&quot;2,6&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke=&quot;#809bc0&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#809bc0&quot; stroke-width=&quot;5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#809bc0&quot; stroke-width=&quot;8.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#809bc0&quot; stroke-width=&quot;11&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a9dba9&quot; stroke-width=&quot;2.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a9dba9&quot; stroke-width=&quot;7&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a9dba9&quot; stroke-width=&quot;11&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a9dba9&quot; stroke-width=&quot;15.5&quot; stroke-linecap=&quot;round&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom11;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ec989a&quot; stroke-width=&quot;2.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ec989a&quot; stroke-width=&quot;7&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt; 
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ec989a&quot; stroke-width=&quot;11&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ec989a&quot; stroke-width=&quot;15.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fed7a5&quot; stroke-width=&quot;2&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fed7a5&quot; stroke-width=&quot;8&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fed7a5&quot; stroke-width=&quot;11&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fed7a5&quot; stroke-width=&quot;15.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway] = &#39;rail&#39; and [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffffff&quot; stroke-width=&quot;3&quot; stroke-dasharray=&quot;1,9&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fdfdfd&quot; stroke-width=&quot;3&quot; stroke-dasharray=&quot;0,1,1,8&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ececec&quot; stroke-width=&quot;3&quot; stroke-dasharray=&quot;0,2,1,7&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#cacaca&quot; stroke-width=&quot;3&quot; stroke-dasharray=&quot;0,3,1,6&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#afafaf&quot; stroke-width=&quot;3&quot; stroke-dasharray=&quot;0,4,1,5&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a1a1a1&quot; stroke-width=&quot;3&quot; stroke-dasharray=&quot;0,5,1,4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#9b9b9b&quot; stroke-width=&quot;3&quot; stroke-dasharray=&quot;0,6,1,3&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;Filter&gt;([railway] = &#39;disused&#39; or [railway] = &#39;abandoned&#39; or [railway]=&#39;construction&#39;) and not [highway] != &#39;&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;grey&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;2,4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;Filter&gt;[railway] = &#39;rail&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#999999&quot; stroke-width=&quot;3&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;1&quot; stroke-dasharray=&quot;8,12&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway] = &#39;rail&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#999999&quot; stroke-width=&quot;3&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;1&quot; stroke-dasharray=&quot;0,11,8,1&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom11;
      &amp;minscale_zoom12;
      &lt;Filter&gt;[railway] = &#39;spur-siding-yard&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#aaa&quot; stroke-width=&quot;1&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway] = &#39;spur-siding-yard&#39; and [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffffff&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;1,9&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fdfdfd&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;0,1,1,8&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ececec&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;0,2,1,7&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#cacaca&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;0,3,1,6&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#afafaf&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;0,4,1,5&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a1a1a1&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;0,5,1,4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#9b9b9b&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;0,6,1,3&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway] = &#39;spur-siding-yard&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#999999&quot; stroke-width=&quot;2&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;0.8&quot; stroke-dasharray=&quot;0,8,11,1&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;Filter&gt;([railway]=&#39;narrow_gauge&#39; or [railway]=&#39;funicular&#39;) and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#666&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;Filter&gt;([railway]=&#39;narrow_gauge&#39; or [railway]=&#39;funicular&#39;) and [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#666&quot; stroke-width=&quot;5&quot; stroke-dasharray=&quot;5,3&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;#fff&quot; stroke-width=&quot;4&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;#aaa&quot; stroke-width=&quot;1.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway]=&#39;miniature&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#999&quot; stroke-width=&quot;1.2&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;#999&quot; stroke-width=&quot;3&quot; stroke-dasharray=&quot;1,10&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;Filter&gt;[railway]=&#39;tram&#39; and [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#444&quot; stroke-width=&quot;1&quot; stroke-dasharray=&quot;5,3&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway]=&#39;tram&#39; and [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#444&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;5,3&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway]=&#39;light_rail&#39; and [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#666&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;5,3&quot;/&gt;
    &lt;/Rule&gt;
     &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway]=&#39;light_rail&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#666&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway]=&#39;subway&#39; and [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#999&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;5,3&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway]=&#39;subway&#39; and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#999&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; or [highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom10;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke=&quot;#bbb&quot; stroke-width=&quot;1&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ddd&quot; stroke-width=&quot;2&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ddd&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ddd&quot; stroke-width=&quot;6.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ddd&quot; stroke-width=&quot;9.4&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ddd&quot; stroke-width=&quot;13&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;([highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39;) and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fff&quot; stroke-width=&quot;2&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;([highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39;) and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fff&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;([highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39;) and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fff&quot; stroke-width=&quot;6.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;([highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39;) and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fff&quot; stroke-width=&quot;9.4&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;([highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39;) and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fff&quot; stroke-width=&quot;13&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;living_street&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ccc&quot; stroke-width=&quot;1.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;living_street&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ccc&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;living_street&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ccc&quot; stroke-width=&quot;4.7&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;living_street&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ccc&quot; stroke-width=&quot;7.4&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;living_street&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ccc&quot; stroke-width=&quot;13&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffffb3&quot; stroke-width=&quot;4.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffffb3&quot; stroke-width=&quot;6&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffffb3&quot; stroke-width=&quot;9.4&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffffb3&quot; stroke-width=&quot;13&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;service&#39; and not [service]=&#39;INT-minor&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke=&quot;#bbbbbb&quot; stroke-width=&quot;1&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;service&#39; and not [service]=&#39;INT-minor&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;2&quot; stroke-linecap=&quot;round&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;service&#39; and not [service]=&#39;INT-minor&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;6&quot; stroke-linecap=&quot;round&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;service&#39; and [service]=&#39;INT-minor&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fff&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
   &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ededed&quot; stroke-width=&quot;1.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ededed&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ededed&quot; stroke-width=&quot;5.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ededed&quot; stroke-width=&quot;8&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
       &lt;Filter&gt;[highway] = &#39;platform&#39; or [railway] = &#39;platform&#39;&lt;/Filter&gt;
       &amp;maxscale_zoom16;
       &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;grey&quot; stroke-width=&quot;6&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[railway] = &#39;turntable&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;LineSymbolizer stroke=&quot;#999&quot; stroke-width=&quot;1.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;steps&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &lt;LineSymbolizer stroke=&quot;salmon&quot; stroke-width=&quot;5.0&quot; stroke-dasharray=&quot;2,1&quot;/&gt;
    &lt;/Rule&gt;  
    &lt;Rule&gt;
      &lt;Filter&gt;([highway] = &#39;bridleway&#39; or ([highway] = &#39;path&#39; and [horse] = &#39;designated&#39;)) and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fff&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot; stroke-opacity=&quot;0.4&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;green&quot; stroke-width=&quot;1.2&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;  
    &lt;Rule&gt;
      &lt;Filter&gt;([highway] = &#39;footway&#39; or ([highway] = &#39;path&#39; and [foot] = &#39;designated&#39;)) and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fff&quot; stroke-width=&quot;4&quot; stroke-linecap=&quot;round&quot; stroke-opacity=&quot;0.4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;salmon&quot; stroke-width=&quot;1.5&quot; stroke-dasharray=&quot;1,3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;   
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;path&#39; and not ([bicycle] = &#39;designated&#39; or [foot] = &#39;designated&#39; or [horse] = &#39;designated&#39;) and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt; 
      &amp;maxscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;1.0&quot; stroke-linecap=&quot;round&quot; stroke-opacity=&quot;0.4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;black&quot; stroke-width=&quot;0.5&quot; stroke-dasharray=&quot;6,3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
       &lt;Filter&gt;[highway] = &#39;platform&#39; or [railway] = &#39;platform&#39;&lt;/Filter&gt;
       &amp;maxscale_zoom16;
       &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#bbbbbb&quot; stroke-width=&quot;4&quot; stroke-linecap=&quot;round&quot;/&gt;
     &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;steps&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;#fff&quot; stroke-width=&quot;6&quot; stroke-opacity=&quot;0.4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;salmon&quot; stroke-width=&quot;2.0&quot; stroke-dasharray=&quot;1,3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;([highway] = &#39;cycleway&#39; or ([highway] = &#39;path&#39; and [bicycle] = &#39;designated&#39;)) and not [tunnel] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot; stroke-opacity=&quot;0.4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;blue&quot; stroke-width=&quot;1.2&quot; stroke-dasharray=&quot;1,3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;byway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;4&quot; stroke-linecap=&quot;round&quot; stroke-opacity=&quot;0.4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffcc00&quot; stroke-width=&quot;1.5&quot; stroke-dasharray=&quot;3,4&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;2.5&quot; stroke-linecap=&quot;round&quot; stroke-opacity=&quot;0.4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#996600&quot; stroke-width=&quot;1.2&quot; stroke-dasharray=&quot;3,4&quot; stroke-linecap=&quot;round&quot;/&gt;
     &lt;/Rule&gt;    
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;unsurfaced&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fff&quot; stroke-width=&quot;3.5&quot; stroke-linecap=&quot;round&quot; stroke-opacity=&quot;0.4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#debd9c&quot; stroke-width=&quot;2.5&quot; stroke-dasharray=&quot;2,4&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;unsurfaced&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fff&quot; stroke-width=&quot;5&quot; stroke-linecap=&quot;round&quot; stroke-opacity=&quot;0.4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#debd9c&quot; stroke-width=&quot;4&quot; stroke-dasharray=&quot;4,6&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[aeroway] = &#39;runway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom11;
      &amp;minscale_zoom11;
      &lt;LineSymbolizer stroke=&quot;#bbc&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[aeroway] = &#39;runway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke=&quot;#bbc&quot; stroke-width=&quot;4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[aeroway] = &#39;runway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke=&quot;#bbc&quot; stroke-width=&quot;7&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[aeroway] = &#39;runway&#39; and not [bridge]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;#bbc&quot; stroke-width=&quot;18&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[aeroway] = &#39;taxiway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom11;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke=&quot;#bbc&quot; stroke-width=&quot;1&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[aeroway] = &#39;taxiway&#39; and not [bridge]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;#bbc&quot; stroke-width=&quot;4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[aeroway] = &#39;taxiway&#39; and not [bridge]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &lt;LineSymbolizer stroke=&quot;#bbc&quot; stroke-width=&quot;6&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;access&quot;&gt;
     &lt;Rule&gt;
      &lt;Filter&gt;[access] = &#39;permissive&#39; and ([highway]=&#39;unclassified&#39; or [highway]=&#39;residential&#39; or [highway]=&#39;footway&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.5&quot; stroke=&quot;#cf9&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;6,8&quot; stroke-width=&quot;6&quot;/&gt;
    &lt;/Rule&gt;
     &lt;Rule&gt;
      &lt;Filter&gt;[access] = &#39;permissive&#39; and ([highway] = &#39;service&#39; and not [service] = &#39;INT-minor&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.5&quot; stroke=&quot;#cf9&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;6,8&quot; stroke-width=&quot;3&quot;/&gt;
    &lt;/Rule&gt;
     &lt;Rule&gt;
      &lt;Filter&gt;[access] = &#39;permissive&#39; and ([highway]=&#39;unclassified&#39; or [highway]=&#39;residential&#39; or [highway]=&#39;footway&#39; or [highway]=&#39;service&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.5&quot; stroke=&quot;#cf9&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;6,8&quot; stroke-width=&quot;6&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[access]=&#39;destination&#39; and ([highway]=&#39;unclassified&#39; or [highway]=&#39;residential&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.5&quot; stroke=&quot;#c2e0ff&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;6,8&quot; stroke-width=&quot;6&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[access]=&#39;destination&#39; and ([highway] = &#39;service&#39; and not [service] = &#39;INT-minor&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.5&quot; stroke=&quot;#c2e0ff&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;6,8&quot; stroke-width=&quot;3&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[access]=&#39;destination&#39; and ([highway]=&#39;unclassified&#39; or [highway]=&#39;residential&#39; or [highway]=&#39;service&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.5&quot; stroke=&quot;#c2e0ff&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;6,8&quot; stroke-width=&quot;6&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;([access] = &#39;private&#39; or [access] = &#39;no&#39;) and not [highway] = &#39;service&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.5&quot; stroke=&quot;#efa9a9&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;6,8&quot; stroke-width=&quot;6&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;([access] = &#39;private&#39; or [access] = &#39;no&#39;) and ([highway] = &#39;service&#39; and not [service] = &#39;INT-minor&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.5&quot; stroke=&quot;#efa9a9&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;6,8&quot; stroke-width=&quot;3&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[access] = &#39;private&#39; or [access] = &#39;no&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.5&quot; stroke=&quot;#efa9a9&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;6,8&quot; stroke-width=&quot;6&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;footbikecycle-tunnels&quot;&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;bridleway&#39; or ([highway] = &#39;path&#39; and [horse] = &#39;designated&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &lt;LineSymbolizer stroke=&quot;grey&quot; stroke-width=&quot;5&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fff&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.5&quot; stroke=&quot;green&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;4,2&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;footway&#39; or ([highway] = &#39;path&#39; and [foot] = &#39;designated&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &lt;LineSymbolizer stroke=&quot;grey&quot; stroke-width=&quot;5.5&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fff&quot; stroke-width=&quot;3.5&quot; stroke-linecap=&quot;round&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.5&quot; stroke=&quot;salmon&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;1,3&quot; stroke-width=&quot;2.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;path&#39; and not ([bicycle] = &#39;designated&#39; or [foot] = &#39;designated&#39; or [horse] = &#39;designated&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &lt;LineSymbolizer stroke=&quot;grey&quot; stroke-width=&quot;5.5&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;1.0&quot; stroke-linecap=&quot;round&quot; stroke-opacity=&quot;0.4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;black&quot; stroke-width=&quot;0.5&quot; stroke-dasharray=&quot;6,3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;cycleway&#39; or ([highway] = &#39;path&#39; and [bicycle] = &#39;designated&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &lt;LineSymbolizer stroke=&quot;grey&quot; stroke-width=&quot;5&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.5&quot; stroke=&quot;blue&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;1,3&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;tracks-notunnel-nobridge&quot;&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tracktype]=&#39;grade1&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;3.5&quot; stroke-opacity=&quot;0.4&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;#b37700&quot; stroke-width=&quot;2&quot; stroke-opacity=&quot;0.7&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tracktype]=&#39;grade2&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot; stroke-opacity=&quot;0.4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.8&quot; stroke=&quot;#a87000&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;9,4&quot; stroke-width=&quot;1.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tracktype]=&#39;grade3&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot; stroke-opacity=&quot;0.4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.8&quot; stroke=&quot;#996600&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;3,4&quot; stroke-width=&quot;1.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tracktype]=&#39;grade4&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot; stroke-opacity=&quot;0.4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.8&quot; stroke=&quot;#996600&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;4,7,1,5&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tracktype]=&#39;grade5&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot; stroke-opacity=&quot;0.4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.8&quot; stroke=&quot;#996600&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;1,5&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;ElseFilter/&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot; stroke-opacity=&quot;0.4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#996600&quot; stroke-width=&quot;1.5&quot; stroke-dasharray=&quot;3,4&quot; stroke-linecap=&quot;round&quot;/&gt;
     &lt;/Rule&gt;    
&lt;/Style&gt;
&lt;Style name=&quot;tracks-tunnels&quot;&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tracktype]=&#39;grade1&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;grey&quot; stroke-width=&quot;5&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;3.5&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;#b37700&quot; stroke-width=&quot;2&quot; stroke-opacity=&quot;0.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tracktype]=&#39;grade2&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;grey&quot; stroke-width=&quot;4.5&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.5&quot; stroke=&quot;#a87000&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;3,4&quot; stroke-width=&quot;1.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tracktype]=&#39;grade3&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;grey&quot; stroke-width=&quot;4.5&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3.5&quot; stroke-linecap=&quot;round&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#996600&quot; stroke-width=&quot;2&quot; stroke-linecap=&quot;round&quot; stroke-opacity=&quot;0.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tracktype]=&#39;grade4&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;grey&quot; stroke-width=&quot;4.5&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.5&quot; stroke=&quot;#996600&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;4,7,1,5&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[tracktype]=&#39;grade5&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;grey&quot; stroke-width=&quot;4.5&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.5&quot; stroke=&quot;#996600&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;1,5&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;ElseFilter/&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;grey&quot; stroke-width=&quot;4.5&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.5&quot; stroke=&quot;#996600&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;3,4&quot; stroke-width=&quot;1.5&quot;/&gt;
     &lt;/Rule&gt;    
&lt;/Style&gt;
&lt;Style name=&quot;waterway-bridges&quot;&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#000&quot; stroke-width=&quot;7&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#b5d0d0&quot; stroke-width=&quot;6&quot; stroke-linecap=&quot;round&quot;/&gt;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#6699cc&quot; placement=&quot;line&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#000&quot; stroke-width=&quot;11&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#b5d0d0&quot; stroke-width=&quot;10&quot; stroke-linecap=&quot;round&quot;/&gt;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#6699cc&quot; placement=&quot;line&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;bridges_casing&quot;&gt;
     &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway]=&#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke=&quot;#506077&quot; stroke-width=&quot;3&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway]=&#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;6.5&quot;/&gt;
    &lt;/Rule&gt;    
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway]=&#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;9&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway]=&#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;12&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway]=&#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke=&quot;#477147&quot; stroke-width=&quot;4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway]=&#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;8&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway]=&#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;11&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway]=&#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;16&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway]=&#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke=&quot;#8d4346&quot; stroke-width=&quot;4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway]=&#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;8&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway]=&#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;11&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway]=&#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;16&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; or [highway]=&#39;secondary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;10&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; or [highway]=&#39;secondary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;12&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; or [highway]=&#39;secondary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;16&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; or [highway]=&#39;tertiary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;7.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; or [highway]=&#39;tertiary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;11&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; or [highway]=&#39;tertiary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;16&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;4.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;9&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;11&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39; or [highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;16&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;service&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;3&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;service&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;8&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;2.2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;3.8&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;7&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;9.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[aeroway] = &#39;runway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;19&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[aeroway] = &#39;taxiway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[aeroway] = &#39;taxiway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;7&quot;/&gt;
    &lt;/Rule&gt;
     &lt;Rule&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway]=&#39;subway&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;5.5&quot;/&gt;
     &lt;/Rule&gt;
     &lt;Rule&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway]=&#39;light_rail&#39; or [railway]=&#39;narrow_gauge&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#555&quot; stroke-width=&quot;5.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;unsurfaced&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;unsurfaced&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;6.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;bridleway&#39; or ([highway] = &#39;path&#39; and [horse] = &#39;designated&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;5.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;footway&#39; or ([highway] = &#39;path&#39; and [foot] = &#39;designated&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;6&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;path&#39; and not ([bicycle] = &#39;designated&#39; or [foot] = &#39;designated&#39; or [horse] = &#39;designated&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom14;  
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;4&quot;/&gt;
    &lt;/Rule&gt;         
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;cycleway&#39; or ([highway] = &#39;path&#39; and [bicycle] = &#39;designated&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;5.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;byway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;5.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway] = &#39;rail&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;black&quot; stroke-width=&quot;6.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway] = &#39;INT-spur-siding-yard&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;black&quot; stroke-width=&quot;5.7&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;Filter&gt;([railway] = &#39;disused&#39; or [railway] = &#39;abandoned&#39; or [railway]=&#39;construction&#39;) and not [highway] != &#39;&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;6&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39; and [tracktype] = &#39;grade1&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39; and [tracktype] = &#39;grade2&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;4.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39; and [tracktype] = &#39;grade3&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;4.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39; and [tracktype] = &#39;grade4&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;4.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39; and [tracktype] = &#39;grade5&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;4.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39; and not [tracktype] != &#39;&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;4.5&quot;/&gt;
     &lt;/Rule&gt;    
&lt;/Style&gt;
&lt;Style name=&quot;bridges_casing2&quot;&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway]=&#39;subway&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway]=&#39;light_rail&#39; or [railway]=&#39;narrow_gauge&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;unsurfaced&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;4&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;unsurfaced&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;bridleway&#39; or ([highway] = &#39;path&#39; and [horse] = &#39;designated&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;4&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;footway&#39; or ([highway] = &#39;path&#39; and [foot] = &#39;designated&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;4.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;path&#39; and not ([bicycle] = &#39;designated&#39; or [foot] = &#39;designated&#39; or [horse] = &#39;designated&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom14;  
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;2.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;         
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;cycleway&#39; or ([highway] = &#39;path&#39; and [bicycle] = &#39;designated&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;4&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;byway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;4&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway] = &#39;rail&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway] = &#39;INT-spur-siding-yard&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;Filter&gt;([railway] = &#39;disused&#39; or [railway] = &#39;abandoned&#39; or [railway]=&#39;construction&#39;) and not [highway] != &#39;&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;4.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39; and [tracktype] = &#39;grade1&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;3.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39; and [tracktype] = &#39;grade2&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
     &lt;Filter&gt;[highway] = &#39;track&#39; and [tracktype] = &#39;grade3&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39; and [tracktype] = &#39;grade4&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39; and [tracktype] = &#39;grade5&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39; and not [tracktype] != &#39;&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
     &lt;/Rule&gt;    
&lt;/Style&gt;
&lt;Style name=&quot;bridges_fill&quot;&gt;
     &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway]=&#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#809bc0&quot; stroke-width=&quot;2&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;   
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway]=&#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#809bc0&quot; stroke-width=&quot;5.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;   
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway]=&#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#809bc0&quot; stroke-width=&quot;7.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway]=&#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#809bc0&quot; stroke-width=&quot;10&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway]=&#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a9dba9&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway]=&#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a9dba9&quot; stroke-width=&quot;7&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway]=&#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a9dba9&quot; stroke-width=&quot;9.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway]=&#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#a9dba9&quot; stroke-width=&quot;14.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway]=&#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ec989a&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway]=&#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ec989a&quot; stroke-width=&quot;7&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;   
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway]=&#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ec989a&quot; stroke-width=&quot;9.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway]=&#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ec989a&quot; stroke-width=&quot;14.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; or [highway] = &#39;secondary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fed7a5&quot; stroke-width=&quot;9&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; or [highway] = &#39;secondary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fed7a5&quot; stroke-width=&quot;10.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;  
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; or [highway] = &#39;secondary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fed7a5&quot; stroke-width=&quot;14.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; or [highway]=&#39;tertiary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffffb3&quot; stroke-width=&quot;6&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; or [highway]=&#39;tertiary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffffb3&quot; stroke-width=&quot;9.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; or [highway]=&#39;tertiary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffffb3&quot; stroke-width=&quot;14&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ddd&quot; stroke-width=&quot;3.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ddd&quot; stroke-width=&quot;9.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;road&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ddd&quot; stroke-width=&quot;14&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;3.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;7.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;9.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;residential&#39; or [highway] = &#39;unclassified&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;14&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;service&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;2&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;service&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;6&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ededed&quot; stroke-width=&quot;1.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ededed&quot; stroke-width=&quot;3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ededed&quot; stroke-width=&quot;5.5&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;pedestrian&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ededed&quot; stroke-width=&quot;8&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[aeroway] = &#39;runway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;#bbc&quot; stroke-width=&quot;18&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[aeroway] = &#39;taxiway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;#bbc&quot; stroke-width=&quot;4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[aeroway] = &#39;taxiway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &lt;LineSymbolizer stroke=&quot;#bbc&quot; stroke-width=&quot;6&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway]=&#39;subway&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#999&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway]=&#39;light_rail&#39; or [railway]=&#39;narrow_gauge&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#666&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;unsurfaced&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#debd9c&quot; stroke-width=&quot;3&quot; stroke-dasharray=&quot;2,4&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;unsurfaced&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#debd9c&quot; stroke-width=&quot;4&quot; stroke-dasharray=&quot;4,6&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;bridleway&#39; or ([highway] = &#39;path&#39; and [horse] = &#39;designated&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;green&quot; stroke-width=&quot;1.5&quot; stroke-dasharray=&quot;4,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;footway&#39; or ([highway] = &#39;path&#39; and [foot] = &#39;designated&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;salmon&quot; stroke-width=&quot;2.0&quot; stroke-dasharray=&quot;1,3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;path&#39; and not ([bicycle] = &#39;designated&#39; or [foot] = &#39;designated&#39; or [horse] = &#39;designated&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom14;  
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;black&quot; stroke-width=&quot;0.5&quot; stroke-dasharray=&quot;6,3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;         
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;cycleway&#39; or ([highway] = &#39;path&#39; and [bicycle] = &#39;designated&#39;)&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;blue&quot; stroke-width=&quot;1.5&quot; stroke-dasharray=&quot;1,3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;byway&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#ffcc00&quot; stroke-width=&quot;1.5&quot; stroke-dasharray=&quot;3,4&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;Filter&gt;[railway] = &#39;rail&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#999999&quot; stroke-width=&quot;3&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;1&quot; stroke-dasharray=&quot;8,12&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway] = &#39;rail&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#999999&quot; stroke-width=&quot;3&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;1&quot; stroke-dasharray=&quot;0,11,8,1&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway] = &#39;INT-spur-siding-yard&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#999999&quot; stroke-width=&quot;2&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;0.8&quot; stroke-dasharray=&quot;0,8,11,1&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;Filter&gt;([railway] = &#39;disused&#39; or [railway] = &#39;abandoned&#39; or [railway]=&#39;construction&#39;) and not [highway] != &#39;&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;grey&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;2,4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39; and [tracktype] = &#39;grade1&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;#b37700&quot; stroke-width=&quot;2&quot; stroke-opacity=&quot;0.7&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39; and [tracktype] = &#39;grade2&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.8&quot; stroke=&quot;#a87000&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;3,4&quot; stroke-width=&quot;1.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39; and [tracktype] = &#39;grade3&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#996600&quot; stroke-width=&quot;2&quot; stroke-linecap=&quot;round&quot; stroke-opacity=&quot;0.7&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39; and [tracktype] = &#39;grade4&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.8&quot; stroke=&quot;#996600&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;4,7,1,5&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39; and [tracktype] = &#39;grade5&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke-opacity=&quot;0.8&quot; stroke=&quot;#996600&quot; stroke-linecap=&quot;round&quot; stroke-dasharray=&quot;1,5&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;track&#39; and not [tracktype] != &#39;&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#996600&quot; stroke-width=&quot;1.5&quot; stroke-dasharray=&quot;3,4&quot; stroke-linecap=&quot;round&quot;/&gt;
     &lt;/Rule&gt;    
&lt;/Style&gt;
&lt;Style name=&quot;roads&quot;&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway] = &#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom5;
      &amp;minscale_zoom6;
      &lt;LineSymbolizer stroke=&quot;#809bc0&quot; stroke-width=&quot;0.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway] = &#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom7;
      &amp;minscale_zoom8;
      &lt;LineSymbolizer stroke=&quot;#809bc0&quot; stroke-width=&quot;1&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway] = &#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom9;
      &amp;minscale_zoom9;
      &lt;LineSymbolizer stroke=&quot;#809bc0&quot; stroke-width=&quot;1.4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway] = &#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom10;
      &amp;minscale_zoom10;
      &lt;LineSymbolizer stroke=&quot;#809bc0&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; or [highway] = &#39;motorway_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom11;
      &amp;minscale_zoom11;
      &lt;LineSymbolizer stroke=&quot;#809bc0&quot; stroke-width=&quot;2.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;!-- TRUNK --&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway] = &#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom5;
      &amp;minscale_zoom6;
      &lt;LineSymbolizer stroke=&quot;#a9dba9&quot; stroke-width=&quot;0.4&quot;/&gt;
    &lt;/Rule&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway] = &#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom7;
      &amp;minscale_zoom8;
      &lt;LineSymbolizer stroke=&quot;#97d397&quot; stroke-width=&quot;1&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway] = &#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom9;
      &amp;minscale_zoom10;
      &lt;LineSymbolizer stroke=&quot;#97d397&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway] = &#39;trunk_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom11;
      &amp;minscale_zoom11;
      &lt;LineSymbolizer stroke=&quot;#97d397&quot; stroke-width=&quot;2.5&quot;/&gt;
    &lt;/Rule&gt;
   &lt;!-- PRIMARY--&gt;
   &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway] = &#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom7;
      &amp;minscale_zoom8;
      &lt;LineSymbolizer stroke=&quot;#ec989a&quot; stroke-width=&quot;0.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway] = &#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom9;
      &amp;minscale_zoom9;
      &lt;LineSymbolizer stroke=&quot;#ec989a&quot; stroke-width=&quot;1.2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway] = &#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom10;
      &amp;minscale_zoom10;
      &lt;LineSymbolizer stroke=&quot;#ec989a&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39; or [highway] = &#39;primary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom11;
      &amp;minscale_zoom11;
      &lt;LineSymbolizer stroke=&quot;#ec989a&quot; stroke-width=&quot;2.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;!-- SECONDARY --&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; or [highway] = &#39;secondary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom9;
      &amp;minscale_zoom10;
      &lt;LineSymbolizer stroke=&quot;#fecc8b&quot; stroke-width=&quot;1&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; or [highway] = &#39;secondary_link&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom11;
      &amp;minscale_zoom11;
      &lt;LineSymbolizer stroke=&quot;#fecc8b&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;!-- RAIL --&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom6;
      &amp;minscale_zoom8;
      &lt;Filter&gt;[railway] = &#39;rail&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#aaa&quot; stroke-width=&quot;0.6&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom9;
      &amp;minscale_zoom9;
      &lt;Filter&gt;[railway] = &#39;rail&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#aaa&quot; stroke-width=&quot;1&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom9;
      &amp;minscale_zoom9;
      &lt;Filter&gt;[railway] = &#39;rail&#39; and [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#aaa&quot; stroke-width=&quot;1&quot; stroke-dasharray=&quot;5,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom8;
      &amp;minscale_zoom9;
      &lt;Filter&gt;[railway] = &#39;tram&#39; or [railway] = &#39;light_rail&#39; or [railway] = &#39;narrow_gauge&#39; or [railway]=&#39;funicular&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#ccc&quot; stroke-width=&quot;1&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom10;
      &amp;minscale_zoom12;
      &lt;Filter&gt;[railway] = &#39;rail&#39; and not [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#aaa&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom10;
      &amp;minscale_zoom12;
      &lt;Filter&gt;[railway] = &#39;rail&#39; and [tunnel]=&#39;yes&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#aaa&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;5,2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom10;
      &amp;minscale_zoom12;
      &lt;Filter&gt;[railway] = &#39;tram&#39; or [railway] = &#39;light_rail&#39; or [railway] = &#39;narrow_gauge&#39; or [railway]=&#39;funicular&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#aaa&quot; stroke-width=&quot;1&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;Filter&gt;[railway] = &#39;preserved&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#aaa&quot; stroke-width=&quot;1.5&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway] = &#39;preserved&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#999999&quot; stroke-width=&quot;3&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;1&quot; stroke-dasharray=&quot;0,1,8,1&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;Filter&gt;[railway] = &#39;INT-preserved-ssy&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#aaa&quot; stroke-width=&quot;1&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway] = &#39;INT-preserved-ssy&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#999999&quot; stroke-width=&quot;2&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;0.8&quot; stroke-dasharray=&quot;0,1,8,1&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[railway]=&#39;monorail&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#fff&quot; stroke-width=&quot;4&quot; stroke-linecap=&quot;round&quot; stroke-opacity=&quot;0.4&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#777&quot; stroke-width=&quot;3.0&quot; stroke-dasharray=&quot;2,3&quot; stroke-linecap=&quot;round&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;trams&quot;&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[railway] = &#39;tram&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;LineSymbolizer stroke=&quot;#444&quot; stroke-width=&quot;1&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[railway] = &#39;tram&#39; and not [bridge]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke=&quot;#444&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[railway] = &#39;tram&#39; and [bridge]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke=&quot;black&quot; stroke-width=&quot;5&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;white&quot; stroke-width=&quot;4&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;#444&quot; stroke-width=&quot;2&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;guideways&quot;&gt;
&lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#6666ff&quot; stroke-width=&quot;3&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;1&quot; stroke-dasharray=&quot;8,12&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;#6666ff&quot; stroke-width=&quot;3&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;round&quot; stroke=&quot;white&quot; stroke-width=&quot;1&quot; stroke-dasharray=&quot;0,11,8,1&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;roads-text-ref-low-zoom&quot;&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; and [length] le 6&lt;/Filter&gt;
      &amp;maxscale_zoom10;
      &amp;minscale_zoom12;
      &lt;ShieldSymbolizer size=&quot;10&quot; fill=&quot;#fff&quot; placement=&quot;line&quot; file=&quot;&amp;symbols;/mot_shield[length].png&quot; spacing=&quot;750&quot; minimum-distance=&quot;30&quot; face-name=&quot;DejaVu Sans Bold&quot;&gt;[ref]&lt;/ShieldSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; and [length] = 7&lt;/Filter&gt;
      &amp;maxscale_zoom10;
      &amp;minscale_zoom12;
      &lt;ShieldSymbolizer size=&quot;10&quot; fill=&quot;#fff&quot; placement=&quot;line&quot; file=&quot;&amp;symbols;/mot_shield6.png&quot; spacing=&quot;750&quot; minimum-distance=&quot;30&quot; face-name=&quot;DejaVu Sans Bold&quot;&gt;[ref]&lt;/ShieldSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; and [length] = 8&lt;/Filter&gt;
      &amp;maxscale_zoom10;
      &amp;minscale_zoom12;
      &lt;ShieldSymbolizer size=&quot;10&quot; fill=&quot;#fff&quot; placement=&quot;line&quot; file=&quot;&amp;symbols;/mot_shield7.png&quot; spacing=&quot;750&quot; minimum-distance=&quot;30&quot; face-name=&quot;DejaVu Sans Bold&quot;&gt;[ref]&lt;/ShieldSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom11;
      &amp;minscale_zoom12;
      &lt;ShieldSymbolizer size=&quot;10&quot; fill=&quot;#fff&quot; placement=&quot;line&quot; file=&quot;&amp;symbols;/tru_shield[length].png&quot; spacing=&quot;750&quot; minimum-distance=&quot;30&quot; face-name=&quot;DejaVu Sans Bold&quot;&gt;[ref]&lt;/ShieldSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom11;
      &amp;minscale_zoom12;
      &lt;ShieldSymbolizer size=&quot;10&quot; fill=&quot;#fff&quot; placement=&quot;line&quot; file=&quot;&amp;symbols;/pri_shield[length].png&quot; spacing=&quot;750&quot; minimum-distance=&quot;30&quot; face-name=&quot;DejaVu Sans Bold&quot;&gt;[ref]&lt;/ShieldSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom12;
      &amp;minscale_zoom12;
      &lt;ShieldSymbolizer size=&quot;10&quot; fill=&quot;#fff&quot; placement=&quot;line&quot; file=&quot;&amp;symbols;/sec_shield[length].png&quot; spacing=&quot;750&quot; minimum-distance=&quot;40&quot; face-name=&quot;DejaVu Sans Bold&quot;&gt;[ref]&lt;/ShieldSymbolizer&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;roads-text-ref&quot;&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; and [length] le 6&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;ShieldSymbolizer size=&quot;10&quot; fill=&quot;#fff&quot; placement=&quot;line&quot; file=&quot;&amp;symbols;/mot_shield[length].png&quot; spacing=&quot;750&quot; minimum-distance=&quot;30&quot; face-name=&quot;DejaVu Sans Bold&quot;&gt;[ref]&lt;/ShieldSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; and [length] = 7&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;ShieldSymbolizer size=&quot;10&quot; fill=&quot;#fff&quot; placement=&quot;line&quot; file=&quot;&amp;symbols;/mot_shield6.png&quot; spacing=&quot;750&quot; minimum-distance=&quot;30&quot; face-name=&quot;DejaVu Sans Bold&quot;&gt;[ref]&lt;/ShieldSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;motorway&#39; and [length] = 8&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;ShieldSymbolizer size=&quot;10&quot; fill=&quot;#fff&quot; placement=&quot;line&quot; file=&quot;&amp;symbols;/mot_shield7.png&quot; spacing=&quot;750&quot; minimum-distance=&quot;30&quot; face-name=&quot;DejaVu Sans Bold&quot;&gt;[ref]&lt;/ShieldSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;ShieldSymbolizer size=&quot;10&quot; fill=&quot;#fff&quot; placement=&quot;line&quot; file=&quot;&amp;symbols;/tru_shield[length].png&quot; spacing=&quot;750&quot; minimum-distance=&quot;30&quot; face-name=&quot;DejaVu Sans Bold&quot;&gt;[ref]&lt;/ShieldSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;primary&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;ShieldSymbolizer size=&quot;10&quot; fill=&quot;#fff&quot; placement=&quot;line&quot; file=&quot;&amp;symbols;/pri_shield[length].png&quot; spacing=&quot;750&quot; minimum-distance=&quot;30&quot; face-name=&quot;DejaVu Sans Bold&quot;&gt;[ref]&lt;/ShieldSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39; and not [bridge]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;ShieldSymbolizer size=&quot;10&quot; fill=&quot;#fff&quot; placement=&quot;line&quot; file=&quot;&amp;symbols;/sec_shield[length].png&quot; spacing=&quot;750&quot; minimum-distance=&quot;40&quot; face-name=&quot;DejaVu Sans Bold&quot;&gt;[ref]&lt;/ShieldSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39; and not [bridge]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;ShieldSymbolizer size=&quot;10&quot; fill=&quot;#fff&quot; placement=&quot;line&quot; file=&quot;&amp;symbols;/ter_shield[length].png&quot; spacing=&quot;750&quot; minimum-distance=&quot;40&quot; face-name=&quot;DejaVu Sans Bold&quot;&gt;[ref]&lt;/ShieldSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;([highway] = &#39;unclassified&#39; or [highway]=&#39;residential&#39;) and not [bridge]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#000&quot; spacing=&quot;750&quot; minimum-distance=&quot;18&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot;&gt;[ref]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;([aeroway] = &#39;runway&#39; or [aeroway]=&#39;taxiway&#39;) and not [bridge]=&#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;#333&quot; spacing=&quot;750&quot; placement=&quot;line&quot; minimum-distance=&quot;18&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot;&gt;[ref]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;roads-text-name&quot;&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway] = &#39;primary&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;TextSymbolizer size=&quot;8&quot; fill=&quot;black&quot; placement=&quot;line&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;0&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom13;
      &lt;TextSymbolizer size=&quot;8&quot; fill=&quot;black&quot; placement=&quot;line&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; halo-fill=&quot;#fed7a5&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway] = &#39;primary&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;black&quot; placement=&quot;line&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;0&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;trunk&#39; or [highway] = &#39;primary&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom18;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;black&quot; placement=&quot;line&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;0&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom14;
      &amp;minscale_zoom14;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;black&quot; placement=&quot;line&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; halo-fill=&quot;#fed7a5&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;&lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;secondary&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom18;
      &lt;TextSymbolizer size=&quot;10&quot; fill=&quot;black&quot; placement=&quot;line&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; halo-fill=&quot;#fed7a5&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#000&quot; placement=&quot;line&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;tertiary&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;TextSymbolizer size=&quot;11&quot; fill=&quot;#000&quot; placement=&quot;line&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom15;
      &lt;Filter&gt;[highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;&lt;/Filter&gt;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#000&quot; placement=&quot;line&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[highway] = &#39;proposed&#39; or [highway]=&#39;construction&#39;&lt;/Filter&gt;
      &lt;TextSymbolizer size=&quot;11&quot; fill=&quot;#000&quot; placement=&quot;line&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;unclassified&#39; or [highway] = &#39;residential&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom15;
      &lt;TextSymbolizer size=&quot;8&quot; fill=&quot;#000&quot; spacing=&quot;300&quot; placement=&quot;line&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;unclassified&#39; or [highway] = &#39;residential&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &amp;minscale_zoom16;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#000&quot; spacing=&quot;300&quot; placement=&quot;line&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[highway] = &#39;unclassified&#39; or [highway] = &#39;residential&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;TextSymbolizer size=&quot;11&quot; fill=&quot;#000&quot; spacing=&quot;400&quot; placement=&quot;line&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;ElseFilter/&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom16;
      &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;#000&quot; placement=&quot;line&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;ElseFilter/&gt;
      &amp;maxscale_zoom17;
      &amp;minscale_zoom18;
      &lt;TextSymbolizer size=&quot;11&quot; fill=&quot;#000&quot; placement=&quot;line&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;cliffs&quot;&gt;
     &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;Filter&gt;[natural] = &#39;cliff&#39;&lt;/Filter&gt;       
      &lt;LinePatternSymbolizer file=&quot;&amp;symbols;/cliff.png&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom15;
      &lt;Filter&gt;[natural] = &#39;cliff&#39;&lt;/Filter&gt;
      &lt;LinePatternSymbolizer file=&quot;&amp;symbols;/cliff2.png&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom15;
      &lt;Filter&gt;[man_made] = &#39;embankment&#39;&lt;/Filter&gt;
      &lt;LinePatternSymbolizer file=&quot;&amp;symbols;/cliff.png&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;barriers_area&quot;&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[natural]=&#39;hedge&#39; or [barrier] = &#39;hedge&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;PolygonSymbolizer fill=&quot;#aed1a0&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom16;
      &lt;Filter&gt;[barrier] != &#39;&#39; and not [barrier] = &#39;hedge&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#444&quot; stroke-width=&quot;0.4&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;barriers&quot;&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom14;
      &lt;Filter&gt;[barrier] = &#39;embankment&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#444&quot; stroke-width=&quot;0.4&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom16;
      &lt;Filter&gt;[natural]=&#39;hedge&#39; or [barrier] = &#39;hedge&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#aed1a0&quot; stroke-width=&quot;3&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom16;
      &lt;Filter&gt;[barrier] != &#39;&#39; and not ([barrier] = &#39;hedge&#39; or [barrier] = &#39;embankment&#39;)&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#444&quot; stroke-width=&quot;0.4&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;directions&quot;&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[oneway] = &#39;yes&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;bevel&quot; stroke=&quot;#6c70d5&quot; stroke-width=&quot;1&quot; stroke-dasharray=&quot;0,12,10,152&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;bevel&quot; stroke=&quot;#6c70d5&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;0,12,9,153&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;bevel&quot; stroke=&quot;#6c70d5&quot; stroke-width=&quot;3&quot; stroke-dasharray=&quot;0,18,2,154&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;bevel&quot; stroke=&quot;#6c70d5&quot; stroke-width=&quot;4&quot; stroke-dasharray=&quot;0,18,1,155&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[oneway] = &#39;-1&#39;&lt;/Filter&gt;
      &amp;maxscale_zoom16;
      &lt;LineSymbolizer stroke-linejoin=&quot;bevel&quot; stroke=&quot;#6c70d5&quot; stroke-width=&quot;1&quot; stroke-dasharray=&quot;0,12,10,152&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;bevel&quot; stroke=&quot;#6c70d5&quot; stroke-width=&quot;2&quot; stroke-dasharray=&quot;0,13,9,152&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;bevel&quot; stroke=&quot;#6c70d5&quot; stroke-width=&quot;3&quot; stroke-dasharray=&quot;0,14,2,158&quot;/&gt;
      &lt;LineSymbolizer stroke-linejoin=&quot;bevel&quot; stroke=&quot;#6c70d5&quot; stroke-width=&quot;4&quot; stroke-dasharray=&quot;0,15,1,158&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;boundary&quot;&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom7;
      &amp;minscale_zoom9;
      &lt;PolygonSymbolizer fill-opacity=&quot;0.05&quot; fill=&quot;green&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;green&quot; stroke-width=&quot;1.5&quot; stroke-dasharray=&quot;4,2&quot; stroke-opacity=&quot;0.15&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom10;
      &amp;minscale_zoom12;
      &lt;PolygonSymbolizer fill-opacity=&quot;0.05&quot; fill=&quot;green&quot;/&gt;
      &lt;LineSymbolizer stroke=&quot;green&quot; stroke-width=&quot;3&quot; stroke-dasharray=&quot;6,2&quot; stroke-opacity=&quot;0.15&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom18;
      &lt;LineSymbolizer stroke=&quot;green&quot; stroke-width=&quot;3&quot; stroke-dasharray=&quot;6,2&quot; stroke-opacity=&quot;0.15&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &lt;Filter&gt;[way_area] &amp;gt;= 200000000&lt;/Filter&gt;
      &amp;maxscale_zoom8;
      &amp;minscale_zoom9;
      &lt;TextSymbolizer size=&quot;8&quot; fill=&quot;#9c9&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;14&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom10;
      &amp;minscale_zoom11;
      &lt;TextSymbolizer size=&quot;11&quot; fill=&quot;#9c9&quot; face-name=&quot;DejaVu Sans Bold&quot; halo-radius=&quot;1&quot; wrap-width=&quot;14&quot;&gt;[name]&lt;/TextSymbolizer&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&lt;Style name=&quot;theme_park&quot;&gt;
&lt;Rule&gt;
      &amp;maxscale_zoom13;
      &amp;minscale_zoom14;
      &lt;Filter&gt;[tourism]=&#39;theme_park&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#734a08&quot; stroke-width=&quot;1.5&quot; stroke-dasharray=&quot;9,3&quot; stroke-opacity=&quot;0.6&quot;/&gt;
    &lt;/Rule&gt;
    &lt;Rule&gt;
      &amp;maxscale_zoom15;
      &amp;minscale_zoom18;
      &lt;Filter&gt;[tourism]=&#39;theme_park&#39;&lt;/Filter&gt;
      &lt;LineSymbolizer stroke=&quot;#734a08&quot; stroke-width=&quot;2.5&quot; stroke-dasharray=&quot;9,3&quot; stroke-opacity=&quot;0.6&quot;/&gt;
    &lt;/Rule&gt;
&lt;/Style&gt;
&#10;&amp;layer-shapefiles;
&amp;layer-landcover;
&amp;layer-water;
&amp;layer-water_features;
&lt;Layer name=&quot;tunnels&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;tunnels-casing&lt;/StyleName&gt;
    &lt;StyleName&gt;tunnels-fill&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,highway from &amp;prefix;_line where highway in (&#39;motorway&#39;,&#39;motorway_link&#39;,&#39;trunk&#39;,&#39;trunk_link&#39;,&#39;primary&#39;,&#39;primary_link&#39;,&#39;secondary&#39;,&#39;secondary_link&#39;,&#39;tertiary&#39;,&#39;tertiary_link&#39;,&#39;residential&#39;,&#39;unclassified&#39;) and tunnel in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;) order by z_order) as roads
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&amp;layer-citywall;
&lt;Layer name=&quot;landuse_overlay&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;landuse_overlay&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,landuse,leisure
       from &amp;prefix;_polygon
       where (landuse = &#39;military&#39; or leisure=&#39;nature_reserve&#39;) and building is null
      ) as landuse_overlay
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;turning_circle-casing&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;turning_circle-casing&lt;/StyleName&gt;    
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select distinct on (p.way) p.way as way,l.highway as int_tc_type
       from &amp;prefix;_point p
       join &amp;prefix;_line l
        on ST_DWithin(p.way,l.way,&amp;dwithin_node_way;)
       join (values
        (&#39;tertiary&#39;,1),
        (&#39;unclassified&#39;,2),
        (&#39;residential&#39;,3),
        (&#39;living_street&#39;,4),
        (&#39;service&#39;,5)
       ) as v (highway,prio)
        on v.highway=l.highway
       where p.highway=&#39;turning_circle&#39;
       order by p.way,v.prio
      ) as turning_circle
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;footbikecycle-tunnels&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;footbikecycle-tunnels&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,highway,horse,foot,bicycle from &amp;prefix;_line where highway in (&#39;bridleway&#39;,&#39;footway&#39;,&#39;cycleway&#39;,&#39;path&#39;) and tunnel in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;) order by z_order) as roads
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;tracks-tunnels&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;tracks-tunnels&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,tracktype from &amp;prefix;_line where highway=&#39;track&#39; and tunnel in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;)) as tracks
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;line features&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
     &lt;StyleName&gt;cliffs&lt;/StyleName&gt;
     &lt;StyleName&gt;barriers&lt;/StyleName&gt;
     &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,barrier,&quot;natural&quot;,man_made from &amp;prefix;_line where barrier is not null or &quot;natural&quot; in (&#39;hedge&#39;,&#39;cliff&#39;) or man_made=&#39;embankment&#39;) as roads
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;polygon barriers&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
      &lt;StyleName&gt;barriers_area&lt;/StyleName&gt;
      &lt;Datasource&gt;
             &lt;Parameter name=&quot;table&quot;&gt;
       (select way,barrier,&quot;natural&quot; from &amp;prefix;_polygon where barrier is not null or &quot;natural&quot;=&#39;hedge&#39;) as barriers
       &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;highway-area-casing&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;highway-area-casing&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,highway,railway from &amp;prefix;_polygon
       where highway in (&#39;residential&#39;,&#39;unclassified&#39;,&#39;pedestrian&#39;,&#39;service&#39;,&#39;footway&#39;,&#39;track&#39;,&#39;path&#39;,&#39;platform&#39;)
          or railway=&#39;platform&#39;
       order by z_order,way_area desc) as roads
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;minor-roads-casing&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;minor-roads-casing-links&lt;/StyleName&gt;
    &lt;StyleName&gt;minor-roads-casing&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,highway,
       case when tunnel in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;) then &#39;yes&#39;::text else tunnel end as tunnel,
       case when service in (&#39;parking_aisle&#39;,&#39;drive-through&#39;,&#39;driveway&#39;) then &#39;INT-minor&#39;::text else service end as service
       from &amp;prefix;_line
       where highway in (&#39;motorway&#39;,&#39;motorway_link&#39;,&#39;trunk&#39;,&#39;trunk_link&#39;,&#39;primary&#39;,&#39;primary_link&#39;,&#39;secondary&#39;,&#39;secondary_link&#39;,&#39;tertiary&#39;,&#39;tertiary_link&#39;,&#39;residential&#39;,&#39;unclassified&#39;,&#39;road&#39;,&#39;service&#39;,&#39;pedestrian&#39;,&#39;raceway&#39;,&#39;living_street&#39;)
       order by z_order) as roads
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;highway-area-fill&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;highway-area-fill&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,highway,railway,aeroway from &amp;prefix;_polygon
       where highway in (&#39;residential&#39;,&#39;unclassified&#39;,&#39;pedestrian&#39;,&#39;service&#39;,&#39;footway&#39;,&#39;living_street&#39;,&#39;track&#39;,&#39;path&#39;,&#39;platform&#39;,&#39;services&#39;)
          or railway=&#39;platform&#39;
          or aeroway in (&#39;runway&#39;,&#39;taxiway&#39;,&#39;helipad&#39;)
       order by z_order,way_area desc) as roads
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&amp;layer-buildings;
&lt;Layer name=&quot;tracks-notunnel-nobridge&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;tracks-notunnel-nobridge&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,tracktype from &amp;prefix;_line where highway=&#39;track&#39; and (bridge is null or bridge in (&#39;no&#39;,&#39;false&#39;,&#39;0&#39;)) and (tunnel is null or tunnel in (&#39;no&#39;,&#39;false&#39;,&#39;0&#39;))) as tracks
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;minor-roads-fill&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;minor-roads-fill-links&lt;/StyleName&gt;
    &lt;StyleName&gt;minor-roads-fill&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,highway,horse,bicycle,foot,construction,aeroway,
       case when tunnel in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;) then &#39;yes&#39;::text else tunnel end as tunnel,
       case when bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;) then &#39;yes&#39;::text else bridge end as bridge,
       case when railway in (&#39;spur&#39;,&#39;siding&#39;)
              or (railway=&#39;rail&#39; and service in (&#39;spur&#39;,&#39;siding&#39;,&#39;yard&#39;))
            then &#39;spur-siding-yard&#39;::text else railway end as railway,
       case when service in (&#39;parking_aisle&#39;,&#39;drive-through&#39;,&#39;driveway&#39;) then &#39;INT-minor&#39;::text else service end as service
       from &amp;prefix;_line
       where highway is not null
          or aeroway in (&#39;runway&#39;,&#39;taxiway&#39;)
          or railway in (&#39;light_rail&#39;,&#39;narrow_gauge&#39;,&#39;funicular&#39;,&#39;rail&#39;,&#39;subway&#39;,&#39;tram&#39;,&#39;spur&#39;,&#39;siding&#39;,&#39;platform&#39;,&#39;disused&#39;,&#39;abandoned&#39;,&#39;construction&#39;,&#39;miniature&#39;,&#39;turntable&#39;)
       order by z_order) as roads
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;turning_circle-fill&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;turning_circle-fill&lt;/StyleName&gt;    
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select distinct on (p.way) p.way as way,l.highway as int_tc_type
       from &amp;prefix;_point p
       join &amp;prefix;_line l
        on ST_DWithin(p.way,l.way,&amp;dwithin_node_way;)
       join (values
        (&#39;tertiary&#39;,1),
        (&#39;unclassified&#39;,2),
        (&#39;residential&#39;,3),
        (&#39;living_street&#39;,4),
        (&#39;service&#39;,5)
       ) as v (highway,prio)
        on v.highway=l.highway
       where p.highway=&#39;turning_circle&#39;
       order by p.way,v.prio
      ) as turning_circle
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&amp;layer-ferry-routes;
&amp;layer-aerialways;
&lt;Layer name=&quot;roads&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;roads&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,highway,
       case when tunnel in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;) then &#39;yes&#39;::text else tunnel end as tunnel,
       case when railway=&#39;preserved&#39; and service in (&#39;spur&#39;,&#39;siding&#39;,&#39;yard&#39;) then &#39;INT-preserved-ssy&#39;::text else railway end as railway
       from &amp;prefix;_roads
       where highway is not null
          or (railway is not null and railway!=&#39;preserved&#39; and (service is null or service not in (&#39;spur&#39;,&#39;siding&#39;,&#39;yard&#39;)))
          or railway=&#39;preserved&#39;
       order by z_order
      ) as roads
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;waterway-bridges&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;waterway-bridges&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;(select way,name from &amp;prefix;_line where waterway=&#39;canal&#39; and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;aqueduct&#39;) order by z_order) as water&lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;access-pre_bridges&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;access&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,access,highway,
       case when service in (&#39;parking_aisle&#39;,&#39;drive-through&#39;,&#39;driveway&#39;) then &#39;INT-minor&#39;::text end as service
       from &amp;prefix;_line
       where access is not null and highway is not null
         and (bridge is null or bridge not in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;))
      ) as access
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;direction_pre_bridges&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
     &lt;StyleName&gt;directions&lt;/StyleName&gt;
     &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,
       case when oneway in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;) then &#39;yes&#39;::text else oneway end as oneway
       from &amp;prefix;_line
       where oneway is not null
         and (highway is not null or railway is not null or waterway is not null)
         and (bridge is null or bridge not in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;))
      ) as directions
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;bridges_layer0&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;bridges_casing&lt;/StyleName&gt;
    &lt;StyleName&gt;bridges_casing2&lt;/StyleName&gt;
    &lt;StyleName&gt;bridges_fill&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,highway,aeroway,horse,bicycle,foot,tracktype,
       case when railway in (&#39;spur&#39;,&#39;siding&#39;)
              or (railway=&#39;rail&#39; and service in (&#39;spur&#39;,&#39;siding&#39;,&#39;yard&#39;))
            then &#39;INT-spur-siding-yard&#39;::text else railway end as railway
       from &amp;prefix;_line
       where (highway is not null
              or aeroway in (&#39;runway&#39;,&#39;taxiway&#39;)
              or railway in (&#39;light_rail&#39;,&#39;subway&#39;,&#39;narrow_gauge&#39;,&#39;rail&#39;,&#39;spur&#39;,&#39;siding&#39;,&#39;disused&#39;,&#39;abandoned&#39;,&#39;construction&#39;))
         and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;)
         and (layer is null or layer = &#39;0&#39;)
       order by z_order
      ) as roads
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;bridges_access0&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;access&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,access,highway,
       case when service in (&#39;parking_aisle&#39;,&#39;drive-through&#39;,&#39;driveway&#39;) then &#39;INT-minor&#39;::text end as service
       from &amp;prefix;_line
       where access is not null and highway is not null
         and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;)
         and (layer is null or layer in (&#39;-5&#39;,&#39;-4&#39;,&#39;-3&#39;,&#39;-2&#39;,&#39;-1&#39;,&#39;0&#39;))
      ) as access
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;bridges_directions0&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
     &lt;StyleName&gt;directions&lt;/StyleName&gt;
     &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,
       case when oneway in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;) then &#39;yes&#39;::text else oneway end as oneway
       from &amp;prefix;_line
       where oneway is not null
         and (highway is not null or railway is not null or waterway is not null)
         and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;)
         and (layer is null or layer in (&#39;-5&#39;,&#39;-4&#39;,&#39;-3&#39;,&#39;-2&#39;,&#39;-1&#39;,&#39;0&#39;))
      ) as directions
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;bridges_layer1&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;bridges_casing&lt;/StyleName&gt;
    &lt;StyleName&gt;bridges_casing2&lt;/StyleName&gt;
    &lt;StyleName&gt;bridges_fill&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,highway,aeroway,horse,bicycle,foot,tracktype,
       case when railway in (&#39;spur&#39;,&#39;siding&#39;)
              or (railway=&#39;rail&#39; and service in (&#39;spur&#39;,&#39;siding&#39;,&#39;yard&#39;))
            then &#39;INT-spur-siding-yard&#39;::text else railway end as railway
       from &amp;prefix;_line
       where (highway is not null
              or aeroway in (&#39;runway&#39;,&#39;taxiway&#39;)
              or railway in (&#39;light_rail&#39;,&#39;subway&#39;,&#39;narrow_gauge&#39;,&#39;rail&#39;,&#39;spur&#39;,&#39;siding&#39;,&#39;disused&#39;,&#39;abandoned&#39;,&#39;construction&#39;))
         and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;)
         and layer = &#39;1&#39;
       order by z_order
      ) as roads
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;bridges_access1&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;access&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,access,highway,
       case when service in (&#39;parking_aisle&#39;,&#39;drive-through&#39;,&#39;driveway&#39;) then &#39;INT-minor&#39;::text end as service
       from &amp;prefix;_line
       where access is not null and highway is not null
         and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;)
         and layer = &#39;1&#39;
      ) as access
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;bridges_directions1&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
     &lt;StyleName&gt;directions&lt;/StyleName&gt;
     &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,
       case when oneway in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;) then &#39;yes&#39;::text else oneway end as oneway
       from &amp;prefix;_line
       where oneway is not null
         and (highway is not null or railway is not null or waterway is not null)
         and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;)
         and layer = &#39;1&#39;
      ) as directions
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;bridges_layer2&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;bridges_casing&lt;/StyleName&gt;
    &lt;StyleName&gt;bridges_casing2&lt;/StyleName&gt;
    &lt;StyleName&gt;bridges_fill&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,highway,aeroway,horse,bicycle,foot,tracktype,
       case when railway in (&#39;spur&#39;,&#39;siding&#39;)
              or (railway=&#39;rail&#39; and service in (&#39;spur&#39;,&#39;siding&#39;,&#39;yard&#39;))
            then &#39;INT-spur-siding-yard&#39;::text else railway end as railway
       from &amp;prefix;_line
       where (highway is not null
              or aeroway in (&#39;runway&#39;,&#39;taxiway&#39;)
              or railway in (&#39;light_rail&#39;,&#39;subway&#39;,&#39;narrow_gauge&#39;,&#39;rail&#39;,&#39;spur&#39;,&#39;siding&#39;,&#39;disused&#39;,&#39;abandoned&#39;,&#39;construction&#39;))
         and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;)
         and layer = &#39;2&#39;
       order by z_order
      ) as roads
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;bridges_access2&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;access&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,access,highway,
       case when service in (&#39;parking_aisle&#39;,&#39;drive-through&#39;,&#39;driveway&#39;) then &#39;INT-minor&#39;::text end as service
       from &amp;prefix;_line
       where access is not null and highway is not null
         and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;)
         and layer = &#39;2&#39;
      ) as access
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;bridges_directions2&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
     &lt;StyleName&gt;directions&lt;/StyleName&gt;
     &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,
       case when oneway in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;) then &#39;yes&#39;::text else oneway end as oneway
       from &amp;prefix;_line
       where oneway is not null
         and (highway is not null or railway is not null or waterway is not null)
         and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;)
         and layer = &#39;2&#39;
      ) as directions
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;bridges_layer3&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;bridges_casing&lt;/StyleName&gt;
    &lt;StyleName&gt;bridges_casing2&lt;/StyleName&gt;
    &lt;StyleName&gt;bridges_fill&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,highway,aeroway,horse,bicycle,foot,tracktype,
       case when railway in (&#39;spur&#39;,&#39;siding&#39;)
              or (railway=&#39;rail&#39; and service in (&#39;spur&#39;,&#39;siding&#39;,&#39;yard&#39;))
            then &#39;INT-spur-siding-yard&#39;::text else railway end as railway
       from &amp;prefix;_line
       where (highway is not null
              or aeroway in (&#39;runway&#39;,&#39;taxiway&#39;)
              or railway in (&#39;light_rail&#39;,&#39;subway&#39;,&#39;narrow_gauge&#39;,&#39;rail&#39;,&#39;spur&#39;,&#39;siding&#39;,&#39;disused&#39;,&#39;abandoned&#39;,&#39;construction&#39;))
         and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;)
         and layer = &#39;3&#39;
       order by z_order
      ) as roads
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;bridges_access3&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;access&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,access,highway,
       case when service in (&#39;parking_aisle&#39;,&#39;drive-through&#39;,&#39;driveway&#39;) then &#39;INT-minor&#39;::text end as service
       from &amp;prefix;_line
       where access is not null and highway is not null
         and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;)
         and layer = &#39;3&#39;
      ) as access
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;bridges_directions3&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
     &lt;StyleName&gt;directions&lt;/StyleName&gt;
     &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,
       case when oneway in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;) then &#39;yes&#39;::text else oneway end as oneway
       from &amp;prefix;_line
       where oneway is not null
         and (highway is not null or railway is not null or waterway is not null)
         and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;)
         and layer = &#39;3&#39;
      ) as directions
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;bridges_layer4&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;bridges_casing&lt;/StyleName&gt;
    &lt;StyleName&gt;bridges_casing2&lt;/StyleName&gt;
    &lt;StyleName&gt;bridges_fill&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,highway,aeroway,horse,bicycle,foot,tracktype,
       case when railway in (&#39;spur&#39;,&#39;siding&#39;)
              or (railway=&#39;rail&#39; and service in (&#39;spur&#39;,&#39;siding&#39;,&#39;yard&#39;))
            then &#39;INT-spur-siding-yard&#39;::text else railway end as railway
       from &amp;prefix;_line
       where (highway is not null
              or aeroway in (&#39;runway&#39;,&#39;taxiway&#39;)
              or railway in (&#39;light_rail&#39;,&#39;subway&#39;,&#39;narrow_gauge&#39;,&#39;rail&#39;,&#39;spur&#39;,&#39;siding&#39;,&#39;disused&#39;,&#39;abandoned&#39;,&#39;construction&#39;))
         and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;)
         and layer = &#39;4&#39;
       order by z_order
      ) as roads
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;bridges_access4&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;access&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,access,highway,
       case when service in (&#39;parking_aisle&#39;,&#39;drive-through&#39;,&#39;driveway&#39;) then &#39;INT-minor&#39;::text end as service
       from &amp;prefix;_line
       where access is not null and highway is not null
         and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;)
         and layer = &#39;4&#39;
      ) as access
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;bridges_directions4&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
     &lt;StyleName&gt;directions&lt;/StyleName&gt;
     &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,
       case when oneway in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;) then &#39;yes&#39;::text else oneway end as oneway
       from &amp;prefix;_line
       where oneway is not null
         and (highway is not null or railway is not null or waterway is not null)
         and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;)
         and layer = &#39;4&#39;
      ) as directions
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;bridges_layer5&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;bridges_casing&lt;/StyleName&gt;
    &lt;StyleName&gt;bridges_casing2&lt;/StyleName&gt;
    &lt;StyleName&gt;bridges_fill&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,highway,aeroway,horse,bicycle,foot,tracktype,
       case when railway in (&#39;spur&#39;,&#39;siding&#39;)
              or (railway=&#39;rail&#39; and service in (&#39;spur&#39;,&#39;siding&#39;,&#39;yard&#39;))
            then &#39;INT-spur-siding-yard&#39;::text else railway end as railway
       from &amp;prefix;_line
       where (highway is not null
              or aeroway in (&#39;runway&#39;,&#39;taxiway&#39;)
              or railway in (&#39;light_rail&#39;,&#39;subway&#39;,&#39;narrow_gauge&#39;,&#39;rail&#39;,&#39;spur&#39;,&#39;siding&#39;,&#39;disused&#39;,&#39;abandoned&#39;,&#39;construction&#39;))
         and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;)
         and layer = &#39;5&#39;
       order by z_order
      ) as roads
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;bridges_access5&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;access&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,access,highway,
       case when service in (&#39;parking_aisle&#39;,&#39;drive-through&#39;,&#39;driveway&#39;) then &#39;INT-minor&#39;::text end as service
       from &amp;prefix;_line
       where access is not null and highway is not null
         and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;)
         and layer = &#39;5&#39;
      ) as access
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;bridges_directions5&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
     &lt;StyleName&gt;directions&lt;/StyleName&gt;
     &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,
       case when oneway in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;) then &#39;yes&#39;::text else oneway end as oneway
       from &amp;prefix;_line
       where oneway is not null
         and (highway is not null or railway is not null or waterway is not null)
         and bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;,&#39;viaduct&#39;)
         and layer = &#39;5&#39;
      ) as directions
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;trams&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;trams&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,railway,bridge from &amp;prefix;_line where railway=&#39;tram&#39; and (tunnel is null or tunnel not in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;))) as trams
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;guideways&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;guideways&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way from &amp;prefix;_line where highway=&#39;bus_guideway&#39; and (tunnel is null or tunnel not in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;))) as guideways
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&amp;layer-admin;
&amp;layer-placenames;
&amp;layer-amenity-stations;
&amp;layer-amenity-symbols;
&amp;layer-amenity-points;
&amp;layer-power;
&lt;Layer name=&quot;roads-text-ref-low-zoom&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
     &lt;StyleName&gt;roads-text-ref-low-zoom&lt;/StyleName&gt;
     &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,highway,ref,char_length(ref) as length
       from &amp;prefix;_roads
       where highway in (&#39;motorway&#39;,&#39;trunk&#39;,&#39;primary&#39;,&#39;secondary&#39;)
         and ref is not null
         and char_length(ref) between 1 and 8
      ) as roads
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;highway-junctions&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;highway-junctions&lt;/StyleName&gt;
    &lt;Datasource&gt;
     &lt;Parameter name=&quot;table&quot;&gt;
     (select way,ref,name
      from &amp;prefix;_point
      where highway=&#39;motorway_junction&#39;
     ) as junctions
     &lt;/Parameter&gt;
     &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;roads-text-ref&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
     &lt;StyleName&gt;roads-text-ref&lt;/StyleName&gt;
     &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,highway,aeroway,ref,char_length(ref) as length,
       case when bridge in (&#39;yes&#39;,&#39;true&#39;,&#39;1&#39;) then &#39;yes&#39;::text else bridge end as bridge
       from &amp;prefix;_line
       where (highway is not null or aeroway is not null)
         and ref is not null
         and char_length(ref) between 1 and 8
      ) as roads
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;roads-text-name&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
     &lt;StyleName&gt;roads-text-name&lt;/StyleName&gt;
     &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,highway,name
       from &amp;prefix;_line
       where waterway IS NULL
         and leisure IS NULL
         and landuse IS NULL
         and name is not null
      ) as roads
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;text&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;text&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,amenity,shop,access,leisure,landuse,man_made,&quot;natural&quot;,place,tourism,ele,name,ref,military,aeroway,waterway,historic,&#39;yes&#39;::text as point
       from &amp;prefix;_point
       where amenity is not null
          or shop in (&#39;supermarket&#39;,&#39;bakery&#39;,&#39;clothes&#39;,&#39;fashion&#39;,&#39;convenience&#39;,&#39;doityourself&#39;,&#39;hairdresser&#39;,&#39;department_store&#39;,&#39;butcher&#39;,&#39;car&#39;,&#39;car_repair&#39;,&#39;bicycle&#39;,&#39;florist&#39;)
          or leisure is not null
          or landuse is not null
          or tourism is not null
          or &quot;natural&quot; is not null
          or man_made in (&#39;lighthouse&#39;,&#39;windmill&#39;)
          or place=&#39;island&#39;
          or military=&#39;danger_area&#39;
          or aeroway=&#39;gate&#39;
          or waterway=&#39;lock&#39;
          or historic in (&#39;memorial&#39;,&#39;archaeological_site&#39;)
      ) as text
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;text-poly&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;text&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,aeroway,shop,access,amenity,leisure,landuse,man_made,&quot;natural&quot;,place,tourism,NULL as ele,name,ref,military,waterway,historic,&#39;no&#39;::text as point
       from &amp;prefix;_polygon
       where amenity is not null
          or shop in (&#39;supermarket&#39;,&#39;bakery&#39;,&#39;clothes&#39;,&#39;fashion&#39;,&#39;convenience&#39;,&#39;doityourself&#39;,&#39;hairdresser&#39;,&#39;department_store&#39;, &#39;butcher&#39;,&#39;car&#39;,&#39;car_repair&#39;,&#39;bicycle&#39;)
          or leisure is not null
          or landuse is not null
          or tourism is not null
          or &quot;natural&quot; is not null
          or man_made in (&#39;lighthouse&#39;,&#39;windmill&#39;)
          or place=&#39;island&#39;
          or military=&#39;danger_area&#39;
          or historic in (&#39;memorial&#39;,&#39;archaeological_site&#39;)
      ) as text
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;area-text&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;area-text&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,way_area,name
       from &amp;prefix;_polygon
       where name is not null
         and (waterway is null or waterway != &#39;riverbank&#39;)
         and place is null
       order by way_area desc
      ) as text
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&amp;layer-addressing;
&lt;Layer name=&quot;misc_boundaries&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;boundary&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,way_area,name,boundary from &amp;prefix;_polygon where boundary=&#39;national_park&#39; and building is null) as boundary
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;Layer name=&quot;theme_park&quot; status=&quot;on&quot; srs=&quot;&amp;osm2pgsql_projection;&quot;&gt;
    &lt;StyleName&gt;theme_park&lt;/StyleName&gt;
    &lt;Datasource&gt;
      &lt;Parameter name=&quot;table&quot;&gt;
      (select way,name,tourism from &amp;prefix;_polygon where tourism=&#39;theme_park&#39;) as theme_park
      &lt;/Parameter&gt;
      &amp;datasource-settings;
    &lt;/Datasource&gt;
&lt;/Layer&gt;
&lt;/Map&gt;</code></pre>
<hr />
<p>Python-file: generate_image.py</p>
<pre><code>#!/usr/bin/env python
&#10;#try:
#    import mapnik2 as mapnik
#except:
import mapnik
&#10;import sys, os
&#10;# Set up projections
# spherical mercator (most common target map projection of osm data imported with osm2pgsql)
merc = mapnik.Projection(&#39;+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +no_defs +over&#39;)
&#10;# long/lat in degrees, aka ESPG:4326 and &quot;WGS 84&quot; 
longlat = mapnik.Projection(&#39;+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs&#39;)
# can also be constructed as:
#longlat = mapnik.Projection(&#39;+init=epsg:4326&#39;)
&#10;# ensure minimum mapnik version
if not hasattr(mapnik,&#39;mapnik_version&#39;) and not mapnik.mapnik_version() &gt;= 600:
    raise SystemExit(&#39;This script requires Mapnik &gt;=0.6.0)&#39;)
&#10;if __name__ == &quot;__main__&quot;:
    try:
        mapfile = os.environ[&#39;MAPNIK_MAP_FILE&#39;]
    except KeyError:
        mapfile = &quot;osm.xml&quot;
&#10;    map_uri = &quot;image.png&quot;
&#10;    #---------------------------------------------------
    #  Change this to the bounding box you want
    #
    bounds = (-6.5, 49.5, 2.1, 59)
    #---------------------------------------------------
&#10;    z = 10
    imgx = 500 * z
    imgy = 1000 * z
&#10;    m = mapnik.Map(imgx,imgy)
    mapnik.load_map(m,mapfile)
&#10;    # ensure the target map projection is mercator
    m.srs = merc.params()
&#10;    if hasattr(mapnik,&#39;Box2d&#39;):
        bbox = mapnik.Box2d(*bounds)
    else:
        bbox = mapnik.Envelope(*bounds)
&#10;    # Our bounds above are in long/lat, but our map
    # is in spherical mercator, so we need to transform
    # the bounding box to mercator to properly position
    # the Map when we call `zoom_to_box()`
    transform = mapnik.ProjTransform(longlat,merc)
    merc_bbox = transform.forward(bbox)
&#10;    # Mapnik internally will fix the aspect ratio of the bounding box
    # to match the aspect ratio of the target image width and height
    # This behavior is controlled by setting the `m.aspect_fix_mode`
    # and defaults to GROW_BBOX, but you can also change it to alter
    # the target image size by setting aspect_fix_mode to GROW_CANVAS
    #m.aspect_fix_mode = mapnik.GROW_CANVAS
    # Note: aspect_fix_mode is only available in Mapnik &gt;= 0.6.0
    m.zoom_to_box(merc_bbox)
&#10;    # render the map to an image
    im = mapnik.Image(imgx,imgy)
    mapnik.render(m, im)
    im.save(map_uri,&#39;png&#39;)
&#10;    sys.stdout.write(&#39;output image to %s!\n&#39; % map_uri)
&#10;    # Note: instead of creating an image, rendering to it, and then 
    # saving, we can also do this in one step like:
    # mapnik.render_to_file(m, map_uri,&#39;png&#39;)
&#10;    # And in Mapnik &gt;= 0.7.0 you can also use `render_to_file()` to output
    # to Cairo supported formats if you have Mapnik built with Cairo support
    # For example, to render to pdf or svg do:
    # mapnik.render_to_file(m, &quot;image.pdf&quot;)
    #mapnik.render_to_file(m, &quot;image.svg&quot;)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-type" rel="tag" title="see questions tagged &#39;type&#39;">type</span> <span class="post-tag tag-link-parameters" rel="tag" title="see questions tagged &#39;parameters&#39;">parameters</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Mar '12, 14:13</strong></p>
<img src="https://secure.gravatar.com/avatar/cc0198a02af3c41ad04b61e028c3b126?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MHein&#39;s gravatar image" />
<p><span>MHein</span><br />
<span class="score" title="141 reputation points">141</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MHein has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11504" class="comments-container">
&#10;</div>
<div id="comment-tools-11504" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11504-form-container" class="comment-form-container">
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

6 Answers:

</div>

</div>

<span id="11513"></span>

<div id="answer-container-11513" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11513-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MHein has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well, if all the html code (after the line 22) is really in your file, you should remove it. Your datasource-settings.xml.inc file should only contain the parameter for your datasource, so remove the html code starting at &lt;head&gt;.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '12, 10:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-11513" class="comments-container">
&#10;</div>
<div id="comment-tools-11513" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11513-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11511"></span>

<div id="answer-container-11511" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11511-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your osm.xml file isn't helpfull, you should show your inc/datasource-settings.xml.inc file. Your datasource is described in this file, and the error is about datasource. So, please show us this file :-)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '12, 09:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-11511" class="comments-container">
&#10;</div>
<div id="comment-tools-11511" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11511-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11512"></span>

<div id="answer-container-11512" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11512-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Okay, this is my datasource-settings.xml.inc file!</p>
<p>I hope you can help me by seeing this.</p>
<p>If you need more code, i will upload it!</p>
<hr />
<pre><code>&lt;!DOCTYPE html PUBLIC &quot;-//W3C//DTD XHTML 1.0 Strict//EN&quot; &quot;http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd&quot;&gt;
&lt;html xmlns=&quot;http://www.w3.org/1999/xhtml&quot;&gt;
&#10;&lt;!--
Settings for your postgres setup.
&#10;Note: feel free to leave password, host, port, or use blank
--&gt;
&#10;&lt;Parameter name=&quot;type&quot;&gt;postgis&lt;/Parameter&gt;
&lt;Parameter name=&quot;password&quot;&gt;1234&lt;/Parameter&gt;
&lt;Parameter name=&quot;host&quot;&gt;localhost&lt;/Parameter&gt;
&lt;Parameter name=&quot;port&quot;&gt;5432&lt;/Parameter&gt;
&lt;Parameter name=&quot;user&quot;&gt;Hein&lt;/Parameter&gt;
&lt;Parameter name=&quot;dbname&quot;&gt;gis_schwentine&lt;/Parameter&gt;
&lt;!-- this should be &#39;false&#39; if you are manually providing the &#39;extent&#39; --&gt;
&lt;Parameter name=&quot;estimate_extent&quot;&gt;false&lt;/Parameter&gt;
&lt;!-- manually provided extent in epsg 900913 for whole globe --&gt;
&lt;!-- providing this speeds up Mapnik database queries --&gt;
&lt;Parameter name=&quot;extent&quot;&gt;-20037508,-19929239,20037508,19929239&lt;/Parameter&gt;
&#10;  &lt;head&gt;
    &lt;title&gt;
      /applications/rendering/mapnik/inc/datasource-settings.xml.inc.template – OpenStreetMap
    &lt;/title&gt;
        &lt;link rel=&quot;search&quot; href=&quot;/search&quot; /&gt;
        &lt;link rel=&quot;help&quot; href=&quot;/wiki/TracGuide&quot; /&gt;
        &lt;link rel=&quot;alternate&quot; href=&quot;/export/28155/applications/rendering/mapnik/inc/datasource-settings.xml.inc.template&quot; type=&quot;text/plain&quot; title=&quot;Original Format&quot; /&gt;
        &lt;link rel=&quot;up&quot; href=&quot;/browser/applications/rendering/mapnik/inc&quot; title=&quot;Parent directory&quot; /&gt;
        &lt;link rel=&quot;start&quot; href=&quot;/wiki&quot; /&gt;
        &lt;link rel=&quot;stylesheet&quot; href=&quot;/chrome/common/css/trac.css&quot; type=&quot;text/css&quot; /&gt;&lt;link rel=&quot;stylesheet&quot; href=&quot;/chrome/common/css/code.css&quot; type=&quot;text/css&quot; /&gt;&lt;link rel=&quot;stylesheet&quot; href=&quot;/pygments/trac.css&quot; type=&quot;text/css&quot; /&gt;&lt;link rel=&quot;stylesheet&quot; href=&quot;/chrome/common/css/browser.css&quot; type=&quot;text/css&quot; /&gt;
        &lt;link rel=&quot;shortcut icon&quot; href=&quot;/chrome/site/osm.ico&quot; type=&quot;image/x-icon&quot; /&gt;
        &lt;link rel=&quot;icon&quot; href=&quot;/chrome/site/osm.ico&quot; type=&quot;image/x-icon&quot; /&gt;
      &lt;link type=&quot;application/opensearchdescription+xml&quot; rel=&quot;search&quot; href=&quot;/search/opensearch&quot; title=&quot;Search OpenStreetMap&quot; /&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;/chrome/common/js/jquery.js&quot;&gt;&lt;/script&gt;&lt;script type=&quot;text/javascript&quot; src=&quot;/chrome/common/js/trac.js&quot;&gt;&lt;/script&gt;&lt;script type=&quot;text/javascript&quot; src=&quot;/chrome/common/js/search.js&quot;&gt;&lt;/script&gt;
    &lt;!--[if lt IE 7]&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;/chrome/common/js/ie_pre7_hacks.js&quot;&gt;&lt;/script&gt;
    &lt;![endif]--&gt;
    &lt;script type=&quot;text/javascript&quot;&gt;
      jQuery(document).ready(function($) {
        $(&quot;.trac-toggledeleted&quot;).show().click(function() {
                  $(this).siblings().find(&quot;.trac-deleted&quot;).toggle();
                  return false;
        }).click();
        $(&quot;#jumploc input&quot;).hide();
        $(&quot;#jumploc select&quot;).change(function () {
          this.parentNode.parentNode.submit();
        });
      });
    &lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;div id=&quot;banner&quot;&gt;
      &lt;div id=&quot;header&quot;&gt;
        &lt;a id=&quot;logo&quot; href=&quot;http://www.openstreetmap.org/&quot;&gt;&lt;img src=&quot;/chrome/site/osm.png&quot; alt=&quot;OpenStreetMap&quot; height=&quot;80&quot; width=&quot;228&quot; /&gt;&lt;/a&gt;
      &lt;/div&gt;
      &lt;form id=&quot;search&quot; action=&quot;/search&quot; method=&quot;get&quot;&gt;
        &lt;div&gt;
          &lt;label for=&quot;proj-search&quot;&gt;Search:&lt;/label&gt;
          &lt;input type=&quot;text&quot; id=&quot;proj-search&quot; name=&quot;q&quot; size=&quot;18&quot; value=&quot;&quot; /&gt;
          &lt;input type=&quot;submit&quot; value=&quot;Search&quot; /&gt;
        &lt;/div&gt;
      &lt;/form&gt;
      &lt;div id=&quot;metanav&quot; class=&quot;nav&quot;&gt;
    &lt;ul&gt;
      &lt;li class=&quot;first&quot;&gt;&lt;a href=&quot;/login&quot;&gt;Login&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;/prefs&quot;&gt;Preferences&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;/wiki/TracGuide&quot;&gt;Help/Guide&lt;/a&gt;&lt;/li&gt;&lt;li class=&quot;last&quot;&gt;&lt;a href=&quot;/about&quot;&gt;About Trac&lt;/a&gt;&lt;/li&gt;
    &lt;/ul&gt;
  &lt;/div&gt;
    &lt;/div&gt;
    &lt;div id=&quot;mainnav&quot; class=&quot;nav&quot;&gt;
    &lt;ul&gt;
      &lt;li class=&quot;first&quot;&gt;&lt;a href=&quot;/wiki&quot;&gt;Wiki&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;/timeline&quot;&gt;Timeline&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;/roadmap&quot;&gt;Roadmap&lt;/a&gt;&lt;/li&gt;&lt;li class=&quot;active&quot;&gt;&lt;a href=&quot;/browser&quot;&gt;Browse Source&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;/report&quot;&gt;View Tickets&lt;/a&gt;&lt;/li&gt;&lt;li class=&quot;last&quot;&gt;&lt;a href=&quot;/search&quot;&gt;Search&lt;/a&gt;&lt;/li&gt;
    &lt;/ul&gt;
  &lt;/div&gt;
    &lt;div id=&quot;main&quot;&gt;
      &lt;div id=&quot;ctxtnav&quot; class=&quot;nav&quot;&gt;
        &lt;h2&gt;Context Navigation&lt;/h2&gt;
          &lt;ul&gt;
              &lt;li class=&quot;first&quot;&gt;&lt;a href=&quot;/changeset/18879/applications/rendering/mapnik/inc/datasource-settings.xml.inc.template&quot;&gt;Last Change&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;/browser/applications/rendering/mapnik/inc/datasource-settings.xml.inc.template?annotate=blame&amp;amp;rev=18879&quot; title=&quot;Annotate each line with the last changed revision (this can be time consuming...)&quot;&gt;Annotate&lt;/a&gt;&lt;/li&gt;&lt;li class=&quot;last&quot;&gt;&lt;a href=&quot;/log/applications/rendering/mapnik/inc/datasource-settings.xml.inc.template&quot;&gt;Revision Log&lt;/a&gt;&lt;/li&gt;
          &lt;/ul&gt;
        &lt;hr /&gt;
      &lt;/div&gt;
    &lt;div id=&quot;content&quot; class=&quot;browser&quot;&gt;
      &lt;h1&gt;
    &lt;a class=&quot;pathentry first&quot; title=&quot;Go to root directory&quot; href=&quot;/browser&quot;&gt;root&lt;/a&gt;&lt;span class=&quot;pathentry sep&quot;&gt;/&lt;/span&gt;&lt;a class=&quot;pathentry&quot; title=&quot;View applications&quot; href=&quot;/browser/applications&quot;&gt;applications&lt;/a&gt;&lt;span class=&quot;pathentry sep&quot;&gt;/&lt;/span&gt;&lt;a class=&quot;pathentry&quot; title=&quot;View rendering&quot; href=&quot;/browser/applications/rendering&quot;&gt;rendering&lt;/a&gt;&lt;span class=&quot;pathentry sep&quot;&gt;/&lt;/span&gt;&lt;a class=&quot;pathentry&quot; title=&quot;View mapnik&quot; href=&quot;/browser/applications/rendering/mapnik&quot;&gt;mapnik&lt;/a&gt;&lt;span class=&quot;pathentry sep&quot;&gt;/&lt;/span&gt;&lt;a class=&quot;pathentry&quot; title=&quot;View inc&quot; href=&quot;/browser/applications/rendering/mapnik/inc&quot;&gt;inc&lt;/a&gt;&lt;span class=&quot;pathentry sep&quot;&gt;/&lt;/span&gt;&lt;a class=&quot;pathentry&quot; title=&quot;View datasource-settings.xml.inc.template&quot; href=&quot;/browser/applications/rendering/mapnik/inc/datasource-settings.xml.inc.template&quot;&gt;datasource-settings.xml.inc.template&lt;/a&gt;
    &lt;br style=&quot;clear: both&quot; /&gt;
  &lt;/h1&gt;
      &lt;div id=&quot;jumprev&quot;&gt;
        &lt;form action=&quot;&quot; method=&quot;get&quot;&gt;
          &lt;div&gt;
            &lt;label for=&quot;rev&quot;&gt;
              View revision:&lt;/label&gt;
            &lt;input type=&quot;text&quot; id=&quot;rev&quot; name=&quot;rev&quot; size=&quot;6&quot; /&gt;
          &lt;/div&gt;
        &lt;/form&gt;
      &lt;/div&gt;
      &lt;table id=&quot;info&quot; summary=&quot;Revision info&quot;&gt;
        &lt;tr&gt;
          &lt;th scope=&quot;col&quot;&gt;
            Revision &lt;a href=&quot;/changeset/18879&quot;&gt;18879&lt;/a&gt;, &lt;span title=&quot;692 bytes&quot;&gt;0.7 KB&lt;/span&gt;
            (checked in by ldp, &lt;a class=&quot;timeline&quot; href=&quot;/timeline?from=2009-11-30T19%3A24%3A27Z&amp;amp;precision=second&quot; title=&quot;2009-11-30T19:24:27Z in Timeline&quot;&gt;2 years&lt;/a&gt; ago)
          &lt;/th&gt;
        &lt;/tr&gt;
        &lt;tr&gt;
          &lt;td class=&quot;message searchable&quot;&gt;
              &lt;p&gt;
New script, donated by springmeyer, to set up mapnik with your local settings. See generate_xml.py and README.&lt;br /&gt;
Also renamed .example files to .template&lt;br /&gt;
&lt;/p&gt;
          &lt;/td&gt;
        &lt;/tr&gt;
      &lt;/table&gt;
      &lt;div id=&quot;preview&quot; class=&quot;searchable&quot;&gt;
    &lt;table class=&quot;code&quot;&gt;&lt;thead&gt;&lt;tr&gt;&lt;th class=&quot;lineno&quot; title=&quot;Line numbers&quot;&gt;Line&lt;/th&gt;&lt;th class=&quot;content&quot;&gt; &lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th id=&quot;L1&quot;&gt;&lt;a href=&quot;#L1&quot;&gt;1&lt;/a&gt;&lt;/th&gt;&lt;td&gt;&amp;lt;!--&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th id=&quot;L2&quot;&gt;&lt;a href=&quot;#L2&quot;&gt;2&lt;/a&gt;&lt;/th&gt;&lt;td&gt;Settings for your postgres setup.&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th id=&quot;L3&quot;&gt;&lt;a href=&quot;#L3&quot;&gt;3&lt;/a&gt;&lt;/th&gt;&lt;td&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th id=&quot;L4&quot;&gt;&lt;a href=&quot;#L4&quot;&gt;4&lt;/a&gt;&lt;/th&gt;&lt;td&gt;Note: feel free to leave password, host, port, or use blank&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th id=&quot;L5&quot;&gt;&lt;a href=&quot;#L5&quot;&gt;5&lt;/a&gt;&lt;/th&gt;&lt;td&gt;--&amp;gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th id=&quot;L6&quot;&gt;&lt;a href=&quot;#L6&quot;&gt;6&lt;/a&gt;&lt;/th&gt;&lt;td&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th id=&quot;L7&quot;&gt;&lt;a href=&quot;#L7&quot;&gt;7&lt;/a&gt;&lt;/th&gt;&lt;td&gt;&amp;lt;Parameter name=&quot;type&quot;&amp;gt;postgis&amp;lt;/Parameter&amp;gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th id=&quot;L8&quot;&gt;&lt;a href=&quot;#L8&quot;&gt;8&lt;/a&gt;&lt;/th&gt;&lt;td&gt;&amp;lt;Parameter name=&quot;password&quot;&amp;gt;%(password)s&amp;lt;/Parameter&amp;gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th id=&quot;L9&quot;&gt;&lt;a href=&quot;#L9&quot;&gt;9&lt;/a&gt;&lt;/th&gt;&lt;td&gt;&amp;lt;Parameter name=&quot;host&quot;&amp;gt;%(host)s&amp;lt;/Parameter&amp;gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th id=&quot;L10&quot;&gt;&lt;a href=&quot;#L10&quot;&gt;10&lt;/a&gt;&lt;/th&gt;&lt;td&gt;&amp;lt;Parameter name=&quot;port&quot;&amp;gt;%(port)s&amp;lt;/Parameter&amp;gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th id=&quot;L11&quot;&gt;&lt;a href=&quot;#L11&quot;&gt;11&lt;/a&gt;&lt;/th&gt;&lt;td&gt;&amp;lt;Parameter name=&quot;user&quot;&amp;gt;%(user)s&amp;lt;/Parameter&amp;gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th id=&quot;L12&quot;&gt;&lt;a href=&quot;#L12&quot;&gt;12&lt;/a&gt;&lt;/th&gt;&lt;td&gt;&amp;lt;Parameter name=&quot;dbname&quot;&amp;gt;%(dbname)s&amp;lt;/Parameter&amp;gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th id=&quot;L13&quot;&gt;&lt;a href=&quot;#L13&quot;&gt;13&lt;/a&gt;&lt;/th&gt;&lt;td&gt;&amp;lt;!-- this should be &#39;false&#39; if you are manually providing the &#39;extent&#39; --&amp;gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th id=&quot;L14&quot;&gt;&lt;a href=&quot;#L14&quot;&gt;14&lt;/a&gt;&lt;/th&gt;&lt;td&gt;&amp;lt;Parameter name=&quot;estimate_extent&quot;&amp;gt;%(estimate_extent)s&amp;lt;/Parameter&amp;gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th id=&quot;L15&quot;&gt;&lt;a href=&quot;#L15&quot;&gt;15&lt;/a&gt;&lt;/th&gt;&lt;td&gt;&amp;lt;!-- manually provided extent in epsg 900913 for whole globe --&amp;gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th id=&quot;L16&quot;&gt;&lt;a href=&quot;#L16&quot;&gt;16&lt;/a&gt;&lt;/th&gt;&lt;td&gt;&amp;lt;!-- providing this speeds up Mapnik database queries --&amp;gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;th id=&quot;L17&quot;&gt;&lt;a href=&quot;#L17&quot;&gt;17&lt;/a&gt;&lt;/th&gt;&lt;td&gt;&amp;lt;Parameter name=&quot;extent&quot;&amp;gt;%(extent)s&amp;lt;/Parameter&amp;gt;&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;
      &lt;/div&gt;
      &lt;div id=&quot;help&quot;&gt;
        &lt;strong&gt;Note:&lt;/strong&gt; See &lt;a href=&quot;/wiki/TracBrowser&quot;&gt;TracBrowser&lt;/a&gt;
        for help on using the browser.
      &lt;/div&gt;
      &lt;div id=&quot;anydiff&quot;&gt;
        &lt;form action=&quot;/diff&quot; method=&quot;get&quot;&gt;
          &lt;div class=&quot;buttons&quot;&gt;
            &lt;input type=&quot;hidden&quot; name=&quot;new_path&quot; value=&quot;/applications/rendering/mapnik/inc/datasource-settings.xml.inc.template&quot; /&gt;
            &lt;input type=&quot;hidden&quot; name=&quot;old_path&quot; value=&quot;/applications/rendering/mapnik/inc/datasource-settings.xml.inc.template&quot; /&gt;
            &lt;input type=&quot;hidden&quot; name=&quot;new_rev&quot; /&gt;
            &lt;input type=&quot;hidden&quot; name=&quot;old_rev&quot; /&gt;
            &lt;input type=&quot;submit&quot; value=&quot;View changes...&quot; title=&quot;Select paths and revs for Diff&quot; /&gt;
          &lt;/div&gt;
        &lt;/form&gt;
      &lt;/div&gt;
    &lt;/div&gt;
    &lt;div id=&quot;altlinks&quot;&gt;
      &lt;h3&gt;Download in other formats:&lt;/h3&gt;
      &lt;ul&gt;
        &lt;li class=&quot;last first&quot;&gt;
          &lt;a rel=&quot;nofollow&quot; href=&quot;/export/28155/applications/rendering/mapnik/inc/datasource-settings.xml.inc.template&quot;&gt;Original Format&lt;/a&gt;
        &lt;/li&gt;
      &lt;/ul&gt;
    &lt;/div&gt;
    &lt;/div&gt;
    &lt;div id=&quot;footer&quot; lang=&quot;en&quot; xml:lang=&quot;en&quot;&gt;&lt;hr /&gt;
      &lt;a id=&quot;tracpowered&quot; href=&quot;http://trac.edgewall.org/&quot;&gt;&lt;img src=&quot;/chrome/common/trac_logo_mini.png&quot; height=&quot;30&quot; width=&quot;107&quot; alt=&quot;Trac Powered&quot; /&gt;&lt;/a&gt;
      &lt;p class=&quot;left&quot;&gt;
        Powered by &lt;a href=&quot;/about&quot;&gt;&lt;strong&gt;Trac 0.11.7&lt;/strong&gt;&lt;/a&gt;&lt;br /&gt;
        By &lt;a href=&quot;http://www.edgewall.org/&quot;&gt;Edgewall Software&lt;/a&gt;.
      &lt;/p&gt;
      &lt;p class=&quot;right&quot;&gt;Visit the map at&lt;br /&gt;&lt;a href=&quot;http://www.openstreetmap.org/&quot;&gt;http://www.openstreetmap.org/&lt;/a&gt;&lt;/p&gt;
    &lt;/div&gt;
  &lt;/body&gt;
&lt;/html&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '12, 09:30</strong></p>
<img src="https://secure.gravatar.com/avatar/cc0198a02af3c41ad04b61e028c3b126?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MHein&#39;s gravatar image" />
<p><span>MHein</span><br />
<span class="score" title="141 reputation points">141</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MHein has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11512" class="comments-container">
&#10;</div>
<div id="comment-tools-11512" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11512-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11514"></span>

<div id="answer-container-11514" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11514-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you!</p>
<p>but now, the next ERROR comes up:</p>
<pre><code>RuntimeError: Could not create datasource. Required parameter &#39;type&#39; is missing (encountered during parsing of layer &#39;tunnels&#39; in map &#39;osm_edited.xml&#39;)</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '12, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/cc0198a02af3c41ad04b61e028c3b126?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MHein&#39;s gravatar image" />
<p><span>MHein</span><br />
<span class="score" title="141 reputation points">141</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MHein has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11514" class="comments-container">
&#10;</div>
<div id="comment-tools-11514" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11514-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11515"></span>

<div id="answer-container-11515" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11515-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Oh.. it's still the same error.. sorry!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '12, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/cc0198a02af3c41ad04b61e028c3b126?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MHein&#39;s gravatar image" />
<p><span>MHein</span><br />
<span class="score" title="141 reputation points">141</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MHein has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11515" class="comments-container">
<span id="11516"></span>
<div id="comment-11516" class="comment">
<div id="post-11516-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You're welcome. By the way, it's better to "add new comment" instead adding new answers when you want to answer to another answer (I don't if it's clear).</p>
<p>Have a good day</p>
</div>
<div id="comment-11516-info" class="comment-info">
<span class="comment-age">(27 Mar '12, 10:22)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
<span id="11517"></span>
<div id="comment-11517" class="comment">
<div id="post-11517-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>so don't you know, how to solve my problem?</p>
</div>
<div id="comment-11517-info" class="comment-info">
<span class="comment-age">(27 Mar '12, 10:27)</span> <span class="comment-user userinfo">MHein</span>
</div>
</div>
</div>
<div id="comment-tools-11515" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11515-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43517"></span>

<div id="answer-container-43517" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43517-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Anybody know how to solve this problem ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '15, 13:32</strong></p>
<img src="https://secure.gravatar.com/avatar/082a8682abadb6cbbaa04124dbea1a88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baxos04&#39;s gravatar image" />
<p><span>Baxos04</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baxos04 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43517" class="comments-container">
&#10;</div>
<div id="comment-tools-43517" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43517-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

