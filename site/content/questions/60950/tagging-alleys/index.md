+++
type = "question"
title = "Tagging Alleys"
description = '''Hello! I am a relative newbie and I have noticed an issue in my city since the last time I came in to edit. Alleys are now mapped and indicated by highway=service service=alley. That seems good. The issue I see is that Allowed Access is set to All=Yes. City Code says that all alleys in the city are ...'''
date = "2017-12-02T14:32:00Z"
lastmod = "2017-12-02T16:58:00Z"
weight = 60950
keywords = [ "mass_tagging", "alleys", "private" ]
aliases = [ "/questions/60950" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tagging Alleys](/questions/60950/tagging-alleys)

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
<span id="post-60950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60950-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello! I am a relative newbie and I have noticed an issue in my city since the last time I came in to edit. Alleys are now mapped and indicated by highway=service service=alley. That seems good. The issue I see is that Allowed Access is set to All=Yes. City Code says that all alleys in the city are restricted (see below). My questions:</p>
<ol>
<li>Should these be set to Allowed Access All=Private or All=No? Since owners can use it on a limited basis, I am leaning towards private.</li>
<li>Is there any way this can be fixed for the entire city instead of doing this one-by-one?</li>
</ol>
<p>Area example: <a href="https://www.openstreetmap.org/edit#map=19/33.38303/-111.93356">https://www.openstreetmap.org/edit#map=19/33.38303/-111.93356</a></p>
<p>City Code: Sec. 29 -25. Use of alleys as thoroughfares. No person shall use an alley within the city as a thoroughfare except authorized emergency vehicles, property owners, residents, and tenants within the boundaries of their property, performing loading and unloading from their property, or vehicles otherwise authorized by the city. The chief of police or his designee is designated as the enforcing agent of this section. A violation of this section shall be a class three (3) misdemeanor.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mass_tagging" rel="tag" title="see questions tagged &#39;mass_tagging&#39;">mass_tagging</span> <span class="post-tag tag-link-alleys" rel="tag" title="see questions tagged &#39;alleys&#39;">alleys</span> <span class="post-tag tag-link-private" rel="tag" title="see questions tagged &#39;private&#39;">private</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Dec '17, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/4096afc0846cbc1ac3eefa6ebdef462d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="calliaz&#39;s gravatar image" />
<p><span>calliaz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="calliaz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60950" class="comments-container">
&#10;</div>
<div id="comment-tools-60950" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60950-form-container" class="comment-form-container">
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

<span id="60957"></span>

<div id="answer-container-60957" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60957-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi calliaz</p>
<p>The correct tagging would either be vehicle=destination or motor_vehicle=destination depending on if the regulation applies to bicycles etc. too, or just motor vehicles. Note this doesn't catch every nuance of the code, but should be good enough.</p>
<p>There is currently no established way to change the default access for smaller areas (or even large ones) so you will have to change the tags (semi-)manually, I would suggest using JOSM if you want to do that systematically. Otherwise there is no problem with you slowly changing the tags when you are surveying an areas in any case (I suspect, that there are likely exceptions to the rules, as always that are best captured on the ground).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '17, 16:53</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Dec '17, 16:53</strong> </span></p>
</div>
</div>
<div id="comments-container-60957" class="comments-container">
&#10;</div>
<div id="comment-tools-60957" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60957-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60958"></span>

<div id="answer-container-60958" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60958-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The legal access could also be "destination" (less restricted than "private", but not open to everyone). The Java based editor, JOSM, makes it easier to select and tag many objects. There's not yet a way to do it on the web editor.</p>
<p>On the other hand, the service=alley tag will already imply less than full access to most users of data. So you could just not worry too much about it. Here's one of the demo routing engines on the website not using the alley for through travel:</p>
<p><a href="https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=33.38342%2C-111.93331%3B33.38266%2C-111.92972#map=18/33.38281/-111.93146">https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=33.38342%2C-111.93331%3B33.38266%2C-111.92972#map=18/33.38281/-111.93146</a></p>
<p>The other 2 car options do use the alley directly, but they won't do so aggressively, just for small sections.</p>
<p>You can change the dropdown where it says "Car (OSRM)" to see what assumptions are made about the alley for walking and biking.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '17, 16:58</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-60958" class="comments-container">
&#10;</div>
<div id="comment-tools-60958" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60958-form-container" class="comment-form-container">
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

