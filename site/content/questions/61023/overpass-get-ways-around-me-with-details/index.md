+++
type = "question"
title = "Overpass - Get ways around me with details"
description = '''Hi, for my application I need the ways around me (e.g. in a 2000m radius). At the moment I have the following query (Overpass): &amp;lt;query type=&quot;way&quot;&amp;gt;  &amp;lt;around lat=&quot;40.65541&quot; lon=&quot;-4.70717&quot; radius=&quot;2000&quot;/&amp;gt; &amp;lt;/query&amp;gt; &amp;lt;union&amp;gt;  &amp;lt;item/&amp;gt;  &amp;lt;recurse type=&quot;down&quot;/&amp;gt; &amp;lt;/union&amp;g...'''
date = "2017-12-06T06:59:00Z"
lastmod = "2017-12-06T16:48:00Z"
weight = 61023
keywords = [ "overpass", "reversegeocoding", "nominatim", "query" ]
aliases = [ "/questions/61023" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass - Get ways around me with details](/questions/61023/overpass-get-ways-around-me-with-details)

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
<span id="post-61023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61023-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, for my application I need the ways around me (e.g. in a 2000m radius). At the moment I have the following query (Overpass):</p>
<pre><code>&lt;query type=&quot;way&quot;&gt;
   &lt;around lat=&quot;40.65541&quot; lon=&quot;-4.70717&quot; radius=&quot;2000&quot;/&gt;
&lt;/query&gt;
&lt;union&gt;
  &lt;item/&gt;
  &lt;recurse type=&quot;down&quot;/&gt;
&lt;/union&gt;
&lt;print/&gt;</code></pre>
<p>From this query, I get nodes and ways. Example of a way:</p>
<pre><code>  &lt;way id=&quot;305251304&quot;&gt;
    &lt;nd ref=&quot;634163717&quot;/&gt;
    &lt;nd ref=&quot;3098509510&quot;/&gt;
    &lt;nd ref=&quot;3660108566&quot;/&gt;
    &lt;tag k=&quot;highway&quot; v=&quot;residential&quot;/&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Calle Valladolid&quot;/&gt;
    &lt;tag k=&quot;source&quot; v=&quot;ITACyL&quot;/&gt;
    &lt;tag k=&quot;source:date&quot; v=&quot;2009&quot;/&gt;
  &lt;/way&gt;</code></pre>
<p>My first problem is that I need more details (name, ref name, maxspeed...) for the ways. At the moment, I make another request to Nominatim for each way, e.g.:</p>
<p><a href="https://nominatim.openstreetmap.org/lookup?format=json&amp;namedetails=1&amp;osm_ids=W305251304">https://nominatim.openstreetmap.org/lookup?format=json&amp;namedetails=1&amp;osm_ids=W305251304</a></p>
<p>This takes too long. Is it possible to get the details for all the ways already in the Overpass query? If not, is there another API which I can use for my requirements? By the way: I have installed Nominatim and Overpass on my own server because I send many requests.</p>
<p>My second problem is that I just need streets, I don't need e.g. cycleways, footways and buildings. How can I manage this in my query?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Dec '17, 06:59</strong></p>
<img src="https://secure.gravatar.com/avatar/d0c8a30460b2bb4ced62400dcbee2b54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FM_Pete&#39;s gravatar image" />
<p><span>FM_Pete</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FM_Pete has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61023" class="comments-container">
<span id="61024"></span>
<div id="comment-61024" class="comment">
<div id="post-61024-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I solved the first problem by myself.</p>
<p>I have now the following query:</p>
<pre><code>&lt;query type=&quot;way&quot;&gt;
   &lt;around lat=&quot;40.65541&quot; lon=&quot;-4.70717&quot; radius=&quot;2000&quot;/&gt;
  &lt;has-kv k=&quot;highway&quot; modv=&quot;not&quot; regv=&quot;path|track|cycleway|footway&quot;/&gt;
&lt;/query&gt;
&lt;union&gt;
  &lt;item/&gt;
  &lt;recurse type=&quot;down&quot;/&gt;
&lt;/union&gt;
&lt;print/&gt;</code></pre>
<code> </code>
<p>How can I exclude e.g. areas for landuse? The following query doesn't work:</p>
<pre><code>&lt;query type=&quot;way&quot;&gt;
   &lt;around lat=&quot;40.65541&quot; lon=&quot;-4.70717&quot; radius=&quot;2000&quot;/&gt;
  &lt;has-kv k=&quot;highway&quot; modv=&quot;not&quot; regv=&quot;path|track|cycleway|footway&quot;/&gt;
  &lt;has-kv k=&quot;landuse&quot; modv=&quot;not&quot;/&gt;
&lt;/query&gt;
&lt;union&gt;
  &lt;item/&gt;
  &lt;recurse type=&quot;down&quot;/&gt;
&lt;/union&gt;
&lt;print/&gt;</code></pre>
</code>
</div>
<div id="comment-61024-info" class="comment-info">
<span class="comment-age">(06 Dec '17, 07:32)</span> <span class="comment-user userinfo">FM_Pete</span>
</div>
</div>
</div>
<div id="comment-tools-61023" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61023-form-container" class="comment-form-container">
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

<span id="61033"></span>

<div id="answer-container-61033" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61033-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To just retrieve highways, add a rule for that. In the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL">QL</a>, <code>way[highway][highway!~"path|track|cycleway|footway"];</code>. The first rule includes all highways, the second rule excludes some of them.</p>
<p>As far as the details, Overpass API is returning all of the tags associated with a given way. Nominatim adds a calculated address, something Overpass API can't do.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '17, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Dec '17, 16:49</strong> </span></p>
</div>
</div>
<div id="comments-container-61033" class="comments-container">
&#10;</div>
<div id="comment-tools-61033" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61033-form-container" class="comment-form-container">
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

