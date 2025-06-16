+++
type = "question"
title = "Correctly mapping apartment complex"
description = '''I&#x27;m trying to map a residential apartment complex close to me that has the following features:  It&#x27;s a closed area with two addresses/entrances Inside this area there are two independent buildings of different heights. Each one has a name just so you can say &quot;it&#x27;s on building A&quot; but are otherwise re...'''
date = "2019-10-03T19:46:00Z"
lastmod = "2019-10-05T06:40:00Z"
weight = 71024
keywords = [ "building", "addressing", "apartment", "complex", "mapping" ]
aliases = [ "/questions/71024" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Correctly mapping apartment complex](/questions/71024/correctly-mapping-apartment-complex)

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
<span id="post-71024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71024-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to map a residential apartment complex close to me that has the following features:</p>
<ul>
<li>It's a closed area with two addresses/entrances</li>
<li>Inside this area there are two independent buildings of different heights. Each one has a name just so you can say "it's on building A" but are otherwise referenced by the street address of the complex itself</li>
<li>Has a pool in the area</li>
</ul>
<p>The complex looks roughly like this:</p>
<p><img src="/upfiles/pngout.png" alt="alt text" /></p>
<p>My issue is that I found a few posts with instructions on how to map things similar to this, but some were a bit old and seemed to offer conclicting advice. Some questions:</p>
<ul>
<li>What type of area should the outline be? <code>landuse=residential</code>, <code>type=site</code>, <code>building=apartments</code>? What about the multiple entrance/addresses? What kinds of elements are they and what tags should I apply?</li>
<li>Should the buildings themselves be areas with <code>building=apartments</code> tags?</li>
<li>How do I/should I link each of these parts with relations to show that they're part of the same complex?</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-addressing" rel="tag" title="see questions tagged &#39;addressing&#39;">addressing</span> <span class="post-tag tag-link-apartment" rel="tag" title="see questions tagged &#39;apartment&#39;">apartment</span> <span class="post-tag tag-link-complex" rel="tag" title="see questions tagged &#39;complex&#39;">complex</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Oct '19, 19:46</strong></p>
<img src="https://secure.gravatar.com/avatar/69716ae006390622c060f997246cea3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fcoelho&#39;s gravatar image" />
<p><span>fcoelho</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fcoelho has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-71024" class="comments-container">
&#10;</div>
<div id="comment-tools-71024" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71024-form-container" class="comment-form-container">
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

<span id="71033"></span>

<div id="answer-container-71033" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71033-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The two buildings should be building=apartments, yes.</p>
<p>What do you do if you want to send a letter to the residents in either building? What address would you use? I'd put that address also on the building polygons: addr:country, addr:city, addr:postcode, addr:street and addr:housenumber. You can put a ref=A and ref=B on the buildings if there is such simple name. Or name=Building A if it is a more elaborate name, for example West Tower.</p>
<p>The addresses can also be put onto an otherwise empty node at the complex entrances, especially if one of the addresses is not already on one of the buildings.</p>
<p>Usually, the whole surrounding area should have landuse=residential not only this apartment complex (unless of course it is alone inside another type of landuse). If you want to show this complex belongs together you could still use a dedicated landuse=residential for this complex, especially if it has a common name, other than the address ("I live in the South Park Residences."). If the whole complex is fenced you could also map the fence and the gates.</p>
<p>The type=site is only used on relations. I probably wouldn't use a site relation here, since everything is grouped together and not dispersed over a wider area.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '19, 13:35</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-71033" class="comments-container">
<span id="71035"></span>
<div id="comment-71035" class="comment">
<div id="post-71035-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that there are some regional differences for the address information, typically in Belgium you do not put the country, city not postcode on the address-nodes/buildings. In The Netherlands and Denmark, addresses have to be mapped as points. I believe the same is true for Italy, where addresses belong to doors.</p>
</div>
<div id="comment-71035-info" class="comment-info">
<span class="comment-age">(04 Oct '19, 15:33)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="71038"></span>
<div id="comment-71038" class="comment">
<div id="post-71038-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>What address would you use?</p>
</blockquote>
<p>You can use either one and add in the necessary apt number and building as both buildings can have an apartment with the same number, e.g. "123 One Street/Apt 222 building B"</p>
<blockquote>
<p>empty node</p>
</blockquote>
<p>To clarify, an empty node is a point in the editor?</p>
</div>
<div id="comment-71038-info" class="comment-info">
<span class="comment-age">(04 Oct '19, 22:32)</span> <span class="comment-user userinfo">fcoelho</span>
</div>
</div>
<span id="71039"></span>
<div id="comment-71039" class="comment">
<div id="post-71039-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So the same apartment could be referenced by both "123 One Street/Apt 222 building B" and "321 Two Street/Apt 222 building B"? I don't know what country this is in, but that seems like it could get very confusing.</p>
</div>
<div id="comment-71039-info" class="comment-info">
<span class="comment-age">(04 Oct '19, 23:24)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="71040"></span>
<div id="comment-71040" class="comment">
<div id="post-71040-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>By empty node I meant a point in the editor that carries no other tags except the address. But as Escada pointed out the address could also be added to an entrance.</p>
</div>
<div id="comment-71040-info" class="comment-info">
<span class="comment-age">(05 Oct '19, 06:40)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-71033" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71033-form-container" class="comment-form-container">
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

