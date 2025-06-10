+++
type = "question"
title = "How to tag and structure multi use (foot, bicycle) route relations?"
description = '''I&#x27;ve been having some disagreements about whether or not the Trans-Canada Trail should have a route relation tagged as a bicycle route, as it has had since at least 2011. The argument presented against it, is that it is not exclusively for bicycle use, and some sections are not for bicycle use at al...'''
date = "2020-08-17T19:06:00Z"
lastmod = "2020-08-18T17:38:00Z"
weight = 76170
keywords = [ "multi-use", "route", "bicycle", "tagging", "relations" ]
aliases = [ "/questions/76170" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag and structure multi use (foot, bicycle) route relations?](/questions/76170/how-to-tag-and-structure-multi-use-foot-bicycle-route-relations)

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
<span id="post-76170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76170-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been having some disagreements about whether or not the <a href="https://en.wikipedia.org/wiki/Trans_Canada_Trail">Trans-Canada Trail</a> should have a route relation tagged as a bicycle route, as it has had since at least 2011.</p>
<p>The argument presented against it, is that it is not exclusively for bicycle use, and some sections are not for bicycle use at all. At places alternative routes for foot and bicycles, in other places there is not a designated route for bicycles. As such there are discontinuities in the bicycle route.</p>
<p>They only want a foot relation to exist, and all sections of the route that are exclusively for bicycle use to be removed from the relation.</p>
<p>I feel that the appropriate way to structure this on OSM is with a couple relations, one for the bicycle sections, one for foot (and if there are other people interested in it, additional relations for the sections designated for horseback, etc). This is what I've seen done with other multi-use recreational routes, and it seems a sensible approach.</p>
<p>I do not think the relatively short discontinuities in the designated bicycle sections of the TCT disqualify it from tagging as a national bicycle route.</p>
<p>Am I mistaken on my understanding of the OSM approach here?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-multi-use" rel="tag" title="see questions tagged &#39;multi-use&#39;">multi-use</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-bicycle" rel="tag" title="see questions tagged &#39;bicycle&#39;">bicycle</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Aug '20, 19:06</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-76170" class="comments-container">
&#10;</div>
<div id="comment-tools-76170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76170-form-container" class="comment-form-container">
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

<span id="76184"></span>

<div id="answer-container-76184" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76184-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are two popular ways to do this:</p>
<ul>
<li>Create two separate relations, one <code>route=hiking</code>, one <code>route=bicycle</code></li>
<li>Create a single relation, with <code>route=hiking;bicycle</code></li>
</ul>
<p>The latter is not universally supported by renderers/routers but is used sometimes in North America.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '20, 14:45</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-76184" class="comments-container">
&#10;</div>
<div id="comment-tools-76184" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76184-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76186"></span>

<div id="answer-container-76186" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76186-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The current state of the Trans-Canada Trail on OSM is a bit of a mess.</p>
<ul>
<li>There's a <code>type=route</code> + <code>route=hiking</code> <a href="https://www.openstreetmap.org/relation/3060299">Trans-Canada Trail super-super-relation</a> whose memebers are the super-relations for each province -- plus a few stray segments that may be mistakes? (Also the Quebec sub-relation is named "<a href="https://www.openstreetmap.org/relation/8274591">Trans Canada Trail (Montréal to Gatineau)</a>" rather than "Trans Canada Trial (Quebec)".)</li>
<li>The Canada page of the OSM wiki suggests that if <em>all</em> the TCT segments in a particular province are cyclable, then that province's TCT route relation should be tagged as a <code>network=ncn</code> bicycle route (<a href="https://wiki.openstreetmap.org/wiki/Canada#Trans_Canada_Trail">https://wiki.openstreetmap.org/wiki/Canada#Trans_Canada_Trail</a>).</li>
<li>Perhaps for this reason, the province-level super-relations are not consistent -- some are <code>route=hiking</code>, some are <code>route=bicycle</code>. But there other inconsistencies as well: Some are <code>type=superroute</code> (an undocumented relation type) instead of route, some contain individual segments as well as sub-relations.</li>
</ul>
<p>From your description, the <a href="https://thegreattrail.ca">Trans-Canada Trail website</a>, and a quick browse of relevant OSM elements and changesets, my conclusion is: While it might be valid to use <code>route=bicycle</code> on some sub-relations, it's not appropriate for the main TCT super-super-relation.</p>
<p>If (and only if) the "alternative routes for foot and bicycle" that you mention are part of the official published route -- that is, if there are official Trans-Candada Trail signs or maps that say "bicycles go this way, foot traffic go that way" -- then I believe those bicycle sections belong in the route sub-relations. I'd add them with <code>role=alternate</code> (which is undocumented but heavily used.)</p>
<p>See also the changeset comment for <a href="https://www.openstreetmap.org/changeset/87691196">changeset 87691196</a> which links to a Facebook (yech) discussion about this question. The recommendation there is to create seperate cycle routes as part the Bike Across Canada Route, which is still under development. <em>Edit -- See Richard's comment below, the Bike Across Canada Route is currently just a dream, so probably best to avoid working on it in OSM for now.</em></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '20, 16:11</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Aug '20, 20:48</strong> </span></p>
</div>
</div>
<div id="comments-container-76186" class="comments-container">
<span id="76187"></span>
<div id="comment-76187" class="comment">
<div id="post-76187-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The "Bike Across Canada Route" is entirely the invention of an enthusiastic person with no official status, signposting, etc. etc. I can well believe it might be better than the notorious TCT, but it doesn't merit inclusion in OSM.</p>
</div>
<div id="comment-76187-info" class="comment-info">
<span class="comment-age">(18 Aug '20, 16:18)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="76188"></span>
<div id="comment-76188" class="comment">
<div id="post-76188-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah, good to know. Then my conclusion is: As of now, there is <strong>no</strong> national cycle route in Canada, and the TCT should remain route=hiking (even though it apparently includes some sections that are traversable only by boat! That's another discussion I guess.)</p>
</div>
<div id="comment-76188-info" class="comment-info">
<span class="comment-age">(18 Aug '20, 16:23)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="76189"></span>
<div id="comment-76189" class="comment">
<div id="post-76189-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think that it's important to differentiate between the super-relation and the sub-relations, and I failed to do so. I was talking about the sub-relations, as those are the ones that I have been editing. I have failed to pay much attention to the super relation at all.</p>
<p>When you say "some subsections" do you mean <em>all</em> sections that are designated as a bicycle route should be in bicycle sub-relation? To me it makes sense to do so. It is also worth pointing out that there are many sections that are specifically for cycling, and not a designated walking route.</p>
<p>The enthusiastic individual who has invented the "Bike Across Canada Route"(s) frequently cites facebook as a source, and has made significant detrimental edits to the TCT.</p>
</div>
<div id="comment-76189-info" class="comment-info">
<span class="comment-age">(18 Aug '20, 17:24)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
<span id="76190"></span>
<div id="comment-76190" class="comment">
<div id="post-76190-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ultimately this is going to be a decision for the "local" (Canada is huge!) community. My best <em>interpretation</em> of the community consensus is:</p>
<ul>
<li>Super-super-relation for the entire TCT is <code>route=hiking</code></li>
<li>Super-relation for an individual province should be <code>route=bicycle</code> if the officially designated TCT route in that province is cyclable end-to-end. (The wiki link I included says these should be tagged <code>network=ncn</code>, but best I can tell there is no national cycle network in Canada, just regional cycle routes which are often part of the TCT. So possibly <code>network=rcn</code> would be better -- again, up to the local community, but IMO it would be nice if all of the fully-cyclable provinces were tagged the same way.)</li>
<li>Lowest-level route relations (the sub-relations of the province-level routes) should likewise be <code>route=bicycle</code> if that portion of the official TCT is cyclable -- and should be tagged <code>network=rcn</code> or <code>network=lcn</code> as appropriate.</li>
</ul>
</div>
<div id="comment-76190-info" class="comment-info">
<span class="comment-age">(18 Aug '20, 17:38)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-76186" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76186-form-container" class="comment-form-container">
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

