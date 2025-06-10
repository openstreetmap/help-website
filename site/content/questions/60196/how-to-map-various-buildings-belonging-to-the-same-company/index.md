+++
type = "question"
title = "How to map various buildings belonging to the same company?"
description = '''When I was mapping the buildings of a company, I found it a bit strange to have to tag all of them with name=company name. It would make all the buildings appear with the company name in the maps. What can I do in general to have all the buildings associated with the company without having to apply ...'''
date = "2017-10-20T19:55:00Z"
lastmod = "2017-10-21T02:29:00Z"
weight = 60196
keywords = [ "operator", "multiple", "name", "area" ]
aliases = [ "/questions/60196" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to map various buildings belonging to the same company?](/questions/60196/how-to-map-various-buildings-belonging-to-the-same-company)

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
<span id="post-60196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60196-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I was mapping the buildings of a company, I found it a bit strange to have to tag all of them with <em>name=company name</em>. It would make all the buildings appear with the company name in the maps. What can I do in general to have all the buildings associated with the company without having to apply the company name to every building? I considered adding the <em>operator</em> tag, but that would again have the problem of not being rendered in OSM-Carto.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-operator" rel="tag" title="see questions tagged &#39;operator&#39;">operator</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Oct '17, 19:55</strong></p>
<img src="https://secure.gravatar.com/avatar/ad3e998af874e04adfb3a569d8125995?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wanderw%C3%BCtiger&#39;s gravatar image" />
<p><span>wanderwütiger</span><br />
<span class="score" title="375 reputation points">375</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wanderwütiger has one accepted answer">16%</span></p>
</div>
</div>
<div id="comments-container-60196" class="comments-container">
&#10;</div>
<div id="comment-tools-60196" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60196-form-container" class="comment-form-container">
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

<span id="60198"></span>

<div id="answer-container-60198" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60198-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wanderwütiger has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I agree that <code>name=company</code> is a bit strange, but I'd go farther and say that it is, in fact, incorrect. It's tempting to tag things so that they are rendered how you or I'd like. This is called <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">Tagging for the renderer</a>, and is well established as an error. Your alternative suggesting the <code>operator</code> tag is the correct approach, even if it's not as gratifying when you don't get to see it in the default rendering. Do remember that the default rendering is just one of many. If someone wanted to have a map showing all the operators of buildings, and you'd put the operator in the name tag, then your buildings operator wouldn't show up on their map.</p>
<p>As has already been suggested the operator's name could be put in an area tagged as <code>landuse=commercial</code> (or <code>landuse=industrial</code>, or potentially another <code>landuse</code>) tag. However this should <em>only</em> be done if it's a reasonable name for the area. For example, if there are many buildings belonging in an industrial park owned by Bob's Bicycles, and the industrial park called <em>Bob's Bicycle Industrial park</em>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Oct '17, 02:29</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-60198" class="comments-container">
&#10;</div>
<div id="comment-tools-60198" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60198-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60197"></span>

<div id="answer-container-60197" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60197-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-60197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the buildings are within some fairly welldefined area, I'd recommend creating and naming a landuse=commercial (or similar) polygon (as is common with schools: <a href="https://www.openstreetmap.org/way/104718161">example</a>) rather than name individual buildings. Another option could be using a <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">multipolygon</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '17, 20:50</strong></p>
<img src="https://secure.gravatar.com/avatar/6edf3a421a450237beae62ba93582637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hjart&#39;s gravatar image" />
<p><span>Hjart</span><br />
<span class="score" title="2961 reputation points"><span>3.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hjart has 14 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Oct '17, 18:02</strong> </span></p>
</div>
</div>
<div id="comments-container-60197" class="comments-container">
&#10;</div>
<div id="comment-tools-60197" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60197-form-container" class="comment-form-container">
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

