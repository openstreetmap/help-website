+++
type = "question"
title = "How to fix a wrong place hierarchy?"
description = '''Some places are not noted in the right hierarchy in OSM. Example : La Lande, Vannes, Morbihan, Bretagne, France métropolitaine, France should be : La Lande, Rieux, Vannes, Morbihan, Bretagne, France métropolitaine, France because Rieux is the municipality of this hamlet. How to fix this issue ? Rega...'''
date = "2016-09-27T18:45:00Z"
lastmod = "2016-09-28T15:30:00Z"
weight = 52251
keywords = [ "hierarchy", "place" ]
aliases = [ "/questions/52251" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to fix a wrong place hierarchy?](/questions/52251/how-to-fix-a-wrong-place-hierarchy)

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
<span id="post-52251-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52251-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52251-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Some places are not noted in the right hierarchy in OSM.</p>
<p>Example : La Lande, Vannes, Morbihan, Bretagne, France métropolitaine, France</p>
<p>should be :</p>
<p>La Lande, Rieux, Vannes, Morbihan, Bretagne, France métropolitaine, France</p>
<p>because Rieux is the municipality of this hamlet.</p>
<p>How to fix this issue ?</p>
<p>Regards.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hierarchy" rel="tag" title="see questions tagged &#39;hierarchy&#39;">hierarchy</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Sep '16, 18:45</strong></p>
<img src="https://secure.gravatar.com/avatar/6cb807168ed11b6b2bad19df33b8000b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arpaf&#39;s gravatar image" />
<p><span>Arpaf</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arpaf has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Sep '16, 08:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-52251" class="comments-container">
&#10;</div>
<div id="comment-tools-52251" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52251-form-container" class="comment-form-container">
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

<span id="52263"></span>

<div id="answer-container-52263" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52263-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Arpaf has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When I search for Rieux <a href="http://nominatim.openstreetmap.org/details.php?place_id=145027088,">http://nominatim.openstreetmap.org/details.php?place_id=145027088,</a> I have the impression that this boundary does not include La Lande <a href="http://nominatim.openstreetmap.org/details.php?place_id=19008327">http://nominatim.openstreetmap.org/details.php?place_id=19008327</a> , hence it is impossible for Nominatim (the search engine) to place La Lande in Rieux.</p>
<p>In order to fix this, the boundary of Rieux has to change. However, if you are new to OpenStreetMap, I would not recommend to do this. It is better to contact the French community (as Hendrikklaas wrote), but I doubt the forum is heavily used. You could leave a note on the map, referring to this discussion or you could sign up on the <a href="https://lists.openstreetmap.org/listinfo/talk-fr">French mailing list</a>, which is used more by the French community, and discuss the issue there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '16, 08:09</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-52263" class="comments-container">
<span id="52279"></span>
<div id="comment-52279" class="comment">
<div id="post-52279-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok. Thank you to you and Hendrikklaas for your pertinent answers.</p>
</div>
<div id="comment-52279-info" class="comment-info">
<span class="comment-age">(28 Sep '16, 15:27)</span> <span class="comment-user userinfo">Arpaf</span>
</div>
</div>
<span id="52280"></span>
<div id="comment-52280" class="comment">
<div id="post-52280-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>you're welcome</p>
</div>
<div id="comment-52280-info" class="comment-info">
<span class="comment-age">(28 Sep '16, 15:30)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-52263" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52263-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52254"></span>

<div id="answer-container-52254" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52254-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Arpaf, some options, would you mind to ask this at the France community, <a href="http://forum.openstreetmap.org/viewforum.php?id=22">http://forum.openstreetmap.org/viewforum.php?id=22</a> Ask the original mapper or contributer and if you dont get an answer within a reasonable period (14 days) you could change the value.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Sep '16, 21:13</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-52254" class="comments-container">
&#10;</div>
<div id="comment-tools-52254" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52254-form-container" class="comment-form-container">
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

