+++
type = "question"
title = "Overpass: How can I create my own area"
description = '''Is it possible to create an area, as part of an Overpass query, for an arbitrary multypolygon relation?  Overpass does not create areas for multipolygons that have no name or postal code, according to areas.osm3s.  For example, I&#x27;d like to find all orphan nodes in the area defined by relation 619535...'''
date = "2017-12-08T10:58:00Z"
lastmod = "2017-12-11T18:01:00Z"
weight = 61078
keywords = [ "overpass", "area", "overpass-ql", "multipolygon" ]
aliases = [ "/questions/61078" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass: How can I create my own area](/questions/61078/overpass-how-can-i-create-my-own-area)

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
<span id="post-61078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61078-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to create an area, as part of an Overpass query, for an arbitrary multypolygon relation?</p>
<p>Overpass does not create areas for multipolygons that have no name or postal code, according to <a href="https://github.com/drolbr/Overpass-API/blob/master/src/rules/areas.osm3s">areas.osm3s</a>.</p>
<p>For example, I'd like to find all orphan nodes in the area defined by <a href="https://www.openstreetmap.org/relation/6195356">relation 6195356</a>.</p>
<p><strong>If</strong> this relation had a built-in area, the Overpass query would be:</p>
<pre><code>  node (area:3606195356);     // Find all nodes in multipolygon
  (._; - (way(bn);node(w));); // Remove nodes used by ways
  (._; - node._[~&quot;.&quot;~&quot;.&quot;];);  // Remove nodes with tags
  (._; - (rel(bn);node(r));); // Remove nodes used by relations
  out meta qt geom;</code></pre>
<p>The requested solution would be Overpass Query statement(s) that will replace <code>node (area:3606195356);</code></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Dec '17, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/7f7ca553e7227a0e0fe502d1db88cb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zstadler&#39;s gravatar image" />
<p><span>zstadler</span><br />
<span class="score" title="116 reputation points">116</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zstadler has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>11 Dec '17, 17:58</strong> </span></p>
</div>
</div>
<div id="comments-container-61078" class="comments-container">
<span id="61144"></span>
<div id="comment-61144" class="comment">
<div id="post-61144-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The short and sad answer is it is not possible:</p>
<pre><code>... you as a user cannot influence the area creation process by sending queries to the server. It&#39;s all defined in the area creation rules, see Overpass_API/Areas Mmd (talk) 17:22, 9 December 2017 (UTC)</code></pre>
<p>Ref: - <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/status">https://wiki.openstreetmap.org/wiki/Overpass_API/status</a> - <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Areas">https://wiki.openstreetmap.org/wiki/Overpass_API/Areas</a></p>
</div>
<div id="comment-61144-info" class="comment-info">
<span class="comment-age">(11 Dec '17, 17:57)</span> <span class="comment-user userinfo">zstadler</span>
</div>
</div>
<span id="61145"></span>
<div id="comment-61145" class="comment">
<div id="post-61145-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The short and sad answer is it is not possible:</p>
<pre><code>... you as a user cannot influence the area creation process by sending queries to the server. It&#39;s all defined in the area creation rules, see Overpass_API/Areas Mmd (talk) 17:22, 9 December 2017 (UTC)</code></pre>
<p>Ref: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/status">https://wiki.openstreetmap.org/wiki/Overpass_API/status</a></p>
</div>
<div id="comment-61145-info" class="comment-info">
<span class="comment-age">(11 Dec '17, 18:01)</span> <span class="comment-user userinfo">zstadler</span>
</div>
</div>
</div>
<div id="comment-tools-61078" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61078-form-container" class="comment-form-container">
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

<span id="61085"></span>

<div id="answer-container-61085" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61085-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's a <code>map_to_area</code> operation that creates an area:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Map_way.2Frelation_to_area_.28map_to_area.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Map_way.2Frelation_to_area_.28map_to_area.29</a></p>
<p>The documentation only says that the operation returns the area associated with the OSM object but it also appears to create it if it doesn't exist. I'm not sure how persistent the new areas are, but at the moment there is an area associated with that relation on the overpass-api.de server, apparently due to my experimenting.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Dec '17, 12:43</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Dec '17, 12:44</strong> </span></p>
</div>
</div>
<div id="comments-container-61085" class="comments-container">
<span id="61089"></span>
<div id="comment-61089" class="comment">
<div id="post-61089-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately, this does not seem to work for the relation at hand. The following Overpass query returns nothing:</p>
<pre><code>    rel(6195356);
    map_to_area;
    out;</code></pre>
</div>
<div id="comment-61089-info" class="comment-info">
<span class="comment-age">(08 Dec '17, 14:58)</span> <span class="comment-user userinfo">zstadler</span>
</div>
</div>
<span id="61092"></span>
<div id="comment-61092" class="comment">
<div id="post-61092-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could be server specific. Here it returns an area: <a href="http://overpass-turbo.eu/s/tEL">http://overpass-turbo.eu/s/tEL</a></p>
<p>(with overpass-api.de selected in the settings)</p>
</div>
<div id="comment-61092-info" class="comment-info">
<span class="comment-age">(08 Dec '17, 16:22)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="61099"></span>
<div id="comment-61099" class="comment">
<div id="post-61099-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm getting an empty set from the overpass-api.de server</p>
<p><a href="http://overpass-api.de/api/interpreter?data=rel%286195356%29%3Bmap_to_area%3Bout%3B">http://overpass-api.de/api/interpreter?data=rel(6195356);map_to_area;out;</a></p>
<p>or</p>
<p><a href="http://overpass-api.de/api/interpreter?data=%5Bout:popup(%22Results%22;%5Btype%5D;)%5D;rel(6195356);map_to_area;out;">http://overpass-api.de/api/interpreter?data=[out:popup("Result:";[type];)];rel(6195356);map_to_area;out;</a></p>
</div>
<div id="comment-61099-info" class="comment-info">
<span class="comment-age">(08 Dec '17, 20:58)</span> <span class="comment-user userinfo">zstadler</span>
</div>
</div>
<span id="61104"></span>
<div id="comment-61104" class="comment">
<div id="post-61104-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here's the output I get clicking your first link:</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;osm version=&quot;0.6&quot; generator=&quot;Overpass API&quot;&gt;
&lt;note&gt;The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.&lt;/note&gt;
&lt;meta osm_base=&quot;2017-12-09T00:25:02Z&quot; areas=&quot;2017-12-08T23:26:03Z&quot;/&gt;
&#10;  &lt;area id=&quot;3606195356&quot;&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Israel and Palestine&quot;/&gt;
    &lt;tag k=&quot;name:de&quot; v=&quot;Israel und Palästina&quot;/&gt;
    &lt;tag k=&quot;name:en&quot; v=&quot;Israel and Palestine&quot;/&gt;
    &lt;tag k=&quot;note&quot; v=&quot;Do not delete!&quot;/&gt;
    &lt;tag k=&quot;type&quot; v=&quot;multipolygon&quot;/&gt;
  &lt;/area&gt;
&#10;&lt;/osm&gt;</code></pre>
</div>
<div id="comment-61104-info" class="comment-info">
<span class="comment-age">(09 Dec '17, 00:28)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="61106"></span>
<div id="comment-61106" class="comment not_top_scorer">
<div id="post-61106-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here is what I get:</p>
<pre><code>    &lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
    &lt;osm version=&quot;0.6&quot; generator=&quot;Overpass API 0.7.54.12 054bb0bb&quot;&gt;
    &lt;note&gt;The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.&lt;/note&gt;
    &lt;meta osm_base=&quot;2017-12-09T06:15:02Z&quot; areas=&quot;2017-12-09T05:42:02Z&quot;/&gt;
&#10;    &lt;/osm&gt;</code></pre>
<p>Also note the difference in the "generator" text.</p>
<p>Strange indeed.</p>
</div>
<div id="comment-61106-info" class="comment-info">
<span class="comment-age">(09 Dec '17, 06:19)</span> <span class="comment-user userinfo">zstadler</span>
</div>
</div>
<span id="61107"></span>
<div id="comment-61107" class="comment not_top_scorer">
<div id="post-61107-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There seems to be a difference between the two servers behind overpass-api.de</p>
<pre><code>&gt; wget -q -O - http://178.63.48.217/api/interpreter?data=rel%286195356%29%3Bmap_to_area%3Bout%3B
&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;osm version=&quot;0.6&quot; generator=&quot;Overpass API 0.7.54.12 054bb0bb&quot;&gt;
&lt;note&gt;The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.&lt;/note&gt;
&lt;meta osm_base=&quot;2017-12-09T06:34:02Z&quot; areas=&quot;2017-12-09T05:42:02Z&quot;/&gt;
&#10;&lt;/osm&gt;
&#10;&gt; wget -q -O - http://136.243.42.136/api/interpreter?data=rel%286195356%29%3Bmap_to_area%3Bout%3B
&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;osm version=&quot;0.6&quot; generator=&quot;Overpass API&quot;&gt;
&lt;note&gt;The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.&lt;/note&gt;
&lt;meta osm_base=&quot;2017-12-09T06:34:02Z&quot; areas=&quot;2017-12-09T05:21:02Z&quot;/&gt;
&#10;  &lt;area id=&quot;3606195356&quot;&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Israel and Palestine&quot;/&gt;
    &lt;tag k=&quot;name:de&quot; v=&quot;Israel und Pal├ñstina&quot;/&gt;
    &lt;tag k=&quot;name:en&quot; v=&quot;Israel and Palestine&quot;/&gt;
    &lt;tag k=&quot;note&quot; v=&quot;Do not delete!&quot;/&gt;
    &lt;tag k=&quot;type&quot; v=&quot;multipolygon&quot;/&gt;
  &lt;/area&gt;
&#10;&lt;/osm&gt;</code></pre>
</div>
<div id="comment-61107-info" class="comment-info">
<span class="comment-age">(09 Dec '17, 06:40)</span> <span class="comment-user userinfo">zstadler</span>
</div>
</div>
<span id="61117"></span>
<div id="comment-61117" class="comment">
<div id="post-61117-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Apparently, the result provided the by "z.overpass-api.de" server (136.243.42.136), which contains the area element, is outdated. See <a href="https://github.com/drolbr/Overpass-API/issues/285#issuecomment-350312885">this comment for GitHub issue 285</a> and a <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/status">9-Dec-2017 server issue report</a>.</p>
</div>
<div id="comment-61117-info" class="comment-info">
<span class="comment-age">(09 Dec '17, 17:44)</span> <span class="comment-user userinfo">zstadler</span>
</div>
</div>
<span id="61132"></span>
<div id="comment-61132" class="comment not_top_scorer">
<div id="post-61132-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It seems like the old areas were also removed from the "z.overpass-api.de" server (136.243.42.136):</p>
<pre><code>&gt; wget -q -O - http://z.overpass-api.de/api/interpreter?data=rel%286195356%29%3Bmap_to_area%3Bout%3B
&#10;&lt;osm version=&quot;0.6&quot; generator=&quot;Overpass API 0.7.54.12 054bb0bb&quot;&gt;
&lt;note&gt;The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.&lt;/note&gt;
&lt;meta osm_base=&quot;2017-12-11T09:57:02Z&quot; areas=&quot;2017-12-11T08:55:02Z&quot;/&gt;
&#10;&lt;/osm&gt;</code></pre>
<p>The question remains open</p>
</div>
<div id="comment-61132-info" class="comment-info">
<span class="comment-age">(11 Dec '17, 10:00)</span> <span class="comment-user userinfo">zstadler</span>
</div>
</div>
</div>
<div id="comment-tools-61085" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-61085-form-container" class="comment-form-container">
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

