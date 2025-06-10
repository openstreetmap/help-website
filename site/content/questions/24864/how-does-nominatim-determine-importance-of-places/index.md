+++
type = "question"
title = "How does Nominatim determine importance of places?"
description = '''I&#x27;m using Nominatim to reverse-geocode natural language location descriptions for a research project. I spent some time looking through the source code (in particular, website/search.php), but I can&#x27;t seem to make heads or tails of how the &quot;importance&quot; score is calculated.  From what I can tell, the...'''
date = "2013-08-03T16:36:00Z"
lastmod = "2018-12-04T14:10:00Z"
weight = 24864
keywords = [ "importance", "ranking", "nominatim" ]
aliases = [ "/questions/24864" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How does Nominatim determine importance of places?](/questions/24864/how-does-nominatim-determine-importance-of-places)

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
<span id="post-24864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24864-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using Nominatim to reverse-geocode natural language location descriptions for a research project. I spent some time looking through the source code (in particular, website/search.php), but I can't seem to make heads or tails of how the "importance" score is calculated.<br />
</p>
<p>From what I can tell, there is some baseline calculation and then numerous tweaks - one line, for example, says</p>
<p><code>$aResult['importance'] = $aResult['importance'] + ($iCountWords*0.1); // 0.1 is a completely arbitrary number but something in the range 0.1 to 0.5 would seem right</code></p>
<p>I also noticed in the documentation that Nominatim will use Wikipedia to improve the ranking of results, but once again nothing specific beyond "the importance value is calculated as log(totalcount)/log(max totalcount)." I assume that "totalcount" is the number of internal links to an article about a specific location in the result set, and "max totalcount" is the maximum of that value across the entire result set. But this only tells me the scoring contribution from Wikipedia, and not how the baseline score is calculated.</p>
<p>My question is, what properties of the OSM data go into the calculation, and then how is the importance score actually calculated? What special tweaks and thresholds should I be aware of?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-importance" rel="tag" title="see questions tagged &#39;importance&#39;">importance</span> <span class="post-tag tag-link-ranking" rel="tag" title="see questions tagged &#39;ranking&#39;">ranking</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Aug '13, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/557eff6ea360379b6cf0daac3ea3e2e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aweissman&#39;s gravatar image" />
<p><span>aweissman</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aweissman has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-24864" class="comments-container">
&#10;</div>
<div id="comment-tools-24864" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24864-form-container" class="comment-form-container">
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

<span id="24867"></span>

<div id="answer-container-24867" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24867-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For in-depth technical discussion of nominatim, you'd be better off asking on the geocoding mailing list.</p>
<p><a href="http://lists.openstreetmap.org/listinfo/geocoding">http://lists.openstreetmap.org/listinfo/geocoding</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '13, 18:01</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-24867" class="comments-container">
&#10;</div>
<div id="comment-tools-24867" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24867-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67059"></span>

<div id="answer-container-67059" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67059-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From the mailing list: <a href="https://lists.openstreetmap.org/pipermail/geocoding/2013-August/000916.html">https://lists.openstreetmap.org/pipermail/geocoding/2013-August/000916.html</a></p>
<blockquote>
<p>The major weight of importance comes indeed from the Wikipedia link count. If no article can be found for an object, the base score is based on the object rank (country, county, city, etc.)</p>
<p>There are a few minor tweaks to this wikipedia importance. The one you have found is the reranking by exactness of match with the query (the one you cited above). The more words from the query appear verbatim in the display name (that's the one including the address) of the result, the higher it gets ranked.</p>
<p>The second reranking is related to the viewbox. If you supply a viewbox parameter, then anything within or close to the viewbox is ranked higher. (e.g. <a href="https://github.com/twain47/Nominatim/blob/master/website/search.php#L976)">https://github.com/twain47/Nominatim/blob/master/website/search.php#L976)</a></p>
<p>There is also a small tweak to take the importance of the address members into account but that only has an effect if objects have an equal importance. (e.g. <a href="https://github.com/twain47/Nominatim/blob/master/website/search.php#L1241)">https://github.com/twain47/Nominatim/blob/master/website/search.php#L1241)</a></p>
</blockquote>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Dec '18, 14:10</strong></p>
<img src="https://secure.gravatar.com/avatar/6863bef08c5e0bc17bee1e10c2b56b83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Potdeyaourt&#39;s gravatar image" />
<p><span>Potdeyaourt</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Potdeyaourt has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Dec '18, 14:10</strong> </span></p>
</div>
</div>
<div id="comments-container-67059" class="comments-container">
&#10;</div>
<div id="comment-tools-67059" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67059-form-container" class="comment-form-container">
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

