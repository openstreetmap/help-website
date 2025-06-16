+++
type = "question"
title = "How can I change Nominatim&#x27;s reverse geocoding behaviour?"
description = '''I&#x27;m conducting some tests against nominatim.openstreetmap.org, looking at reverse geocoding. Based upon my observations I have two questions: 1) Given that I&#x27;m looking at data generated from a vehicle, this request and response are unexpected: http://nominatim.openstreetmap.org/reverse?lat=52.50676&amp;...'''
date = "2013-12-02T16:18:00Z"
lastmod = "2013-12-28T02:25:00Z"
weight = 28695
keywords = [ "reversegeocoding", "maxspeed", "nominatim" ]
aliases = [ "/questions/28695" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How can I change Nominatim's reverse geocoding behaviour?](/questions/28695/how-can-i-change-nominatims-reverse-geocoding-behaviour)

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
<span id="post-28695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28695-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm conducting some tests against nominatim.openstreetmap.org, looking at reverse geocoding. Based upon my observations I have two questions:</p>
<p>1) Given that I'm looking at data generated from a vehicle, this request and response are unexpected:</p>
<p><a href="http://nominatim.openstreetmap.org/reverse?lat=52.50676&amp;lon=-1.99523&amp;addressdetails=1&amp;format=json&amp;zoom=18">http://nominatim.openstreetmap.org/reverse?lat=52.50676&amp;lon=-1.99523&amp;addressdetails=1&amp;format=json&amp;zoom=18</a></p>
<pre><code>{&quot;place_id&quot;:&quot;9146383198&quot;,&quot;licence&quot;:&quot;Data \u00a9 OpenStreetMap contributors, ODbL 1.0. https://www.openstreetmap.org/copyright&quot;,&quot;osm_type&quot;:&quot;way&quot;,&quot;osm_id&quot;:&quot;60694393&quot;,&quot;lat&quot;:&quot;52.506753&quot;,&quot;lon&quot;:&quot;-1.9943365&quot;,&quot;display_name&quot;:&quot;CLOSED for 60 weeks from Sep 2013, Londonderry, Warley, Sandwell, West Midlands, England, B70 6AS, United Kingdom&quot;,&quot;address&quot;:{&quot;footway&quot;:&quot;CLOSED for 60 weeks from Sep 2013&quot;,&quot;neighbourhood&quot;:&quot;Londonderry&quot;,&quot;suburb&quot;:&quot;Warley&quot;,&quot;city&quot;:&quot;Sandwell&quot;,&quot;county&quot;:&quot;West Midlands&quot;,&quot;state_district&quot;:&quot;West Midlands&quot;,&quot;state&quot;:&quot;England&quot;,&quot;postcode&quot;:&quot;B70 6AS&quot;,&quot;country&quot;:&quot;United Kingdom&quot;,&quot;country_code&quot;:&quot;gb&quot;}}</code></pre>
<p>It seems that I need Nominatim to ignore ways with highway=footway - can I achieve this?</p>
<p>2) Can I ask for a reverse geocoded response to include other tag values? I have been able to find the maxspeed tag value by requesting an api lookup following the reverse geocode request, for example:</p>
<p><a href="http://api.openstreetmap.org/api/0.6/way/144176050">http://api.openstreetmap.org/api/0.6/way/144176050</a></p>
<p>This is ok but it would be far better if I could obtain the information from a single reverse geocode call as it seems reasonable to expect to be able to obtain other tag values from Nominatim. Is this possible? I note the Extra Tags shown from the Nominatim data here: <a href="http://nominatim.openstreetmap.org/details.php?place_id=9146205970">http://nominatim.openstreetmap.org/details.php?place_id=9146205970</a></p>
<p>If these things are not possible then I wonder if I could better achieve it I had my own Nominatim instance? I'm prepared to get into the Nominatim coding and make changes if necessary (but obviously need to consider the impact of the change and ensure it avoids any behavioural change for other contributors).</p>
<p>Thanks for any advice.</p>
<p>Note I also asked this question here: <a href="http://stackoverflow.com/questions/20331620/how-can-i-change-nominatims-reverse-geocoding-behaviour">http://stackoverflow.com/questions/20331620/how-can-i-change-nominatims-reverse-geocoding-behaviour</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Dec '13, 16:18</strong></p>
<img src="https://secure.gravatar.com/avatar/68791600aba005984a3eddbd82f6c0ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Elliveny&#39;s gravatar image" />
<p><span>Elliveny</span><br />
<span class="score" title="66 reputation points">66</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Elliveny has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Dec '13, 16:20</strong> </span></p>
</div>
</div>
<div id="comments-container-28695" class="comments-container">
&#10;</div>
<div id="comment-tools-28695" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28695-form-container" class="comment-form-container">
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

<span id="28711"></span>

<div id="answer-container-28711" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28711-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-28711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Elliveny has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Neither of these two problems can be solved with the current API. However, solutions are fairly easy to implement and would be a welcome addition to the API. If you know a bit of PHP and like to get your hands dirty, they are a good place to start contributing to Nominatim. For a more in-depth discussion on how to best proceed, join the <a href="https://lists.openstreetmap.org/listinfo/geocoding">geocoding mailinglist</a> or <a href="https://wiki.openstreetmap.org/wiki/Irc">#osm-nominatim on IRC</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '13, 09:14</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-28711" class="comments-container">
&#10;</div>
<div id="comment-tools-28711" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28711-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29394"></span>

<div id="answer-container-29394" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29394-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>if that way was named correctly (or not named at all). You would have gotten a better hit from a nearby source. I <a href="https://www.openstreetmap.org/changeset/19672738">fixed</a> that bad tagging for you in OSM in 5min. It will disappear eventually from nominatim too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Dec '13, 02:25</strong></p>
<img src="https://secure.gravatar.com/avatar/39f5ad4949a7d408894b29769069a869?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gplv2&#39;s gravatar image" />
<p><span>gplv2</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gplv2 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29394" class="comments-container">
&#10;</div>
<div id="comment-tools-29394" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29394-form-container" class="comment-form-container">
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

