+++
type = "question"
title = "What&#x27;s the best way to map a hospital department?"
description = '''I&#x27;ve had a look in the wiki and there&#x27;s surprisingly little. If it has a speciality I can use healthcare:speciality for that of course, but how to say &quot;this is a department of a hospital&quot; ? Can anyone point to hospital departments that have already been mapped?'''
date = "2017-10-22T16:02:00Z"
lastmod = "2017-11-14T21:16:00Z"
weight = 60217
keywords = [ "hospital", "tagging" ]
aliases = [ "/questions/60217" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What's the best way to map a hospital department?](/questions/60217/whats-the-best-way-to-map-a-hospital-department)

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
<span id="post-60217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60217-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've had a look in the wiki and there's surprisingly little. If it has a speciality I can use healthcare:speciality for that of course, but how to say "this is a department of a hospital" ?</p>
<p>Can anyone point to hospital departments that have already been mapped?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hospital" rel="tag" title="see questions tagged &#39;hospital&#39;">hospital</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '17, 16:02</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-60217" class="comments-container">
<span id="60220"></span>
<div id="comment-60220" class="comment">
<div id="post-60220-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there a particular hospital you're trying to map that you could link to? (to make the discussion concrete)</p>
<p>Would a spatial relation suffice? E.g., in my area a hospital department would be a building in the hospital campus; the campus would be a closed way tagged as a hospital and the building would be tagged with healthcare:specialty and reside within the campus.</p>
</div>
<div id="comment-60220-info" class="comment-info">
<span class="comment-age">(22 Oct '17, 21:59)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
<span id="60221"></span>
<div id="comment-60221" class="comment">
<div id="post-60221-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, York District Hospital. The hospital building itself is <a href="https://www.openstreetmap.org/relation/916106#map=16/53.9702/-1.0840">https://www.openstreetmap.org/relation/916106#map=16/53.9702/-1.0840</a> and I've so far added some departments as e.g. <a href="https://www.openstreetmap.org/node/4785109291">https://www.openstreetmap.org/node/4785109291</a> , but without any tagging of them beyond a "name" it's difficult to do much with them.</p>
</div>
<div id="comment-60221-info" class="comment-info">
<span class="comment-age">(22 Oct '17, 22:30)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-60217" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60217-form-container" class="comment-form-container">
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

<span id="60621"></span>

<div id="answer-container-60621" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60621-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As you already discovered, <a href="https://wiki.openstreetmap.org/wiki/Key:healthcare">healthcare=*</a> is a established schema. To group departments, I know different approaches: * hospital &gt; clinic &gt; centre so you might want to chose clinic for facilities on the site * operator tag * <a href="https://wiki.openstreetmap.org/wiki/Relation:site">site relation</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '17, 21:16</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-60621" class="comments-container">
&#10;</div>
<div id="comment-tools-60621" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60621-form-container" class="comment-form-container">
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

