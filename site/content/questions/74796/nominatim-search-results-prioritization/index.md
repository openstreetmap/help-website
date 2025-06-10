+++
type = "question"
title = "Nominatim search results prioritization"
description = '''Hello, When performing searches that yield multiple results, I&#x27;ve noticed what looks like an intuitive ordering in the output. For instance, searching London yields the English capital as first result, as opposed to the London county in Ontario, Canada or the city in Arkansas, USA; searching Manhatt...'''
date = "2020-05-13T23:01:00Z"
lastmod = "2023-03-31T08:17:00Z"
weight = 74796
keywords = [ "prioritization", "search", "nominatim", "geocoding", "order" ]
aliases = [ "/questions/74796" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim search results prioritization](/questions/74796/nominatim-search-results-prioritization)

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
<span id="post-74796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74796-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>When performing searches that yield multiple results, I've noticed what looks like an intuitive ordering in the output. For instance, searching <a href="https://nominatim.openstreetmap.org/search.php?q=london">London</a> yields the English capital as first result, as opposed to the London county in Ontario, Canada or the city in Arkansas, USA; searching <a href="https://nominatim.openstreetmap.org/search.php?q=manhattan">Manhattan</a> gives the New York City municipality as first result, as opposed to the city in Kansas, USA or the locality in Poland; searching <a href="https://nominatim.openstreetmap.org/search.php?q=berlin">Berlin</a> yields the German capital as first result as opposed to any of the (surprisingly numerous) cities named Berlin in the US.</p>
<p>I've also noticed that the Geopy Nominatim client, when configured to return exactly one result, seems to always return the first one.</p>
<p>Is it true that results are ordered according to certain criteria? In that case, are the criteria documented? It would actually be helpful for me if this was the case, but I'd love to understand if this is a feature provided by design, a best-effort kind of thing that is provided but isn't guaranteed by the API, or mere coincidence.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-prioritization" rel="tag" title="see questions tagged &#39;prioritization&#39;">prioritization</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-order" rel="tag" title="see questions tagged &#39;order&#39;">order</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 May '20, 23:01</strong></p>
<img src="https://secure.gravatar.com/avatar/ede0a84ad576e5a6dc3b1b650869aa6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shai&#39;s gravatar image" />
<p><span>Shai</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shai has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74796" class="comments-container">
<span id="74810"></span>
<div id="comment-74810" class="comment">
<div id="post-74810-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks to both, it doesn't seem like I'm able to upvote your answers :( but I appreciate the help.</p>
</div>
<div id="comment-74810-info" class="comment-info">
<span class="comment-age">(14 May '20, 17:42)</span> <span class="comment-user userinfo">Shai</span>
</div>
</div>
</div>
<div id="comment-tools-74796" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74796-form-container" class="comment-form-container">
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

<span id="74808"></span>

<div id="answer-container-74808" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74808-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-74808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Shai has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(Can't seem to add a comment).</p>
<p>The default settings are in <code>settings/address-levels.json</code> and for points-of-interest types there's also a frequency list in <code>lib/ClassTypes.php</code>.</p>
<p>When you install Nominatim yourself, and added the wikipedia ranking file (described in the install instructions), it will be almost the same as nominatim.openstreetmap.org.</p>
<p>There's a difference searching via a browser (e.g. on openstreetmap.org) and via a script (e.g. geopy): a browser will send your preferred language, and the website usually the current viewpoint of the map. That gives additional hints to the ranking. For example if the map is zoomed a London in the United States then London, UK is less relevant. You can set those with the <code>accept-language</code> and <code>viewbox</code> API parameters.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '20, 17:27</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-74808" class="comments-container">
<span id="74809"></span>
<div id="comment-74809" class="comment">
<div id="post-74809-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, now having a look at <code>settings/address-levels.json</code> I'm getting an idea of the criteria. Thanks. In my installation I haven't used the Wikipedia ranking file, so I suppose I'm getting the results based on the default settings.</p>
</div>
<div id="comment-74809-info" class="comment-info">
<span class="comment-age">(14 May '20, 17:41)</span> <span class="comment-user userinfo">Shai</span>
</div>
</div>
</div>
<div id="comment-tools-74808" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74808-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74801"></span>

<div id="answer-container-74801" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74801-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74801-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-74801-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, results are ordered and this is documented in Nominatim's documentation. Of special interest are probably the chapter on <a href="http://nominatim.org/release-docs/latest/develop/Ranking/">Place Ranking</a> and <a href="http://nominatim.org/release-docs/latest/data-sources/Wikipedia-Wikidata/">Wikipedia &amp; Wikidata</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '20, 08:08</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-74801" class="comments-container">
<span id="74805"></span>
<div id="comment-74805" class="comment">
<div id="post-74805-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great, thank you Jochen, I totally missed that section.</p>
<p>So, Place Ranking section describes how places are ranked using search ranks and address ranks, which it states are assigned to places on import. It then explains how may one go about configuring ranks. However, I haven't configured any ranks when I imported data into my database, and judging by the intuition I explained in the original post, ranks definitely seem to have been assigned automatically. In that case, do we know with what criteria? Also, is it the same as the online Nominatim?</p>
<p>Thanks again.</p>
</div>
<div id="comment-74805-info" class="comment-info">
<span class="comment-age">(14 May '20, 14:29)</span> <span class="comment-user userinfo">Shai</span>
</div>
</div>
</div>
<div id="comment-tools-74801" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74801-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87005"></span>

<div id="answer-container-87005" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87005-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87005-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87005-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi everyone, I've got a follow-up issue:</p>
<p>The Nominatim search results are displayed in the left side pane on openstreetmap.org. However, at the same time, the map already zooms in on the first result. I assume that this will lead many (perhaps less tech-savvy) users to miss the other search results.</p>
<p>As has been said in this thread before, there are ranking mechanisms, so in many cases this behaviour is fine. And in other cases, the user should notice that the map is not showing the desired place and then find the other search results.</p>
<p>My issue is with cases where all n search results are equally plausible, and the user is not familiar with the region (which is why he/she uses a map service) so as to recognize an undesired result. Now the first search result only has a chance of 1/n for being the desired result. In these cases, it would make more sense <strong>not</strong> to immediately zoom in on the first result, but keep the current view, or even display a more prominent notification saying that the search term is ambiguous.</p>
<p>Example: Surprisingly many towns, villages, municipalities have multiple cases of double, triple, quadruple occurrences of the same street name, under the same postal code. In Germany, these can be remnants from the nation-wide consolidation of villages into larger municipalities in the 1970s or from the change to 5-digit postal codes in the 1990s. In most towns, such duplicates have been resolved, but in many cases, they have not (e.g., when residents resisted renaming of their street). For example, in the municipality of Burgwedel (postal code 30938, Germany), there are 19 doubles, 5 triplets, and one quadruplet street name ("Hinter den Höfen"), for a total of 57 streets in this small municipality of 20k residents alone. Other cases can quickly be found on the internet, probably in other countries as well.</p>
<p>Only the address system of Deutsche Post / DHL properly deals with this and asks for the specific village or district when entering an address for parcel shipment. Most other systems deal with this poorly, Google Maps even shows only one search result. This issue constantly annoys, sometimes endangers the affected residents:</p>
<p>Consider streetmap users such as visitors, delivery services, and sometimes even ambulances. Nowadays many of those tend to rely on search engines and go for the result they are given, especially if the map zooms in on one address - just tap on "calculate route" and off you go - probably to the wrong address in another village. Additional address information given by the resident is often omitted by the navigation or address handling systems, or missed by those navigating there.</p>
<p>Therefore, my feature request would be to deal with search results differently, if their probability score (?) is the same, and bring this to the user's attention or even force him/her to make a choice, before zooming in on one of the possible addresses. Thanks!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '23, 16:20</strong></p>
<img src="https://secure.gravatar.com/avatar/63bc71b14944d0dde74964cd27eb9f69?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Soundlover&#39;s gravatar image" />
<p><span>Soundlover</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Soundlover has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Mar '23, 16:24</strong> </span></p>
</div>
</div>
<div id="comments-container-87005" class="comments-container">
<span id="87007"></span>
<div id="comment-87007" class="comment">
<div id="post-87007-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is not a discussion board. Please use <a href="https://community.openstreetmap.org">https://community.openstreetmap.org</a> or the issue tracker at <a href="https://github.com/openstreetmap/openstreetmap-website/issues">https://github.com/openstreetmap/openstreetmap-website/issues</a> for your ideas.</p>
</div>
<div id="comment-87007-info" class="comment-info">
<span class="comment-age">(29 Mar '23, 16:55)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="87008"></span>
<div id="comment-87008" class="comment">
<div id="post-87008-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... but the topic is very closely related to the original topic of this thread. For once someone searches for existing threads before posting, and it still isn't right ;-)</p>
</div>
<div id="comment-87008-info" class="comment-info">
<span class="comment-age">(29 Mar '23, 16:59)</span> <span class="comment-user userinfo">Soundlover</span>
</div>
</div>
<span id="87018"></span>
<div id="comment-87018" class="comment">
<div id="post-87018-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/22874/soundlover">@Soundlover</a> This is <em>not</em> a thread. OSM Help is a Question&amp;Answer platform. One question - multiple answers. Posting a subsequent question as an answer is <em>not</em> supported. In such case please always create a <em>new question</em>.</p>
</div>
<div id="comment-87018-info" class="comment-info">
<span class="comment-age">(31 Mar '23, 08:17)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-87005" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87005-form-container" class="comment-form-container">
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

