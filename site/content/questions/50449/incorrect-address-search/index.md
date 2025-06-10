+++
type = "question"
title = "incorrect address search"
description = '''A little frustrated. We are about to launch a new website that uses a plugin to map with openstreetmap. The problem is when it searches (1404 W Covina Blvd, San Dimas, CA 91773) It finds it 2 miles away from our real building which I have placed in the system (http://nominatim.openstreetmap.org/deta...'''
date = "2016-06-24T17:26:00Z"
lastmod = "2016-07-06T06:59:00Z"
weight = 50449
keywords = [ "incorrect", "search", "address" ]
aliases = [ "/questions/50449" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [incorrect address search](/questions/50449/incorrect-address-search)

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
<span id="post-50449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50449-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A little frustrated. We are about to launch a new website that uses a plugin to map with openstreetmap. The problem is when it searches (1404 W Covina Blvd, San Dimas, CA 91773) It finds it 2 miles away from our real building which I have placed in the system (<a href="http://nominatim.openstreetmap.org/details.php?place_id=2621271778).">http://nominatim.openstreetmap.org/details.php?place_id=2621271778).</a> The frustrating part that I can't fix is when you look at the address portion of our church it mentions place:hamlet as Charter Oak Mobile Estates which is where the incorrect search goes to. We are not anywhere near that place. Can someone assist me on how to get this correct?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-incorrect" rel="tag" title="see questions tagged &#39;incorrect&#39;">incorrect</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jun '16, 17:26</strong></p>
<img src="https://secure.gravatar.com/avatar/02250a8ec3a1fc5960c99e8aeb0bf6d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="randyaccv&#39;s gravatar image" />
<p><span>randyaccv</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="randyaccv has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50449" class="comments-container">
&#10;</div>
<div id="comment-tools-50449" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50449-form-container" class="comment-form-container">
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

<span id="50454"></span>

<div id="answer-container-50454" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50454-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do not use abbreviated street names: <a href="http://nominatim.openstreetmap.org/search.php?q=1404+West+Covina+Boulevard%2C+Charter+Oak+Mobile+Estates%2C+Los+Angeles+County&amp;polygon=1&amp;viewbox=">example</a>.</p>
<p>I guess that <a href="http://nominatim.openstreetmap.org/search.php?q=1404+W+Covina+Blvd%2C+San+Dimas%2C+CA+91773&amp;polygon=1&amp;viewbox=">your search</a> finds a location somewhere else, because there the abbreviated names have been explicitly mapped: <a href="https://www.openstreetmap.org/way/401215294">https://www.openstreetmap.org/way/401215294</a> - not really good. That should be done by software. I not sure why Nominatim evaluates those Tiger tags at all.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '16, 23:32</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-50454" class="comments-container">
<span id="50455"></span>
<div id="comment-50455" class="comment">
<div id="post-50455-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This does not fix my issue. Even when I search for 1404 West Covina Boulevard, my address doesn't come up even though I have created a node for it.</p>
</div>
<div id="comment-50455-info" class="comment-info">
<span class="comment-age">(25 Jun '16, 01:01)</span> <span class="comment-user userinfo">randyaccv</span>
</div>
</div>
<span id="50456"></span>
<div id="comment-50456" class="comment">
<div id="post-50456-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When I search for "1404 West Covina Boulevard" or "West Covina Boulevard 1404" I get two results: A house in the middle of the road and a worship place.</p>
</div>
<div id="comment-50456-info" class="comment-info">
<span class="comment-age">(25 Jun '16, 09:46)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
<span id="50457"></span>
<div id="comment-50457" class="comment">
<div id="post-50457-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/12466/randyaccv">@randyaccv</a>: could you please post a link to a search with an unabbreviated address, so we can reproduce your experience?</p>
</div>
<div id="comment-50457-info" class="comment-info">
<span class="comment-age">(25 Jun '16, 12:03)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="50458"></span>
<div id="comment-50458" class="comment">
<div id="post-50458-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Looks like this query will do it: <a href="http://www.openstreetmap.org/search?query=1404%20West%20Covina%20Boulevard#map=16/34.1004/-117.8242">http://www.openstreetmap.org/search?query=1404%20West%20Covina%20Boulevard#map=16/34.1004/-117.8242</a></p>
<p>The tiger tags ought to be removed from those road sections but regardless, I don't see why they are being picked over <a href="http://www.openstreetmap.org/way/426625081#map=19/34.09874/-117.83605">http://www.openstreetmap.org/way/426625081#map=19/34.09874/-117.83605</a> as the tagging on the church looks okay to me other than maybe adding a denomination tag which should not affect address based searches.</p>
</div>
<div id="comment-50458-info" class="comment-info">
<span class="comment-age">(25 Jun '16, 16:00)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="50637"></span>
<div id="comment-50637" class="comment">
<div id="post-50637-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there anyone who can speak into why a road that is miles long is only returning 2 small sections in the nominatim search? That looks like the core of the issue since everything else is in place.</p>
</div>
<div id="comment-50637-info" class="comment-info">
<span class="comment-age">(05 Jul '16, 17:25)</span> <span class="comment-user userinfo">randyaccv</span>
</div>
</div>
<span id="50638"></span>
<div id="comment-50638" class="comment not_top_scorer">
<div id="post-50638-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>@randayaccv It probably boils down to "because it is currently implemented that way and nobody improved it yet". I guess it isn't easy to fix.</p>
</div>
<div id="comment-50638-info" class="comment-info">
<span class="comment-age">(05 Jul '16, 20:42)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="50654"></span>
<div id="comment-50654" class="comment not_top_scorer">
<div id="post-50654-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I thought nominatim (on osm.org) only returned the first result when all the other tags are the same. I expect that the 2 sections you see will have e.g. a different road classification or are located in different towns.</p>
</div>
<div id="comment-50654-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 06:59)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-50454" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-50454-form-container" class="comment-form-container">
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

