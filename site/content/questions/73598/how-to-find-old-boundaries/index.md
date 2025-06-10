+++
type = "question"
title = "How to find old boundaries"
description = '''Recently there have been changes in the provinces in Norway. I would like to know how I can find the old provinces in OSM. How do I search for those?'''
date = "2020-03-18T13:57:00Z"
lastmod = "2020-03-19T16:19:00Z"
weight = 73598
keywords = [ "polygons", "historical" ]
aliases = [ "/questions/73598" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to find old boundaries](/questions/73598/how-to-find-old-boundaries)

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
<span id="post-73598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73598-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Recently there have been changes in the provinces in Norway. I would like to know how I can find the old provinces in OSM. How do I search for those?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-polygons" rel="tag" title="see questions tagged &#39;polygons&#39;">polygons</span> <span class="post-tag tag-link-historical" rel="tag" title="see questions tagged &#39;historical&#39;">historical</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Mar '20, 13:57</strong></p>
<img src="https://secure.gravatar.com/avatar/d9857ae3e4f09cde43279e6968d656aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mischa&#39;s gravatar image" />
<p><span>Mischa</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mischa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73598" class="comments-container">
<span id="73612"></span>
<div id="comment-73612" class="comment">
<div id="post-73612-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your question is not really clear: are you looking for the current boundaries for the provinces so that you can update them, or are you looking for the previous versions because the updates have already been done?</p>
</div>
<div id="comment-73612-info" class="comment-info">
<span class="comment-age">(18 Mar '20, 19:47)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="73613"></span>
<div id="comment-73613" class="comment">
<div id="post-73613-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Or a third alternate: are you looking for a current relaiton that defines the old boundaries?</p>
</div>
<div id="comment-73613-info" class="comment-info">
<span class="comment-age">(18 Mar '20, 19:50)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="73616"></span>
<div id="comment-73616" class="comment">
<div id="post-73616-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>I'm sorry if I wasn't clear. What I mean is, how do I find the old relation that defines the former boundaries. Example: per January 1, 2020 the provinces of Buskerud, Akershus and Østfold were merged into a new province, Viken. How do I find the relation that defined the former province Akershus? What happens to those relations? Are they deleted?</p>
</div>
<div id="comment-73616-info" class="comment-info">
<span class="comment-age">(19 Mar '20, 06:42)</span> <span class="comment-user userinfo">Mischa</span>
</div>
</div>
</div>
<div id="comment-tools-73598" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73598-form-container" class="comment-form-container">
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

<span id="73620"></span>

<div id="answer-container-73620" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73620-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OK, unluckily the answer is "it depends".</p>
<p>The good news is that nothing in OSM is actually ever "deleted" so in principle the old information will still be there in any case. However, the bad news, it may be a significant amount of work to extract whatever information you want to have.</p>
<p>To the "it depends" bit: what happens with the old relations and old border ways is a question of local policy/whatever the person making the changes decided to do. You can and should naturally should ask on the NO communications channels about this. In my experience (this year was the first time after many years that I didn't organize the similar effort in Switzerland to update our municipality boundaries), this tends to be a matter of much debate.</p>
<p>But we don't have to wait for that to have a look. The changeset that made the new county "Viken" "active" was <a href="https://www.openstreetmap.org/changeset/78911743#map=5/65.440/17.930">https://www.openstreetmap.org/changeset/78911743#map=5/65.440/17.930</a> (found by working backwards from the current data).</p>
<p>It says in its comments that the old boundaries were retained as multipolygons, and see for example <a href="https://www.openstreetmap.org/relation/406106">https://www.openstreetmap.org/relation/406106</a> for Akershus.</p>
<p>PS: I'm not particularly enthusiastic about retaining the old boundaries as unspecific multi-polygons, as they cannot be searched for and found that way, but still add complexity to our data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Mar '20, 09:39</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Mar '20, 09:42</strong> </span></p>
</div>
</div>
<div id="comments-container-73620" class="comments-container">
<span id="73621"></span>
<div id="comment-73621" class="comment">
<div id="post-73621-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanx! That is already much clearer. But what I don't quite understand is that working backwards. If I work backwards from the new county Viken I get a different changeset. From which relation did you work backwards?</p>
</div>
<div id="comment-73621-info" class="comment-info">
<span class="comment-age">(19 Mar '20, 13:27)</span> <span class="comment-user userinfo">Mischa</span>
</div>
</div>
<span id="73630"></span>
<div id="comment-73630" class="comment">
<div id="post-73630-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you work backwards through <a href="https://www.openstreetmap.org/relation/10155539/history">https://www.openstreetmap.org/relation/10155539/history</a> , the changeset Simon mentioned is the earliest one with the tag boundary=administrative. The relation existed prior to that, as it was created earlier in preparation for the changes. But it was tagged as proposed:boundary=administrative, which would be ignored by most users of the data. As it happens the old Akershus relation has been treated in a similar way in reverse, as it is now tagged was:boundary=administrative. (As Simon says there are multiple approaches to this, so nobody reading this should count on this working beyond this specific case).</p>
</div>
<div id="comment-73630-info" class="comment-info">
<span class="comment-age">(19 Mar '20, 16:12)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="73631"></span>
<div id="comment-73631" class="comment">
<div id="post-73631-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If it helps to visualise it, you can also look at <a href="http://osm.mapki.com/history/relation.php?id=10155539">http://osm.mapki.com/history/relation.php?id=10155539</a> .</p>
</div>
<div id="comment-73631-info" class="comment-info">
<span class="comment-age">(19 Mar '20, 16:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-73620" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73620-form-container" class="comment-form-container">
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

