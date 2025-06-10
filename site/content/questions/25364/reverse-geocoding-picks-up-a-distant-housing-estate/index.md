+++
type = "question"
title = "Reverse geocoding picks up a distant housing estate"
description = '''Hi, I&#x27;m just getting to grips with editing and this is too hard for me right now.  Search for &#x27;Bushey Hill Road SE5 UK&#x27; yields on OSM Nominatim &#x27;Bushey Hill Road, Champion Hill Estate, Camberwell, London Borough of Southwark, London, Greater London, England, SE5, United Kingdom, European Union&#x27; whic...'''
date = "2013-08-14T13:09:00Z"
lastmod = "2013-08-14T18:56:00Z"
weight = 25364
keywords = [ "incorrect", "nominatim", "geocoding", "reverse", "address" ]
aliases = [ "/questions/25364" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reverse geocoding picks up a distant housing estate](/questions/25364/reverse-geocoding-picks-up-a-distant-housing-estate)

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
<span id="post-25364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25364-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-25364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm just getting to grips with editing and this is too hard for me right now.</p>
<p>Search for 'Bushey Hill Road SE5 UK' yields on OSM Nominatim 'Bushey Hill Road, Champion Hill Estate, Camberwell, London Borough of Southwark, London, Greater London, England, SE5, United Kingdom, European Union' which is all correct except for Champion Hill Estate. In fact large parts of my local area show Champion Hill Estate which is a very small estate in fact. The estate is actually bounded by Champion Hill (N) between intersection nodes 70723150 and 1594723995, and the area S and E of estate road bounded by Dog Kennel Hill and Dog Kennel Open Space.</p>
<p>Presumably if the Champion Hill Estate can be confined to these limits then the rest of Camberwell will get the right address.</p>
<p>I'd like to know how to correct this, though I'm hoping someone else will do it and tell what they did!</p>
<p>Regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-incorrect" rel="tag" title="see questions tagged &#39;incorrect&#39;">incorrect</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-reverse" rel="tag" title="see questions tagged &#39;reverse&#39;">reverse</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '13, 13:09</strong></p>
<img src="https://secure.gravatar.com/avatar/500f3573bb1c6069343eeece9b384196?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul5730&#39;s gravatar image" />
<p><span>Paul5730</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul5730 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-25364" class="comments-container">
&#10;</div>
<div id="comment-tools-25364" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25364-form-container" class="comment-form-container">
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

<span id="25365"></span>

<div id="answer-container-25365" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25365-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-25365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Go to <a href="http://nominatim.openstreetmap.org/">nominatim.openstreetmap.org</a>, enter your search query and click on "<em>(details)</em>" on the result your are interested in. For <a href="http://nominatim.openstreetmap.org/search.php?q=Bushey+Hill+Road+SE5+UK">Bushey Hill Road SE5 UK</a> this will be <a href="http://nominatim.openstreetmap.org/details.php?place_id=20806299">this page</a>. Here Nominatim presents you its internal view on the specific place including a hierarchic representation of the address. Inside this hierarchy you will find the <a href="http://www.openstreetmap.org/browse/node/70740565">node Champion Hill Estate</a>. Because <em>Champion Hill Estate</em> is only a node, Nominatim has to <em>estimate</em> how large this area is. Obviously this estimation won't be correct most of the time.</p>
<p>If you want to fix this you can replace the Champion Hill Estate <em>node</em> with an <em>area</em> having the same tags. This area doesn't necessarily have to be 100% correct but with the help of some local knowledge you will be able to make a better estimation than Nominatim can.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '13, 13:35</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-25365" class="comments-container">
<span id="25369"></span>
<div id="comment-25369" class="comment">
<div id="post-25369-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I've created an area, I needed to use iD rather than potlatch which made it easy. I'll figure out how to give the area tags in a minute. I don't see how to delete the node however?</p>
</div>
<div id="comment-25369-info" class="comment-info">
<span class="comment-age">(14 Aug '13, 14:15)</span> <span class="comment-user userinfo">Paul5730</span>
</div>
</div>
<span id="25370"></span>
<div id="comment-25370" class="comment">
<div id="post-25370-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just <a href="http://www.openstreetmap.org/edit?editor=id&amp;node=70740565">open the node in iD</a>, click on it and choose the trash icon.</p>
</div>
<div id="comment-25370-info" class="comment-info">
<span class="comment-age">(14 Aug '13, 14:18)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="25371"></span>
<div id="comment-25371" class="comment">
<div id="post-25371-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I deleted all the node tags and that seems to have done the trick. And the area selects correctly in search, and nearby locations no longer erroneously appear to be part of the estate.</p>
<p>Fantastic!</p>
<p>Many thanks.</p>
</div>
<div id="comment-25371-info" class="comment-info">
<span class="comment-age">(14 Aug '13, 14:23)</span> <span class="comment-user userinfo">Paul5730</span>
</div>
</div>
<span id="25372"></span>
<div id="comment-25372" class="comment">
<div id="post-25372-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Great! But the node <a href="http://www.openstreetmap.org/browse/node/70740565">still exists</a>. Deleting all tags doesn't delete the object. Also the tag of the <a href="http://www.openstreetmap.org/browse/way/233513215">new area</a> is slightly wrong, instead of "place=housing_estate" you used "place=Housing Estate" (capitalization and whitespace instead of underscore). This won't work correctly.</p>
</div>
<div id="comment-25372-info" class="comment-info">
<span class="comment-age">(14 Aug '13, 15:09)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="25374"></span>
<div id="comment-25374" class="comment">
<div id="post-25374-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>place=housing_estate is not the correct tag anyway (I'm surprised that Nominatim actually used it). It should be place=suburb or place=neighbourhood</p>
</div>
<div id="comment-25374-info" class="comment-info">
<span class="comment-age">(14 Aug '13, 15:25)</span> <span class="comment-user userinfo">Vclaw</span>
</div>
</div>
<span id="25381"></span>
<div id="comment-25381" class="comment not_top_scorer">
<div id="post-25381-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I dont know about 'correct' tags, the reality is that Nominatim places undue emphasis on place tags it is not familiar with. It would be better practice for such tags to be given an index value which placed them more locally.</p>
</div>
<div id="comment-25381-info" class="comment-info">
<span class="comment-age">(14 Aug '13, 18:56)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-25365" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-25365-form-container" class="comment-form-container">
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

