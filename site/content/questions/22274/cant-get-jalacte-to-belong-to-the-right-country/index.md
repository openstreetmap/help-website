+++
type = "question"
title = "Can&#x27;t get Jalacte to belong to the right country"
description = '''A month ago (April 10), I noticed that the Belize/Guatemala border was very wrong. Several towns that were unquestionably part of Belize were shown to be on the wrong side of the border and in Guatemala instead. I fixed the border to be accurate (using the actual physical features that define the bo...'''
date = "2013-05-10T21:58:00Z"
lastmod = "2013-05-11T01:27:00Z"
weight = 22274
keywords = [ "caching", "guatemala", "belize", "bug" ]
aliases = [ "/questions/22274" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can't get Jalacte to belong to the right country](/questions/22274/cant-get-jalacte-to-belong-to-the-right-country)

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
<span id="post-22274-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22274-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22274-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A month ago (April 10), I noticed that the Belize/Guatemala border was very wrong. Several towns that were unquestionably part of Belize were shown to be on the wrong side of the border and in Guatemala instead. I fixed the border to be accurate (using the actual physical features that define the border), and double-checked it against maps.google.com, www.bing.com/maps/, and a CIA map. This put the towns back in the right countries (at least in edit view). A month later, the border in the non-editing interface is still wrong in all but 3 of the 19 zoom levels. In addition, if you search for a town like Jalacte, it still reports that the town belongs to Guatemala. How can this problem be fixed?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-caching" rel="tag" title="see questions tagged &#39;caching&#39;">caching</span> <span class="post-tag tag-link-guatemala" rel="tag" title="see questions tagged &#39;guatemala&#39;">guatemala</span> <span class="post-tag tag-link-belize" rel="tag" title="see questions tagged &#39;belize&#39;">belize</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 May '13, 21:58</strong></p>
<img src="https://secure.gravatar.com/avatar/3ea139a72c7705308d73069fa3be5e01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kaldari&#39;s gravatar image" />
<p><span>kaldari</span><br />
<span class="score" title="35 reputation points">35</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kaldari has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22274" class="comments-container">
&#10;</div>
<div id="comment-tools-22274" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22274-form-container" class="comment-form-container">
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

<span id="22276"></span>

<div id="answer-container-22276" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22276-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim says <a href="http://nominatim.openstreetmap.org/details.php?place_id=3666062473">Jalacte</a> belongs to Petén, which in turn belongs to Guatemala. <a href="http://keepright.ipax.at/report_map.php?schema=68&amp;error=46722696">KeepRight</a> says "The boundary of Petén is not closed-loop". The <a href="http://www.openstreetmap.org/browse/relation/214699">Petén (214699)</a>-relation has this problem in a number of places.</p>
<p>So, my guess is that the Petén relation is leaking. Fix the relation, and the problem might be gone. (But there are more "not closed-loop"-errors in the region, so new problems may arise.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 May '13, 23:05</strong></p>
<img src="https://secure.gravatar.com/avatar/c2a980da3fdfa1ee2659ad70d1e21f31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnurk&#39;s gravatar image" />
<p><span>gnurk</span><br />
<span class="score" title="6114 reputation points"><span>6.1k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="silver">●</span><span class="badgecount">60</span></span><span title="96 badges"><span class="bronze">●</span><span class="badgecount">96</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnurk has 18 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 May '13, 23:13</strong> </span></p>
</div>
</div>
<div id="comments-container-22276" class="comments-container">
<span id="22280"></span>
<div id="comment-22280" class="comment">
<div id="post-22280-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How do you make a boundary closed-loop? I can't seem to even find the Petan border in the editing interface. Would anyone be able to help with this. I'm afraid it may be a bit over my head :(</p>
</div>
<div id="comment-22280-info" class="comment-info">
<span class="comment-age">(10 May '13, 23:39)</span> <span class="comment-user userinfo">kaldari</span>
</div>
</div>
<span id="22285"></span>
<div id="comment-22285" class="comment">
<div id="post-22285-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I find it easier to fix boundary problems using JOSM, as the relation editor in JOSM shows very clearly when a boundary forms a closed loop or not.</p>
<p>I just fixed both the Petén and Izabal boundaries. They still used the river centerline and were not connected to the west boundary of Belize.</p>
</div>
<div id="comment-22285-info" class="comment-info">
<span class="comment-age">(11 May '13, 00:16)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="22292"></span>
<div id="comment-22292" class="comment">
<div id="post-22292-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! Hopefully that will help :)</p>
</div>
<div id="comment-22292-info" class="comment-info">
<span class="comment-age">(11 May '13, 01:27)</span> <span class="comment-user userinfo">kaldari</span>
</div>
</div>
</div>
<div id="comment-tools-22276" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22276-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22275"></span>

<div id="answer-container-22275" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22275-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22275-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22275-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After searching for 10 minutes or so I finally found the OSM bugtracking site and filed a bug: <a href="https://trac.openstreetmap.org/ticket/4857">https://trac.openstreetmap.org/ticket/4857</a></p>
<p>Why is that site so secret?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 May '13, 22:06</strong></p>
<img src="https://secure.gravatar.com/avatar/3ea139a72c7705308d73069fa3be5e01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kaldari&#39;s gravatar image" />
<p><span>kaldari</span><br />
<span class="score" title="35 reputation points">35</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kaldari has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22275" class="comments-container">
<span id="22284"></span>
<div id="comment-22284" class="comment">
<div id="post-22284-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Trac is for reporting bugs in software. What you found is a problem with the data, so it shouldn't go into trac.</p>
</div>
<div id="comment-22284-info" class="comment-info">
<span class="comment-age">(11 May '13, 00:09)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="22287"></span>
<div id="comment-22287" class="comment">
<div id="post-22287-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, there's also the problem that the boundary changes I made only show up at 3 of the 19 zoom levels. There seems to be some sort of caching issue there.</p>
</div>
<div id="comment-22287-info" class="comment-info">
<span class="comment-age">(11 May '13, 00:41)</span> <span class="comment-user userinfo">kaldari</span>
</div>
</div>
<span id="22289"></span>
<div id="comment-22289" class="comment">
<div id="post-22289-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That is probably a caching "problem" at your local PC. Try clearing your browser cache.</p>
<p>If I click on the <a href="http://nominatim.openstreetmap.org/details.php?place_id=3666062473">Jalacte link</a> in gnurk's answer and slowly zoom out, then I see the blue circle on the Belize side of the boundary in zoom level 18 till 10. Zooming further out it impossible to tell the difference.</p>
</div>
<div id="comment-22289-info" class="comment-info">
<span class="comment-age">(11 May '13, 00:50)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="22291"></span>
<div id="comment-22291" class="comment">
<div id="post-22291-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's definitely not my browser cache. I can completely reset Safari and empty the cache and I still get the same behavior, plus it is consistent for me across different browsers. Zoom levels 1 (maximum zoom) and 2 show the correct updated boundary. Zoom 3 and 4 show the old boundary (for the most part). Zoom 5 and 6 show the updated boundary. Everything else shows the old boundary (with the border cutting straight through Jalacte instead of being to the west of it).</p>
</div>
<div id="comment-22291-info" class="comment-info">
<span class="comment-age">(11 May '13, 01:07)</span> <span class="comment-user userinfo">kaldari</span>
</div>
</div>
</div>
<div id="comment-tools-22275" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22275-form-container" class="comment-form-container">
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

