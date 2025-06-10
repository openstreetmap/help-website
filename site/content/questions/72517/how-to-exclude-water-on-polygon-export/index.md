+++
type = "question"
title = "How to exclude water on polygon export?"
description = '''Hi to all, my request;  var request = $&quot;https://nominatim.openstreetmap.org/reverse?q=&amp;amp;polygon_kml=1&amp;amp;format=xml&quot; + $&quot;&amp;amp;place_id={feature.properties.place_id}&quot; + $&quot;&amp;amp;osm_id={feature.properties.osm_id}&quot; + $&quot;&amp;amp;lat={feature.geometry.coordinates[1].ToString(CultureInfo.InvariantCulture)....'''
date = "2020-01-16T09:37:00Z"
lastmod = "2020-01-17T12:46:00Z"
weight = 72517
keywords = [ "water", "exclude", "nominatim" ]
aliases = [ "/questions/72517" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to exclude water on polygon export?](/questions/72517/how-to-exclude-water-on-polygon-export)

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
<span id="post-72517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72517-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi to all, my request; <img src="https://image.prntscr.com/image/VEOTRIS0TNi7jFf80-FJJg.png" alt="alt text" /></p>
<pre><code>var request = $&quot;https://nominatim.openstreetmap.org/reverse?q=&amp;polygon_kml=1&amp;format=xml&quot; + $&quot;&amp;place_id={feature.properties.place_id}&quot; + $&quot;&amp;osm_id={feature.properties.osm_id}&quot; + $&quot;&amp;lat={feature.geometry.coordinates[1].ToString(CultureInfo.InvariantCulture).Replace(&quot;,&quot;, &quot;.&quot;)}&quot; + $&quot;&amp;lon={feature.geometry.coordinates[0].ToString(CultureInfo.InvariantCulture).Replace(&quot;,&quot;, &quot;.&quot;)}&amp;class=boundary&amp;type=administrative&amp;osm_type=R&quot;;</code></pre>
<p>And my output kml is; <img src="https://i.ibb.co/80JtYKM/ss2.png" alt="alt text" /></p>
<p>But i wan't without water like this; <img src="https://i.ibb.co/sFWtwDz/ss1.png" alt="alt text" /></p>
<p>How can i request a polygon area without water?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-exclude" rel="tag" title="see questions tagged &#39;exclude&#39;">exclude</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jan '20, 09:37</strong></p>
<img src="https://secure.gravatar.com/avatar/6759a38600f93a4633ede907070deda3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="roslyncompiler&#39;s gravatar image" />
<p><span>roslyncompiler</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="roslyncompiler has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jan '20, 09:01</strong> </span></p>
</div>
</div>
<div id="comments-container-72517" class="comments-container">
<span id="72521"></span>
<div id="comment-72521" class="comment">
<div id="post-72521-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm afraid your links haven't worked. Perhaps you could update the question to provide them.</p>
</div>
<div id="comment-72521-info" class="comment-info">
<span class="comment-age">(16 Jan '20, 13:13)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="72546"></span>
<div id="comment-72546" class="comment">
<div id="post-72546-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which links? Screenshots? This is the request;</p>
<p>var request = $"https://nominatim.openstreetmap.org/reverse?q=&amp;polygon_kml=1&amp;format=xml" + $"&amp;place_id={feature.properties.place_id}" + $"&amp;osm_id={feature.properties.osm_id}" + $"&amp;lat={feature.geometry.coordinates[1].ToString(CultureInfo.InvariantCulture).Replace(",", ".")}" + $"&amp;lon={feature.geometry.coordinates[0].ToString(CultureInfo.InvariantCulture).Replace(",", ".")}&amp;class=boundary&amp;type=administrative&amp;osm_type=R";</p>
</div>
<div id="comment-72546-info" class="comment-info">
<span class="comment-age">(17 Jan '20, 08:43)</span> <span class="comment-user userinfo">roslyncompiler</span>
</div>
</div>
<span id="72549"></span>
<div id="comment-72549" class="comment">
<div id="post-72549-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The image hoster seems to be a bit unreliable. Reloading the images a couple of times made them show up here.</p>
</div>
<div id="comment-72549-info" class="comment-info">
<span class="comment-age">(17 Jan '20, 08:48)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="72550"></span>
<div id="comment-72550" class="comment">
<div id="post-72550-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've changed to host. Sorry about that.</p>
</div>
<div id="comment-72550-info" class="comment-info">
<span class="comment-age">(17 Jan '20, 08:56)</span> <span class="comment-user userinfo">roslyncompiler</span>
</div>
</div>
</div>
<div id="comment-tools-72517" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72517-form-container" class="comment-form-container">
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

<span id="72522"></span>

<div id="answer-container-72522" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72522-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim can't do that. (The /reverse endpoint also doesn't support the <code>place_id</code>, <code>osm_type</code>, <code>osm_id</code>, <code>class</code> and <code>type</code> you're sending.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jan '20, 13:38</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</img>
</div>
</div>
<div id="comments-container-72522" class="comments-container">
<span id="72547"></span>
<div id="comment-72547" class="comment">
<div id="post-72547-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So just to make sure, are there no way get only land area in nominatim?</p>
</div>
<div id="comment-72547-info" class="comment-info">
<span class="comment-age">(17 Jan '20, 08:45)</span> <span class="comment-user userinfo">roslyncompiler</span>
</div>
</div>
<span id="72558"></span>
<div id="comment-72558" class="comment">
<div id="post-72558-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, no way. Nominatim only returns places from the OSM data, it doesn't change the boundaries/polygons.</p>
</div>
<div id="comment-72558-info" class="comment-info">
<span class="comment-age">(17 Jan '20, 12:46)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-72522" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72522-form-container" class="comment-form-container">
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

