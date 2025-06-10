+++
type = "question"
title = "Nominatim &amp; osmnx: Looking for cities Aarau &amp; Fribourg, getting &quot;City Märt&quot; in Aarau and Freiburg City Hotel in Freibug im Breigsau"
description = '''I am coding in Python, using the package osmnx, and in particular the function geocode_to_gdf from osmnx to get the geometry of some cities in Switzerland. If I send the request &quot;Fribourg, Switzerland&quot;, I get the canton as first answer. If I send the request &quot;Aarau, Switzerland&quot;, the risk is to get ...'''
date = "2023-01-24T09:55:00Z"
lastmod = "2023-01-24T11:39:00Z"
weight = 86557
keywords = [ "geometry", "city", "geocoding", "district", "python" ]
aliases = [ "/questions/86557" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim & osmnx: Looking for cities Aarau & Fribourg, getting "City Märt" in Aarau and Freiburg City Hotel in Freibug im Breigsau](/questions/86557/nominatim-osmnx-looking-for-cities-aarau-fribourg-getting-city-mart-in-aarau-and-freiburg-city-hotel-in-freibug-im-breigsau)

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
<span id="post-86557-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86557-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86557-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am coding in Python, using the package <a href="https://osmnx.readthedocs.io/en/stable/">osmnx</a>, and in particular the function <a href="https://osmnx.readthedocs.io/en/stable/osmnx.html?highlight=geocode_to_gdf#osmnx.geocoder.geocode_to_gdf">geocode_to_gdf</a> from osmnx to get the geometry of some cities in Switzerland. If I send the request "Fribourg, Switzerland", I get the canton as first answer. If I send the request "Aarau, Switzerland", the risk is to get the "Bezirk"/district. To avoid these problems, I send the request as a dictionary: "{'city': 'Aarau, Schweiz'}" or "{'city': 'Fribourg'}". Seems safer and is <a href="https://stackoverflow.com/a/54950721/762435">recommended by the author of the osmnx package on Stackoverflow</a>. I have two questions:</p>
<ul>
<li>Why are the results not stable? Depending when I run it and how (in code or in a jupyter notebook), I get different results. "{'city': 'Fribourg'}" sometimes gives as output the city of Fribourg in Switzerland and sometimes "Freiburg City Süd Hotel, 19, Heinrich-von-Stephan-Straße, Unterwiehre-Nord, Wiehre, Freiburg im Breisgau, Baden-Württemberg, 79100, Germany". "{'city': 'Aarau, Schweiz'}" sometimes gives "City Märit, Aarau, Bezirk Aarau, Aargau, 5000, Switzerland".</li>
<li>Why are the results sometimes empty? "{'city': 'Fribourg, Switzerland'}" generates 0 answers. Same with "{'city': 'Fribourg, Schweiz'}", as well as "{'city': 'Fribourg, Suisse'}"</li>
</ul>
<p>I'm not sure if it is more a question about the data structure in OSM, or a question regarding the package osmnx.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geometry" rel="tag" title="see questions tagged &#39;geometry&#39;">geometry</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-district" rel="tag" title="see questions tagged &#39;district&#39;">district</span> <span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jan '23, 09:55</strong></p>
<img src="https://secure.gravatar.com/avatar/65da3e87020b1932ba6fc144a74394f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="antonind&#39;s gravatar image" />
<p><span>antonind</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="antonind has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86557" class="comments-container">
&#10;</div>
<div id="comment-tools-86557" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86557-form-container" class="comment-form-container">
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

<span id="86558"></span>

<div id="answer-container-86558" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86558-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="antonind has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sth. like</p>
<pre><code>&quot;{&#39;city&#39;: &#39;Fribourg, Suisse&#39;}&quot;</code></pre>
<p>is semantically wrong, you should use:</p>
<pre><code>&quot;{&#39;city&#39;: &#39;Fribourg&#39;,&#39;country&#39;: &#39;Suisse&#39;}&quot;</code></pre>
<p>If you only need results from Switzerland, I would also recommend to include <code>'countrycodes': 'ch'</code>.</p>
<p>If you still get different results for the same request, please trace you requests and check the Nominatim instance that is responding to your requests (e.g. IP address of the responder). Do they differ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jan '23, 11:39</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jan '23, 11:47</strong> </span></p>
</div>
</div>
<div id="comments-container-86558" class="comments-container">
&#10;</div>
<div id="comment-tools-86558" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86558-form-container" class="comment-form-container">
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

