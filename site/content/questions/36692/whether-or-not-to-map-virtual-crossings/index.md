+++
type = "question"
title = "Whether or not to map virtual crossings"
description = '''Imagine a simple intersection of two streets. Both streets have sidewalks on each side. But, there is no marked way for pedestrians to cross the street walking from one sidewalk to the oposite one. Should I map a way with &quot;crossing=unmarked&quot;, &quot;footway=crossing&quot; and/or &quot;highway=footway&quot;? There is no ...'''
date = "2014-09-09T01:36:00Z"
lastmod = "2014-09-10T03:25:00Z"
weight = 36692
keywords = [ "crossing", "pedestrian", "sidewalk" ]
aliases = [ "/questions/36692" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Whether or not to map virtual crossings](/questions/36692/whether-or-not-to-map-virtual-crossings)

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
<span id="post-36692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36692-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Imagine a simple intersection of two streets. Both streets have sidewalks on each side. But, there is no marked way for pedestrians to cross the street walking from one sidewalk to the oposite one.</p>
<p>Should I map a way with "crossing=unmarked", "footway=crossing" and/or "highway=footway"? There is no such an explicit way in the real world, but people usually cross the street there. I'm afraid that routing on foot wouldn't let you cross the street. There is no marked crossing in a long distance, not even something like this:</p>
<p><img src="http://wiki.openstreetmap.org/w/images/thumb/1/10/Crossing_with_sloped_curbs.jpg/800px-Crossing_with_sloped_curbs.jpg" alt="Slightly (un)marked crossing" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-crossing" rel="tag" title="see questions tagged &#39;crossing&#39;">crossing</span> <span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span> <span class="post-tag tag-link-sidewalk" rel="tag" title="see questions tagged &#39;sidewalk&#39;">sidewalk</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Sep '14, 01:36</strong></p>
<img src="https://secure.gravatar.com/avatar/552d28190b10de4eb02f7e0891aefa5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xoko&#39;s gravatar image" />
<p><span>xoko</span><br />
<span class="score" title="75 reputation points">75</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xoko has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-36692" class="comments-container">
<span id="36702"></span>
<div id="comment-36702" class="comment">
<div id="post-36702-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You write "not even something like this", but then what is there? crossing=unmarked would be perfect for the situation in your image, but if there is no physical connection between the sidewalk and the road at all, then I don't think this can be mapped. (An informal footpath carved by usage <em>could</em> be mapped, however.)</p>
</div>
<div id="comment-36702-info" class="comment-info">
<span class="comment-age">(09 Sep '14, 11:44)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="36711"></span>
<div id="comment-36711" class="comment">
<div id="post-36711-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is nothing at all.</p>
</div>
<div id="comment-36711-info" class="comment-info">
<span class="comment-age">(09 Sep '14, 15:50)</span> <span class="comment-user userinfo">xoko</span>
</div>
</div>
</div>
<div id="comment-tools-36692" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36692-form-container" class="comment-form-container">
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

<span id="36698"></span>

<div id="answer-container-36698" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36698-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-36698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No. I would just make sure the path nodes connect to the road, otherwise walking routing won't work. If crossing is illegal at that point or as a barrier then the path should join the road where foot crossing is allowed, even if there is no zebra or light controlled crossing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Sep '14, 09:29</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Sep '14, 09:30</strong> </span></p>
</div>
</div>
<div id="comments-container-36698" class="comments-container">
<span id="36710"></span>
<div id="comment-36710" class="comment">
<div id="post-36710-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not sure about the legality of crossing the street where it is not marked. If it is not, I understand you're proposing not to connect the sidewalk at this uncertain point, only when it's explicit, such as these cases: <a href="http://wiki.openstreetmap.org/wiki/Crossing#Examples.">http://wiki.openstreetmap.org/wiki/Crossing#Examples.</a> What do you think about "crossing=no", though?</p>
</div>
<div id="comment-36710-info" class="comment-info">
<span class="comment-age">(09 Sep '14, 15:50)</span> <span class="comment-user userinfo">xoko</span>
</div>
</div>
<span id="36712"></span>
<div id="comment-36712" class="comment">
<div id="post-36712-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Legality varies by jurisiction - for example in England and Wales you can cross a street anywhere you like (provided that you don't break any other laws in the process), although there are explicit exceptions, like here:</p>
<p><a href="http://www.openstreetmap.org/changeset/25330411">http://www.openstreetmap.org/changeset/25330411</a></p>
</div>
<div id="comment-36712-info" class="comment-info">
<span class="comment-age">(09 Sep '14, 16:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="36722"></span>
<div id="comment-36722" class="comment">
<div id="post-36722-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In your example I see no other sidewalks crossing the street other than some explictly marked (traffic lights).</p>
</div>
<div id="comment-36722-info" class="comment-info">
<span class="comment-age">(10 Sep '14, 03:23)</span> <span class="comment-user userinfo">xoko</span>
</div>
</div>
<span id="36723"></span>
<div id="comment-36723" class="comment">
<div id="post-36723-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Also, about the legality in the US (which is the case), I've found this: <a href="http://en.wikipedia.org/wiki/Pedestrian_crossing#cite_note-7.">http://en.wikipedia.org/wiki/Pedestrian_crossing#cite_note-7.</a> From where I deduce that in the US you can cross at all intersections.</p>
</div>
<div id="comment-36723-info" class="comment-info">
<span class="comment-age">(10 Sep '14, 03:25)</span> <span class="comment-user userinfo">xoko</span>
</div>
</div>
</div>
<div id="comment-tools-36698" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36698-form-container" class="comment-form-container">
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

