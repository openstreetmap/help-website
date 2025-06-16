+++
type = "question"
title = "Mapbox | Roads visibility on zoom 10"
description = '''Hello, I need help with a mapbox.com. Small roads disappear when I zoom out (10). I need them to be seen at level 10. http://bit.ly/zoom-11 http://bit.ly/zoom-10 I need it all over the world. Is there a way to do this? Thank you for any advice.'''
date = "2019-12-18T12:21:00Z"
lastmod = "2019-12-18T15:43:00Z"
weight = 72154
keywords = [ "mapbox" ]
aliases = [ "/questions/72154" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapbox | Roads visibility on zoom 10](/questions/72154/mapbox-roads-visibility-on-zoom-10)

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
<span id="post-72154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72154-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I need help with a mapbox.com. Small roads disappear when I zoom out (10). I need them to be seen at level 10.</p>
<p><a href="http://bit.ly/zoom-11">http://bit.ly/zoom-11</a></p>
<p><a href="http://bit.ly/zoom-10">http://bit.ly/zoom-10</a></p>
<p>I need it all over the world. Is there a way to do this?</p>
<p>Thank you for any advice.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapbox" rel="tag" title="see questions tagged &#39;mapbox&#39;">mapbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Dec '19, 12:21</strong></p>
<img src="https://secure.gravatar.com/avatar/076a379691a9112855b498213de5ded5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="toto4ever&#39;s gravatar image" />
<p><span>toto4ever</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="toto4ever has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Dec '19, 13:13</strong> </span></p>
</div>
</div>
<div id="comments-container-72154" class="comments-container">
<span id="72155"></span>
<div id="comment-72155" class="comment">
<div id="post-72155-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I'm not sure exactly what you mean by "a mapbox"?</p>
<p>If you mean <a href="https://mapbox.com/">https://mapbox.com/</a> the company, I'd suggest that you contact their support.</p>
</div>
<div id="comment-72155-info" class="comment-info">
<span class="comment-age">(18 Dec '19, 12:35)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-72154" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72154-form-container" class="comment-form-container">
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

<span id="72160"></span>

<div id="answer-container-72160" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72160-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72160-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-72160-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Vector tiles, as used by Mapbox, have a certain selection of features baked in at each zoom level.</p>
<p>If Mapbox have chosen not to include minor roads at zoom level 10, there's not much you can do about that, I'm afraid. You should contact Mapbox support and ask if they are willing to provide a product that meets your needs. Unfortunately, there doesn't seem to be any public documentation as to what Mapbox include at each zoom level.</p>
<p>Alternatively, you can consider another tile provider or even creating your own, as documented in this similar answer: <a href="/questions/45934/smaller-roads-visibility-on-zoom-13-with-mapbox">https://help.openstreetmap.org/questions/45934/smaller-roads-visibility-on-zoom-13-with-mapbox</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '19, 15:43</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-72160" class="comments-container">
&#10;</div>
<div id="comment-tools-72160" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72160-form-container" class="comment-form-container">
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

