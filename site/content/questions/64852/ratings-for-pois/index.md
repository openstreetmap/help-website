+++
type = "question"
title = "Ratings for POI&#x27;s?"
description = '''Is there something like a rating tag for POI&#x27;s (e.g. rating=1-10)? If not then this certainly would be a nice addition. Mappers could check online (Tripadvisor, Google, Booking.com) and enter the value. There is a certain risk of edit wars between POI owner and mappers though...'''
date = "2018-07-22T09:51:00Z"
lastmod = "2018-07-24T17:47:00Z"
weight = 64852
keywords = [ "rating", "poi" ]
aliases = [ "/questions/64852" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Ratings for POI's?](/questions/64852/ratings-for-pois)

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
<span id="post-64852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64852-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-64852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there something like a rating tag for POI's (e.g. rating=1-10)? If not then this certainly would be a nice addition. Mappers could check online (Tripadvisor, Google, Booking.com) and enter the value. There is a certain risk of edit wars between POI owner and mappers though...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rating" rel="tag" title="see questions tagged &#39;rating&#39;">rating</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jul '18, 09:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a6e2839b04b99e35e45d64fe66b9a500?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rene78&#39;s gravatar image" />
<p><span>rene78</span><br />
<span class="score" title="700 reputation points">700</span><span title="29 badges"><span class="badge1">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rene78 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64852" class="comments-container">
&#10;</div>
<div id="comment-tools-64852" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64852-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="64864"></span>

<div id="answer-container-64864" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64864-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-64864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One of the key principals of OpenStreetMap is "Verifiability" -- the idea is that any data entered into OpenStreetMap should be factual not editorial, available to the general public, and verifiable by the next mapper that comes along. See <a href="https://wiki.openstreetmap.org/wiki/Good_practice">Good Practice</a> on the wiki.</p>
<p>A mapper assigning a rating to a restaurant (etc) is clearly not verifiable -- it's a matter of personal taste and ephemeral experience. So it doesn't belong in the OSM database. And yes, it would immediately motivate spam and edit wars.</p>
<p>Generally, online ratings are made using weighted averages of reviews. OSM doesn't have any facility for averaging data like this. We don't vote on values for keys; new values simply replace the old ones.</p>
<p>It would certainly be possible to create a review system that used data from OSM to provide the factual info for the restaurants etc that were being rated -- location, name, phone numbers, opening hours, cuisine, wheelchair accessibility, etc -- and keep its own database for the ratings data. I know of at least one project that intends to provide this review functionality in a way that works alongside OSM data -- It's called <a href="https://lib.reviews/team/developers/post/30c5fb18-e2c3-4a5c-b25d-4d957c5344b7">lib.reviews</a>. There may be others.</p>
<p>(This also brings to mind the question of "permanent IDs" that's currently being discussed in <a href="/questions/64817/what-are-the-technical-problems-with-permanent-id">another question</a> -- ie, how and whether to maintain a link to the old reviews if a restaurant is remapped from a node to a way, or moves to another location but keeps the same name and menu. How to make sure a spelling correction of a restaurant's name doesn't eliminate old reviews, but a new restaurant opening in the closed space of another doesn't inherit the previous reviews. That sort of thing.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '18, 17:45</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-64864" class="comments-container">
<span id="64884"></span>
<div id="comment-64884" class="comment">
<div id="post-64884-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But isn't it verifiable by simply going to those popular websites and check the rating? I am often surprised how close the ratings for the same POI are on each of them. That shows in my opinion that swarm intelligence works. But I already see, that I'm the only one who thinks that it would be a good idea to have a POI-rating in OSM ;)</p>
<p>Your question in brackets could be tackled by Wikidata ID's(?)</p>
</div>
<div id="comment-64884-info" class="comment-info">
<span class="comment-age">(24 Jul '18, 09:15)</span> <span class="comment-user userinfo">rene78</span>
</div>
</div>
<span id="64891"></span>
<div id="comment-64891" class="comment">
<div id="post-64891-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The general rule is: Map what can be observed in person by the general public. Some stricter mappers interpret this as just the physical attributes of a POI and whatever signage is visible from the street. Others are more lenient and will consider info gathered from menu cards, talking with staff, and even the official website and social media posts of a business to be the equivalent of signage. But opinions posted by random people and aggregated by Google etc. are beyond the pale. (And also probably prohibited by license.)</p>
</div>
<div id="comment-64891-info" class="comment-info">
<span class="comment-age">(24 Jul '18, 17:29)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="64892"></span>
<div id="comment-64892" class="comment">
<div id="post-64892-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I think understand your use case -- travelling without reliable internet access and wishing for a simple offline database of amenity ratings to help decide where to eat and sleep. IMO it's a feature best implemented by a third party. A developer could offer it as a feature of an offline map app: At the time of map data download, process the list of POIs and attempt to scrape various web sites for ratings info, using some fuzzy matching of name and location. The result could be added as a tag in the local copy of the map data, on your phone or tablet. This could be quite useful. And it's possible that the developer in question would get a cease-and-desist order from the review sites, but it wouldn't become a legal problem for OSM itself.</p>
</div>
<div id="comment-64892-info" class="comment-info">
<span class="comment-age">(24 Jul '18, 17:31)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="64893"></span>
<div id="comment-64893" class="comment">
<div id="post-64893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(As far as using Wikidata for a Permanet ID/Persistent Place Identifier -- yes, or something along those lines. But Wikidata inherits Wikipedia's "notability" criteria for things. They'll have a code for a famous restaurant, but not for the corner burrito joint.</p>
<p>One suggestion is that OSM make use of a variety of permanent ID authorities, so if something doesn't warrant a Wikidata ID it can be tagged with an ID from, say, Burritodata. Or both, if it's a famous burrito place. At this point it's still an open discussion and it's not going to be settled for a while.)</p>
</div>
<div id="comment-64893-info" class="comment-info">
<span class="comment-age">(24 Jul '18, 17:47)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-64864" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64864-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64854"></span>

<div id="answer-container-64854" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64854-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-64854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>All the services you mention have their own rating system. I doubt you are allowed to copy this data. Honestly, I think OSM should stay away from those kind of subjective ratings.</p>
<p>There is a difference though with the stars you find on hotels on European hotels, as they tend to be visible for anyone passing the hotel. The tag for such stars is described on the <a href="https://wiki.openstreetmap.org/wiki/Key:stars">wiki</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '18, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-64854" class="comments-container">
<span id="64859"></span>
<div id="comment-64859" class="comment">
<div id="post-64859-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A single rating is subjective. Hundreds or thousands of them give a good impression of the quality of a place. All this information is gathered from people like you and me. It belongs to nobody in my opinion. I guess that is the reason why Google collects the ratings from all major sites (i.e. Tripadvisor, booking.com, etc.) in their rating system.</p>
<p>This is the only reason when travelling, that I have to rely on the internet again: To see whether this hotel, restaurant, etc. is any good. Would be nice to stay completely in my OSM based offline navigation app.</p>
</div>
<div id="comment-64859-info" class="comment-info">
<span class="comment-age">(22 Jul '18, 14:00)</span> <span class="comment-user userinfo">rene78</span>
</div>
</div>
<span id="64861"></span>
<div id="comment-64861" class="comment">
<div id="post-64861-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>One more thing. It could be implemented like that: Restaurant x got 3.5/5 from website x, a 7/10 from website y and 7.5/10 from z. Then the OSM rating tag would be set to 7. No rocket science. Just a quick check online. (I hope in a decade we'll have independent rating systems based on blockchain though...)</p>
</div>
<div id="comment-64861-info" class="comment-info">
<span class="comment-age">(22 Jul '18, 15:45)</span> <span class="comment-user userinfo">rene78</span>
</div>
</div>
<span id="64863"></span>
<div id="comment-64863" class="comment">
<div id="post-64863-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Since those ratings will change over time it is much better that your favorite app would directly integrate the values from those third party sites, instead of copying them first to osm. A bit like OsmAnd works with Wikipadia at this moment.</p>
<p>And again, I doubt that you sre legally allowed copy the data from their websites</p>
</div>
<div id="comment-64863-info" class="comment-info">
<span class="comment-age">(22 Jul '18, 15:54)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="64876"></span>
<div id="comment-64876" class="comment">
<div id="post-64876-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>One would have expected that someone with over 11000 uploaded changesets would have a better understanding of basic OSM concepts like verifiability and license/copyright issues.</p>
</div>
<div id="comment-64876-info" class="comment-info">
<span class="comment-age">(23 Jul '18, 18:47)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="64880"></span>
<div id="comment-64880" class="comment">
<div id="post-64880-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8189/alester"></a><a href="https://help.openstreetmap.org/users/8189/alester">@alester</a>, when TripAdvisor writes on their <a href="https://tripadvisor.mediaroom.com/us-terms-of-use">terms of use page</a></p>
<p>"The content and information on this Website (including, but not limited to, messages, data, information, text, music, sound, photos, graphics, video, maps, icons, software, code or other material), as well as the infrastructure used to provide such content and information, is proprietary to us. You agree not to otherwise modify, copy, distribute, transmit, display, perform, reproduce, publish, license, create derivative works from, transfer, or sell or re-sell any information, software, products, or services obtained from or through this Website."</p>
<p>and also "Additionally, you agree not to:</p>
<p>(i) use this Website or its contents for any commercial purpose"</p>
<p>my understanding is that you cannot copy their rating in OSM. but I can be mistaken. Please let me know if you can copy data from another database if they post a text like this on their webiste</p>
</div>
<div id="comment-64880-info" class="comment-info">
<span class="comment-age">(24 Jul '18, 04:47)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="64881"></span>
<div id="comment-64881" class="comment not_top_scorer">
<div id="post-64881-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8189/alester">@alester</a>: as for verifiability, you are correct that taking ratings from another source is verifiable. Having our own rating system is not. When the OP write "rating tag for POI's" this meant to me, a rating given by mappers. When the OP wrote to copy the value from other sites, it's a DB license issue.</p>
<p>For me, those rating sites live from people visiting their website/use their app and click on ads or make bookings through them after seeing the score and reviews. By moving their ratings elsewhere, they loose clicks and thus revenue. I think that is the reason they do no allow you to copy any content from their website.</p>
</div>
<div id="comment-64881-info" class="comment-info">
<span class="comment-age">(24 Jul '18, 05:38)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="64885"></span>
<div id="comment-64885" class="comment not_top_scorer">
<div id="post-64885-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"One would have expected that someone with over 11000 uploaded changesets would have a better understanding of basic OSM concepts like verifiability and license/copyright issues."</p>
<p>Verifiablility would be easy. Just go back after a year and check whether the ratings have changed significantly. Regarding copyright I am not sure. Of course the rating portals don't want you to copy pictures and text from their websites, but a simple overall rating number? Google is collecting those numbers at least. But they could have a deal with them.</p>
</div>
<div id="comment-64885-info" class="comment-info">
<span class="comment-age">(24 Jul '18, 09:26)</span> <span class="comment-user userinfo">rene78</span>
</div>
</div>
<span id="64888"></span>
<div id="comment-64888" class="comment not_top_scorer">
<div id="post-64888-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5390/escada"></a><a href="https://help.openstreetmap.org/users/5390/escada">@escada</a>: Sorry, I should have been more clear. My comment was referencing rene78, not you. I'm on your side as far as thinking that this is a bad idea. :)</p>
</div>
<div id="comment-64888-info" class="comment-info">
<span class="comment-age">(24 Jul '18, 16:47)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="64889"></span>
<div id="comment-64889" class="comment not_top_scorer">
<div id="post-64889-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8189/alester">@alester</a>, thanks for letting me know! It was indeed confusing.</p>
</div>
<div id="comment-64889-info" class="comment-info">
<span class="comment-age">(24 Jul '18, 16:49)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="64890"></span>
<div id="comment-64890" class="comment not_top_scorer">
<div id="post-64890-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/1829/rene78">@rene78</a>: A collection or average of subjective data is still subjective data and not verifiable (ie. if you ask a few different people, you'll probably get different results). As for the legal use of third-party data, remember that OSM has very different licensing terms and goals than Google, who can effectively do whatever they want. OSM is limited to sources that are compatible with the ODbL license.</p>
</div>
<div id="comment-64890-info" class="comment-info">
<span class="comment-age">(24 Jul '18, 16:55)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-64854" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-64854-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64883"></span>

<div id="answer-container-64883" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64883-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One possible option is to just point to corresponding entries at online rating systems via tags. Example:</p>
<pre><code>rating:tripadvisor=http://www.tripadvisor.com/Moes_Tavern.html
rating:google=http://www.google.com/super_long_and_ugly_and_mysterious_google_url_gibberish.html
rating:booking.com=http://www.booking.com/hotel/Moes_hovel.html</code></pre>
<p>This approach would be verifiable and neutral. However I'm still not convinced that this is a good idea.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '18, 08:02</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-64883" class="comments-container">
<span id="64886"></span>
<div id="comment-64886" class="comment">
<div id="post-64886-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>@"not [...] good idea": what about my supercool rating website ( rating:acme=<a href="http://example.com/acme/the_windhound_london">http://example.com/acme/the_windhound_london</a> )? Isn't that spam for unrelated companies (who make money e.g. from ads on their pages)? I tend to think that everybody should use their own favourite web search engine to find ratings or directly go to their favourite ratings website.</p>
</div>
<div id="comment-64886-info" class="comment-info">
<span class="comment-age">(24 Jul '18, 11:38)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="64887"></span>
<div id="comment-64887" class="comment">
<div id="post-64887-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes. Sure you can already add links to your favorite spam website via the <code>website</code> key to attract potential visitors. But the above scheme will certainly attract even more spam.</p>
</div>
<div id="comment-64887-info" class="comment-info">
<span class="comment-age">(24 Jul '18, 11:47)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64883" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64883-form-container" class="comment-form-container">
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

