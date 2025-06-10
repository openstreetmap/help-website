+++
type = "question"
title = "Get length of all power / railway lines mapped by 1 user"
description = '''For applying to a project I would like to find out the length of all power (power=line) and railway lines (railway=rail) mapped by me. Is there any way to find this out – maybe with osmium? I&#x27;m ready to go at great lengths, e.g. getting this information from a global dumpfile (if it fits into my 32 ...'''
date = "2018-05-19T17:02:00Z"
lastmod = "2018-05-19T21:10:00Z"
weight = 63564
keywords = [ "osmium", "length", "railway", "power" ]
aliases = [ "/questions/63564" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get length of all power / railway lines mapped by 1 user](/questions/63564/get-length-of-all-power-railway-lines-mapped-by-1-user)

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
<span id="post-63564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63564-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For applying to a project I would like to find out the length of all power (power=line) and railway lines (railway=rail) mapped by me.</p>
<p>Is there any way to find this out – maybe with osmium? I'm ready to go at great lengths, e.g. getting this information from a global dumpfile (if it fits into my 32 GB of memory).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-power" rel="tag" title="see questions tagged &#39;power&#39;">power</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 May '18, 17:02</strong></p>
<img src="https://secure.gravatar.com/avatar/bdb6a1b49c42d8be4b8d87f3096a3622?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Druzhba&#39;s gravatar image" />
<p><span>Druzhba</span><br />
<span class="score" title="150 reputation points">150</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Druzhba has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63564" class="comments-container">
&#10;</div>
<div id="comment-tools-63564" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63564-form-container" class="comment-form-container">
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

<span id="63566"></span>

<div id="answer-container-63566" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63566-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63566-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63566-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Depending on the how spread out the areas in wich you mapped railways and whether you want to include lines later edited by other mappers, you could try downloading via Overpass in JOSM (see <a href="https://overpass-turbo.eu/s/yWD">https://overpass-turbo.eu/s/yWD</a> , which will find a few bits of railway mapped by you).</p>
<p>The code I entered into the wizard: <strong>type:way &amp; railway=rail &amp; user:Druzhba</strong></p>
<p>Once you have the lines in JOSM, just do <strong>Ctrl-F</strong> <code>type:way</code> to see the total length at the lower edge of the window.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 May '18, 18:37</strong></p>
<img src="https://secure.gravatar.com/avatar/6edf3a421a450237beae62ba93582637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hjart&#39;s gravatar image" />
<p><span>Hjart</span><br />
<span class="score" title="2961 reputation points"><span>3.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hjart has 14 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 May '18, 21:08</strong> </span></p>
</div>
</div>
<div id="comments-container-63566" class="comments-container">
<span id="63567"></span>
<div id="comment-63567" class="comment">
<div id="post-63567-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answers. Is it possible, that the URL was truncated?</p>
</div>
<div id="comment-63567-info" class="comment-info">
<span class="comment-age">(19 May '18, 21:02)</span> <span class="comment-user userinfo">Druzhba</span>
</div>
</div>
<span id="63568"></span>
<div id="comment-63568" class="comment">
<div id="post-63568-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry,the trailing comma wasn't supposed to be a part of the link. I've fixed it now</p>
</div>
<div id="comment-63568-info" class="comment-info">
<span class="comment-age">(19 May '18, 21:10)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
</div>
<div id="comment-tools-63566" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63566-form-container" class="comment-form-container">
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

