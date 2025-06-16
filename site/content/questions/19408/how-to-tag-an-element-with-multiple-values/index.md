+++
type = "question"
title = "How to tag an element with multiple values?"
description = '''I am trying to tag a fast food restaurant with the cuisine tag. The place is called Four in One so I tried using cuisine=italian;indian;american;turkish. However Potlatch gives a warning triangle and puts the text in red, with a message &quot;the tag contains more than one value - please check&quot;. Should I...'''
date = "2013-01-28T20:20:00Z"
lastmod = "2015-11-20T00:42:00Z"
weight = 19408
keywords = [ "cuisine", "tags", "multiple", "restaurant" ]
aliases = [ "/questions/19408" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag an element with multiple values?](/questions/19408/how-to-tag-an-element-with-multiple-values)

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
<span id="post-19408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19408-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-19408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to tag a fast food restaurant with the cuisine tag. The place is called <a href="http://www.fourinone.co.uk">Four in One</a> so I tried using cuisine=italian;indian;american;turkish. However Potlatch gives a warning triangle and puts the text in red, with a message "the tag contains more than one value - please check".</p>
<p>Should I use the cuisine=* four separate times?<br />
</p>
<p>Similarly, when tagging the source of my data, how should I tag source = survey (for checking what is on the ground) and Bing (for tracing the outline)?</p>
<p>What is the recommended method of applying multiple values to one tag?<br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-cuisine" rel="tag" title="see questions tagged &#39;cuisine&#39;">cuisine</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-restaurant" rel="tag" title="see questions tagged &#39;restaurant&#39;">restaurant</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jan '13, 20:20</strong></p>
<img src="https://secure.gravatar.com/avatar/355ebf3e5f403d28976b5c8bc54f9dd4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hobgoblin&#39;s gravatar image" />
<p><span>Hobgoblin</span><br />
<span class="score" title="151 reputation points">151</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hobgoblin has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jan '13, 20:22</strong> </span></p>
</div>
</div>
<div id="comments-container-19408" class="comments-container">
&#10;</div>
<div id="comment-tools-19408" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19408-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="19410"></span>

<div id="answer-container-19410" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19410-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19410-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-19410-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hobgoblin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The acceptable way of tagging two values in one element is as you suggest to separate by a semicolon.<br />
</p>
<p>The reason that Potlatch 2 highlights it is in case you've merged two ways together and now have conflicting values. For example, if you merge together a stretch of street with no sidewalk with a stetch with sidewalk on the left the result will be "sidewalk=left; none" which is clearly nonsensical.</p>
<p>In your case it would seem to make sense to tag with semicolon-separated values (although as I'm sure you're aware few renderers will understand them).</p>
<p>With regard to source I to often use something like "source=survey;Bing".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '13, 20:49</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-19410" class="comments-container">
&#10;</div>
<div id="comment-tools-19410" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19410-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19409"></span>

<div id="answer-container-19409" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19409-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Hobgoblin, You should try to forget the red signals in the advanced menu of P2. Its the same with GSM mast or antennas. And talk on this platform made me use the ; in between different values. Greetz</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '13, 20:27</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-19409" class="comments-container">
&#10;</div>
<div id="comment-tools-19409" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19409-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44066"></span>

<div id="answer-container-44066" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44066-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The use of semicolon is NOT recommended: <a href="https://wiki.openstreetmap.org/wiki/Semi-colon_value_separator">https://wiki.openstreetmap.org/wiki/Semi-colon_value_separator</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '15, 14:21</strong></p>
<img src="https://secure.gravatar.com/avatar/fd1035a2bbd533c4ec6fbd22fc705a5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sakudo&#39;s gravatar image" />
<p><span>sakudo</span><br />
<span class="score" title="131 reputation points">131</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sakudo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44066" class="comments-container">
<span id="44067"></span>
<div id="comment-44067" class="comment">
<div id="post-44067-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That's not entirely true. Whether the use of semicolons is recommended or not depends on the specific use case. Both the wiki page you have mentioned as well as SomeoneElse's answer list several tags where the use of semicolons is perfectly fine.</p>
</div>
<div id="comment-44067-info" class="comment-info">
<span class="comment-age">(09 Jul '15, 14:33)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44068"></span>
<div id="comment-44068" class="comment">
<div id="post-44068-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, that's correct, the wiki page lists some use cases. But still, generally it is not recommended ("In general avoid ';' separated values whenever possible.") - Altough I understand the necessity and use of the semicolon for attributing several key values, the main argument (on the mentioned wiki page) is that most renderers and processors, tools etc. do not handle semicolon lists, hence (in a client-focused thinking), we should not use them as they are not going to be processed...</p>
</div>
<div id="comment-44068-info" class="comment-info">
<span class="comment-age">(09 Jul '15, 14:40)</span> <span class="comment-user userinfo">sakudo</span>
</div>
</div>
<span id="44069"></span>
<div id="comment-44069" class="comment">
<div id="post-44069-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/11216/sakudo">@sakudo</a> unfortunately a major contributor to that wiki page was a prolific wiki editor who subsequently got banned because of (among other things) their inability to balance their views with those of other people.</p>
<p>However this case (multiple cuisines) is analogous to the "service" example on the wiki page where use of a semicolon <em>is</em> suggested.</p>
<p>Perhaps you could suggest how the questioner should tag their restaurant?</p>
</div>
<div id="comment-44069-info" class="comment-info">
<span class="comment-age">(09 Jul '15, 14:50)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="46728"></span>
<div id="comment-46728" class="comment">
<div id="post-46728-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have the same type of problem with shop types I don't mind what seperator to use as long as it is agreed as ok. as far as I can tell I can choose from ,: and somepeople think ; is best while others say no? so is it right to deduce that ,: are the best to choose from instead?</p>
</div>
<div id="comment-46728-info" class="comment-info">
<span class="comment-age">(19 Nov '15, 21:26)</span> <span class="comment-user userinfo">Govanus</span>
</div>
</div>
<span id="46729"></span>
<div id="comment-46729" class="comment not_top_scorer">
<div id="post-46729-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Govanus credit to someneelse who frased (28-01-13) the semicolon (;) about 2,5 year ago and use it in between the different articles or tags.</p>
</div>
<div id="comment-46729-info" class="comment-info">
<span class="comment-age">(19 Nov '15, 21:37)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="46730"></span>
<div id="comment-46730" class="comment">
<div id="post-46730-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/7473/govanus">@Govanus</a>: I think you can safely assume that ",:" (a comma followed by a colon) is rarely if ever used, so that wouldn't be the best separator to use. The generally agreed-upon separator is a single ";" (semi-colon character).</p>
</div>
<div id="comment-46730-info" class="comment-info">
<span class="comment-age">(20 Nov '15, 00:42)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-44066" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-44066-form-container" class="comment-form-container">
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

