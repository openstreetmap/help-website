+++
type = "question"
title = "TIGER 2008 / CDP doesn&#x27;t look like what I&#x27;d expect in some cases (exclaves)"
description = '''Tried searching but couldn&#x27;t find anything specific to this issue. I&#x27;m starting editing with OSM and figured the best place to start is near where I live since I know that area well. Everything is going fine (I think...) but there&#x27;s some Administrative Boundary that I don&#x27;t understand. I live at the...'''
date = "2017-12-06T16:58:00Z"
lastmod = "2017-12-07T04:37:00Z"
weight = 61035
keywords = [ "tiger", "city_limits" ]
aliases = [ "/questions/61035" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [TIGER 2008 / CDP doesn't look like what I'd expect in some cases (exclaves)](/questions/61035/tiger-2008-cdp-doesnt-look-like-what-id-expect-in-some-cases-exclaves)

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
<span id="post-61035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61035-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Tried searching but couldn't find anything specific to this issue.</p>
<p>I'm starting editing with OSM and figured the best place to start is near where I live since I know that area well. Everything is going fine (I think...) but there's some Administrative Boundary that I don't understand. I live at the edge of a town. On the other side of the town boundary is a CDP. That would all be normal, but there's a normal of exclaves in OSM where there are pockets of the CDP close to the town Administrative Boundary, but wholly within it. This looks weird and doesn't match my expectations, but its very difficult to tell whether that's reality or not.</p>
<p>The Administrative Boundary has a source of "TIGER/Line 2008 Place Shapefiles".</p>
<p>Questions: 1) Is TIGER 2008 generally reliable? I don't want to modify/delete this until I'm certain. There's a number of these showing up currently. 2) How can I find a definition of CDPs so I can externally validate the boundaries of the CDP?</p>
<p>Apologies for not including a link to the location. It's a bit close to my house :) If a link would really help I'll try to find one that's a little bit less personally identifying.</p>
<p>ETA: After some digging I found a source on my county's GIS website (incredibly useful website...). Apparently there are many random holes out near the edge of the town that are not part of the town. So the TIGER data was correct, it just looks really weird.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiger" rel="tag" title="see questions tagged &#39;tiger&#39;">tiger</span> <span class="post-tag tag-link-city_limits" rel="tag" title="see questions tagged &#39;city_limits&#39;">city_limits</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Dec '17, 16:58</strong></p>
<img src="https://secure.gravatar.com/avatar/8de15b79a84b6c58ac6f7b58170d2b22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="treznor&#39;s gravatar image" />
<p><span>treznor</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="treznor has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Dec '17, 04:38</strong> </span></p>
</div>
</div>
<div id="comments-container-61035" class="comments-container">
<span id="61036"></span>
<div id="comment-61036" class="comment">
<div id="post-61036-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A link would be very helpful, so others can look at how things are tagged/mapped right now. Maybe find another spot a bit farther from home with the same situation?</p>
</div>
<div id="comment-61036-info" class="comment-info">
<span class="comment-age">(06 Dec '17, 17:32)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="61048"></span>
<div id="comment-61048" class="comment">
<div id="post-61048-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://www.openstreetmap.org/query?lat=35.76355&amp;lon=-81.26943">https://www.openstreetmap.org/query?lat=35.76355&amp;lon=-81.26943</a></p>
<p>This link shows the issue I'm describing (though in reverse, in this case its the city with an exclave in the CDP, same concept though). This is a tiny bit of Hickory in the St Stephens CDP. That may be reality, but I'd like to check it against something "official" to validate that. I just can't figure out what that something official would be exactly.</p>
<p>I also have small holes I've seen that are part of neither the town nor the CDP so would just be part of the county. Considering they're completely surrounding by the town, that's possible but unusual. Would like to confirm those are the real borders of town.</p>
</div>
<div id="comment-61048-info" class="comment-info">
<span class="comment-age">(06 Dec '17, 19:18)</span> <span class="comment-user userinfo">treznor</span>
</div>
</div>
<span id="61051"></span>
<div id="comment-61051" class="comment">
<div id="post-61051-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you clarify exactly what issue you're trying to resolve? Based on what I've read, a CDP is completely different and unrelated to a town boundary, so it may be perfectly normal for there to be overlap between these entities. Do you just want to find an authoritative source for the town boundary?</p>
</div>
<div id="comment-61051-info" class="comment-info">
<span class="comment-age">(06 Dec '17, 19:44)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="61054"></span>
<div id="comment-61054" class="comment">
<div id="post-61054-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>After having thought about it a bit more, I realize that the CDP is just a red herring as it just starts at the town boundary.</p>
<p>So yes, I'm looking for an authoritative source for the town boundary.</p>
</div>
<div id="comment-61054-info" class="comment-info">
<span class="comment-age">(06 Dec '17, 20:01)</span> <span class="comment-user userinfo">treznor</span>
</div>
</div>
<span id="61064"></span>
<div id="comment-61064" class="comment">
<div id="post-61064-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>After some digging I found a source on my county's GIS website (incredibly useful website...). Apparently there are many random holes out near the edge of the town that are not part of the town. So the TIGER data was correct, it just looks really weird.</p>
</div>
<div id="comment-61064-info" class="comment-info">
<span class="comment-age">(07 Dec '17, 04:37)</span> <span class="comment-user userinfo">treznor</span>
</div>
</div>
</div>
<div id="comment-tools-61035" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61035-form-container" class="comment-form-container">
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

<span id="61046"></span>

<div id="answer-container-61046" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61046-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61046-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61046-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="treznor has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>CDPs are defined as Census sees fit. There's some discussion of just deleting them being the best thing to do. If you want to update them I guess newer versions from Census would be the best source.</p>
<p>Municipal boundaries from Census seem to mostly be reasonable. I think they aren't particularly accurate overall though. Ideally you'd be able to track down an authoritative source that had a suitable license and use that to update the data in OSM. Short of that I wouldn't hesitate to make changes once you are pretty confident that the exclaves are incorrect.</p>
<p>I've been researching such sources for Michigan on and off and finally found <a href="http://www.michigan.gov/sos/0,4670,7-127-1638_8733_8750---,00.html">http://www.michigan.gov/sos/0,4670,7-127-1638_8733_8750---,00.html</a> by searching on "Michigan municipal city limits" (the municipal is just thrown in there to trick Google into avoiding results about Michigan City, Indiana).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '17, 19:11</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Dec '17, 19:16</strong> </span></p>
</div>
</div>
<div id="comments-container-61046" class="comments-container">
<span id="61050"></span>
<div id="comment-61050" class="comment">
<div id="post-61050-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Based on what I'm reading/seeing, I think I'm less worried about making sure the CDP boundary is correct and more worried about making sure the city limit is correct (which would fix the CDP boundary for a large portion of the CDP boundary since they're next to each other).</p>
<p>As a result, I'm following up on your suggestion of searching for the town limits. I'm not having a ton of luck so far, but I'll continue looking. My internet is a bit slow where I'm at currently, but hopefully I'll have better luck tonight. Generally what has a suitable license? I found an ArcGIS map that might be useful (downloading it is taking a while) and it says it doesn't have any rights limits, but I haven't had a chance to determine whether ArcGIS in general has a suitable license (wanted to see if the map was useful first). I'm assuming something directly from the county/town should have a suitable license, assuming I can find that somewhere? My county has a GIS site that I'm looking into, but again can't currently download enough information to tell if its useful.</p>
</div>
<div id="comment-61050-info" class="comment-info">
<span class="comment-age">(06 Dec '17, 19:38)</span> <span class="comment-user userinfo">treznor</span>
</div>
</div>
<span id="61052"></span>
<div id="comment-61052" class="comment">
<div id="post-61052-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately it's not safe to assume the license will be suitable. A lot of government data in the US is pretty unrestricted, but there are jurisdictions with exceptions. Getting the source entity to make a clear statement that the data can be contributed to OSM is the best thing.</p>
</div>
<div id="comment-61052-info" class="comment-info">
<span class="comment-age">(06 Dec '17, 19:59)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="61053"></span>
<div id="comment-61053" class="comment">
<div id="post-61053-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's annoying, but understood. I'll do what I can!</p>
</div>
<div id="comment-61053-info" class="comment-info">
<span class="comment-age">(06 Dec '17, 20:00)</span> <span class="comment-user userinfo">treznor</span>
</div>
</div>
</div>
<div id="comment-tools-61046" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61046-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61037"></span>

<div id="answer-container-61037" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61037-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I assume the CDP is tagged as an administrative boundary, and renders similarly to the town boundary. As per <a href="https://wiki.openstreetmap.org/wiki/United_States_admin_level#Not_all_boundaries_are_administrative">this wiki article</a>:</p>
<pre><code>Census Designated Places (CDPs) are boundaries maintained by the Census Bureau for statistical purposes. CDPs should be tagged boundary=census, ideally without an admin_level=* tag. In 2009, many CDPs were imported from TIGER as boundary=administrative + admin_level=8, but the talk-us mailing list reached a consensus to treat them as non-administrative boundaries.</code></pre>
<p>...in which case you probably just need to change the tags on the CDP.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '17, 17:43</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-61037" class="comments-container">
<span id="61049"></span>
<div id="comment-61049" class="comment">
<div id="post-61049-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't think this is the issue that I'm describing. However, I do see that the CDP border is created this way. I'll edit it shortly to reflect your guidance above (but it won't change the issue I'm describing, and linked to in a different comment).</p>
</div>
<div id="comment-61049-info" class="comment-info">
<span class="comment-age">(06 Dec '17, 19:19)</span> <span class="comment-user userinfo">treznor</span>
</div>
</div>
</div>
<div id="comment-tools-61037" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61037-form-container" class="comment-form-container">
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

