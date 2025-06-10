+++
type = "question"
title = "Tagging railway stations on heritage railway"
description = '''Hi all, I&#x27;m seeking advice on how to tag railway stations on a heritage railway. The railway is tagged railway:preserved=yes but am unsure how to properly tag the stations (e.g. https://www.openstreetmap.org/node/8921361750) There is no guidance on the wiki page or precedent that I can find. My main...'''
date = "2021-11-24T09:58:00Z"
lastmod = "2021-11-24T18:50:00Z"
weight = 82670
keywords = [ "railway" ]
aliases = [ "/questions/82670" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tagging railway stations on heritage railway](/questions/82670/tagging-railway-stations-on-heritage-railway)

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
<span id="post-82670-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82670-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82670-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I'm seeking advice on how to tag railway stations on a heritage railway.</p>
<p>The railway is tagged railway:preserved=yes but am unsure how to properly tag the stations (e.g. <a href="https://www.openstreetmap.org/node/8921361750">https://www.openstreetmap.org/node/8921361750</a>)</p>
<p>There is no guidance on the wiki page or precedent that I can find.</p>
<p>My main concern with using the usual railway=station is that this will mess up directions APIs and similar things for people looking for their closest operating railway station - as one example.</p>
<p>Can anyone assist?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Nov '21, 09:58</strong></p>
<img src="https://secure.gravatar.com/avatar/109b4b042580ca2017fb1f29d0602e71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="philam48&#39;s gravatar image" />
<p><span>philam48</span><br />
<span class="score" title="86 reputation points">86</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="philam48 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Nov '21, 13:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-82670" class="comments-container">
&#10;</div>
<div id="comment-tools-82670" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82670-form-container" class="comment-form-container">
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

<span id="82676"></span>

<div id="answer-container-82676" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82676-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Tag:usage=tourism"><code>usage=tourism</code></a> tag looks like it might be suitable for this.</p>
<p>It should at least give something that does static renders something to go on. I would hope that anything that tries to give directions would only suggest a train station if there was some onward connection to the final destination through e.g. <a href="https://wiki.openstreetmap.org/wiki/Tag:route%3Dtrain"><code>route=train</code></a> or external timetables.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Nov '21, 18:50</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-82676" class="comments-container">
&#10;</div>
<div id="comment-tools-82676" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82676-form-container" class="comment-form-container">
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

