+++
type = "question"
title = "Ideal tag combination for branches?"
description = '''In the case of business branches that people generally distinguish by the name of a place/area or road that is located nearby (for instance, &quot;KFC Downtown&quot; (a specific area), &quot;Starbucks Riverside&quot; (an avenue), &quot;DHL Waterfall Mall&quot; (a place it&#x27;s in) etc.), which would be the best practice to tag them...'''
date = "2017-11-01T17:03:00Z"
lastmod = "2017-11-03T11:10:00Z"
weight = 60414
keywords = [ "search", "nominatim", "name", "branch" ]
aliases = [ "/questions/60414" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Ideal tag combination for branches?](/questions/60414/ideal-tag-combination-for-branches)

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
<span id="post-60414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60414-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In the case of business branches that people generally distinguish by the name of a place/area or road that is located nearby (for instance, "KFC Downtown" (a specific area), "Starbucks Riverside" (an avenue), "DHL Waterfall Mall" (a place it's in) etc.), which would be the best practice to tag them in a way they can be found by search terms like "starbucks riverside" or "kfc downtown", etc? Please note the name of the place/road/area isn't necessarily part of the "official" name of that specific branch, just how people will call it.</p>
<ul>
<li>One option, the most straightforward one, would simply be using <code>name=KFC Downtown</code> for the element, but the wiki recommends not to put additional information in the name tag.</li>
<li>Another option would be using <code>alt_name=KFC Downtown; name=KFC</code>.</li>
<li>Tagging <code>name=KFC; branch=Downtown</code> doesn't seem return any hit on both the OSM site and Nominatim for "kfc downtown".</li>
</ul>
<p>What could be the ideal tag combination to get an accurate lookup?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-branch" rel="tag" title="see questions tagged &#39;branch&#39;">branch</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Nov '17, 17:03</strong></p>
<img src="https://secure.gravatar.com/avatar/37882972d0db7a93230b8e5e7fdbabc3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Absay&#39;s gravatar image" />
<p><span>Absay</span><br />
<span class="score" title="61 reputation points">61</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Absay has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60414" class="comments-container">
&#10;</div>
<div id="comment-tools-60414" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60414-form-container" class="comment-form-container">
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

<span id="60415"></span>

<div id="answer-container-60415" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60415-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Absay has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would use <a href="https://wiki.openstreetmap.org/wiki/Key:name">loc_name</a> (local name), since that seems to best describe what you've described. I don't know whether Nominatim uses that tag or not, but really that's beside the point.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '17, 17:37</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-60415" class="comments-container">
<span id="60418"></span>
<div id="comment-60418" class="comment">
<div id="post-60418-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, a tag being picked up by the search engines is what I'm looking for, so the OMS and Nominatim searches are relevant here, and loc_name seems to be the way to go in this case. Thanks!</p>
</div>
<div id="comment-60418-info" class="comment-info">
<span class="comment-age">(01 Nov '17, 20:07)</span> <span class="comment-user userinfo">Absay</span>
</div>
</div>
<span id="60420"></span>
<div id="comment-60420" class="comment">
<div id="post-60420-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The first priority should always be to tag the object as accurately as possible. Anything beyond that, like how it looks in a renderer, how it's found in a search engine, or how a routing engine uses it, are all secondary. If an object is tagged accurately but doesn't work as intended in a data consumer, it's the data consumer that needs to change, not the data.</p>
</div>
<div id="comment-60420-info" class="comment-info">
<span class="comment-age">(01 Nov '17, 20:28)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="60423"></span>
<div id="comment-60423" class="comment not_top_scorer">
<div id="post-60423-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>While finding an object in a Nominatim search may indeed be secondary, I think it is still important for users (and mappers) to be able to find it using variations on its name. I have been faced with the same problem many times and honestly don't know the best tags to use either.</p>
</div>
<div id="comment-60423-info" class="comment-info">
<span class="comment-age">(01 Nov '17, 22:45)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="60424"></span>
<div id="comment-60424" class="comment">
<div id="post-60424-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The branch tag was intended to adress this problem, but is a relatively new invention, which maybe hasn't been advertised as much as needed</p>
</div>
<div id="comment-60424-info" class="comment-info">
<span class="comment-age">(01 Nov '17, 23:56)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
<span id="60428"></span>
<div id="comment-60428" class="comment not_top_scorer">
<div id="post-60428-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I did not know of the "branch" tag, and I like it, but I cannot determine if it is searchable through Nominatim.</p>
</div>
<div id="comment-60428-info" class="comment-info">
<span class="comment-age">(02 Nov '17, 11:46)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="60429"></span>
<div id="comment-60429" class="comment not_top_scorer">
<div id="post-60429-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I found the list of names imported and indexed by Nominatim. It's on the Development page:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Nominatim/Development_overview">https://wiki.openstreetmap.org/wiki/Nominatim/Development_overview</a></p>
<p>Branch is not mentioned but old_name, loc_name, alt_name, among others, and their language variations like name:en, are processed</p>
</div>
<div id="comment-60429-info" class="comment-info">
<span class="comment-age">(02 Nov '17, 11:55)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="60436"></span>
<div id="comment-60436" class="comment not_top_scorer">
<div id="post-60436-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If branch=* is the correct tag to use (and it's used over 50K times as of today, so it seems likely), then maybe an issue should be entered in the Nominatim github to include branch values in the indexing: <a href="https://github.com/openstreetmap/Nominatim">https://github.com/openstreetmap/Nominatim</a></p>
</div>
<div id="comment-60436-info" class="comment-info">
<span class="comment-age">(02 Nov '17, 15:09)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="60437"></span>
<div id="comment-60437" class="comment">
<div id="post-60437-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>God, that page hasn't been updated in more than 2.5 years. One could think new tags have been added but at least from first hand I know "branch" hasn't yet. Maybe raising an issue on GitHub would be helpful? :)</p>
<p>Though to be fair, I don't necessarily care about Nominatim per se, which seems to be what OSM mappers use to "debug" their work. I guess I'm more interested in the most common search egines used by sites an apps that allow people to scout areas. The OSM default page would be one of them. But as far as I can see, this is platform-dependent and subject to separate development, where tags can be imported or left out depending on any given engine.</p>
<p>So as <a href="https://help.openstreetmap.org/users/8189/alester">@alester</a> said, accurate information is more important, that's the bottom line, so based on what I'm getting from this answers the combination <code>name=KFC + loc_name=KFC Downtown + branch=Downtown + brand=KFC + operator=KFC &lt;or whatever&gt;</code> seems to be good enough, though certainly a bit repetitive in regards to loc_name and branch. But hopefully this should encompass the majority of common search engines and return valuable hits to the end user.</p>
</div>
<div id="comment-60437-info" class="comment-info">
<span class="comment-age">(02 Nov '17, 15:17)</span> <span class="comment-user userinfo">Absay</span>
</div>
</div>
<span id="60443"></span>
<div id="comment-60443" class="comment">
<div id="post-60443-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>loc_name is for what local people call the place. It seems that loc_name=KFC Downtown is the exact opposite of that. Perhaps official_name is better</p>
</div>
<div id="comment-60443-info" class="comment-info">
<span class="comment-age">(03 Nov '17, 05:54)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-60415" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-60415-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60425"></span>

<div id="answer-container-60425" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60425-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-60425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would map it as name=KFC Downtown + brand=KFC This is how it is explained on the <a href="https://wiki.openstreetmap.org/wiki/Key:brand">brand</a> wiki page.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '17, 07:18</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Nov '17, 07:22</strong> </span></p>
</div>
</div>
<div id="comments-container-60425" class="comments-container">
<span id="60432"></span>
<div id="comment-60432" class="comment">
<div id="post-60432-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><em>"but the wiki recommends not to put additional information in the name tag"</em>, which is something that makes lots of sense, so adding the place to the name is discarded for me.</p>
</div>
<div id="comment-60432-info" class="comment-info">
<span class="comment-age">(02 Nov '17, 14:40)</span> <span class="comment-user userinfo">Absay</span>
</div>
</div>
<span id="60434"></span>
<div id="comment-60434" class="comment">
<div id="post-60434-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If the name on the receipt says "KFC Downtown" which incorrect additional information do you add then ? For me this means that I should e.g. not add "Restaurant' in e.g. "KFC Downtown Restaurant" even though There might be a "Restaurant" sign.</p>
</div>
<div id="comment-60434-info" class="comment-info">
<span class="comment-age">(02 Nov '17, 14:47)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-60425" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60425-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60449"></span>

<div id="answer-container-60449" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60449-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-60449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would base what I put in the name tag on signs outside the location.</p>
<p>If it says "KFC Downtown" then put that in the name; if the signs just say "KFC" put that in the name. The name on the receipt will be a short form (because of the allowable character width) of the internal (official name), which will be something like "KFC Downtown Anyplace".</p>
<p>If you are aware that people in the local area use "KFC Downtown" but this is not signed then loc_name is appropriate.</p>
<p>It is always a good idea to add brand=KFC too: this is more likely to be mapped consistently than name.</p>
<p>As other's have said don't map for a specific application such as Nominatim.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Nov '17, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-60449" class="comments-container">
&#10;</div>
<div id="comment-tools-60449" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60449-form-container" class="comment-form-container">
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

