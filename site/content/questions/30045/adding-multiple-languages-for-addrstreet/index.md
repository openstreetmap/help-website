+++
type = "question"
title = "Adding Multiple Languages for addr:street"
description = '''Hello Everyone! I am new to OpenStreetMap. I primarily speak English but I have been adding tags to various places I have been in Ukraine. I want to add tags in both Ukrainian and English but I am not sure the best way to handle this. I have been adding a new tag &quot;addr:street:en&quot; but I don&#x27;t know if...'''
date = "2014-01-21T21:36:00Z"
lastmod = "2014-01-22T07:37:00Z"
weight = 30045
keywords = [ "addr_city", "addr_street", "addresses" ]
aliases = [ "/questions/30045" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Adding Multiple Languages for addr:street](/questions/30045/adding-multiple-languages-for-addrstreet)

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
<span id="post-30045-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30045-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30045-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello Everyone!</p>
<p>I am new to OpenStreetMap. I primarily speak English but I have been adding tags to various places I have been in Ukraine. I want to add tags in both Ukrainian and English but I am not sure the best way to handle this. I have been adding a new tag "addr:street:en" but I don't know if this is actually accomplishing anything. How do I create a tag for addr:street, addr:city, etc. in multiple languages without disrupting the tag in the local language?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-addr_city" rel="tag" title="see questions tagged &#39;addr_city&#39;">addr_city</span> <span class="post-tag tag-link-addr_street" rel="tag" title="see questions tagged &#39;addr_street&#39;">addr_street</span> <span class="post-tag tag-link-addresses" rel="tag" title="see questions tagged &#39;addresses&#39;">addresses</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '14, 21:36</strong></p>
<img src="https://secure.gravatar.com/avatar/cc149af9594f960e197e3f2b46f3dbb0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="duphii&#39;s gravatar image" />
<p><span>duphii</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="duphii has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jan '14, 21:47</strong> </span></p>
</div>
</div>
<div id="comments-container-30045" class="comments-container">
<span id="30063"></span>
<div id="comment-30063" class="comment">
<div id="post-30063-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please note that, in general, we use the language variants :ua :en etc. for objects that actually have a commonly used name in the language in question not for translations. The exception being transliterations.</p>
</div>
<div id="comment-30063-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 07:37)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30045" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30045-form-container" class="comment-form-container">
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

<span id="30047"></span>

<div id="answer-container-30047" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30047-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="duphii has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While there <em>are</em> a few <a href="http://taginfo.openstreetmap.org/search?q=addr%3Astreet">instances of addr:street:XX in the db</a>, I don't think they are usefull, because the single "name" tag will link back to the actual street way, which has all the names. This work even better if you use an <a href="http://wiki.openstreetmap.org/wiki/Relation:associatedStreet">associatedstreet relation</a> instead of the addr:street tag.</p>
<p>A search on nominatim for one of the name:xx value works just fine without using extra addr:street:XX tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '14, 23:03</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-30047" class="comments-container">
&#10;</div>
<div id="comment-tools-30047" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30047-form-container" class="comment-form-container">
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

