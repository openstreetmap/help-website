+++
type = "question"
title = "Overpass API : Supermarkets - slow queries"
description = '''I have two requests to get supermarkets within a country but both are slow and I&#x27;m asking myself if there is a way to improve them. The first query is used to get supermarkets in France only, within a radius of 2 kilometers around the coordinates provided : [out:json][timeout:25];  area(3602202162)-...'''
date = "2019-08-13T15:21:00Z"
lastmod = "2019-08-19T18:04:00Z"
weight = 70369
keywords = [ "shop", "country", "overpass-turbo", "supermarket" ]
aliases = [ "/questions/70369" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API : Supermarkets - slow queries](/questions/70369/overpass-api-supermarkets-slow-queries)

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
<span id="post-70369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70369-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have two requests to get supermarkets within a country but both are slow and I'm asking myself if there is a way to improve them.</p>
<p>The first query is used to get supermarkets in France only, within a radius of 2 kilometers around the coordinates provided :</p>
<pre><code>[out:json][timeout:25];
&#10;area(3602202162)-&gt;.searchArea;
(
  nwr[&quot;shop&quot;=&quot;supermarket&quot;](around:2000,48.8534,2.3488)(area.searchArea);
);
&#10;out;</code></pre>
<p>(In this example, the coordinates correspond to the location of Paris).</p>
<p>For the second request, I want to obtain supermarkets in France only as well but sorted by brand and city. Currently, I use the query below to get all the supermarkets in a given city (but it's not limited to France). After my request, I sort the results by brand in my code.</p>
<pre><code>[out:json][timeout:25];
&#10;area[&quot;name&quot;=&quot;Paris&quot;]-&gt;.RESULTS;
(
  nwr[&quot;shop&quot;=&quot;supermarket&quot;](area.RESULTS);
);
&#10;out;</code></pre>
<p>Is it possible to improve both queries and make them faster? I'd also like to limit the second query to France, and why not, if it's more efficient sort the results by brand with the API and not with my code.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shop" rel="tag" title="see questions tagged &#39;shop&#39;">shop</span> <span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-supermarket" rel="tag" title="see questions tagged &#39;supermarket&#39;">supermarket</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Aug '19, 15:21</strong></p>
<img src="https://secure.gravatar.com/avatar/74ae61e8df92de6db79dad4be81051c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arouraz&#39;s gravatar image" />
<p><span>Arouraz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arouraz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Aug '19, 18:06</strong> </span></p>
</div>
</div>
<div id="comments-container-70369" class="comments-container">
<span id="70373"></span>
<div id="comment-70373" class="comment">
<div id="post-70373-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>please note that supermarkets (and POIs in general) can also be mapped as ways or as relations. You have to use 'nwr' instead of 'node'</p>
</div>
<div id="comment-70373-info" class="comment-info">
<span class="comment-age">(14 Aug '19, 04:10)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="70379"></span>
<div id="comment-70379" class="comment">
<div id="post-70379-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I didn't know that, I updated the code, thank you!</p>
</div>
<div id="comment-70379-info" class="comment-info">
<span class="comment-age">(14 Aug '19, 18:08)</span> <span class="comment-user userinfo">Arouraz</span>
</div>
</div>
</div>
<div id="comment-tools-70369" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70369-form-container" class="comment-form-container">
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

<span id="70428"></span>

<div id="answer-container-70428" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70428-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Default timeout value is 180. Setting it to 40 isn't required.</p>
<p>Depending on what you want to do with the output data, converting it to json is often unnecessary.</p>
<p>Quotation marks are only needed when a colon is in the expression.</p>
<p>Specifying France isn't required as the <code>around</code> statement limits the search area.</p>
<p>As there's only one line of code the containing brackets aren't required</p>
<pre><code>nwr[shop=supermarket](around:2000,48.8534,2.3488);
out center;</code></pre>
<p>There's quire a few areas with Paris as it's name. Best to specify a single one. I used this one <a href="https://www.openstreetmap.org/relation/7444,">https://www.openstreetmap.org/relation/7444,</a> If you wish to use another relation, add its id to 3600000000 to get the area id. If you're only using using a single area once, then there's no need to store it in a variable (RESULTS).</p>
<pre><code>area(id:3600007444);
nwr[shop=supermarket](area);
out center;
&#10;rel(id:7444);
out geom;</code></pre>
<p>I think relation 2202162 is the incorrect one to use for mainland France:</p>
<p><a href="https://overpass-turbo.eu/s/LDR">https://overpass-turbo.eu/s/LDR</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '19, 18:04</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Aug '19, 18:13</strong> </span></p>
</div>
</div>
<div id="comments-container-70428" class="comments-container">
&#10;</div>
<div id="comment-tools-70428" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70428-form-container" class="comment-form-container">
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

