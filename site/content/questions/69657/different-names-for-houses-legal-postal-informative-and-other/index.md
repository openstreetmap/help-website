+++
type = "question"
title = "Different names for houses; legal, postal, informative and other"
description = '''I am actively editing OSM around Helsinki area, and running into certain hair-splitting issues regarding naming and addressing of buildings - to be more specific, residential buildings, often apartment buildings (or &quot;flats&quot;). My question involves what should go or not go to &quot;name&quot; or &quot;addr:housename...'''
date = "2019-06-18T17:46:00Z"
lastmod = "2019-06-19T05:09:00Z"
weight = 69657
keywords = [ "houses", "addressing" ]
aliases = [ "/questions/69657" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Different names for houses; legal, postal, informative and other](/questions/69657/different-names-for-houses-legal-postal-informative-and-other)

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
<span id="post-69657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69657-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am actively editing OSM around Helsinki area, and running into certain hair-splitting issues regarding naming and addressing of buildings - to be more specific, residential buildings, often apartment buildings (or "flats").</p>
<p>My question involves what should go or not go to "name" or "addr:housename" fields of a building. My current assumption is that if an address doesn't make sense or be necessary as a postal address or wouldn't be recognized by a local on the street, it shouldn't be in the "addr:housename" field. I also feel that "name" should have only names that make sense to the locals - that is, not names of obscure legal entities or such. Are my assumptions reasonable?</p>
<p>The background to this question is that some mappers in Finland seem to add names (full or abbreviated) of <a href="https://en.wikipedia.org/wiki/Housing_cooperative">housing companies</a> - which are legal entity names, as names of buildings. Housing companies operate one or multiple buildings, and if they operate multiple buildings, these buildings may often have more than one postal address. At the same time, the name of the company is, to my knowledge, never necessary to identify a specific building, either in postal address or in common speech location. In fact, post office would consider such addressing an unnecessary nuisance!</p>
<p>Other, considerably less common activity is to include a name for particularly (culturally, architecturally, or locally) significant apartment buildings in one of these fields. These names are often known (much better than legal company names) by the locals, but never part of a postal address.</p>
<p>So, my question is the following: should such names be included in "name" or "addr:housename" fields? If not, how they should be indicated? I understand that removing information from OSM metadata is counterproductive, but I'm unaware of the best field to put such details...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-houses" rel="tag" title="see questions tagged &#39;houses&#39;">houses</span> <span class="post-tag tag-link-addressing" rel="tag" title="see questions tagged &#39;addressing&#39;">addressing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jun '19, 17:46</strong></p>
<img src="https://secure.gravatar.com/avatar/9104ef5e4f029338cf8df36de3ad23d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kirma&#39;s gravatar image" />
<p><span>kirma</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kirma has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '19, 05:11</strong> </span></p>
</div>
</div>
<div id="comments-container-69657" class="comments-container">
&#10;</div>
<div id="comment-tools-69657" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69657-form-container" class="comment-form-container">
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

<span id="69667"></span>

<div id="answer-container-69667" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69667-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69667-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69667-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kirma has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ul>
<li>the name of a building goes in name (in case of what you call the significant apartment buildings) I also use it for the name that people sometimes give to their house, typically seen as homemade sign above the door.</li>
<li>use addr:housename to replace addr:housenumber (for those buildings that do not have a house number). The use of the tag will depend on where you live, in some countries you should not use this tag, as the house name is never part of the official address.</li>
<li>housing companies seems like an operator to me, so that goes in the operator tag. This is not common practice around me.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '19, 04:10</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-69667" class="comments-container">
<span id="69669"></span>
<div id="comment-69669" class="comment">
<div id="post-69669-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Housing company as an operator would sound like a reasonable compromise, but there's still a little bit of background to this: housing companies in Finland are often owned by individual dwellers of the house or their individual landlords (although commune and privately owned housing companies where all occupants are tenants also exist), making the concept of "operator" slightly abstract. Of course this is conceptually not that different from any other operator owned through a shareholder system...</p>
</div>
<div id="comment-69669-info" class="comment-info">
<span class="comment-age">(19 Jun '19, 05:09)</span> <span class="comment-user userinfo">kirma</span>
</div>
</div>
</div>
<div id="comment-tools-69667" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69667-form-container" class="comment-form-container">
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

