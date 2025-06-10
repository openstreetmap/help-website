+++
type = "question"
title = "why overpass API can not find my search ?"
description = '''I have 50 rows dataset, and &#x27;m trying to match those locations with OSM data. I want to have info such as polygon, lat&amp;amp;long, housenumber, street etc (whatever it has) from OSM. One of my location Moncoeur Belleville in France. As you can see in the link, there is information about the place with...'''
date = "2019-07-08T12:04:00Z"
lastmod = "2019-07-09T11:17:00Z"
weight = 69925
keywords = [ "pyhton", "overpass", "overpassapi", "osmapi_python", "api" ]
aliases = [ "/questions/69925" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [why overpass API can not find my search ?](/questions/69925/why-overpass-api-can-not-find-my-search)

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
<span id="post-69925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69925-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have 50 rows dataset, and 'm trying to match those locations with OSM data. I want to have info such as polygon, lat&amp;long, housenumber, street etc (whatever it has) from OSM. One of my location <a href="https://www.openstreetmap.org/node/446868082#map=19/48.87163/2.38586">Moncoeur Belleville</a> in France. As you can see in the link, there is information about the place with node number: 446868082 When I search based on OsmApi with node number, I got the output that I want to take.</p>
<pre><code>from osmapi import OsmApi
MyApi = OsmApi()
MyApi.NodeGet(446868082)</code></pre>
<p>output:</p>
<pre><code>{&#39;id&#39;: 446868082,
 &#39;visible&#39;: True,
 &#39;version&#39;: 7,
 &#39;changeset&#39;: 67256996,
 &#39;timestamp&#39;: datetime.datetime(2019, 2, 16, 16, 16, 53),
 &#39;user&#39;: &#39;Britzz&#39;,
 &#39;uid&#39;: 7550430,
 &#39;lat&#39;: 48.8716239,
 &#39;lon&#39;: 2.3858689,
 &#39;tag&#39;: {&#39;addr:city&#39;: &#39;Paris&#39;,
  &#39;addr:housenumber&#39;: &#39;1&#39;,
  &#39;addr:postcode&#39;: &#39;75020&#39;,
  &#39;addr:street&#39;: &#39;Rue des Envierges&#39;,
  &#39;amenity&#39;: &#39;cafe&#39;,
  &#39;internet_access&#39;: &#39;wlan&#39;,
  &#39;name&#39;: &#39;Moncœur Belleville&#39;,
  &#39;old_name&#39;: &quot;O&#39;Paris&quot;,
  &#39;opening_hours&#39;: &#39;Mo-Su 10:00-02:00&#39;,
  &#39;outdoor_seating&#39;: &#39;yes&#39;,
  &#39;phone&#39;: &#39;+33 1 43 66 38 54&#39;,
  &#39;website&#39;: &#39;http://moncoeurbelleville.com/&#39;}}</code></pre>
<p>However, If I made a search based on the overpass, this place can not found. I tried a varios different combination for my search :</p>
<pre><code>first_search = api.get(&#39;way[&quot;name&quot;=&quot;Moncoeur Belleville&quot;]&#39;, verbosity=&#39;geom&#39;)
print(first_search)
out: {&quot;features&quot;: [], &quot;type&quot;: &quot;FeatureCollection&quot;}
&#10;second_search = api.get(&#39;way(around:100.0, 48.8716239, 2.3858689)&#39;, verbosity=&#39;geom&#39;)
&#10;third_search = api.get(&#39;node[&quot;name&quot;=&quot;Moncoeur Belleville&quot;]&#39;)
out: {&quot;features&quot;: [], &quot;type&quot;: &quot;FeatureCollection&quot;}</code></pre>
<p>In the second search, many places found however none of them are Moncoeur Belleville. So may I learn why I can't find this location using Overpass? I'm asking this cause I don't think it is a good idea to check each time this kind of location's node number from OSM map. That's why I believe I need to use overpass API.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pyhton" rel="tag" title="see questions tagged &#39;pyhton&#39;">pyhton</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-osmapi_python" rel="tag" title="see questions tagged &#39;osmapi_python&#39;">osmapi_python</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jul '19, 12:04</strong></p>
<img src="https://secure.gravatar.com/avatar/855cd4bb720f760e72b5b9f349e209af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="donniedarko123&#39;s gravatar image" />
<p><span>donniedarko123</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="donniedarko123 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jul '19, 15:33</strong> </span></p>
</div>
</div>
<div id="comments-container-69925" class="comments-container">
&#10;</div>
<div id="comment-tools-69925" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69925-form-container" class="comment-form-container">
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

<span id="69926"></span>

<div id="answer-container-69926" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69926-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The spelling of the place isn't what you'd expect - have a look at <a href="https://overpass-turbo.eu/s/KyM">https://overpass-turbo.eu/s/KyM</a> (which does find it) and you can see that the "œ" is written as one character not two.</p>
<p>Whether Overpass should be expected to understand this is a different question - if you edit the query <a href="https://overpass-turbo.eu/s/KyN">https://overpass-turbo.eu/s/KyN</a> to contain "ss" it doesn't work, so it doesn't do automatic ss / eszett translation (and I can understand why that decision was made).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '19, 12:12</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jul '19, 12:17</strong> </span></p>
</div>
</div>
<div id="comments-container-69926" class="comments-container">
<span id="69928"></span>
<div id="comment-69928" class="comment">
<div id="post-69928-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I understand it makes sense. However, if I make a search based on lat&amp;long (see in my second_search), not name or address, still this place cannot be found. In my example above, I searched for 100, and just now I increased to 400, and I printed whole places around 400meters based this lat&amp;long, but still, this place is not in the list. I don't think it is a matter of character situation only.</p>
</div>
<div id="comment-69928-info" class="comment-info">
<span class="comment-age">(08 Jul '19, 12:19)</span> <span class="comment-user userinfo">donniedarko123</span>
</div>
</div>
<span id="69929"></span>
<div id="comment-69929" class="comment">
<div id="post-69929-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It's a node. You are searching for ways only.</p>
</div>
<div id="comment-69929-info" class="comment-info">
<span class="comment-age">(08 Jul '19, 13:16)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="69932"></span>
<div id="comment-69932" class="comment">
<div id="post-69932-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, now I ve edited my question. as you can see above at my third_search, I made a search with node, however, I got nothing. But I changed as "Moncœur Belleville" as <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> warned me. And I got the node info. Thank you. Is there any way to search the node using lat&amp;long?</p>
</div>
<div id="comment-69932-info" class="comment-info">
<span class="comment-age">(08 Jul '19, 15:42)</span> <span class="comment-user userinfo">donniedarko123</span>
</div>
</div>
<span id="69934"></span>
<div id="comment-69934" class="comment">
<div id="post-69934-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Edit the lat/long search to search for nodes instead of ways.</p>
<p><a href="https://overpass-turbo.eu/s/Kzo">https://overpass-turbo.eu/s/Kzo</a></p>
</div>
<div id="comment-69934-info" class="comment-info">
<span class="comment-age">(08 Jul '19, 16:23)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="69945"></span>
<div id="comment-69945" class="comment">
<div id="post-69945-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a> it works, many thanks</p>
</div>
<div id="comment-69945-info" class="comment-info">
<span class="comment-age">(09 Jul '19, 11:17)</span> <span class="comment-user userinfo">donniedarko123</span>
</div>
</div>
</div>
<div id="comment-tools-69926" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69926-form-container" class="comment-form-container">
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

