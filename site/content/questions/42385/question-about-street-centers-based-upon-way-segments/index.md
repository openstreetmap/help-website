+++
type = "question"
title = "Question about street centers based upon way-segments"
description = '''Hello there, here&#x27;s a question I&#x27;ve looked for on this forum but surprisingly I could not find an answer, so maybe my approach or assumptions aren&#x27;t right. I&#x27;ve recently imported an osm-file into postgresql for the purpose of geocoding. using the planet_osm_line table I could extract the street name...'''
date = "2015-04-16T12:46:00Z"
lastmod = "2015-04-16T12:46:00Z"
weight = 42385
keywords = [ "osm", "street", "postgresql" ]
aliases = [ "/questions/42385" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Question about street centers based upon way-segments](/questions/42385/question-about-street-centers-based-upon-way-segments)

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
<span id="post-42385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42385-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello there, here's a question I've looked for on this forum but surprisingly I could not find an answer, so maybe my approach or assumptions aren't right.</p>
<p>I've recently imported an osm-file into postgresql for the purpose of geocoding. using the planet_osm_line table I could extract the street names of a particular city. However the lines table contains multiple way-segments/records for one street. I can join the segments into a single line but that does not work in all cases. Is there a way to extract the "real" CenterPoint of a street ?</p>
<p>I've created a recusive function to create a table with all connected segments like this:</p>
<pre><code>CREATE OR REPLACE FUNCTION public.connectedways (
  main_id bigint
)
RETURNS SETOF public.planet_osm_line AS
$body$
   BEGIN
      Insert into connected Select osm_id,name,way from planet_osm_line where osm_id = main_id; 
  Perform connectedways(b.osm_id) from planet_osm_line a, planet_osm_line b where a.osm_id = main_id 
    and st_touches(a.way,b.way) AND (st_startpoint(a.way)=st_endpoint(b.way)  or 
            st_startpoint(b.way)=st_endpoint(a.way))
    and a.name=b.name and not EXISTS(Select osm_id from connected c where c.osm_id=b.osm_id);        
  RETURN;</code></pre>
<p>END $body$ LANGUAGE 'plpgsql'</p>
</pre>
Using the result table I merge all geometry to a single line and use st_line_interpolate_point(way, 0.5) to get the centerpoint ;
<pre><code>SELECT ST_AsEWKT(ST_Line_Interpolate_Point(st_makeline(way), 0.50)) from connected;</code></pre>
Using this method it works but the results are not correct???
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Apr '15, 12:46</strong></p>
<img src="https://secure.gravatar.com/avatar/393b97cb8806b53dd4463b8a02855112?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eric%20Bossink&#39;s gravatar image" />
<p><span>Eric Bossink</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eric Bossink has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Apr '15, 14:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-42385" class="comments-container">
&#10;</div>
<div id="comment-tools-42385" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42385-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

