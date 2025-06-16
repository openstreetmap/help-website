+++
type = "question"
title = "geocoding Latitude and Longitude registering"
description = '''hi can some body help me? I need to extract a specific road or highway gps data (Latitude and Longitude)from(openstreetmap)is it possible to extract these informations from it? I will appreciate your help'''
date = "2014-07-21T09:42:00Z"
lastmod = "2014-07-30T14:45:00Z"
weight = 35039
keywords = [ "geocoding" ]
aliases = [ "/questions/35039" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [geocoding Latitude and Longitude registering](/questions/35039/geocoding-latitude-and-longitude-registering)

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
<span id="post-35039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35039-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi can some body help me? I need to extract a specific road or highway gps data (Latitude and Longitude)from(openstreetmap)is it possible to extract these informations from it? I will appreciate your help</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '14, 09:42</strong></p>
<img src="https://secure.gravatar.com/avatar/65419f05b3e3ab9ec50bc296b1c92887?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="backtome&#39;s gravatar image" />
<p><span>backtome</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="backtome has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jul '14, 07:45</strong> </span></p>
</div>
</div>
<div id="comments-container-35039" class="comments-container">
<span id="35040"></span>
<div id="comment-35040" class="comment">
<div id="post-35040-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Would it be possible to add a bit more information about what you're trying to do? Are you trying to add data to OpenStreetMap, retrieve data from it, or do something else?</p>
<p>Also - don't feel that you have to ask in English - there are lots of people who speak many languages here.</p>
</div>
<div id="comment-35040-info" class="comment-info">
<span class="comment-age">(21 Jul '14, 09:45)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-35039" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35039-form-container" class="comment-form-container">
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

<span id="35210"></span>

<div id="answer-container-35210" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35210-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First, if you've not seen it already, have a read of <a href="https://wiki.openstreetmap.org/wiki/Beginners_Guide_1.3">this section</a> of the beginners' guide in the OpenStreetMap wiki - it explains the sorts of data that you'll find in OSM.</p>
<p>One of the sorts of data that that page refers to is a "way" - a list of OSM "nodes". Each OSM node has a latitude and longitude value. A street may consist of several ways (if you look at <a href="https://www.openstreetmap.org/node/300457718">this node</a> you'll see that it is part of three ways with the same name - one single carriageway part and two ways each forming half of a dual carriageway) so you'll probably want to select ways by name</p>
<p>How you search for things by name depends on how much data you want. If you just want one specific road then <a href="http://overpass-turbo.eu/">Overpass Turbo</a> might be an option - browse to an area of interest and use a query like this:</p>
<pre><code>&lt;osm-script output=&quot;json&quot; timeout=&quot;25&quot;&gt;
  &lt;!-- gather results --&gt;
  &lt;union&gt;
    &lt;query type=&quot;way&quot;&gt;
      &lt;has-kv k=&quot;name&quot; v=&quot;Rosemary Street&quot;/&gt;
      &lt;bbox-query {{bbox}}/&gt;
    &lt;/query&gt;
  &lt;/union&gt;
  &lt;!-- print results --&gt;
  &lt;print mode=&quot;body&quot;/&gt;
  &lt;recurse type=&quot;down&quot;/&gt;
  &lt;print mode=&quot;skeleton&quot; order=&quot;quadtile&quot;/&gt;
&lt;/osm-script&gt;</code></pre>
<p>If you want more data, then you'll want to download an extract of the OSM for your area (use one of the "extract" links from <a href="http://planet.openstreetmap.org/">here</a>) and then extract data from it, perhaps as described in <a href="/questions/9816/the-best-way-to-extract-street-list">this question</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jul '14, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-35210" class="comments-container">
<span id="35313"></span>
<div id="comment-35313" class="comment">
<div id="post-35313-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>thank you for your helpful answer</p>
</div>
<div id="comment-35313-info" class="comment-info">
<span class="comment-age">(30 Jul '14, 14:45)</span> <span class="comment-user userinfo">backtome</span>
</div>
</div>
</div>
<div id="comment-tools-35210" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35210-form-container" class="comment-form-container">
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

