+++
type = "question"
title = "How convert OSM relation to GeoJSON based on relation member&#x27;s roles"
description = '''I just want to convert OSM data to GeoJSON where it is pretty simple with node and way tags of OSM data, but relation which is giving complex can&#x27;t find the logic to convert OSM relation to GeoJSON format, especially how to form coordinates parameter of GeoJSON based on their relation member roles (...'''
date = "2019-05-20T12:16:00Z"
lastmod = "2020-04-29T09:30:00Z"
weight = 69245
keywords = [ "geometry", "osmtogeojson", "osm", "osmosis", "geojson" ]
aliases = [ "/questions/69245" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How convert OSM relation to GeoJSON based on relation member's roles](/questions/69245/how-convert-osm-relation-to-geojson-based-on-relation-members-roles)

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
<span id="post-69245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69245-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just want to convert OSM data to GeoJSON where it is pretty simple with node and way tags of OSM data, but relation which is giving complex can't find the logic to convert OSM relation to GeoJSON format, especially how to form coordinates parameter of GeoJSON based on their relation member roles (ex. Inner, outer,admin_centre,riverbank,side_stream,main_stream,from,via,to,forward,backward,stop_entry_only,stop_exit_only and platform_exit_only).</p>
<p>I have tried many documentation but no logics or code found in Java and Python.</p>
<p>In Python <a href="https://pypi.org/project/osm2geojson/">https://pypi.org/project/osm2geojson/</a> osm Official <a href="https://wiki.openstreetmap.org">https://wiki.openstreetmap.org</a> geojson Official <a href="https://geojson.org/">https://geojson.org/</a> sample data: <a href="https://download.geofabrik.de/asia/maldives-latest.osm.bz2">https://download.geofabrik.de/asia/maldives-latest.osm.bz2</a> <a href="https://download.geofabrik.de/asia/bhutan-latest.osm.pbf">https://download.geofabrik.de/asia/bhutan-latest.osm.pbf</a></p>
<p>As simple, how to form relation member's latitude and longitude in coordinates parameter of GeoJSON based on their roles?</p>
<p>EXample code</p>
<pre><code>public void processRelations() {
    try {
        LineIterable lineIterable = LineIterable.openGzipFile(dir + OsmJoin.REL_ID_COMPLETE_JSON);
        try (JsonWriter writer = createJsonWriter(OsmType.RELATION)) {
            Processor&lt;String, JsonObject&gt; p = compose(entryParsingProcessor, jsonParsingProcessor, new Processor&lt;JsonObject, JsonObject&gt;() {
                @Override
                public JsonObject process(JsonObject input) {
                    // FIXME see if we can extract some useful things from relations                       
                    return null;
                }
            });
            try (ConcurrentProcessingIterable&lt;String, JsonObject&gt; concIt = processConcurrently(lineIterable, p, 10, 9, 100)) {
                for (JsonObject o : concIt) {
                    if (o != null) {
                        writer.add(o);
                    }
                }
            } catch (IOException e) {
                throw new IllegalStateException(e);
            }
        }
    } catch (IOException e) {
        throw new IllegalStateException(e);
    }
}</code></pre>
<p>I have tried in Java and Python but reason is I could not find the logic behind the conversion of the relation tags from OSM to GeoJSON</p>
<p>I am expecting the logic behind the conversion of the relation tags from OSM to GeoJSON and sample code for that.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geometry" rel="tag" title="see questions tagged &#39;geometry&#39;">geometry</span> <span class="post-tag tag-link-osmtogeojson" rel="tag" title="see questions tagged &#39;osmtogeojson&#39;">osmtogeojson</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 May '19, 12:16</strong></p>
<img src="https://secure.gravatar.com/avatar/545b9ba53f0b1764bbaf495f040d5d06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaye19&#39;s gravatar image" />
<p><span>jaye19</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaye19 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69245" class="comments-container">
&#10;</div>
<div id="comment-tools-69245" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69245-form-container" class="comment-form-container">
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

<span id="74468"></span>

<div id="answer-container-74468" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74468-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try using <code>ogr2ogr</code> command instead. You need to export different "layers" but it could work like:</p>
<pre><code>ogr2ogr -f GeoJSON tmp_lines.geojson myosm.pbf lines
ogr2ogr -f GeoJSON tmp_mpoly.geojson myosm.pbf multipolygons</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '20, 09:30</strong></p>
<img src="https://secure.gravatar.com/avatar/cb99b2abaa73502ace0175863ca12b92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mcld&#39;s gravatar image" />
<p><span>mcld</span><br />
<span class="score" title="81 reputation points">81</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mcld has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74468" class="comments-container">
&#10;</div>
<div id="comment-tools-74468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74468-form-container" class="comment-form-container">
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

