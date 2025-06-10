+++
type = "question"
title = "Why is that a wrong area is located for a postal code 94110 and country &quot;US&quot; ?"
description = '''Hi, When searching for a location, by giving postal code as &quot;94110&quot; and country as &quot;United States&quot; we get a wrong result, as it is showing a point inside a sea. FYR:- The address for this wrong location is &quot;San Francisco, California, 94110, United States&quot; , when you enter this address in OSM then yo...'''
date = "2023-05-30T21:12:00Z"
lastmod = "2023-06-02T07:04:00Z"
weight = 87324
keywords = [ "bug" ]
aliases = [ "/questions/87324" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why is that a wrong area is located for a postal code 94110 and country "US" ?](/questions/87324/why-is-that-a-wrong-area-is-located-for-a-postal-code-94110-and-country-us)

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
<span id="post-87324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87324-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>When searching for a location, by giving postal code as "94110" and country as "United States" we get a wrong result, as it is showing a point inside a sea.</p>
<p>FYR:- The address for this wrong location is "San Francisco, California, 94110, United States" , when you enter this address in OSM then you will get a point inside the sea.</p>
<p>Hope this is a bug and will be fixed soon.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 May '23, 21:12</strong></p>
<img src="https://secure.gravatar.com/avatar/2a094121950e4181aa4dc4ddeb1d371d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mohamed%20umar&#39;s gravatar image" />
<p><span>Mohamed umar</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mohamed umar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87324" class="comments-container">
<span id="87336"></span>
<div id="comment-87336" class="comment">
<div id="post-87336-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But postal code "94110" does not cover any island and it is a part of center of San Francisco. when we search postal code as "94110" and country code "US" it points in right of the San Francisco inside the sea, while Farallon islands are in left of the San Francisco</p>
</div>
<div id="comment-87336-info" class="comment-info">
<span class="comment-age">(02 Jun '23, 07:04)</span> <span class="comment-user userinfo">Mohamed umar</span>
</div>
</div>
</div>
<div id="comment-tools-87324" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87324-form-container" class="comment-form-container">
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

<span id="87325"></span>

<div id="answer-container-87325" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87325-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The search ends up looking for the City and County of San Francisco and it finds it. Then it centers things in the geometric center of the area.</p>
<p>The problem here is that the Farallon Islands are apparently part of the City and County of San Francisco so the geometric center is in the ocean between what a normal human would consider San Francisco and the islands.</p>
<p>Nominatim, the software that actually does this lookup is quite complicated as it has to deal with a whole world of different conventions. But it seems that a reasonable thing for it to do would be to return the location of the node in the relation that is marked as the label which would center the map at <a href="https://www.openstreetmap.org/node/26819236">https://www.openstreetmap.org/node/26819236</a></p>
<p>You may wish to submit a but to the project that develops and maintains Nominatim. I think the project is located at <a href="https://github.com/osm-search/Nominatim">https://github.com/osm-search/Nominatim</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 May '23, 21:23</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-87325" class="comments-container">
&#10;</div>
<div id="comment-tools-87325" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87325-form-container" class="comment-form-container">
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

