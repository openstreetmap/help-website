+++
type = "question"
title = "Mapnik does not render my new ways already for a couple of day now"
description = '''Dear all! I have a question: Mapnik does not render my new ways already for a couple of day now. If you look at https://www.openstreetmap.org/?lat=-26.8272&amp;amp;lon=-65.1402&amp;amp;zoom=13&amp;amp;layers=M you can see that there is a secondary road south of the Tucuman airport. In zoom level 12 this road dis...'''
date = "2010-12-22T08:51:00Z"
lastmod = "2010-12-22T13:30:00Z"
weight = 1887
keywords = [ "rendering", "mapnik" ]
aliases = [ "/questions/1887" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Mapnik does not render my new ways already for a couple of day now](/questions/1887/mapnik-does-not-render-my-new-ways-already-for-a-couple-of-day-now)

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
<span id="post-1887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1887-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear all!</p>
<p>I have a question: Mapnik does not render my new ways already for a couple of day now.</p>
<p>If you look at <a href="https://www.openstreetmap.org/?lat=-26.8272&amp;lon=-65.1402&amp;zoom=13&amp;layers=M"></a><a href="https://www.openstreetmap.org/?lat=-26.8272&amp;lon=-65.1402&amp;zoom=13&amp;layers=M"></a><a href="https://www.openstreetmap.org/?lat=-26.8272&amp;lon=-65.1402&amp;zoom=13&amp;layers=M">https://www.openstreetmap.org/?lat=-26.8272&amp;lon=-65.1402&amp;zoom=13&amp;layers=M</a> you can see that there is a secondary road south of the Tucuman airport. In zoom level 12 this road disapears: <a href="https://www.openstreetmap.org/?lat=-26.8094&amp;lon=-65.1664&amp;zoom=12&amp;layers=M"></a><a href="https://www.openstreetmap.org/?lat=-26.8094&amp;lon=-65.1664&amp;zoom=12&amp;layers=M"></a><a href="https://www.openstreetmap.org/?lat=-26.8094&amp;lon=-65.1664&amp;zoom=12&amp;layers=M">https://www.openstreetmap.org/?lat=-26.8094&amp;lon=-65.1664&amp;zoom=12&amp;layers=M</a> . Marking the respective tiles as dirty did not help. Reloading the map with Control+F5 also did not help.</p>
<p>Do you have any other suggestions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Dec '10, 08:51</strong></p>
<img src="https://secure.gravatar.com/avatar/3f398da25e1453020723c955139a4ec7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ALE&#39;s gravatar image" />
<p><span>ALE</span><br />
<span class="score" title="1943 reputation points"><span>1.9k</span></span><span title="41 badges"><span class="badge1">●</span><span class="badgecount">41</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ALE has 4 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-1887" class="comments-container">
&#10;</div>
<div id="comment-tools-1887" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1887-form-container" class="comment-form-container">
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

<span id="1888"></span>

<div id="answer-container-1888" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1888-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ALE has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect that mapnik simply doesn't render <code>highway=tertiary_link</code> in zoom level 12. That does NOT mean that you made an error in mapping that street NOR that mapnik is buggy. It's just a design choise. The way is in the database and other renderers (like osmarender) which make other design choices happily render the street.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Dec '10, 10:42</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-1888" class="comments-container">
<span id="1890"></span>
<div id="comment-1890" class="comment">
<div id="post-1890-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi petschge.</p>
<p>Well it was a mapping error as this road should have been tertiary and not tertiary_link. Now I know at least what went wrong and it get's rendered now. Thanks!</p>
</div>
<div id="comment-1890-info" class="comment-info">
<span class="comment-age">(22 Dec '10, 13:30)</span> <span class="comment-user userinfo">ALE</span>
</div>
</div>
</div>
<div id="comment-tools-1888" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1888-form-container" class="comment-form-container">
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

