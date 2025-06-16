+++
type = "question"
title = "import OSM data to PostGIS database via imposm3"
description = '''I use imposm3 (install binary from http://imposm.org/static/rel/ on Ubuntu Server) for import OSM data (features &#x27;protected_area&#x27; with &quot;boundary&quot;=&quot;protected_area&quot; (https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dprotected_area)) in PostGIS database. When I import data on full Ukraine (http://www.o...'''
date = "2015-06-25T08:13:00Z"
lastmod = "2015-06-25T08:13:00Z"
weight = 43771
keywords = [ "import", "imposm", "osm", "postgis", "relation" ]
aliases = [ "/questions/43771" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [import OSM data to PostGIS database via imposm3](/questions/43771/import-osm-data-to-postgis-database-via-imposm3)

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
<span id="post-43771-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43771-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43771-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I use imposm3 (install binary from <a href="http://imposm.org/static/rel/">http://imposm.org/static/rel/</a> on Ubuntu Server) for import OSM data (features 'protected_area' with "boundary"="protected_area" (<a href="https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dprotected_area))">https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dprotected_area))</a> in PostGIS database. When I import data on full Ukraine (<a href="https://www.openstreetmap.org/relation/3791141)">https://www.openstreetmap.org/relation/3791141)</a> area I receive in table multipolygon from relation <a href="https://www.openstreetmap.org/relation/4650441">https://www.openstreetmap.org/relation/4650441</a> with name from <a href="https://www.openstreetmap.org/way/331465943">https://www.openstreetmap.org/way/331465943</a> object. But when I import small area (Donetskaya oblast <a href="https://www.openstreetmap.org/relation/71973)">https://www.openstreetmap.org/relation/71973)</a> I received correct polygons from <a href="https://www.openstreetmap.org/relation/4650441">https://www.openstreetmap.org/relation/4650441</a> relation (not multipolygon). How receive polygons from <a href="https://www.openstreetmap.org/relation/4650441">https://www.openstreetmap.org/relation/4650441</a> relation when importing protected_areas on Ukraine (<a href="https://www.openstreetmap.org/relation/3791141)?">https://www.openstreetmap.org/relation/3791141)?</a> For import I use command:</p>
<pre><code>imposm3 import -read ${BASEDIR}/osmdownloads/ukraine-latest.osm.pbf -write -cachedir ${BASEDIR}/cache -connection &#39;postgis://user:password@localhost:5432/uaosm?sslmode=disable&amp;prefix=NONE&#39; -dbschema-import public -mapping ${BASEDIR}/mapping.json -diff -srid 4326 -overwritecache</code></pre>
<p>Example mapping.json file:</p>
<pre><code>{
        &quot;tags&quot;: {
            &quot;load_all&quot;: true
        },
        &quot;tables&quot;: {
&#10;
            &quot;protected_area_polygon&quot;: {
                &quot;fields&quot;: [
                    {
                        &quot;type&quot;: &quot;geometry&quot;,
                        &quot;name&quot;: &quot;the_geom&quot;,
                        &quot;key&quot;: null
                    },               
                    {
                        &quot;type&quot;: &quot;id&quot;,
                        &quot;name&quot;: &quot;osm_id&quot;,
                        &quot;key&quot;: null
                    },
                    {
                        &quot;type&quot;: &quot;string&quot;,
                        &quot;name&quot;: &quot;name&quot;,
                        &quot;key&quot;: &quot;name&quot;
                    },
                    {
                        &quot;type&quot;: &quot;string&quot;,
                        &quot;name&quot;: &quot;name_uk&quot;,
                        &quot;key&quot;: &quot;name:uk&quot;
                    },  
                    {
                        &quot;type&quot;: &quot;string&quot;,
                        &quot;name&quot;: &quot;name_ru&quot;,
                        &quot;key&quot;: &quot;name:ru&quot;
                    },  
                    {
                        &quot;type&quot;: &quot;string&quot;,
                        &quot;name&quot;: &quot;name_en&quot;,
                        &quot;key&quot;: &quot;name:en&quot;
                    },              
                    {
                        &quot;type&quot;: &quot;string&quot;,
                        &quot;name&quot;: &quot;boundary&quot;,
                        &quot;key&quot;: &quot;boundary&quot;
                    },
                    {
                        &quot;type&quot;: &quot;string&quot;,
                        &quot;name&quot;: &quot;prot_class&quot;,
                        &quot;key&quot;: &quot;protect_class&quot;
                    },              
                    {
                        &quot;type&quot;: &quot;string&quot;,
                        &quot;name&quot;: &quot;prot_stat&quot;,
                        &quot;key&quot;: &quot;protection_status&quot;
                    },
                    {
                        &quot;type&quot;: &quot;string&quot;,
                        &quot;name&quot;: &quot;prot_title&quot;,
                        &quot;key&quot;: &quot;protection_title&quot;
                    },                  
                    {
                        &quot;type&quot;: &quot;string&quot;,
                        &quot;name&quot;: &quot;naturalt&quot;,
                        &quot;key&quot;: &quot;natural&quot;
                    },              
                    {
                        &quot;type&quot;: &quot;string&quot;,
                        &quot;name&quot;: &quot;amenity&quot;,
                        &quot;key&quot;: &quot;amenity&quot;
                    },
                    {
                        &quot;type&quot;: &quot;string&quot;,
                        &quot;name&quot;: &quot;leisure&quot;,
                        &quot;key&quot;: &quot;leisure&quot;
                    },
                    {
                        &quot;type&quot;: &quot;string&quot;,
                        &quot;name&quot;: &quot;landuse&quot;,
                        &quot;key&quot;: &quot;landuse&quot;
                    },
                    {
                        &quot;type&quot;: &quot;string&quot;,
                        &quot;name&quot;: &quot;operator&quot;,
                        &quot;key&quot;: &quot;operator&quot;
                    },  
                    {
                        &quot;type&quot;: &quot;string&quot;,
                        &quot;name&quot;: &quot;place&quot;,
                        &quot;key&quot;: &quot;place&quot;
                    },  
                    {
                        &quot;type&quot;: &quot;string&quot;,
                        &quot;name&quot;: &quot;website&quot;,
                        &quot;key&quot;: &quot;website&quot;
                    },
                    {
                        &quot;type&quot;: &quot;string&quot;,
                        &quot;name&quot;: &quot;wikipedia&quot;,
                        &quot;key&quot;: &quot;wikipedia&quot;
                    },              
                    {
                        &quot;type&quot;: &quot;string&quot;,
                        &quot;name&quot;: &quot;note&quot;,
                        &quot;key&quot;: &quot;note&quot;
                    }   
                ],
                &quot;type&quot;: &quot;polygon&quot;,
                &quot;mapping&quot;: {
                     &quot;boundary&quot;: [&quot;protected_area&quot;]
                }
            }
        }
    }</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-imposm" rel="tag" title="see questions tagged &#39;imposm&#39;">imposm</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jun '15, 08:13</strong></p>
<img src="https://secure.gravatar.com/avatar/eee6f11bbcb9d9107f59d3f66517a98f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HasT&#39;s gravatar image" />
<p><span>HasT</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HasT has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jun '15, 08:14</strong> </span></p>
</div>
</div>
<div id="comments-container-43771" class="comments-container">
&#10;</div>
<div id="comment-tools-43771" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43771-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

