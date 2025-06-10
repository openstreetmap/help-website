+++
type = "question"
title = "OSM data query by overpass for multiple bbox"
description = '''I&#x27;m trying to build a query to download data (for example parks) from different bbox (can&#x27;t be substituted by nominatim) by overpass-turbo. Here my query but it doesn&#x27;t work:  &amp;lt;osm-script output=&quot;json&quot; timeout=&quot;50&quot;&amp;gt;  &amp;lt;!-- fetch area to search in --&amp;gt;  &amp;lt;union into=&quot;area&quot;&amp;gt;  &amp;lt;bbox-q...'''
date = "2017-05-03T14:29:00Z"
lastmod = "2017-05-03T17:04:00Z"
weight = 56020
keywords = [ "overpass", "overpass-turbo", "bbox", "osm", "query" ]
aliases = [ "/questions/56020" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM data query by overpass for multiple bbox](/questions/56020/osm-data-query-by-overpass-for-multiple-bbox)

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
<span id="post-56020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56020-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to build a query to download data (for example parks) from different bbox (can't be substituted by nominatim) by overpass-turbo. Here my query but it doesn't work:</p>
<pre><code> &lt;osm-script output=&quot;json&quot; timeout=&quot;50&quot;&gt;
  &lt;!-- fetch area to search in --&gt;
  &lt;union into=&quot;area&quot;&gt;
    &lt;bbox-query e=&quot;20&quot; n=&quot;30&quot; s=&quot;28&quot; w=&quot;18&quot;/&gt;
    &lt;bbox-query e=&quot;30&quot; n=&quot;40&quot; s=&quot;38&quot; w=&quot;28&quot;/&gt;
    &lt;bbox-query e=&quot;40&quot; n=&quot;50&quot; s=&quot;48&quot; w=&quot;38&quot;/&gt;
  &lt;/union&gt;
  &lt;!-- gather results --&gt;
  &lt;union&gt;
    &lt;!-- query part for: “leisure=park” --&gt;
    &lt;query type=&quot;node&quot;&gt;
      &lt;has-kv k=&quot;leisure&quot; v=&quot;park&quot;/&gt;
      &lt;area-query from=&quot;area&quot;/&gt;
    &lt;/query&gt;
    &lt;query type=&quot;way&quot;&gt;
      &lt;has-kv k=&quot;leisure&quot; v=&quot;park&quot;/&gt;
      &lt;area-query from=&quot;area&quot;/&gt;
    &lt;/query&gt;
    &lt;query type=&quot;relation&quot;&gt;
      &lt;has-kv k=&quot;leisure&quot; v=&quot;park&quot;/&gt;
      &lt;area-query from=&quot;area&quot;/&gt;
    &lt;/query&gt;
  &lt;/union&gt;
  &lt;!-- print results --&gt;
  &lt;print from=&quot;area&quot; geometry=&quot;skeleton&quot; mode=&quot;body&quot; order=&quot;id&quot;/&gt;
 &lt;!-- &lt;recurse type=&quot;down&quot;/&gt; --&gt;
  &lt;print from=&quot;area&quot; geometry=&quot;skeleton&quot; mode=&quot;skeleton&quot; order=&quot;quadtile&quot; /&gt;
&lt;/osm-script&gt;</code></pre>
<p>Please help to fix it. I can't find suitable solution in documentation on wiki and here in previous questions.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 May '17, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/60ea91f0a29c6e6c7096e8f61e09c8f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seevgenia&#39;s gravatar image" />
<p><span>seevgenia</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seevgenia has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 May '17, 14:36</strong> </span></p>
</div>
</div>
<div id="comments-container-56020" class="comments-container">
&#10;</div>
<div id="comment-tools-56020" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56020-form-container" class="comment-form-container">
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

<span id="56024"></span>

<div id="answer-container-56024" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56024-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the non XML query language you can pass a bbox to a filter:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Bounding_box">http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Bounding_box</a></p>
<p>I don't know if there is an equivalent in the XML. In any case, a union of such queries should work for your query:</p>
<pre><code>(
node(50.6,7.0,50.8,7.3)[leisure=park];
way(50.6,7.0,50.8,7.3)[leisure=park];
rel(50.6,7.0,50.8,7.3)[leisure=park];
node(51.6,7.0,51.8,7.3)[leisure=park];
way(51.6,7.0,51.8,7.3)[leisure=park];
rel(51.6,7.0,51.8,7.3)[leisure=park];
);</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 May '17, 17:04</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-56024" class="comments-container">
&#10;</div>
<div id="comment-tools-56024" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56024-form-container" class="comment-form-container">
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

