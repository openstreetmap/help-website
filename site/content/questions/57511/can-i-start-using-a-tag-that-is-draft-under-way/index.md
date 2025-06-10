+++
type = "question"
title = "Can I start using a tag that is &quot;Draft (under way)&quot;?"
description = '''I&#x27;ve done some simple searching for what &quot;Draft&quot; and &quot;under way&quot; mean exactly, but the Wiki just links those terms to lists of tags that are &quot;Draft&quot; and &quot;under way&quot;.  The one I&#x27;m looking at specifically is  https://wiki.openstreetmap.org/wiki/Proposed_features/Trailer_Park which is currently listed ...'''
date = "2017-08-08T19:47:00Z"
lastmod = "2017-08-09T16:48:00Z"
weight = 57511
keywords = [ "status", "features", "tagging" ]
aliases = [ "/questions/57511" ]
osqa_answers = 5
osqa_accepted = true
+++

<div class="headNormal">

# [Can I start using a tag that is "Draft (under way)"?](/questions/57511/can-i-start-using-a-tag-that-is-draft-under-way)

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
<span id="post-57511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57511-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've done some simple searching for what "Draft" and "under way" mean exactly, but the Wiki just links those terms to lists of tags that are "Draft" and "under way".</p>
<p>The one I'm looking at specifically is</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Trailer_Park">https://wiki.openstreetmap.org/wiki/Proposed_features/Trailer_Park</a></p>
<p>which is currently listed as "Status: Draft (under way)"</p>
<p>I am a bike tourist and recently accidentally went to a trailer park in France that was labeled as "amenity=camp_site" when it was definitely not a camp site as that tag is typically used in France (a place where someone can pay 10 euros for a hot shower and a camping pitch). This was a place to semi-permanently live in a prefabricated home. After making friends with some of the residents I did in fact camp there in a shred of grass next to a huge propane tank, but now I would like to change its OSM tagging to something more accurate to avoid awkward future arrivals by other tourists, and I'm trying to figure out what the best tag is.</p>
<p>Should I use the accurate draft tag, amenity=trailer_park? Or a more established tag, like place=hamlet?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-status" rel="tag" title="see questions tagged &#39;status&#39;">status</span> <span class="post-tag tag-link-features" rel="tag" title="see questions tagged &#39;features&#39;">features</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Aug '17, 19:47</strong></p>
<img src="https://secure.gravatar.com/avatar/9d31424c5c97e0ccb8439d98d5f1066d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joe_mo&#39;s gravatar image" />
<p><span>joe_mo</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joe_mo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Aug '17, 00:08</strong> </span></p>
</div>
</div>
<div id="comments-container-57511" class="comments-container">
&#10;</div>
<div id="comment-tools-57511" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57511-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="57512"></span>

<div id="answer-container-57512" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57512-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-57512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="joe_mo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap has an open tagging model, so you can use any tag you want. So you can either invent your own tags, rely on approved tags or use draft tags. That's up to you. In general, approved tags with a large usage number will more likely get support from data consumers, including map makers. As for stability, it does not matter whether a tag is approved or draft, any tags can be replaced in the future. Of course, this is less likely if the tag is used a lot (regardless of it's status).</p>
<p>If it is a trailer park, you should use amenity=trailer_park. place=hamlet just looks like a tag to see the name on the map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '17, 20:11</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-57512" class="comments-container">
&#10;</div>
<div id="comment-tools-57512" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57512-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="57531"></span>

<div id="answer-container-57531" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57531-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-57531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes of course you can use a tag with proposed status: with a free-format tagging system the status on the wiki is at best indicative, at worst downright wrong.</p>
<p>For some reason trailer parks (or to use british-english, mobile home parks) were rather neglected in the early stages of OSM. Consequently tagging is a little hit-and-miss. Do read some of the earlier answers on this site.</p>
<p>My personal preference is to map these as a special type of residential area: landuse=residential, residential=mobile_home_park. I'd tend to avoid both amenity &amp; leisure keys as these are not generally available facilities.</p>
<p>Note there is still ambiguity between what in the UK we call mobile home parks and static caravan sites, and the draft of trailer park seems to show this as well. One is distinctly residential, the other a leisure facility: even then they may be mixed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Aug '17, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-57531" class="comments-container">
&#10;</div>
<div id="comment-tools-57531" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57531-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="57513"></span>

<div id="answer-container-57513" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57513-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-57513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can always use any tag you want.</p>
<p>A different question is, if is going off on your own is the best course of action from a practical point of view (for example will data consumers actually do something with my newly thought up tagging and so on), so most contributors tend to stay with popular tagging (and will change tagging that they consider out of line with that).</p>
<p>In any case you should not just check the wiki but have a look at taginfo <a href="https://taginfo.openstreetmap.org/search?q=trailer_park#values">https://taginfo.openstreetmap.org/search?q=trailer_park#values</a> which would indicate that the tagging is not very popular, but in use.</p>
<p>You can always start a discussion on the tagging mailing list <a href="https://lists.openstreetmap.org/listinfo/tagging">https://lists.openstreetmap.org/listinfo/tagging</a> in this case, due to cultural considerations, actually asking on the US list might be a better approach <a href="https://lists.openstreetmap.org/listinfo/talk-us">https://lists.openstreetmap.org/listinfo/talk-us</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '17, 20:16</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Aug '17, 20:18</strong> </span></p>
</div>
</div>
<div id="comments-container-57513" class="comments-container">
&#10;</div>
<div id="comment-tools-57513" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57513-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="57514"></span>

<div id="answer-container-57514" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57514-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-57514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The simple answer is yes, you can use any tag you like, even if some mappers disapprove of it.</p>
<p>However, the example you gave is one in which the tagging is incorrect on two counts. It is neither an amenity nor a camp_site. Your assumption about the camp_site tag is 100% correct. It should have been a tagged as <em>leisure</em>=caravan_site and then optionally enhanced with other tags that more fully describe the object such as, for example, fee=yes/no, capacity=*, sanitary_dump_station=yes/no, etc.</p>
<p>The amenity=trailer_park tagging would not be appropriate for a caravan_site because trailer parks are set up for more or less permanent residency. People live there in portable or mobile homes but for the most part they are merely landuse=residential. Same with place=hamlet. This is a permanent area of dense population, similar to a town or village but smaller.</p>
<p>Cheers,</p>
<p>Dave</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '17, 20:17</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Aug '17, 22:50</strong> </span></p>
</div>
</div>
<div id="comments-container-57514" class="comments-container">
&#10;</div>
<div id="comment-tools-57514" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57514-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="57517"></span>

<div id="answer-container-57517" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57517-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-57517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Joe-mo, consider to ad tents=no since its hard to determine how a caravan park should be tagged. They could have trailers for rent mixed with permanent inhabitants and you wont be able to determine if your neighbour is camping on a seasonal contract.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '17, 20:52</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-57517" class="comments-container">
&#10;</div>
<div id="comment-tools-57517" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57517-form-container" class="comment-form-container">
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

