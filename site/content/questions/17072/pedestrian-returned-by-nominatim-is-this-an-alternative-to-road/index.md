+++
type = "question"
title = "&quot;Pedestrian&quot; returned by Nominatim.  Is this an alternative to &quot;road&quot;?"
description = '''Hi A couple of addresses in the capital raise some questions in Nominatim - tested calling via api  (A) &quot;http://nominatim.openstreetmap.org/search?format=json&amp;amp;q=2400 Pennsylvania Avenue Northwest, Washington, DC 20037&amp;amp;countrycodes=US&amp;amp;addressdetails=1&quot; Postcode is specified - however Nomi...'''
date = "2012-10-21T16:42:00Z"
lastmod = "2012-10-22T15:43:00Z"
weight = 17072
keywords = [ "nominatim" ]
aliases = [ "/questions/17072" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# ["Pedestrian" returned by Nominatim. Is this an alternative to "road"?](/questions/17072/pedestrian-returned-by-nominatim-is-this-an-alternative-to-road)

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
<span id="post-17072-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17072-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17072-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>A couple of addresses in the capital raise some questions in Nominatim - tested calling via api</p>
<p>(A) "http://nominatim.openstreetmap.org/search?format=json&amp;q=2400 Pennsylvania Avenue Northwest, Washington, DC 20037&amp;countrycodes=US&amp;addressdetails=1"</p>
<p>Postcode is specified - however Nominatim returns 2x places - one postcode 20037 - one postcode 20006 - why was the 20006 result included?</p>
<p>No house_number is returned in either case - why is that?</p>
<p>(B) "http://nominatim.openstreetmap.org/search?format=json&amp;q=1600 Pennsylvania Avenue Northwest&amp;countrycodes=US&amp;addressdetails=1"</p>
<p>Instead of returning "road" address component - Nominatim returns "pedestrian" as "Pennsylvania Avenue Northwest" - why is this? Is this an alternative to "road" - are there any other names by which "road" may be returned?</p>
<p>Thanks!</p>
<p>Regards</p>
<p>Julian</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Oct '12, 16:42</strong></p>
<img src="https://secure.gravatar.com/avatar/ef5277fef092958525333343e415e6ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Julian88&#39;s gravatar image" />
<p><span>Julian88</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Julian88 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Oct '12, 18:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-17072" class="comments-container">
&#10;</div>
<div id="comment-tools-17072" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17072-form-container" class="comment-form-container">
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

<span id="17102"></span>

<div id="answer-container-17102" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17102-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(A1) Short answer: Nominatim thinks that the street goes through two postcode areas and returns both.</p>
<p>Long answer: Postcodes are currently saved mostly as points in the Nominatim database, not as an area. As this is not very precise, Nominatim also returns results that are (spatially) close to the postcode you requested but are annotated with a different one. It does not filter results where only the postcode differs. But the result with the postcode from the query should always appear higher in the list.</p>
<p>(A2) As for the house number, if you have a look at the <a href="http://nominatim.openstreetmap.org/details.php?osmtype=W&amp;osmid=66417794">details page for the house</a>, you can see that Nominatim did not put it into the city of Washington. This looks suspiciously like a bug, the neighbouring streets seem fine.</p>
<p>(B) The label that is returned for roads depends on the highway tag. Currently, the following may be returned: Road(for anything a 4-wheeled vehicle can use), Footway, Pedestrian, Cycleway, Bridleway. (You may get others if there is a typo in the highway tag or somebody invented a new value but that should be so rare that it can be safely ignored.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '12, 15:43</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-17102" class="comments-container">
&#10;</div>
<div id="comment-tools-17102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17102-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17083"></span>

<div id="answer-container-17083" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17083-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17083-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17083-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(A) You can use Nominatim's <a href="http://nominatim.openstreetmap.org/search.php?q=2400+Pennsylvania+Avenue+Northwest%2C+Washington%2C+DC+20037&amp;viewbox=-337.5%2C84.7%2C337.5%2C-79.2">web search</a> to find out. It returns two results, <a href="http://nominatim.openstreetmap.org/details.php?place_id=53784449">53784449</a> and <a href="http://nominatim.openstreetmap.org/details.php?place_id=51321945">51321945</a>. Both are the <em>Pennsylvania Avenue Northwest</em>, but one belongs to the suburb <a href="https://www.openstreetmap.org/browse/node/158249984">Georgetown</a> and the other one to the suburb <a href="http://nominatim.openstreetmap.org/details.php?place_id=51321945">Farragut Square</a>. Both suburbs are just nodes in OSM so Nominatim has to guess their sizes. If you think this is incorrect, try adding both suburbs as an area.</p>
<p>(B) According to <a href="http://rdoc.info/github/jakubsvehla/nominatim/master/Nominatim/Address">this documentation</a> there seems to be only road and pedestrian as the smallest elements, but that's just a guess and it's not the official documentation (if there is any at all). Better ask twain or lonvia about this issue.</p>
<p>Note that depending on the object you are searching for neither road nor pedestrian has to be returned as Nominatim does not only search for street addresses but for everything. Thus it can also happen that you just get something like "POI, suburb, city, country" without a road/house number part.</p>
<p>After taking a short look at the code I think every <a href="https://trac.openstreetmap.org/browser/applications/utils/nominatim/lib/lib.php#L291">class</a> label can be returned, so there are lots of alternatives to <em>road</em> and <em>pedestrian</em>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '12, 06:20</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Oct '12, 07:29</strong> </span></p>
</div>
</div>
<div id="comments-container-17083" class="comments-container">
&#10;</div>
<div id="comment-tools-17083" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17083-form-container" class="comment-form-container">
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

