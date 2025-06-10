+++
type = "question"
title = "Street bordering two cities is &quot;East&quot; on one side and &quot;West&quot; on the other"
description = '''How do you identify a street name that borders two cities where on the north side of the street it is &quot;East StreetName&quot; and on the south side of the street (in a different city) it is &quot;West StreetName&quot;?'''
date = "2017-06-04T17:38:00Z"
lastmod = "2017-06-05T06:51:00Z"
weight = 56445
keywords = [ "streetnames" ]
aliases = [ "/questions/56445" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Street bordering two cities is "East" on one side and "West" on the other](/questions/56445/street-bordering-two-cities-is-east-on-one-side-and-west-on-the-other)

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
<span id="post-56445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56445-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do you identify a street name that borders two cities where on the north side of the street it is "East StreetName" and on the south side of the street (in a different city) it is "West StreetName"?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jun '17, 17:38</strong></p>
<img src="https://secure.gravatar.com/avatar/33635a4222af289982526fd5de3c3611?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FletchFFletch&#39;s gravatar image" />
<p><span>FletchFFletch</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FletchFFletch has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56445" class="comments-container">
&#10;</div>
<div id="comment-tools-56445" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56445-form-container" class="comment-form-container">
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

<span id="56449"></span>

<div id="answer-container-56449" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56449-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-56449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In Belgium we typically map this as name="name1 - name2" and we add name:left=name1 and name:right=2 where left and right are determined by the direction of the OSM-way. This will show both names on the standard map, but some people will not like that the name tag contains 2 names. Furthermore Nomination (the standard geocoder / search engine) will not find the streets with name "name1" or "name2" anymore. In the case Hendrikklaas gave (with name:nl and name:de), this name lookup still works, as name:&lt;language_code&gt; is recognized by Nominatim.</p>
<p>An alternative would be to map it as name=name1 and alt_name=name2, and while this uses more standard tags, you loose the information which side of the street has a particular name. You will also not see the alt_name on the standard OpenStreetMap rendering. But Nominatim will work in this case.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jun '17, 06:51</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-56449" class="comments-container">
&#10;</div>
<div id="comment-tools-56449" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56449-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56446"></span>

<div id="answer-container-56446" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56446-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi just specify, the street name and ad the city name to it. Just like large city's ad the old suburb or regional name to it. It’s even possible to do so by international borders. Have a look here <a href="https://www.openstreetmap.org/#map=19/50.86019/6.07763">https://www.openstreetmap.org/#map=19/50.86019/6.07763</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '17, 21:27</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-56446" class="comments-container">
<span id="56447"></span>
<div id="comment-56447" class="comment">
<div id="post-56447-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, thanks!</p>
</div>
<div id="comment-56447-info" class="comment-info">
<span class="comment-age">(04 Jun '17, 21:50)</span> <span class="comment-user userinfo">FletchFFletch</span>
</div>
</div>
</div>
<div id="comment-tools-56446" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56446-form-container" class="comment-form-container">
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

