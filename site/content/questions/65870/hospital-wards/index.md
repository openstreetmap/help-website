+++
type = "question"
title = "Hospital wards"
description = '''Hospitals in my city are organized as following:  they are typically located in several smaller buildings, each having their own number (building 1, building 5A and so on). &quot;Building #1&quot; goes into the name, right? each building holds one or more wards. For example: building number 1 holds surgical w...'''
date = "2018-09-12T18:08:00Z"
lastmod = "2018-09-16T19:46:00Z"
weight = 65870
keywords = [ "hospital", "emergency", "tagging" ]
aliases = [ "/questions/65870" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Hospital wards](/questions/65870/hospital-wards)

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
<span id="post-65870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65870-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hospitals in my city are organized as following:</p>
<ul>
<li>they are typically located in several smaller buildings, each having their own number (building 1, building 5A and so on). "Building #1" goes into the name, right?</li>
<li>each building holds one or more wards. For example: building number 1 holds surgical ward and hepatology ward. How do I tag these? I've put that into name: "Building #1 - wards: surgical, hepatology" - but this doesn't feel right</li>
<li>when you have an emergency you go to a reception room where they put you on a stretcher if necessary and transfer you to the doctor. I've seen <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Tag:emergency%3Demergency_ward_entrance">this proposed feature</a> in the wiki but it doesn't seem to be implemented - not even autocompletion in iD knows about this tag. What's the right way to tag it? It's the most crucial information in life threatening situations and it's not always obvious where this entrance is.</li>
</ul>
<p>Any idea about this, or maybe someone could point me to a properly tagged hospital with all that information?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hospital" rel="tag" title="see questions tagged &#39;hospital&#39;">hospital</span> <span class="post-tag tag-link-emergency" rel="tag" title="see questions tagged &#39;emergency&#39;">emergency</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Sep '18, 18:08</strong></p>
<img src="https://secure.gravatar.com/avatar/8d38646cc88f2d7d0e2c5a0536dd340e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wawg&#39;s gravatar image" />
<p><span>wawg</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wawg has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65870" class="comments-container">
&#10;</div>
<div id="comment-tools-65870" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65870-form-container" class="comment-form-container">
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

<span id="65914"></span>

<div id="answer-container-65914" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65914-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wawg has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>WRT to "wards" I would suggest using SIT (<a href="https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging">Simple Indoor Tagging</a>) if you really want to go in to so much detail.</p>
<p>Entrances should be nodes tagged with "entrance=yes" (not with entrance=emergency that is for emergency exits) and potentially an appropriate name.</p>
<p>There is likely no harm in adding a emergency=emergency_ward_entrance tag to the entrance, but I wouldn't expect any rendering of it on its own.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '18, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Sep '18, 09:05</strong> </span></p>
</div>
</div>
<div id="comments-container-65914" class="comments-container">
&#10;</div>
<div id="comment-tools-65914" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65914-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65924"></span>

<div id="answer-container-65924" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65924-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A building number should go into a <em>ref</em> and not into a <em>name</em> in my opinion. Emergency ward entrances are for example rendered in <a href="https://wambachers-osm.website/emergency/">Wambacher's emergency map</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '18, 19:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-65924" class="comments-container">
&#10;</div>
<div id="comment-tools-65924" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65924-form-container" class="comment-form-container">
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

