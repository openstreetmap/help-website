+++
type = "question"
title = "The tag addr: interpolation = (even / odd), has other attributes?"
description = '''I&#x27;m numbering streets through interpolation tag, each way (block), for example, 1250 to 1370. The usage is tranquil, simply add a line parallel to the street, with addr: interpolation = even or odd, and the numbers of the stretch at line ends. I&#x27;ve done some tests with nominatin and the result was n...'''
date = "2015-09-08T00:24:00Z"
lastmod = "2015-09-08T16:23:00Z"
weight = 45106
keywords = [ "address", "interpolation" ]
aliases = [ "/questions/45106" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [The tag addr: interpolation = (even / odd), has other attributes?](/questions/45106/the-tag-addr-interpolation-even-odd-has-other-attributes)

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
<span id="post-45106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45106-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm numbering streets through interpolation tag, each way (block), for example, 1250 to 1370.</p>
<p>The usage is tranquil, simply add a line parallel to the street, with addr: interpolation = even or odd, and the numbers of the stretch at line ends.</p>
<p>I've done some tests with nominatin and the result was not as accurate ... only located after about 2 or 3 attempts.</p>
<p>My question is whether it is necessary to add the addr: street = [street name] on line or at points where the numbers are.</p>
<p>It is an example in this link: <a href="https://www.openstreetmap.org/edit#map=19/-20.46229/-54.61504">https://www.openstreetmap.org/edit#map=19/-20.46229/-54.61504</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span> <span class="post-tag tag-link-interpolation" rel="tag" title="see questions tagged &#39;interpolation&#39;">interpolation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Sep '15, 00:24</strong></p>
<img src="https://secure.gravatar.com/avatar/62b0db5708737186a53757d471a515ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seth&#39;s gravatar image" />
<p><span>seth</span><br />
<span class="score" title="201 reputation points">201</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seth has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Sep '15, 00:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45106" class="comments-container">
&#10;</div>
<div id="comment-tools-45106" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45106-form-container" class="comment-form-container">
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

<span id="45107"></span>

<div id="answer-container-45107" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45107-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-45107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="seth has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The address nodes should get the street too (otherwise software needs to guess to which street the numbers belong). The interpolation line does not need the street, it just needs the interpolation info (e.g. addr:interpolation=even).</p>
<p>See for example <span>Ober-Rodener Straße 36, Rodgau</span>.</p>
<p>I cannot tell you if Nominatim needs that street info, but it seems very useful to me.</p>
<p>Also see <a href="https://wiki.openstreetmap.org/wiki/Interpolation#Using_interpolation">https://wiki.openstreetmap.org/wiki/Interpolation#Using_interpolation</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Sep '15, 00:51</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Sep '15, 00:53</strong> </span></p>
</div>
</div>
<div id="comments-container-45107" class="comments-container">
<span id="45109"></span>
<div id="comment-45109" class="comment">
<div id="post-45109-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But if the line has the name of the street would not be simpler? For nodes with the numbers. Otherwise, each node with number ... another street name.</p>
<p>If line already have the street name, the search software does not associate the node number with the street name that is on the line?</p>
</div>
<div id="comment-45109-info" class="comment-info">
<span class="comment-age">(08 Sep '15, 01:30)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
<span id="45113"></span>
<div id="comment-45113" class="comment">
<div id="post-45113-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The currently widely used <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/House_numbers/Karlsruhe_Schema">Karlsruhe Schema</a> has many duplicated fields. But it makes it easier for end user tools to process this data and also works with broken administrative boundaries.</p>
<p>Also, putting the street name on the nodes instead of the interpolation line allows even tools that don't support address interpolation to read the address data from the node. And it allows to just delete the interpolation line once every address has been mapped without the need to change/add/del any other tags.</p>
</div>
<div id="comment-45113-info" class="comment-info">
<span class="comment-age">(08 Sep '15, 09:50)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45125"></span>
<div id="comment-45125" class="comment">
<div id="post-45125-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok. Thank you.</p>
</div>
<div id="comment-45125-info" class="comment-info">
<span class="comment-age">(08 Sep '15, 16:23)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
</div>
<div id="comment-tools-45107" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45107-form-container" class="comment-form-container">
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

