+++
type = "question"
title = "License question: Save attribution with copied data?"
description = '''I have a question about attribution requirements. If I access OpenStreetMap data and save the OSM data into a database, do I need to save an attribution with the saved data? Do I then need to display that attribution every time the saved data is accessed? Here&#x27;s what I want to do: I&#x27;d like to create...'''
date = "2012-06-09T17:43:00Z"
lastmod = "2012-06-10T00:38:00Z"
weight = 13379
keywords = [ "attribute", "copied", "attribution", "license", "data" ]
aliases = [ "/questions/13379" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [License question: Save attribution with copied data?](/questions/13379/license-question-save-attribution-with-copied-data)

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
<span id="post-13379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13379-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a question about attribution requirements. If I access OpenStreetMap data and save the OSM data into a database, do I need to save an attribution with the saved data? Do I then need to display that attribution every time the saved data is accessed?</p>
<p>Here's what I want to do: I'd like to create a "driving distance calculator" for a database application. My software will run within a database application. My software will take two addresses from the database, geocode both of them, then calculate the driving distance between them (using a routing service). Once the driving distance is possessed, my software will save it into the database.</p>
<p>This will run on the "view page" of a single record. The user will have a single record open, and on the view form they will see a "Calculate Driving Distance" button. Clicking the button will invoke my software as described above. I plan to add the required attributions on this page, for both the OpenStreetMap data and the MapQuest API.</p>
<p>But after that has occurred and the data is now saved in the database application, do I need to maintain an attribution with the saved copy of the data? I want to write my software so that it can use different mapping services, so it's possible that the driving distances saved on different records were acquired from different mapping services.</p>
<p>The saved driving distance will be used for private purposes only, and won't be republished. The database application is a password-protected application. My software may be used by both commercial and non-profit organizations.</p>
<p>Thanks! - Nathan</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-attribute" rel="tag" title="see questions tagged &#39;attribute&#39;">attribute</span> <span class="post-tag tag-link-copied" rel="tag" title="see questions tagged &#39;copied&#39;">copied</span> <span class="post-tag tag-link-attribution" rel="tag" title="see questions tagged &#39;attribution&#39;">attribution</span> <span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jun '12, 17:43</strong></p>
<img src="https://secure.gravatar.com/avatar/34d83abec60be6f5eebbbb5bcaa59c28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PlaysWithLife&#39;s gravatar image" />
<p><span>PlaysWithLife</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PlaysWithLife has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13379" class="comments-container">
&#10;</div>
<div id="comment-tools-13379" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13379-form-container" class="comment-form-container">
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

<span id="13390"></span>

<div id="answer-container-13390" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13390-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13390-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13390-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The question is a bit tricky, however my general approach would be to</p>
<ul>
<li>be conservative and attribute OSM when you have used OSM data</li>
<li>be fair and attribute OSM when you have used OSM data even if you would not be legally strictly required to do so</li>
</ul>
<p>When we switch to the ODbL you will have to determine if what you are doing falls in the "produced work" or derived database categories, the later will add further requirements and duties over attribution. This is naturally only relevant if you redistribute or publish the saved data. However even if you currently don't intend to do so, down the road you may change your plans and use the data for a public project and it would be very silly to not be able to do so because you didn't save the original source with your derived data.</p>
<p>The LWG (Licence Working Group) is currently discussing similar questions to yours with respect to geocoding, please see the minutes for the current state of the deliberations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '12, 00:38</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jun '12, 00:48</strong> </span></p>
</div>
</div>
<div id="comments-container-13390" class="comments-container">
&#10;</div>
<div id="comment-tools-13390" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13390-form-container" class="comment-form-container">
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

