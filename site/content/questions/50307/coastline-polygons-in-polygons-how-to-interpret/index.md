+++
type = "question"
title = "Coastline polygons-in-polygons, how to interpret?"
description = '''There is a large number of polygons in polygons in the coastline data. The topology logic suggests that these should be interpreted as outer borders of lakes.  Unfortunately, this is just partly correct. So, the question is - do you have a well-tested criterion to check whether these polygons are mi...'''
date = "2016-06-19T10:14:00Z"
lastmod = "2016-06-20T15:12:00Z"
weight = 50307
keywords = [ "holes", "coasline", "interpretation" ]
aliases = [ "/questions/50307" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Coastline polygons-in-polygons, how to interpret?](/questions/50307/coastline-polygons-in-polygons-how-to-interpret)

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
<span id="post-50307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50307-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There is a large number of polygons in polygons in the coastline data. The topology logic suggests that these should be interpreted as outer borders of lakes. Unfortunately, this is just partly correct. So, the question is - do you have a well-tested criterion to check whether these polygons are missing lakes, missing islands or just erroneous tagging cases.<br />
If needed I can provide large number of illustrative cases/examples.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-holes" rel="tag" title="see questions tagged &#39;holes&#39;">holes</span> <span class="post-tag tag-link-coasline" rel="tag" title="see questions tagged &#39;coasline&#39;">coasline</span> <span class="post-tag tag-link-interpretation" rel="tag" title="see questions tagged &#39;interpretation&#39;">interpretation</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jun '16, 10:14</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></p>
</div>
</div>
<div id="comments-container-50307" class="comments-container">
<span id="50308"></span>
<div id="comment-50308" class="comment">
<div id="post-50308-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It would be very helpful to show at least one example.</p>
</div>
<div id="comment-50308-info" class="comment-info">
<span class="comment-age">(19 Jun '16, 11:10)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="50309"></span>
<div id="comment-50309" class="comment">
<div id="post-50309-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I second scai. Please link a region where the kind of data appears you talk about.</p>
</div>
<div id="comment-50309-info" class="comment-info">
<span class="comment-age">(19 Jun '16, 12:44)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
<span id="50320"></span>
<div id="comment-50320" class="comment">
<div id="post-50320-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There are many 100s polygons in polygons, all in the source coastline data. Examples: 1. missing lake here <a href="http://osm.org/go/euGUE19fV-">http://osm.org/go/euGUE19fV-</a> ; 2. land over land here <a href="http://osm.org/go/4lYpy4t">http://osm.org/go/4lYpy4t</a> ; 3. some more missing lakes here <a href="http://osm.org/go/S_yZx64">http://osm.org/go/S_yZx64</a> ; 4. missing (many) islands here <a href="http://osm.org/go/ud5K_gk--">http://osm.org/go/ud5K_gk--</a> (besides, riverbank and lake overlap)and so on. Just overlap the coastline data over the areas in links.</p>
</div>
<div id="comment-50320-info" class="comment-info">
<span class="comment-age">(19 Jun '16, 20:23)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
</div>
<div id="comment-tools-50307" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50307-form-container" class="comment-form-container">
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

<span id="50321"></span>

<div id="answer-container-50321" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50321-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Regarding your examples:</p>
<ol>
<li>has a beach mapped additionally to the coastline, nothing amiss.</li>
<li>coastline with reef and boundaries on them: can't see an error.</li>
<li>the "missing lakes" are mapped with coastlines going the wrong way.</li>
<li>is a messy combination of waterway=riverbank, natural=coastline and a multipolygon relation. I am not astonished that the renderer obviously is balky there.</li>
</ol>
<p>On the <a href="https://wiki.openstreetmap.org/wiki/Tag:natural%3Dcoastline">wiki</a> you can read for natural=coastline: <strong>land is on the left side and water on the right side</strong><br />
IMHO an easy-to-memorize-criterion.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '16, 20:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span> </br></p>
</div>
</div>
<div id="comments-container-50321" class="comments-container">
<span id="50322"></span>
<div id="comment-50322" class="comment">
<div id="post-50322-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Further to (1) someone's imported a bunch of OS Vector Map District and made it all coastline, when part of it (<a href="http://www.openstreetmap.org/way/255902449">http://www.openstreetmap.org/way/255902449</a> ) should be a small lake, not coastline at all.</p>
<p>Like any import, it just needs properly checking afterwards.</p>
</div>
<div id="comment-50322-info" class="comment-info">
<span class="comment-age">(19 Jun '16, 21:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50328"></span>
<div id="comment-50328" class="comment">
<div id="post-50328-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the (quick) answer. My question was pretty explicit and it was not meant to be provocation or irritation. I meat the many, many hundreds of coastline polygons-in-polygons issues when I try to resolve missing objects in other area classes (rivers, lakes, forests ...). The problem is that these polygons are in the OSM source data but confuse the renderers and researchers. The 1-4 example analyses in the answer even add more confusion. Just look at SomeoneElse's confrontation to your #1 text (thanks SomeoneElse) or just click over the layers in the link #2, and so on.</p>
</div>
<div id="comment-50328-info" class="comment-info">
<span class="comment-age">(20 Jun '16, 08:56)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
<span id="50329"></span>
<div id="comment-50329" class="comment">
<div id="post-50329-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I didn't think I was "confronting" anything....</p>
</div>
<div id="comment-50329-info" class="comment-info">
<span class="comment-age">(20 Jun '16, 08:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50336"></span>
<div id="comment-50336" class="comment">
<div id="post-50336-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/3194/sanser">@sanser</a>: I didn't feel provoked by you but seemingly still fail to get your point.<br />
By looking at the existing data, comparing it to aerial imagery and – if needed – looking at the mapping suggestions there is not much left to create confusion. IMHO</p>
</div>
<div id="comment-50336-info" class="comment-info">
<span class="comment-age">(20 Jun '16, 15:12)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
</div>
<div id="comment-tools-50321" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50321-form-container" class="comment-form-container">
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

