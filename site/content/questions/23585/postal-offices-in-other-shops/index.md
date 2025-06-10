+++
type = "question"
title = "Postal offices in other shops"
description = '''In Germany we have many postal offices in other shops like bakery etc. Is it necessary to tag both as individual POIs or is a way to describe that there is a postal-office from Deutsche Post, Hermes, DHL etc. in a shop? As the have the same opening hours, phone number, location etc. it seems not to ...'''
date = "2013-06-21T18:10:00Z"
lastmod = "2013-06-21T19:59:00Z"
weight = 23585
keywords = [ "post", "parcel" ]
aliases = [ "/questions/23585" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Postal offices in other shops](/questions/23585/postal-offices-in-other-shops)

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
<span id="post-23585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23585-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In Germany we have many postal offices in other shops like bakery etc. Is it necessary to tag both as individual POIs or is a way to describe that there is a postal-office from Deutsche Post, Hermes, DHL etc. in a shop?</p>
<p>As the have the same opening hours, phone number, location etc. it seems not to create seperate POIs.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-post" rel="tag" title="see questions tagged &#39;post&#39;">post</span> <span class="post-tag tag-link-parcel" rel="tag" title="see questions tagged &#39;parcel&#39;">parcel</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jun '13, 18:10</strong></p>
<img src="https://secure.gravatar.com/avatar/7ef3a3c25492438c9f0e5a548a36fa07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ogmios&#39;s gravatar image" />
<p><span>Ogmios</span><br />
<span class="score" title="766 reputation points">766</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ogmios has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-23585" class="comments-container">
&#10;</div>
<div id="comment-tools-23585" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23585-form-container" class="comment-form-container">
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

<span id="23586"></span>

<div id="answer-container-23586" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23586-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23586-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-23586-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ogmios has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, the accepted method is to add one POI per shop. The rule is "one entity, one OSM object", and if the postal offices is somehow separate from the rest of the shop (even if it's only a separate counter), then a POI of its own seems appropriate.</p>
<p>As to the opening hours, address etc: There is no need to map them redundantly. Map the main shop as an area, and put the POI node inside that area. Then just tag the main shop; most people (and hopefully software) will understand that the opening hours are "inherited" from the main shop (because the POI is located inside the shop).</p>
<p>This "inheritance" is used in several cases in OSM: For example, when tagging sites with a large area and several buildings (schools, big companies), typically all tags (name, type etc.) go on the area, and the buildings only get tags specific to that building.</p>
<p>That said, you <em>could</em> also just put multiple tags on the main shop; but this only works well if the tags do not conflict: <code>shop=supermarket</code> and <code>amenity=post_office</code> would work, but e.g. a bakery inside a supermarket would not (because both use <code>shop=</code>).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '13, 19:16</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jun '13, 19:18</strong> </span></p>
</div>
</div>
<div id="comments-container-23586" class="comments-container">
<span id="23589"></span>
<div id="comment-23589" class="comment">
<div id="post-23589-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much. Your answer was most helpful. Maybe you could have a look: <a href="http://osm.org/go/0Gtqz2HMx--">http://osm.org/go/0Gtqz2HMx--</a></p>
<p>But I'm still not sure how to get the "inherited" address and opening hours when using the data in a website.</p>
</div>
<div id="comment-23589-info" class="comment-info">
<span class="comment-age">(21 Jun '13, 19:59)</span> <span class="comment-user userinfo">Ogmios</span>
</div>
</div>
</div>
<div id="comment-tools-23586" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23586-form-container" class="comment-form-container">
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

