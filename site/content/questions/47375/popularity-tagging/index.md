+++
type = "question"
title = "Popularity Tagging"
description = '''We are creating printed maps and collected lots of POIs. Now we want to rank the popularity of certain POIs, so that for example a big international hotel next to a smaller one is favored on the map. Is there any kind of popularity tagging proposal already? Current ideas are: popularity_score from 1...'''
date = "2016-01-05T09:40:00Z"
lastmod = "2016-01-05T11:56:00Z"
weight = 47375
keywords = [ "printing", "data", "tagging" ]
aliases = [ "/questions/47375" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Popularity Tagging](/questions/47375/popularity-tagging)

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
<span id="post-47375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47375-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We are creating printed maps and collected lots of POIs. Now we want to rank the popularity of certain POIs, so that for example a big international hotel next to a smaller one is favored on the map.</p>
<p>Is there any kind of popularity tagging proposal already?</p>
<p>Current ideas are:</p>
<p>popularity_score from 1-100 based on some kind of algorithm we would have to develop.</p>
<p>Or</p>
<p>popularity with a comma separated list such as "in_travel_guide_bradt,in_travel_guide_lonely_planet" and other sources .. ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-printing" rel="tag" title="see questions tagged &#39;printing&#39;">printing</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '16, 09:40</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47375" class="comments-container">
&#10;</div>
<div id="comment-tools-47375" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47375-form-container" class="comment-form-container">
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

<span id="47377"></span>

<div id="answer-container-47377" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47377-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-47377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AddisMap_Alexander has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a number of reasons while there is no existing such tagging (at least none that I know of) and why inventing such tagging is really not a good idea.</p>
<p>But to give this answer a positive spin: naturally it makes sense to order search results by additional criteria, for example Nominatim uses wikipedia to determine the importance of places, and there is no reason you couldn't do something similar with travel guides.</p>
<p>It just isn't necessary to hard code the results in to the OSM data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '16, 11:56</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-47377" class="comments-container">
&#10;</div>
<div id="comment-tools-47377" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47377-form-container" class="comment-form-container">
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

