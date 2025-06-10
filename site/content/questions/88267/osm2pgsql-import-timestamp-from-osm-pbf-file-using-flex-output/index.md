+++
type = "question"
title = "[closed] OSM2PGSQL import timestamp from osm PBF file using flex output"
description = '''Hi, I am new to osm2pgsql and i am figuring out how to import timestamp from osm .pbf file using the flex output. I am using version 1.8.0 My problem: Can&#x27;t access to object.timestamp as the documentation says My Lua file: local pois = osm2pgsql.define_table({  name = &#x27;pois&#x27;,  ids = { type = &#x27;any&#x27;, ...'''
date = "2024-03-05T09:20:00Z"
lastmod = "2024-03-06T10:50:00Z"
weight = 88267
keywords = [ "timestamps", "osm2pgsql" ]
aliases = [ "/questions/88267" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] OSM2PGSQL import timestamp from osm PBF file using flex output](/questions/88267/osm2pgsql-import-timestamp-from-osm-pbf-file-using-flex-output)

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
<span id="post-88267-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88267-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88267-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am new to osm2pgsql and i am figuring out how to import timestamp from osm .pbf file using the flex output. I am using version 1.8.0</p>
<p>My problem: Can't access to object.timestamp as the <a href="https://osm2pgsql.org/doc/manual.html#processing-callbacks">documentation</a> says</p>
<p>My Lua file:</p>
<pre><code>local pois = osm2pgsql.define_table({
    name = &#39;pois&#39;,
    ids = { type = &#39;any&#39;, type_column = &#39;osm_type&#39;, id_column = &#39;osm_id&#39; },
    columns = {
        { column = &#39;updated_at&#39;},
        { column = &#39;name&#39; },
        { column = &#39;class&#39;, not_null = true },
        { column = &#39;subclass&#39; },
        { column = &#39;geom&#39;, type = &#39;point&#39;, not_null = true },
        { column = &#39;tags&#39;, type = &#39;jsonb&#39; },
}})
&#10;
function process_poi(object, geom)
    local a = {
        updated_at = object.timestamp or nil,
        name = object.tags.name,
        geom = geom,
        tags = object.tags,
    }
&#10;    if object.tags.amenity and ( 
           object.tags.amenity == &#39;place_of_worship&#39; or 
           object.tags.amenity == &#39;drinking_water&#39; 
        )
        then
        a.class = &#39;amenity&#39;
        a.subclass = object.tags.amenity
    elseif object.tags.natural and (
           object.tags.natural == &#39;peak&#39; or
           object.tags.natural == &#39;spring&#39;
        )
        then
        a.class = &#39;natural&#39;
        a.subclass = object.tags.natural   
    else
        return
    end
&#10;    pois:insert(a)
end
&#10;function osm2pgsql.process_node(object)
    process_poi(object, object:as_point())
end
&#10;function osm2pgsql.process_way(object)
    if object.is_closed and object.tags.building then
        process_poi(object, object:as_polygon():centroid())
    end
end</code></pre>
<p>What am i missing here?</p>
<p>Thank you for the attention.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-timestamps" rel="tag" title="see questions tagged &#39;timestamps&#39;">timestamps</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Mar '24, 09:20</strong></p>
<img src="https://secure.gravatar.com/avatar/86e6372f950b0edfb6b0b946efb1540d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gemanzo&#39;s gravatar image" />
<p><span>Gemanzo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gemanzo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>06 Mar '24, 10:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-88267" class="comments-container">
<span id="88272"></span>
<div id="comment-88272" class="comment">
<div id="post-88272-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Duplicate of <a href="https://community.openstreetmap.org/t/osm2pgsql-import-timestamp-from-osm-pbf-file-using-flex-output/110138">https://community.openstreetmap.org/t/osm2pgsql-import-timestamp-from-osm-pbf-file-using-flex-output/110138</a> and answered there.</p>
</div>
<div id="comment-88272-info" class="comment-info">
<span class="comment-age">(06 Mar '24, 10:50)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-88267" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88267-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question" by SomeoneElse 06 Mar '24, 10:50

</div>

</div>

</div>

