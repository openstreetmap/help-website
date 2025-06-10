+++
type = "question"
title = "Walgreens buildings with separate pharmacy nodes"
description = '''In Portland, most Walgreens stores have tags on the building with a separate node for the pharmacy counter. This seems wrong to me, and makes each store show up twice in search results. Most of the pharmacy tags are duplicates (address, phone, etc.) but have different opening hours. How could I tag ...'''
date = "2019-05-08T10:33:00Z"
lastmod = "2019-09-19T01:18:00Z"
weight = 69123
keywords = [ "opening_hours", "duplicate", "store" ]
aliases = [ "/questions/69123" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Walgreens buildings with separate pharmacy nodes](/questions/69123/walgreens-buildings-with-separate-pharmacy-nodes)

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
<span id="post-69123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69123-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In Portland, most Walgreens stores have tags on the building with a separate node for the pharmacy counter. This seems wrong to me, and makes each store show up twice in search results. Most of the pharmacy tags are duplicates (address, phone, etc.) but have different opening hours. How could I tag the building with pharmacy hours while preserving the store hours so I can remove the extra nodes? Or is there a better way to deal with this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-opening_hours" rel="tag" title="see questions tagged &#39;opening_hours&#39;">opening_hours</span> <span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-store" rel="tag" title="see questions tagged &#39;store&#39;">store</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 May '19, 10:33</strong></p>
<img src="https://secure.gravatar.com/avatar/6203fe5d1e41fd2c3f1c1354049b3efc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tguen&#39;s gravatar image" />
<p><span>tguen</span><br />
<span class="score" title="141 reputation points">141</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tguen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69123" class="comments-container">
&#10;</div>
<div id="comment-tools-69123" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69123-form-container" class="comment-form-container">
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

<span id="70838"></span>

<div id="answer-container-70838" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70838-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70838-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70838-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tguen has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When pharmacies have differing info -- name, operator, phone, or opening hours -- I tend to map them as separate nodes inside the enclosing shop (which can either be an entire building or just a closed way indicating the shop footprint, if it doesn't occupy the entire building.) The node gets the <code>amenity=pharmacy</code> tag (which is being transitioned to <code>healthcare=pharmacy</code>, so usually both.) The enclosing shop will generally be <code>shop=chemist</code>, <code>shop=convenience</code>, or <code>shop=supermarket</code>.)</p>
<p>Other mappers have approached this situation differently, of course. You may see tags like <code>pharmacy:operator</code>, <code>pharmacy:phone</code> etc. invented to shoehorn all the data into a single element. I've also often seen, for example, <code>opening_hours=24/7 "store"||Mo-Fr 08:00-21:00; Sa 09:00-18:00 "pharmacy"</code>.</p>
<p>It really comes down to the question of how to best encode the information so it's least ambiguous and most useful. There's no clear answer at the moment, but my gut tells me that both human readers and software are more likely to successfully parse the data when the pharmacies are mapped as separate nodes. And I've never mapped in Portland, so obviously others have come to this same conclusion.</p>
<p>By the way, it's reasonably common to have a Walgreens Pharmacy inside a shop that is not a Walgreens. Here's a particularly surprising one is inside a Rite Aid: <a href="https://www.openstreetmap.org/node/5827855718">https://www.openstreetmap.org/node/5827855718</a></p>
<p>Many people would probably think that Rite Aid <em>is</em> a pharmacy, but in this case it isn't. It's good to occasionally question your idea of what a particular brand is. The scope of we call "drug stores" in the USA has gradually shifted over the years. Often toys, groceries, and drinks occupy just as much shelf space as medicine and beauty products. So my recommendation is to tag what the shop actually is, rather than what the brand suggests it ought to be.</p>
<p>Anyway, back on topic, I don't consider using separate nodes for the pharmacies to be an error. I'd recommend just leaving them alone, since there's a general ethic to respect previous mappers' work unless it's erroneous or deprecated (see <a href="https://help.openstreetmap.org/questions/69363/rule-about-discouraging-remapping">https://help.openstreetmap.org/questions/69363/rule-about-discouraging-remapping</a> for a discussion of that topic.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Sep '19, 01:18</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-70838" class="comments-container">
&#10;</div>
<div id="comment-tools-70838" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70838-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69127"></span>

<div id="answer-container-69127" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69127-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69127-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69127-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How to do shops within shops is still debated, but most would agree there should not be both.</p>
<p>Having a node within the building outline of the store allows tags like opening_hours to be specific. You can also place the node in the correct area of the store, which could help with directions or locating it (e.g. it's at the back of the store, or go in and it's to the right). For this, you can also make sure entrances are mapped (a node that forms part of the building outline to be tagged with entrance=main or entrance=yes).</p>
<p>Adding the tags to the building (and store) allows us to simply ask: Does this Walgreens have a pharmacy? List all Walgreens with pharmacies. However being a little bit more sophisticated it would still be possible to look at the geometry of the building and see what nodes are within it.</p>
<p>A third option might be to have a relation that specifically links the Pharmacy node and the Walgreens area. There isn't such a relation schema for that, and I'm not aware of any in use. The closest might be the <a href="https://wiki.openstreetmap.org/wiki/Relations/Proposed/Site">type=site</a> relation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 May '19, 11:51</strong></p>
<img src="https://secure.gravatar.com/avatar/f846f21cfbcf60a35e1f69c2cc74df77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LivingWithDragons&#39;s gravatar image" />
<p><span>LivingWithDr...</span><br />
<span class="score" title="524 reputation points">524</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LivingWithDragons has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-69127" class="comments-container">
<span id="69155"></span>
<div id="comment-69155" class="comment">
<div id="post-69155-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think there is a clue here, in that a Walgreens building (or single address) contains more than one map-able entity. In contains a pharmacy, a variety store, and (in a few situations) a minimal clinic. Each may have it's own hours and contact information. In effect, it is a micro-mall names 'Walgreens'. A similar argument could be made for a Wal-Mart which contains variety, pharmacy, a liquor store, a hair salon, an optician, and an automotive department, all at the same address and under the same roof. A car dealership might have sales, parts, service, and body shop. Once again, all at the same address, but with different phone numbers. It is a common problem in an evolving marketplace.</p>
</div>
<div id="comment-69155-info" class="comment-info">
<span class="comment-age">(10 May '19, 14:46)</span> <span class="comment-user userinfo">NitaRae</span>
</div>
</div>
<span id="70783"></span>
<div id="comment-70783" class="comment">
<div id="post-70783-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Every Walgreen’s has a pharmacy. In fact, the chain is considered a pharmacy, even though it has diversified a bit over the years.</p>
</div>
<div id="comment-70783-info" class="comment-info">
<span class="comment-age">(15 Sep '19, 02:05)</span> <span class="comment-user userinfo">Happy Hobo</span>
</div>
</div>
</div>
<div id="comment-tools-69127" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69127-form-container" class="comment-form-container">
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

