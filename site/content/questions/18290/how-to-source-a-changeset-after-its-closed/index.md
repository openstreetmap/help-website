+++
type = "question"
title = "How to source=* a changeset after its closed?"
description = '''I have been source=* my elements, but for this changeset I decided to try putting the source attribution in the changeset instead. lo and behold I forgot to source my changeset. How can I select all members of a changeset to simply make another changeset with a source=Bing? Looks like I got 43 ways ...'''
date = "2012-12-08T14:51:00Z"
lastmod = "2012-12-12T12:26:00Z"
weight = 18290
keywords = [ "source", "missing", "mistake" ]
aliases = [ "/questions/18290" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to source=\* a changeset after its closed?](/questions/18290/how-to-source-a-changeset-after-its-closed)

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
<span id="post-18290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18290-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been source=* my elements, but for this changeset I decided to try putting the source attribution in the changeset instead. lo and behold I forgot to source my changeset. How can I select all members of a changeset to simply make another changeset with a source=Bing? Looks like I got 43 ways to attribute...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span> <span class="post-tag tag-link-mistake" rel="tag" title="see questions tagged &#39;mistake&#39;">mistake</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Dec '12, 14:51</strong></p>
<img src="https://secure.gravatar.com/avatar/391dd37726bc8eadfad6c66c0e114928?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="j_smurfy&#39;s gravatar image" />
<p><span>j_smurfy</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="j_smurfy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18290" class="comments-container">
&#10;</div>
<div id="comment-tools-18290" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18290-form-container" class="comment-form-container">
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

<span id="18345"></span>

<div id="answer-container-18345" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18345-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="j_smurfy has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As said by Simon, you can't in the current state of the API, add a source tag to a previous changeset. The only overkill solution would be to revert (cancel) your changeset and re-do it with the correct source tag.</p>
<p>That's why your best option would be to add the source tag to all object modified in your changeset, and to do that :</p>
<ul>
<li>Open JOSM</li>
<li>Download the whole zone (if possible)</li>
<li>ctrl+F to find</li>
<li>changeset:your changeset number</li>
<li>find</li>
<li>Add your source tag (it will add on all object selected)</li>
</ul>
<p>(I guess it might not work on objects modified since your changeset)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Dec '12, 22:53</strong></p>
<img src="https://secure.gravatar.com/avatar/0137f3597f9ca0efbda5c3b1e2678aa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sly&#39;s gravatar image" />
<p><span>sly</span><br />
<span class="score" title="290 reputation points">290</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sly has one accepted answer">25%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Dec '12, 22:55</strong> </span></p>
</div>
</div>
<div id="comments-container-18345" class="comments-container">
<span id="18350"></span>
<div id="comment-18350" class="comment">
<div id="post-18350-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>sly, looks like it worked. First time using JOSM, too. Thanks!</p>
</div>
<div id="comment-18350-info" class="comment-info">
<span class="comment-age">(11 Dec '12, 02:36)</span> <span class="comment-user userinfo">j_smurfy</span>
</div>
</div>
</div>
<div id="comment-tools-18345" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18345-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18297"></span>

<div id="answer-container-18297" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18297-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-18297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Changeset tags can't be changed/added currently after creating the changeset (and there are no plans to add such a facility).</p>
<p>BTW it should be source=bing imagery or similar (IMHO), assuming you were actually using their aerial imagery.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Dec '12, 19:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Dec '12, 10:32</strong> </span></p>
</div>
</div>
<div id="comments-container-18297" class="comments-container">
<span id="18298"></span>
<div id="comment-18298" class="comment">
<div id="post-18298-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>source=Bing is the recommended (and commonly used) source tag for changesets made using Bing aerial imagery. See e.g. <a href="https://wiki.openstreetmap.org/wiki/Bing#Source_tag">Bing#Source_tag</a> in the wiki, but also other pages.</p>
</div>
<div id="comment-18298-info" class="comment-info">
<span class="comment-age">(08 Dec '12, 19:15)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="18308"></span>
<div id="comment-18308" class="comment">
<div id="post-18308-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The wiki is littered with references of tag=astericks, I used that notation in my question. I am not placing source=astericks if that is what you mean. Also I understand changesets are permanent and perhaps I should rephrase the question. What I really mean is 'How do I select ALL elements from a previous changeset?' Or 'How do I make a changeset referencing another changeset?' Or 'Can I simultaneaously rollback/delete a changeset and copy its contents for editing, saving as new changeset?' I just need to duplicate a changeset's contents, add the tag, and save out a new changeset.Thanks!</p>
</div>
<div id="comment-18308-info" class="comment-info">
<span class="comment-age">(09 Dec '12, 02:00)</span> <span class="comment-user userinfo">j_smurfy</span>
</div>
</div>
<span id="18309"></span>
<div id="comment-18309" class="comment">
<div id="post-18309-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>About the only way to acheive what you want to do, is to add a source tag after the fact to the ways you created and further add a note tag explaining that it should have already been on the original changeset. I personally however would consider that massive overkill and would just leave the data as it is and try to do better next time.</p>
</div>
<div id="comment-18309-info" class="comment-info">
<span class="comment-age">(09 Dec '12, 10:35)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="18397"></span>
<div id="comment-18397" class="comment">
<div id="post-18397-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For example: I use source=Bing dated 2008 It allows others to justify changing my entries based on newer data which could even include newer Bing imagery in years to come.</p>
</div>
<div id="comment-18397-info" class="comment-info">
<span class="comment-age">(12 Dec '12, 12:26)</span> <span class="comment-user userinfo">dcp</span>
</div>
</div>
</div>
<div id="comment-tools-18297" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18297-form-container" class="comment-form-container">
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

