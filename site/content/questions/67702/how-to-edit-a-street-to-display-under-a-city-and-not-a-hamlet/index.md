+++
type = "question"
title = "How to Edit a Street to Display Under a City and not a Hamlet"
description = '''How can I edit the city / hamlet that some newly added streets I have mapped are showing under? I need to remove the hamlet because it is incorrect and should be showing under a city instead.  Scenario: one street I added is showing as Evans Woods Drive, Orchard Park, Mecklenburg County, NC This is ...'''
date = "2019-01-23T17:25:00Z"
lastmod = "2019-01-24T10:30:00Z"
weight = 67702
keywords = [ "editing", "street", "help", "hamlet" ]
aliases = [ "/questions/67702" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to Edit a Street to Display Under a City and not a Hamlet](/questions/67702/how-to-edit-a-street-to-display-under-a-city-and-not-a-hamlet)

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
<span id="post-67702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67702-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I edit the city / hamlet that some newly added streets I have mapped are showing under? I need to remove the hamlet because it is incorrect and should be showing under a city instead.</p>
<p>Scenario: one street I added is showing as Evans Woods Drive, Orchard Park, Mecklenburg County, NC<br />
This is incorrect. This address is deeded as Charlotte, NC and is not listed under the Orchard Park hamlet.</p>
<p>With that being said, how do I correct the address for the street I have added to show up as Charlotte.</p>
<p>Any help is appreciate! :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span> <span class="post-tag tag-link-hamlet" rel="tag" title="see questions tagged &#39;hamlet&#39;">hamlet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jan '19, 17:25</strong></p>
<img src="https://secure.gravatar.com/avatar/7fb1e5195d774726f2ed29a1ebf43591?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tiffany%20Mapping&#39;s gravatar image" />
<p><span>Tiffany Mapping</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tiffany Mapping has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jan '19, 17:26</strong> </span></p>
</div>
</div>
<div id="comments-container-67702" class="comments-container">
<span id="67703"></span>
<div id="comment-67703" class="comment">
<div id="post-67703-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can't answer directly, but I notice there was a very similar question several years ago and interestingly it also refers to Charlotte, NC: <a href="/questions/14343/road-listed-in-hamlet-instead-of-city">https://help.openstreetmap.org/questions/14343/road-listed-in-hamlet-instead-of-city</a></p>
<p>That coincidence makes me wonder if "place=hamlet" has been mapped differently in Charlotte than other cities in the USA. Certainly from a European point of view it seems odd to have a hamlet inside a city, but I know there are certain practices in OSM to reflect specifically American settlement types or administrative areas.</p>
<p>This is the node for Orchard Park "hamlet"; <a href="https://www.openstreetmap.org/node/153927100">https://www.openstreetmap.org/node/153927100</a></p>
<p>It is quite close to your address so I would guess Nominatim, the OSM search engine, is giving it priority over the city based on proximity. Note that Nominatim has to try to give reasonable answers for all countries in the world, with all their different address systems. I wouldn't necessarily expect it to consistently match what is shown on title deeds even if all underlying data is perfectly correct. But in this case it does seem worth looking further into the choice of place=hamlet, maybe asking in a USA-specific forum or mailing list.</p>
</div>
<div id="comment-67703-info" class="comment-info">
<span class="comment-age">(23 Jan '19, 20:20)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="67704"></span>
<div id="comment-67704" class="comment">
<div id="post-67704-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>By the way I note that you have changed the name of <a href="https://www.openstreetmap.org/way/665624338">https://www.openstreetmap.org/way/665624338</a> to "Evans Woods Drive, Charlotte, NC". That is definitely NOT the solution - the name tag should not include things that are not part of the name, such a non-standard approach won't help you in the long run.</p>
<p>I also notice that this street is outside the boundary of Charlotte (<a href="https://www.openstreetmap.org/relation/177415">https://www.openstreetmap.org/relation/177415</a> ) - you can see that this boundary is a bit to the south roughly following a railway line. That may well be contributing to Nominatim giving priority to the nearby hamlet rather than the city. You say this street is in Charlotte, so maybe it is the city boundary that is the issue?</p>
</div>
<div id="comment-67704-info" class="comment-info">
<span class="comment-age">(23 Jan '19, 20:47)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
</div>
<div id="comment-tools-67702" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67702-form-container" class="comment-form-container">
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

<span id="67705"></span>

<div id="answer-container-67705" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67705-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-67705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I assume you are talking about the search result that you get displayed when searching for the street on www.openstreetmap.org.</p>
<p>Don't worry too much about what is shown there. The search engine (called Nominatim) does some guessing when it comes to how objects are hierarchically related with administrative bodies. It uses information from place nodes (place=hamlet, place=suburb) and other data but frankly speaking does a lousy job in guessing accurately in many cases. To really indicate where an object is located inside an administrative boundary it needs to be mapped <a href="https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative">as such</a>. But even then Nominatim is still making errors. As alan_gr pointed out, don't try to improve the search result display by adding information to the name that is not the name.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jan '19, 10:30</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-67705" class="comments-container">
&#10;</div>
<div id="comment-tools-67705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67705-form-container" class="comment-form-container">
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

