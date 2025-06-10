+++
type = "question"
title = "filter query by total amount of certain locations from same brand"
description = '''edit: I meant overpass not nominatum Hi there, I have a map where I show small locations. In order to do so I send a query to Overpass-api (for example &#x27;amenity=supermarket&#x27;) , then when it gets back I filter out all the big brand names (from a local hand typed array) and display the result on the m...'''
date = "2019-04-15T15:48:00Z"
lastmod = "2019-05-02T08:54:00Z"
weight = 68797
keywords = [ "filter", "query", "tags", "overpass", "poi" ]
aliases = [ "/questions/68797" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [filter query by total amount of certain locations from same brand](/questions/68797/filter-query-by-total-amount-of-certain-locations-from-same-brand)

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
<span id="post-68797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68797-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>edit: I meant overpass not nominatum</p>
<p>Hi there, I have a map where I show small locations. In order to do so I send a query to Overpass-api (for example 'amenity=supermarket') , then when it gets back I filter out all the big brand names (from a local hand typed array) and display the result on the map.</p>
<p>To save time and data usage on both sides it would be great to filter the results on the overpass side before returning the result. For example 'if name and type has more then 10 locations in country x then remove from result'.</p>
<p>My question: is this even possible?</p>
<p>p.s. I know of a 'corporate' or 'chain' tag for shops, but it doesn's seem to be spread much so that's not of use, yet.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '19, 15:48</strong></p>
<img src="https://secure.gravatar.com/avatar/89858e1d0e500ae658bf8cf7fc4964c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tijmenheid&#39;s gravatar image" />
<p><span>tijmenheid</span><br />
<span class="score" title="41 reputation points">41</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tijmenheid has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Apr '19, 12:09</strong> </span></p>
</div>
</div>
<div id="comments-container-68797" class="comments-container">
&#10;</div>
<div id="comment-tools-68797" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68797-form-container" class="comment-form-container">
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

<span id="68973"></span>

<div id="answer-container-68973" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68973-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tijmenheid has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use a query like <a href="https://overpass-turbo.eu/s/Ii9">this one</a>. The parameter for the number of equal named objects is in line 4.</p>
<p>Whether it makes sense if a different question. Note that there are many supermarkets with spelling variants in their name, keeping the less popular spelling variants intact. Or have combined names like "REWE Ihr Kaufpark", thus distinct from "REWE".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '19, 19:01</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-68973" class="comments-container">
<span id="69039"></span>
<div id="comment-69039" class="comment">
<div id="post-69039-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Roland, the 'count' is indeed what I was looking for. (though the example doesn'T seem to work) For now the filtering I do with JS, and some tricks to filter out 'REWE Ihr Kaufpark' were a bit hard in the beginning but got it working now.</p>
</div>
<div id="comment-69039-info" class="comment-info">
<span class="comment-age">(02 May '19, 08:54)</span> <span class="comment-user userinfo">tijmenheid</span>
</div>
</div>
</div>
<div id="comment-tools-68973" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68973-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68801"></span>

<div id="answer-container-68801" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68801-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68801-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-68801-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are not saying what infrastructure you are using (your own instance of Nominatim or some public one) nor if you would be able to change that. But what you are trying to do seems to me to be better served by the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a>. With that you can search for keys (e. g. amenity=supermarket), look in specific areas, count results and add/subtract result sets.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '19, 17:30</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-68801" class="comments-container">
<span id="68807"></span>
<div id="comment-68807" class="comment">
<div id="post-68807-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oops you're right I meant OVerpass-api, just corrected it. Searches work fine, but do you know of a way to filter searches before returning them? (I mean like the example I posted, not the general ones)</p>
</div>
<div id="comment-68807-info" class="comment-info">
<span class="comment-age">(16 Apr '19, 12:12)</span> <span class="comment-user userinfo">tijmenheid</span>
</div>
</div>
<span id="68814"></span>
<div id="comment-68814" class="comment">
<div id="post-68814-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I suggest you look at the language guide and the query examples linked to on the Overpass API page I quoted above. There you find examples of how to count and filter. If you still have issues post the query you are starting with here and someone can give you specific help (too advanced for myself).</p>
</div>
<div id="comment-68814-info" class="comment-info">
<span class="comment-age">(16 Apr '19, 13:58)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="68825"></span>
<div id="comment-68825" class="comment">
<div id="post-68825-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the suggestion TZorn, will take another look, maybe I'll find something to fix it with.</p>
</div>
<div id="comment-68825-info" class="comment-info">
<span class="comment-age">(17 Apr '19, 14:21)</span> <span class="comment-user userinfo">tijmenheid</span>
</div>
</div>
</div>
<div id="comment-tools-68801" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68801-form-container" class="comment-form-container">
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

