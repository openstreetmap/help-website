+++
type = "question"
title = "How to tag an object not existing anymore but still showing the location for historical questioning"
description = '''Hi! At Sommerrodelbahn Grebenzen there exists a former summer_toboggan in the database which was completely removed some years ago. In OSM it is tagged as abandoned=yes.  In Opentopomap it is still shown, most likely because of not questioning the abandoned tag. For me abandoned should be used, when...'''
date = "2022-08-08T09:22:00Z"
lastmod = "2022-08-08T09:56:00Z"
weight = 85287
keywords = [ "abandon", "removed", "historical" ]
aliases = [ "/questions/85287" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag an object not existing anymore but still showing the location for historical questioning](/questions/85287/how-to-tag-an-object-not-existing-anymore-but-still-showing-the-location-for-historical-questioning)

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
<span id="post-85287-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85287-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85287-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! At <a href="https://www.openstreetmap.org/edit#map=17/47.06773/14.31827">Sommerrodelbahn Grebenzen</a> there exists a former summer_toboggan in the database which was completely removed some years ago. In OSM it is tagged as abandoned=yes. In Opentopomap it is still shown, most likely because of not questioning the abandoned tag.</p>
<p>For me abandoned should be used, when the track would be still out there, but is not used anymore. Similar to a "Lost Place".</p>
<p>Now to the question: What would be the correct tagging of an object to say it does not exist anymore, but the old track is still saved for historical questioning?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-abandon" rel="tag" title="see questions tagged &#39;abandon&#39;">abandon</span> <span class="post-tag tag-link-removed" rel="tag" title="see questions tagged &#39;removed&#39;">removed</span> <span class="post-tag tag-link-historical" rel="tag" title="see questions tagged &#39;historical&#39;">historical</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Aug '22, 09:22</strong></p>
<img src="https://secure.gravatar.com/avatar/d83e2fafb601b6599d1b31126afba85d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Khananos&#39;s gravatar image" />
<p><span>Khananos</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Khananos has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Aug '22, 11:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-85287" class="comments-container">
&#10;</div>
<div id="comment-tools-85287" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85287-form-container" class="comment-form-container">
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

<span id="85288"></span>

<div id="answer-container-85288" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85288-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85288-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-85288-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>abanoned=yes</code> is a so-called "troll tag". Don't use it because it leads to the exact problem that you describe - services ignoring the tag will draw the wrong conclusions. It's like "planned=yes" or "destroyed=yes" - if you're looking for a hospital then it is unlikely a planned or destroyed one will be useful to you.</p>
<p>Instead, use an "abandoned:" prefix for the feature tag, e.g. <code>abandoned:highway=motorway</code> or <code>abaondoned:tourism=attaction</code>.</p>
<p>Note that we do not record historic objects of which all traces have vanished - once the thing has been completely dismantled, you should delete it from the database. The "historical questioning" you are talking about would, in OSM, have to take place using the OSM history data file which contains old versions of things.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '22, 09:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Aug '22, 09:40</strong> </span></p>
</div>
</div>
<div id="comments-container-85288" class="comments-container">
<span id="85289"></span>
<div id="comment-85289" class="comment">
<div id="post-85289-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have not tagged it myself with this tag. Just found it and thought that this couldn´t be correct. And was looking for the correct way to fix this in the future.</p>
<p>So i will remove the complete feature from the database to correct this failure. Thanks!</p>
</div>
<div id="comment-85289-info" class="comment-info">
<span class="comment-age">(08 Aug '22, 09:56)</span> <span class="comment-user userinfo">Khananos</span>
</div>
</div>
</div>
<div id="comment-tools-85288" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85288-form-container" class="comment-form-container">
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

