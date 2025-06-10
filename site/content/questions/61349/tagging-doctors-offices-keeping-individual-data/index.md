+++
type = "question"
title = "Tagging doctor&#x27;s offices, keeping individual data"
description = '''In France, it is common to have small doctor offices consisting of 2-10 doctors, each with their own name and speciality, but without a brand or somehow identifiable common name (other than generic &quot;Medical group&quot; names or so). Therefore, doctors are identified by their names only, typically with sm...'''
date = "2017-12-24T18:06:00Z"
lastmod = "2018-05-06T21:39:00Z"
weight = 61349
keywords = [ "tagging", "healthcare" ]
aliases = [ "/questions/61349" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Tagging doctor's offices, keeping individual data](/questions/61349/tagging-doctors-offices-keeping-individual-data)

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
<span id="post-61349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61349-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-61349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In France, it is common to have small doctor offices consisting of 2-10 doctors, each with their own name and speciality, but without a brand or somehow identifiable common name (other than generic "Medical group" names or so). Therefore, doctors are identified by their names only, typically with smal plaques at the entrance of the building stating each doctor's name and speciality.</p>
<p>The <code>amenity=doctors</code> tag seems the right one for this kind of place, however I wonder how should the names be filled in, ideally so that people searching for that doctor's name will be able to find his/her office (similarly to what one can do in Google Maps).</p>
<p>Should I put all doctor's names separated by semicolons, instead of "Medical group"? Also, how could one map each doctor to its speciality, if all specialities are grouped in the <code>healthcare:speciality</code> tag?</p>
<p>I though of the other possibility of doing it, that is, creating a different node for each doctor, but this is less than ideal:</p>
<ul>
<li>It pollutes the visual (so many names, so close to each other, inevitably lead to some names not being readable in most renderers);</li>
<li>Ideally, one should know exactly where each office is, but short of visiting them individually and knowing where in the building each doctor is, I'd have to just clump them together somehow near the building entrance;</li>
<li>In some cases, they have a secretary and a common phone number, but in other cases each has their own phone number, so once again, clumping them together would lose information.</li>
</ul>
<p>In the end, I think that adding a node for the medical group itself, with all specialities, plus a separate node for each doctor, with their specific name, speciality and phone number, would be the only way to preserve all data, but this would require "inventing" their exact locations, plus would be a bit of an overkill.</p>
<p>Is there a good example of how to do it in practice?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-healthcare" rel="tag" title="see questions tagged &#39;healthcare&#39;">healthcare</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Dec '17, 18:06</strong></p>
<img src="https://secure.gravatar.com/avatar/395b52b769f88f777174aeadaaf4be12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="voyageant&#39;s gravatar image" />
<p><span>voyageant</span><br />
<span class="score" title="181 reputation points">181</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="voyageant has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61349" class="comments-container">
&#10;</div>
<div id="comment-tools-61349" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61349-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="61354"></span>

<div id="answer-container-61354" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61354-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="voyageant has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Good thoughts! I would use your suggestion in the penultimate paragraph ("In the end …").</p>
<p>However, if two or three doctors share <em>one</em> office with <em>one</em> speciality, I would merge them and not tag them individually. The individual names are likely reflected in the <code>name</code> (e.g. "Hausärztliche Gemeinschaftspraxis Dr. Meier &amp; Müller") and also could fit into the <code>operator</code> tag with a semicolon.</p>
<p>You are talking about renderers: well, yes, most usual maps will not be able to display all the docs. But they could (automatically!) show a group POI icon which expends on click or something like that. Special maps can show name markers with arrows pointing to the docs. And the prime usage example for the individual tagging is searching for special doctors - e.g. in a page like "<a href="/questions/61129/is-there-a-site-or-service-which-works-like-the-yellow-pages-for-osm-data">OSM yellow pages</a>" or in your navigation software like OsmAnd.</p>
<p>I see no issue in "inventing" locations (except if you go for indoor mapping the building). I would map them in a cluster of nodes, each spaced a bit apart, so clicking them is not too hard. Maybe add a note tag that the position is "symbolic". If, later, someone knows the correct location in the building, the node can be moved - a usual principle (refinement) in OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Dec '17, 11:20</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Dec '17, 11:20</strong> </span></p>
</div>
</div>
<div id="comments-container-61354" class="comments-container">
&#10;</div>
<div id="comment-tools-61354" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61354-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63348"></span>

<div id="answer-container-63348" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63348-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Individual offices do not always contain the names of the doctors.</p>
<p>I sympathize with the original questioners solution.</p>
<p>Better would be a field within healthcare which lists individual practioners, but this field does not currently seem to exist.</p>
<p>My example:</p>
<p>Good Samaritan Hospital Hearth Rhythm Center</p>
<p>has 3 MDs</p>
<p>I want to look up my specific MD, but always want to list the office</p>
<p>All 3 MDs should be listed</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '18, 17:53</strong></p>
<img src="https://secure.gravatar.com/avatar/96cceebb21bf8e94d09c377653972afd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nereocystis&#39;s gravatar image" />
<p><span>nereocystis</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nereocystis has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63348" class="comments-container">
&#10;</div>
<div id="comment-tools-63348" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63348-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63351"></span>

<div id="answer-container-63351" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63351-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've mapped similar small multi-doctor offices in New York City. I generally use separate nearby nodes if the doctors each have their own phone numbers, and otherwise use a single node with the doctors' names listed as a description.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '18, 18:59</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-63351" class="comments-container">
&#10;</div>
<div id="comment-tools-63351" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63351-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63352"></span>

<div id="answer-container-63352" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63352-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I had almost made the same decision as <a href="https://help.openstreetmap.org/users/14350/jmapb">@jmapb</a>, adding doctor's names in description.</p>
<p>Then I made some tests.</p>
<p>I want to be able to search on the doctor's name, as well as the name of the clinic.</p>
<p>Searching on info in the description doesn't seem to work with osmand, or with openstreetmap.org web interface. This could be fixed in both interfaces, but I don't think that it is enough.</p>
<p>There should be a description of the standard practice in the wiki for amenity=doctors, and healthcare=*</p>
<p>If doctors are to be listed in a subfield, there should be a standard subfield, with the names separated by semicolons, perhaps.</p>
<p>Until then, I am strongly thinking of using <a href="https://help.openstreetmap.org/users/14436/voyageant">@voyageant</a> suggestion, with the office as an area, and individual nodes for each doctor.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '18, 20:10</strong></p>
<img src="https://secure.gravatar.com/avatar/96cceebb21bf8e94d09c377653972afd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nereocystis&#39;s gravatar image" />
<p><span>nereocystis</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nereocystis has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63352" class="comments-container">
<span id="63354"></span>
<div id="comment-63354" class="comment">
<div id="post-63354-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hmm, I guess I'm not too surprised to hear that the description fields are not indexed for search. Some people might frown on "tagging for the search" as they do "tagging for the renderer" but I agree that the ideal would be to have to a standard key where doctors' names can comfortably reside, allowing a map application to return a clinic when the corresponding doctor is sought.</p>
<p>There might be a syntax that would be applicable to other sorts of amenities as well. I've seen dentists, veterinarians, estate agents, law offices, and even hairdressers that advertise their personnel by name outside the business. Perhaps consider a general <code>personnel=*</code> or <code>staff=*</code> tag that permits semicolon-separated values.</p>
</div>
<div id="comment-63354-info" class="comment-info">
<span class="comment-age">(06 May '18, 21:19)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="63355"></span>
<div id="comment-63355" class="comment">
<div id="post-63355-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Something like personell= <em>and staff=</em> sounds like a good idea.</p>
</div>
<div id="comment-63355-info" class="comment-info">
<span class="comment-age">(06 May '18, 21:39)</span> <span class="comment-user userinfo">nereocystis</span>
</div>
</div>
</div>
<div id="comment-tools-63352" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63352-form-container" class="comment-form-container">
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

