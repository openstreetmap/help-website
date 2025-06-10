+++
type = "question"
title = "U reference numbers"
description = '''Hi, We have been looking at the following map http://www.openstreetmap.org/#map=17/57.60007/-4.32581 and cannot find any comment as to what the black bold &#x27;U&#x27; references and numbers stand for, can you explain please. Peter'''
date = "2014-06-18T13:04:00Z"
lastmod = "2014-06-18T13:23:00Z"
weight = 34096
keywords = [ "u", "tags" ]
aliases = [ "/questions/34096" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [U reference numbers](/questions/34096/u-reference-numbers)

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
<span id="post-34096-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34096-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34096-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, We have been looking at the following map <a href="http://www.openstreetmap.org/#map=17/57.60007/-4.32581">http://www.openstreetmap.org/#map=17/57.60007/-4.32581</a> and cannot find any comment as to what the black bold 'U' references and numbers stand for, can you explain please.</p>
<p>Peter</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-u" rel="tag" title="see questions tagged &#39;u&#39;">u</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jun '14, 13:04</strong></p>
<img src="https://secure.gravatar.com/avatar/0562a303a5ae3f52480802387fd61957?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dryrun&#39;s gravatar image" />
<p><span>Dryrun</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dryrun has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jun '14, 14:15</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-34096" class="comments-container">
&#10;</div>
<div id="comment-tools-34096" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34096-form-container" class="comment-form-container">
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

<span id="34098"></span>

<div id="answer-container-34098" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34098-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-34098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect that it's the reference number for an unclassified road. Here's one (not yours - another example):</p>
<p><a href="http://www.openstreetmap.org/way/36913872">http://www.openstreetmap.org/way/36913872</a></p>
<p>In that case the previous mapper has added "source_ref:ref" to explain where they got it from (although I'd have just used source:ref personally).</p>
<p>One thing that they didn't do that I would have done would have been to add "ref:signed=no" if there's no sign on the ground - there's no point in a Satnav reading out "turn left on the U1234" if there's no U1234 sign anywhere.</p>
<p>If your example doesn't have any source for the ref I'd definitely ask the previous mapper where it came from - not all sources may be compatible.</p>
<p>Also, I'd consider using "<a href="http://taginfo.openstreetmap.org.uk/keys/official_ref">official_ref</a>" rather than "ref" for references for C, D and U roads that aren't actually signed. No-one knows the numbers apart from the council; it is only misleading to people such as yourself for a general purpose map to display them.</p>
<p>EDIT: Found <a href="http://www.openstreetmap.org/way/26143069">one of yours</a> - looks like one of the same set by the same previous mapper.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '14, 13:23</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jun '14, 13:32</strong> </span></p>
</div>
</div>
<div id="comments-container-34098" class="comments-container">
&#10;</div>
<div id="comment-tools-34098" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34098-form-container" class="comment-form-container">
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

