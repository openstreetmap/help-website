+++
type = "question"
title = "Limiting osm2pgsql import to street data for reverse geocoding only"
description = '''I want to set up a simple reverse geocoding system and was thinking of using osm2pgsql to import the data (possibly of the whole planet). I noticed that the data is very large and slow to import. Is it possible to import just the street data required to perform reverse geocoding?  If yes how do I go...'''
date = "2017-02-02T00:14:00Z"
lastmod = "2017-02-02T11:16:00Z"
weight = 54415
keywords = [ "reversegeocoding", "osm2pgsql" ]
aliases = [ "/questions/54415" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Limiting osm2pgsql import to street data for reverse geocoding only](/questions/54415/limiting-osm2pgsql-import-to-street-data-for-reverse-geocoding-only)

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
<span id="post-54415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54415-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to set up a simple reverse geocoding system and was thinking of using osm2pgsql to import the data (possibly of the whole planet). I noticed that the data is very large and slow to import. Is it possible to import just the street data required to perform reverse geocoding?</p>
<p>If yes how do I go about it, and how do I go about maintaining the database up to date (with osmosis or any alternative) without importing buildings or POIs which are not needed for reverse geocoding? My intention of course is to keep the database size down to only the data I need.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Feb '17, 00:14</strong></p>
<img src="https://secure.gravatar.com/avatar/e01618347bd158e35c34cce5bc006a92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jbx1&#39;s gravatar image" />
<p><span>jbx1</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jbx1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54415" class="comments-container">
&#10;</div>
<div id="comment-tools-54415" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54415-form-container" class="comment-form-container">
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

<span id="54419"></span>

<div id="answer-container-54419" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54419-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The main OpenStreetMap geocoder, Nominatim, is relatively complex and uses much more than just street data. You will likely re-invent the wheel when you build your own (reverse) geocoder, and you'll make a couple mistakes that Nominatim has made and learnt from in the past. But if you really want to set up your own:</p>
<p><code>osm2pgsql</code> has something called a "style file" which determines what to import. You could copy the default style file and remove everything that isn't a highway. Alternatively, you could use osmosis or osmfilter to first create a subset of the planet file that contains only the bits that interest you, and then import.</p>
<p>Note however that this approach will not give you house numbers or an admin hierarchy, i.e. you will be able to find out that a given location is in "Main Street" but not which city, county, country (or post code for that matter). If you want the admin hierarchy, you have to import <code>boundary=administrative</code> objects as well. Additionally some small villages or city quarters are mapped not as <code>boundary=administrative</code> but as <code>landuse=residential</code> or even as a single place node, all of which Nominatim would honour in its reverse geocoding response.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Feb '17, 07:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-54419" class="comments-container">
<span id="54424"></span>
<div id="comment-54424" class="comment">
<div id="post-54424-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply. In actual fact I would like to use Nominatim, but I was wondering if I can remove stuff which is not needed, like building information, points of interest etc. to reduce the database size. I only need reverse geocoding (not geocoding). I had a look at Nominatim's reverse geocoder and it seems to be just an sql query, enlarging the diameter iteratively if the initial query doesn't return any results from the <code>placex</code> table. The extra stuff it seems to do is that it interpolates house numbers if the house cannot be determined directly, and if it still cannot determine it, and the country code is in the US, it uses the TIGER data set to try and find the house. There is an extra check for whether the place is too small, in which case its parent is taken. Other than that there doesn't seem to be much.</p>
<p>My application is related to transportation movement tracking, so going down to the granularity of house number is not really needed (at least not at this point). I will need village, city, country etc. of course.</p>
<p>Would Nominatim still work if I only import highways, administrative boundaries and maybe the special land use residential boundaries?</p>
</div>
<div id="comment-54424-info" class="comment-info">
<span class="comment-age">(02 Feb '17, 10:24)</span> <span class="comment-user userinfo">jbx1</span>
</div>
</div>
<span id="54426"></span>
<div id="comment-54426" class="comment">
<div id="post-54426-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I agree with Frederick's approach. By default Nominatim also fills search index tables only used for forward search (think: word =&gt; list of places). The logic is too deep in the import and data update steps that it can't be easily disabled. And while deleting the (for reverse unused) tables after the initial update would work the updates would fail. As Richard points out have a look at Photon, I think there's monthly data dumps to import now. Takes 60GB disc space.</p>
</div>
<div id="comment-54426-info" class="comment-info">
<span class="comment-age">(02 Feb '17, 11:16)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-54419" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54419-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54422"></span>

<div id="answer-container-54422" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54422-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You may find it easiest to set up a local instance of Photon (<a href="https://github.com/komoot/photon),">https://github.com/komoot/photon),</a> which has reverse geocoding capabilities and for which you can download pre-made data dumps. Note however that Photon development appears to be rather in abeyance.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Feb '17, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-54422" class="comments-container">
&#10;</div>
<div id="comment-tools-54422" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54422-form-container" class="comment-form-container">
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

