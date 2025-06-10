+++
type = "question"
title = "Notification when reaching destination"
description = '''I am developing a Python app in which starting from a source point (given in lat, lon) after reaching a destination point I want to be notified after reaching my destination.  What I had actually thought to do was recalculating the current position of the user after some interval with calculating it...'''
date = "2020-06-02T10:32:00Z"
lastmod = "2020-06-04T07:59:00Z"
weight = 75091
keywords = [ "python", "routing", "osmrm" ]
aliases = [ "/questions/75091" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Notification when reaching destination](/questions/75091/notification-when-reaching-destination)

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
<span id="post-75091-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75091-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75091-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am developing a Python app in which starting from a source point (given in lat, lon) after reaching a destination point I want to be notified after reaching my destination.</p>
<p>What I had actually thought to do was recalculating the current position of the user after some interval with calculating its distance. When the distance becomes less than 0.1 to the destination. I'd assume that the user have reached the destination. (According to Haversine formula).</p>
<p>Could anyone pls suggest me a better approach with OSRM apis? as this approach would be compute-intensive.</p>
<p>Thanks in advance. Rachna.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-osmrm" rel="tag" title="see questions tagged &#39;osmrm&#39;">osmrm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '20, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/481f05d677d38b749a5f5de6d561c221?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rachnarai&#39;s gravatar image" />
<p><span>rachnarai</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rachnarai has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jun '20, 19:56</strong> </span></p>
</div>
</div>
<div id="comments-container-75091" class="comments-container">
<span id="75092"></span>
<div id="comment-75092" class="comment">
<div id="post-75092-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Converted comment (from <a href="https://help.openstreetmap.org/questions/12946/calculate-time-and-distance-between-two-latlng-points-with-a-json-response)">https://help.openstreetmap.org/questions/12946/calculate-time-and-distance-between-two-latlng-points-with-a-json-response)</a> to a question.</p>
</div>
<div id="comment-75092-info" class="comment-info">
<span class="comment-age">(02 Jun '20, 10:42)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="75094"></span>
<div id="comment-75094" class="comment">
<div id="post-75094-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't see why this involves a router at all. Just compare the current position with the position of the destination. If the calculated distance is small enough you have reached your destination. Why do you need a routing engine for this task?</p>
</div>
<div id="comment-75094-info" class="comment-info">
<span class="comment-age">(02 Jun '20, 14:11)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="75108"></span>
<div id="comment-75108" class="comment">
<div id="post-75108-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Alex, yes there won't be any need to do this. But after getting the current user location, at some interval I would need to calculate distance from that point to destination and this distance will be called several times until user reaches his destination. Will this approach be valid anyway? I'm doubtful about it, because I'd be needing to calculate distance periodically.</p>
</div>
<div id="comment-75108-info" class="comment-info">
<span class="comment-age">(02 Jun '20, 17:58)</span> <span class="comment-user userinfo">rachnarai</span>
</div>
</div>
<span id="75110"></span>
<div id="comment-75110" class="comment not_top_scorer">
<div id="post-75110-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you need to calculate the road distance periodically or just the bee line (you mentioned the Haversine formula in your question)?</p>
</div>
<div id="comment-75110-info" class="comment-info">
<span class="comment-age">(02 Jun '20, 19:40)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="75111"></span>
<div id="comment-75111" class="comment not_top_scorer">
<div id="post-75111-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just the Haversine formula, only concerned with comparison. Thats all</p>
</div>
<div id="comment-75111-info" class="comment-info">
<span class="comment-age">(02 Jun '20, 19:45)</span> <span class="comment-user userinfo">rachnarai</span>
</div>
</div>
<span id="75113"></span>
<div id="comment-75113" class="comment">
<div id="post-75113-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Then I can't see what you would need a router for, either. I repeat scai's question: Why do you believe you need a router? What is the router supposed to do?</p>
<p>Do you need something to geo-locate the destination? That would be a one-time call only and you don't have to repeat that with every distance calculation iteration.</p>
</div>
<div id="comment-75113-info" class="comment-info">
<span class="comment-age">(03 Jun '20, 10:01)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="75116"></span>
<div id="comment-75116" class="comment not_top_scorer">
<div id="post-75116-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would already have the destination geocode, but I would have to get the User's current location which would be changing repeatedly due to his moment.</p>
<p>So I need to compare this location until this current location matches the destination geocode.</p>
<p>Therefore, for this I would need to calculate distance until the distance becomes &lt; 0.1. (That's how we compare two geocodes)</p>
<p>Now coming to the question I have asked, I want to reduce the number of calls to my distance calculation function. (of course I would do this after some interval but this can be reduced if i get the estimated time.)</p>
<p>So, for that I wanted to get the estimated time in order to reach a point then after that if user couldn't reach there, I'd calculate estimated time again and check again whether he has reached. (Or by other way as this can be done in multiple ways.) So I had thought maybe this can reduce time complexity in order to accomplish this. Then I came across the OSRM routing engine which gives estimated time and distance but that will be too complicated and would be too compute intensive.</p>
<p>I'm hoping now that my question is clear, Awaiting for your thoughts and suggestions.</p>
</div>
<div id="comment-75116-info" class="comment-info">
<span class="comment-age">(03 Jun '20, 12:59)</span> <span class="comment-user userinfo">rachnarai</span>
</div>
</div>
<span id="75132"></span>
<div id="comment-75132" class="comment">
<div id="post-75132-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can calculate the ETA on your own by looking at distance and speed. Of course this will be less accurate than using a router. However it will also be much cheaper, so you can perform it more frequently. If the ETA is far in the future then use scarce recalculations, if the ETA is near or the distance is short then increase the recalculation frequency.</p>
</div>
<div id="comment-75132-info" class="comment-info">
<span class="comment-age">(04 Jun '20, 07:03)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="75133"></span>
<div id="comment-75133" class="comment not_top_scorer">
<div id="post-75133-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Calculating the distance is pretty cheap. So why not do something like this: If the bee-line distance is &gt; 5km re-calculate every minute. If the distance is &gt; 1km re-calculate every 10 seconds. After that re-calculate every second. I assume a car here. Intervals could be longer or shorter for foot traffic or an airplane.</p>
</div>
<div id="comment-75133-info" class="comment-info">
<span class="comment-age">(04 Jun '20, 07:59)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-75091" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-75091-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

