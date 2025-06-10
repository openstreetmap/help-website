+++
type = "question"
title = "Disused post office"
description = '''Hello, I decided today to finally join the OSM Community.  I have a post office which is closed for some month now but not marked as such. It will most likely stay closed but is a visible landmark.  I post the tags, can someone help me to change them properly? I have to check if the atm still works....'''
date = "2019-09-30T21:36:00Z"
lastmod = "2019-10-01T04:24:00Z"
weight = 70979
keywords = [ "disused" ]
aliases = [ "/questions/70979" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Disused post office](/questions/70979/disused-post-office)

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
<span id="post-70979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70979-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I decided today to finally join the OSM Community. I have a post office which is closed for some month now but not marked as such. It will most likely stay closed but is a visible landmark. I post the tags, can someone help me to change them properly?</p>
<p>I have to check if the atm still works.<br />
Also there are Post office boxes, which are still in use.<br />
The actual post office has moved, can I somehow put the new adress in it and does it make sense?</p>
<pre><code>addr:city=Witzenhausen
addr:housenumber=6
addr:postcode=37213
addr:street=Südbahnhofstraße
amenity=post_office
atm=yes
name=Post
opening_hours=Mo-Fr 09:00-12:00,14:00-17:30; Sa 09:00-12:00
phone=no
wheelchair=yes
wheelchair:description=alles eben</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-disused" rel="tag" title="see questions tagged &#39;disused&#39;">disused</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Sep '19, 21:36</strong></p>
<img src="https://secure.gravatar.com/avatar/4a300296388b7cd5657e52d1cae74309?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erstmal&#39;s gravatar image" />
<p><span>erstmal</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erstmal has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Sep '19, 21:45</strong> </span></p>
</div>
</div>
<div id="comments-container-70979" class="comments-container">
&#10;</div>
<div id="comment-tools-70979" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70979-form-container" class="comment-form-container">
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

<span id="70982"></span>

<div id="answer-container-70982" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70982-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-70982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can change amenity=post_office to disused:amenity=post_office Please note that there a probably no data consumers (maps or apps) that do something with an object tagged as disused:x=y But in this way the data is there to know that this was a former post office. To emphasize this even more, you could tag the building as building=post_office. This means that the building looks like a post office, but not necessarily mean that it is a post office.</p>
<p>You should also remove the openings hours, remove name, phone and wheelchair tags, as it is no longer a functioning post office. Remove the atm once you know for sure it is gone. Or keep it when it is still there of course. It would be better though to map it as a separate node amenity=atm though.</p>
<p>As for the new postal office, create a new node at the new location, and add info like address, opening_hours and wheelchair tags. An alternative would be to move the node on the old position to the new location and change all tags. However, we would lose the information in the old position of "former post office".</p>
<p>p.s. imho it is debatable that the name is "Post", it is a post office, it is not name "Post".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '19, 04:24</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-70982" class="comments-container">
&#10;</div>
<div id="comment-tools-70982" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70982-form-container" class="comment-form-container">
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

