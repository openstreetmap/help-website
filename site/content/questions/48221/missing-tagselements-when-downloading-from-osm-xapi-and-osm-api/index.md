+++
type = "question"
title = "Missing tags/elements when downloading from OSM XAPI and OSM  API"
description = '''I&#x27;m trying to export an osm file for a region larger than that supported by the web interface hence the following command fails: http://api.openstreetmap.org/api/0.6/map?bbox=27.9314,-26.1841,28.1538,-26.0028 I turned to the XAPI which supports larger regions as follows: overpass.osm.rambler.ru/cgi/...'''
date = "2016-02-19T13:39:00Z"
lastmod = "2016-02-23T17:45:00Z"
weight = 48221
keywords = [ "api", "xapi", ".osm", "tags", "bounds" ]
aliases = [ "/questions/48221" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Missing tags/elements when downloading from OSM XAPI and OSM API](/questions/48221/missing-tagselements-when-downloading-from-osm-xapi-and-osm-api)

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
<span id="post-48221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48221-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to export an osm file for a region larger than that supported by the web interface hence the following command fails: <a href="http://api.openstreetmap.org/api/0.6/map?bbox=27.9314,-26.1841,28.1538,-26.0028">http://api.openstreetmap.org/api/0.6/map?bbox=27.9314,-26.1841,28.1538,-26.0028</a></p>
<p>I turned to the XAPI which supports larger regions as follows: overpass.osm.rambler.ru/cgi/xapi_meta?*[bbox=27.9314,-26.1841,28.1538,-26.0028]</p>
<p>However, the downloaded file is missing some of the xml elements/fields which are present in the map.osm file. For example there is no bounds field. Where can I download a larger map with all the relevant field (bounds, node, way, relation, Attributes)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span> <span class="post-tag tag-link-bounds" rel="tag" title="see questions tagged &#39;bounds&#39;">bounds</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Feb '16, 13:39</strong></p>
<img src="https://secure.gravatar.com/avatar/c6260781db2175f71bc861bc9c2030be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="confused1&#39;s gravatar image" />
<p><span>confused1</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="confused1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Feb '16, 18:59</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-48221" class="comments-container">
<span id="48240"></span>
<div id="comment-48240" class="comment">
<div id="post-48240-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What sources in detail have you already tried from <a href="https://wiki.openstreetmap.org/wiki/Planet.osm">https://wiki.openstreetmap.org/wiki/Planet.osm</a> ?</p>
<p>And if you found one source fitting to your aims, why did that not work? Or succes?</p>
</div>
<div id="comment-48240-info" class="comment-info">
<span class="comment-age">(20 Feb '16, 14:06)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="48287"></span>
<div id="comment-48287" class="comment">
<div id="post-48287-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i was using the osm extended api. i just added the bounds field myself which is not there by default.</p>
</div>
<div id="comment-48287-info" class="comment-info">
<span class="comment-age">(22 Feb '16, 11:09)</span> <span class="comment-user userinfo">confused1</span>
</div>
</div>
</div>
<div id="comment-tools-48221" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48221-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="48223"></span>

<div id="answer-container-48223" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48223-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48223-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-48223-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The relevant fields are <code>&lt;node&gt;</code>, <code>&lt;way&gt;</code>, and <code>&lt;relation&gt;</code>, in that order, and lots of them, all enclosed in a big <code>&lt;osm&gt;...&lt;/osm&gt;</code> section. Anything else is superfluous and won't be processed by most applications anyway.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '16, 14:18</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-48223" class="comments-container">
<span id="48288"></span>
<div id="comment-48288" class="comment">
<div id="post-48288-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>thanks very much, makes sense</p>
</div>
<div id="comment-48288-info" class="comment-info">
<span class="comment-age">(22 Feb '16, 11:09)</span> <span class="comment-user userinfo">confused1</span>
</div>
</div>
</div>
<div id="comment-tools-48223" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48223-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48310"></span>

<div id="answer-container-48310" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48310-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I believe, the original question hasn't really been answered yet, which was, why there's no <code>bounds</code> element in the XAPI response. Let's take a closer look.</p>
<p>After all, the XAPI call to the following URL will be translated into something Overpass API can make some sense out of, notably an Overpass XML request.</p>
<p>So, if you query for something like</p>
<p>overpass.osm.rambler.ru/cgi/xapi_meta?*[bbox=27.9314,-26.1841,28.1538,-26.0028]</p>
<p>this will in fact be translated into the following Overpass XML query under the hood:</p>
<pre><code>&lt;query type=&quot;node&quot;&gt;
  &lt;bbox-query s=&quot;-26.1841&quot; n=&quot;-26.0028&quot; w=&quot;27.9314&quot; e=&quot;28.1538&quot;/&gt;
&lt;/query&gt;
&lt;union&gt;
  &lt;item/&gt;
  &lt;query type=&quot;way&quot;&gt;
    &lt;bbox-query s=&quot;-26.1841&quot; n=&quot;-26.0028&quot; w=&quot;27.9314&quot; e=&quot;28.1538&quot;/&gt;
  &lt;/query&gt;
  &lt;recurse type=&quot;way-node&quot;/&gt;
&lt;/union&gt;
&lt;print mode=&quot;meta&quot;/&gt;
&lt;query type=&quot;relation&quot;&gt;
  &lt;bbox-query s=&quot;-26.1841&quot; n=&quot;-26.0028&quot; w=&quot;27.9314&quot; e=&quot;28.1538&quot;/&gt;
&lt;/query&gt;
&lt;print mode=&quot;meta&quot;/&gt;</code></pre>
<p>BTW: You can get to this translated query on your own, if you're following the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/XAPI_Compatibility_Layer#Migrating_from_XAPI_Compatibility_Layer_to_Overpass_XML_.2F_QL">XAPI Compatibility Layer to Overpass XML / QL migration procedure, as outlined in the wiki</a>.</p>
<p>That's already a good starting point to feed into overpass turbo: <a href="http://overpass-turbo.eu/s/eAf">http://overpass-turbo.eu/s/eAf</a></p>
<p>Now, how do we get the <code>bounds</code> element into the query result?</p>
<p>You need to know that this requires something called global bounding box, which can be added by providing an &lt;osm-script&gt; element along with a bbox attribute. Your resulting query looks like this: it's basically the same overpass turbo query as before, but this time also returning a <code>bounds</code> element.</p>
<p><a href="http://overpass-turbo.eu/s/eAh">http://overpass-turbo.eu/s/eAh</a></p>
<p>You can get the query results from overpass turbo via Export -&gt; get raw data directly from Overpass API, you'll end up with a file called interpreter and the following line in the resulting file:</p>
<pre><code> &lt;bounds minlat=&quot;-26.1841&quot; minlon=&quot;27.9314&quot; maxlat=&quot;-26.0028&quot; maxlon=&quot;28.1538&quot;/&gt;</code></pre>
<p>Mission accomplished!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Feb '16, 17:45</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Feb '16, 18:35</strong> </span></p>
</div>
</div>
<div id="comments-container-48310" class="comments-container">
&#10;</div>
<div id="comment-tools-48310" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48310-form-container" class="comment-form-container">
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

