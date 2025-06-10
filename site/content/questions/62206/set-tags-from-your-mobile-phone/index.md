+++
type = "question"
title = "Set tags from your mobile phone"
description = '''Hi. Sorry for my &quot;literacy&quot;, I&#x27;m using a translator. Probably this question was already asked, but search on the forum causes me difficulties. There was a need to set tags from the android device and transfer them to the PC version. How can I do that?'''
date = "2018-02-19T12:49:00Z"
lastmod = "2018-02-20T17:22:00Z"
weight = 62206
keywords = [ "android" ]
aliases = [ "/questions/62206" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Set tags from your mobile phone](/questions/62206/set-tags-from-your-mobile-phone)

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
<span id="post-62206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62206-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. Sorry for my "literacy", I'm using a translator. Probably this question was already asked, but search on the forum causes me difficulties. There was a need to set tags from the android device and transfer them to the PC version. How can I do that?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Feb '18, 12:49</strong></p>
<img src="https://secure.gravatar.com/avatar/52181edededc1130801083d1ed5aceeb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grimmlex&#39;s gravatar image" />
<p><span>Grimmlex</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grimmlex has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62206" class="comments-container">
<span id="62207"></span>
<div id="comment-62207" class="comment">
<div id="post-62207-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>the PC version of what?</p>
</div>
<div id="comment-62207-info" class="comment-info">
<span class="comment-age">(19 Feb '18, 12:54)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="62209"></span>
<div id="comment-62209" class="comment">
<div id="post-62209-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>such as the website</p>
</div>
<div id="comment-62209-info" class="comment-info">
<span class="comment-age">(19 Feb '18, 12:59)</span> <span class="comment-user userinfo">Grimmlex</span>
</div>
</div>
<span id="62213"></span>
<div id="comment-62213" class="comment">
<div id="post-62213-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can ask in another language.</p>
<p>Вы можете спросить на другом языке.</p>
<p>Также см. <a href="Https://forum.openstreetmap.org/viewforum.php?id=21">Https://forum.openstreetmap.org/viewforum.php?id=21</a></p>
</div>
<div id="comment-62213-info" class="comment-info">
<span class="comment-age">(19 Feb '18, 13:25)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62206-form-container" class="comment-form-container">
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

<span id="62212"></span>

<div id="answer-container-62212" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62212-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-62212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I believe you have misunderstood a bit how the infrastructure behind OSM works.</p>
<p>There is a reasonably large database (a structured store of data) that contains the actual OSM data. When you change an object (for example by changing its attributes, "tags" in OSM) or create a new one. The program that does that, regardless where it is located and what its user interface looks like, changes the information in the central database. Everybody and every thing that uses OSM data retrieves it directly or indirectly from that central database.</p>
<p>Now if you are looking for a way to change objects from a mobile device, there are 2-3 apps with restricted functionality that are likely OK for a beginner, most notably the navigation apps osmand and maps.me have minimalistic editors built in.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '18, 13:20</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-62212" class="comments-container">
<span id="62215"></span>
<div id="comment-62215" class="comment">
<div id="post-62215-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank you so much</p>
</div>
<div id="comment-62215-info" class="comment-info">
<span class="comment-age">(19 Feb '18, 19:24)</span> <span class="comment-user userinfo">Grimmlex</span>
</div>
</div>
<span id="62224"></span>
<div id="comment-62224" class="comment">
<div id="post-62224-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also give streetcomplete a try. It asks you all kind of questions about where you are to update the central database.</p>
</div>
<div id="comment-62224-info" class="comment-info">
<span class="comment-age">(20 Feb '18, 17:22)</span> <span class="comment-user userinfo">Pieter Vande...</span>
</div>
</div>
</div>
<div id="comment-tools-62212" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62212-form-container" class="comment-form-container">
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

