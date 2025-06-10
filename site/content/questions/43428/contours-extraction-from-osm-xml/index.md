+++
type = "question"
title = "Contours extraction from OSM XML"
description = '''Hi, I am writing some software to convert contours and produce a contour map, I have downloaded gml data which I have converted to XML, both Osmosis and Splitter reads it correctly, I understand nodes and ways, but I don&#x27;t get Relations... here is a small extract from my file, this part is for coast...'''
date = "2015-06-06T15:32:00Z"
lastmod = "2015-06-09T05:45:00Z"
weight = 43428
keywords = [ "xml", "contours" ]
aliases = [ "/questions/43428" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Contours extraction from OSM XML](/questions/43428/contours-extraction-from-osm-xml)

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
<span id="post-43428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43428-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am writing some software to convert contours and produce a contour map, I have downloaded gml data which I have converted to XML, both Osmosis and Splitter reads it correctly, I understand nodes and ways, but I don't get Relations... here is a small extract from my file, this part is for coastline</p>
<pre><code>&lt;?xml version=&#39;1.0&#39; encoding=&#39;UTF-8&#39;?&gt;
&lt;osm version=&quot;0.6&quot; generator=&quot;Osmosis 0.43.1&quot;&gt;
  &lt;node id=&quot;1000000000088199248&quot; version=&quot;1&quot; timestamp=&quot;2015-06-05T12:12:53:50Z&quot; lat=&quot;54.4568954&quot; lon=&quot;-3.5692281&quot;/&gt;
  &lt;node id=&quot;1000000000088199249&quot; version=&quot;1&quot; timestamp=&quot;2015-06-05T12:12:53:50Z&quot; lat=&quot;54.4570016&quot; lon=&quot;-3.5691505&quot;/&gt;
  &lt;node id=&quot;1000000000088199250&quot; version=&quot;1&quot; timestamp=&quot;2015-06-05T12:12:53:50Z&quot; lat=&quot;54.4569964&quot; lon=&quot;-3.5690654&quot;/&gt;
  &lt;node id=&quot;1000000000088199251&quot; version=&quot;1&quot; timestamp=&quot;2015-06-05T12:12:53:50Z&quot; lat=&quot;54.4568735&quot; lon=&quot;-3.5689789&quot;/&gt;
  &lt;node id=&quot;1000000000088199252&quot; version=&quot;1&quot; timestamp=&quot;2015-06-05T12:12:53:50Z&quot; lat=&quot;54.4567703&quot; lon=&quot;-3.5689611&quot;/&gt;
  &lt;node id=&quot;1000000000088199253&quot; version=&quot;1&quot; timestamp=&quot;2015-06-05T12:12:53:50Z&quot; lat=&quot;54.456821&quot; lon=&quot;-3.5690741&quot;/&gt;
  &lt;node id=&quot;1000000000088199254&quot; version=&quot;1&quot; timestamp=&quot;2015-06-05T12:12:53:50Z&quot; lat=&quot;54.4568464&quot; lon=&quot;-3.5691275&quot;/&gt;
  &lt;way id=&quot;1000000000088199255&quot; version=&quot;5&quot; timestamp=&quot;2015-06-05T12:12:53:50Z&quot;&gt;
    &lt;nd ref=&quot;1000000000088199248&quot;/&gt;
    &lt;nd ref=&quot;1000000000088199249&quot;/&gt;
    &lt;nd ref=&quot;1000000000088199250&quot;/&gt;
    &lt;nd ref=&quot;1000000000088199251&quot;/&gt;
    &lt;nd ref=&quot;1000000000088199252&quot;/&gt;
    &lt;nd ref=&quot;1000000000088199253&quot;/&gt;
    &lt;nd ref=&quot;1000000000088199254&quot;/&gt;
    &lt;nd ref=&quot;1000000000088199248&quot;/&gt;
    &lt;tag k=&quot;natural&quot; v=&quot;coastline&quot;/&gt;
  &lt;/way&gt;
&lt;/osm&gt;</code></pre>
<p>When i produce a map from this there is nothing on it, and the map size isn't what I would expect .</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-contours" rel="tag" title="see questions tagged &#39;contours&#39;">contours</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jun '15, 15:32</strong></p>
<img src="https://secure.gravatar.com/avatar/1a48846e2865ba49198e0fb8e4064358?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rossendale%20Gary&#39;s gravatar image" />
<p><span>Rossendale Gary</span><br />
<span class="score" title="141 reputation points">141</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rossendale Gary has one accepted answer">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jun '15, 07:24</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span></p>
</div>
</div>
<div id="comments-container-43428" class="comments-container">
<span id="43437"></span>
<div id="comment-43437" class="comment">
<div id="post-43437-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not sure if I understand the point of your question. Which filters did you use on osmosis etc? How do you plan to mix contour lines etc...</p>
<p>Did you read the wiki already? <a href="https://wiki.openstreetmap.org/wiki/Contours">https://wiki.openstreetmap.org/wiki/Contours</a></p>
</div>
<div id="comment-43437-info" class="comment-info">
<span class="comment-age">(07 Jun '15, 07:28)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="43439"></span>
<div id="comment-43439" class="comment">
<div id="post-43439-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, I am trying to produce my own contour layer, I am writing the software in C#. I have downloaded the european contour and coastline data which is in gml, I have converted it to xml.</p>
<p>a small file osmosis is happy with, which tells me, I have the main settings in osmosis correct.</p>
<pre><code>    string processCommand = &quot;java&quot;;
    string processCommandArgs = _splitter;
    processCommandArgs += &quot;--mixed=true &quot;;
    processCommandArgs += &quot;--mapid=&quot; + Config.GetMapId(TypeOfMap) + &quot; &quot;;
    processCommandArgs += &quot;--description=&quot; + Config.GetMapName(TypeOfMap) + &quot; &quot;;
    processCommandArgs += &quot;--mixed=true &quot;;
    processCommandArgs += &quot;--max-nodes=5000000 &quot;;
    processCommandArgs += &quot;--keep-complete=false &quot;;
    processCommandArgs += &quot;--max-areas=27 &quot;;
    processCommandArgs += PbfDirectory + PbfFile + &quot; &quot;;
    processCommandArgs += &quot;--output-dir=&quot; + OutputDirectory;</code></pre>
<p>That is my osmosis command it works perfectly on small clumps of data I have produced, I think the problem is down to how big some of the ways are, some have over 6,000 nodes on them</p>
</div>
<div id="comment-43439-info" class="comment-info">
<span class="comment-age">(07 Jun '15, 08:08)</span> <span class="comment-user userinfo">Rossendale Gary</span>
</div>
</div>
<span id="43440"></span>
<div id="comment-43440" class="comment">
<div id="post-43440-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So you try to extract the coastline only (you call it contours?) This is AFAIK a bit tricky on the geometry level (unclosed polys, multipolygones, ...). So IMHO it's worth to consider using <a href="https://wiki.openstreetmap.org/wiki/Coastline">Coastline</a> dump?</p>
</div>
<div id="comment-43440-info" class="comment-info">
<span class="comment-age">(07 Jun '15, 08:32)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="43441"></span>
<div id="comment-43441" class="comment">
<div id="post-43441-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>the downloaded file contains both contours and coastline, I am really after the contours..</p>
<p><a href="https://www.ordnancesurvey.co.uk/opendatadownload/products.html">https://www.ordnancesurvey.co.uk/opendatadownload/products.html</a></p>
<p>The conversions to WSG84 I have done and verified, the problem is somehow I am confusing the splitter. without any meaningful fault report from it. The contours I get are really impressive, it works and it is accurate, the problem I am having is getting all the data through</p>
</div>
<div id="comment-43441-info" class="comment-info">
<span class="comment-age">(07 Jun '15, 09:01)</span> <span class="comment-user userinfo">Rossendale Gary</span>
</div>
</div>
</div>
<div id="comment-tools-43428" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43428-form-container" class="comment-form-container">
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

<span id="43477"></span>

<div id="answer-container-43477" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43477-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Oops, The xml file was spot on, the problem was in my other code used to generate the content for splitter to use.. I now have wonderful contours</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jun '15, 05:45</strong></p>
<img src="https://secure.gravatar.com/avatar/1a48846e2865ba49198e0fb8e4064358?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rossendale%20Gary&#39;s gravatar image" />
<p><span>Rossendale Gary</span><br />
<span class="score" title="141 reputation points">141</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rossendale Gary has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-43477" class="comments-container">
&#10;</div>
<div id="comment-tools-43477" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43477-form-container" class="comment-form-container">
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

