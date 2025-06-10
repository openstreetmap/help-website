+++
type = "question"
title = "Associating an access=customers parking with its amenity?"
description = '''A shop has several parking places reserved for customers. How would I tag the parking places to indicate that they are reserved to that particular shop&#x27;s customers? In most cases such places are adjacent to the shop&#x27;s building, but in one case the parking places are actually on the opposite side of ...'''
date = "2017-07-12T01:10:00Z"
lastmod = "2017-07-14T10:16:00Z"
weight = 57027
keywords = [ "access", "customers", "relation_type-site", "multipolygon" ]
aliases = [ "/questions/57027" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Associating an access=customers parking with its amenity?](/questions/57027/associating-an-accesscustomers-parking-with-its-amenity)

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
<span id="post-57027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57027-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-57027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A shop has several parking places reserved for customers. How would I tag the parking places to indicate that they are reserved to <em>that</em> particular shop's customers?</p>
<p>In most cases such places are adjacent to the shop's building, but in one case the parking places are actually on the opposite side of a <code>highway=service access=public</code> road.</p>
<p>I think perhaps that could be mapped as a multipolygon with the shop and the parking places as role='outer' members, or with a 'site' relationship with both the shop and the parking places as role='' members. Thoughts? Other options?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-customers" rel="tag" title="see questions tagged &#39;customers&#39;">customers</span> <span class="post-tag tag-link-relation_type-site" rel="tag" title="see questions tagged &#39;relation_type-site&#39;">relation_type-site</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '17, 01:10</strong></p>
<img src="https://secure.gravatar.com/avatar/8440750fd002fd989ab2e6b613ca3ccb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsh4&#39;s gravatar image" />
<p><span>dsh4</span><br />
<span class="score" title="867 reputation points">867</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsh4 has one accepted answer">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jan '18, 13:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-57027" class="comments-container">
<span id="57051"></span>
<div id="comment-57051" class="comment">
<div id="post-57051-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There is actually a little used, and presumably NEVER consumed, relation type for exactly this problem called associatedParking. It might not be consumed but at least captures the information.</p>
</div>
<div id="comment-57051-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 09:52)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="57078"></span>
<div id="comment-57078" class="comment">
<div id="post-57078-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a>: This kind of relation is probably the only universally applicable solution. But please use associated_parking, not associatedParking. The naming conventions for OSM tags suggest lowercase words separated by underscores, not camelCase. And given the low usage numbers and lack of application support, there's no reason to keep the problematic spelling around for compatibility.</p>
</div>
<div id="comment-57078-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 16:31)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="57083"></span>
<div id="comment-57083" class="comment">
<div id="post-57083-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For posterity, the current uses of associatedParking has the main entity as a member with role="" and the parking as a member with either role="" or role="parking".</p>
<p>I still feel, though, that a 'site' relation with role="parking" members would scale better (if somebody wants to invent <em>another</em> thing that's associated with a shop, besides its parking spaces).</p>
</div>
<div id="comment-57083-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 18:48)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
<span id="57084"></span>
<div id="comment-57084" class="comment">
<div id="post-57084-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14/tordanik">@Tordanik</a> I merely provide an example which someone else had created and which I used 2-3 times. I suspect along the lines of associatedStreet which has 250k+ instances. Consistency is always good, but needless duplication for the sake of consistency less so.</p>
</div>
<div id="comment-57084-info" class="comment-info">
<span class="comment-age">(13 Jul '17, 23:25)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="57087"></span>
<div id="comment-57087" class="comment">
<div id="post-57087-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Regarding site relations, I did have a look at consuming them for map display, but after looking at their usage I couldn't really figure out which ones were useful and which ones weren't - they seemed to be used (in the UK) for a whole range of "X is somehow associated with Y" that it wasn't easy to do anything useful with at rendering time (not a technical problem - knowing what the user meant was the problem).</p>
<p>If you're going to use either a site relation (or some other sort of relation) for parking add a dozen or so examples and say what you're doing in the changeset comment and discussion, and document it in somewhere in the wiki.</p>
</div>
<div id="comment-57087-info" class="comment-info">
<span class="comment-age">(14 Jul '17, 10:16)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-57027" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57027-form-container" class="comment-form-container">
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

<span id="57039"></span>

<div id="answer-container-57039" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57039-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I thought the common way to map this is, is with access=customers; operator=... Perhaps not on the complete parking but on the amenity-parking_space in this case</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '17, 17:04</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-57039" class="comments-container">
<span id="57043"></span>
<div id="comment-57043" class="comment">
<div id="post-57043-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wouldn't operator= on the parking indicate who operates the parking --- who may be a subcontractor of the shop? E.g., if I saw an operator= on <a href="https://www.openstreetmap.org/way/207066386">this hotel's parking</a>, I would assume the hotel outsourced the operation of the parking lot.</p>
</div>
<div id="comment-57043-info" class="comment-info">
<span class="comment-age">(12 Jul '17, 20:43)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
<span id="57044"></span>
<div id="comment-57044" class="comment">
<div id="post-57044-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I mean, if I saw operator=<em>something other than "Travelodge"</em> on that parking.</p>
</div>
<div id="comment-57044-info" class="comment-info">
<span class="comment-age">(12 Jul '17, 20:44)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
<span id="57045"></span>
<div id="comment-57045" class="comment">
<div id="post-57045-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, operator will work in some cases but won't in others.</p>
</div>
<div id="comment-57045-info" class="comment-info">
<span class="comment-age">(12 Jul '17, 21:00)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-57039" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57039-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="57033"></span>

<div id="answer-container-57033" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57033-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-57033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi read these lines, <a href="http://wiki.openstreetmap.org/wiki/Key:access,">http://wiki.openstreetmap.org/wiki/Key:access,</a> following that you should use access=private and you could add access:conditional=customers "name". And add operator="name" to the area as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '17, 13:03</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-57033" class="comments-container">
&#10;</div>
<div id="comment-tools-57033" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57033-form-container" class="comment-form-container">
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

