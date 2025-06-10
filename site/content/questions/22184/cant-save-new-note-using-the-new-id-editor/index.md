+++
type = "question"
title = "Can&#x27;t save new note using the new iD editor"
description = '''I&#x27;ve only just started contributing to OpenStreetMap, so I may be doing something wrong, but I&#x27;m trying to add a note to a building and when I add the note to the &#x27;note&#x27; box and then close the metadata editor, it doesn&#x27;t seem to save. Furthermore, the Save button doesn&#x27;t become enabled, suggesting t...'''
date = "2013-05-08T10:38:00Z"
lastmod = "2013-05-08T15:08:00Z"
weight = 22184
keywords = [ "ideditor", "editing" ]
aliases = [ "/questions/22184" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can't save new note using the new iD editor](/questions/22184/cant-save-new-note-using-the-new-id-editor)

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
<span id="post-22184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22184-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've only just started contributing to OpenStreetMap, so I may be doing something wrong, but I'm trying to add a note to a building and when I add the note to the 'note' box and then close the metadata editor, it doesn't seem to save.</p>
<p>Furthermore, the Save button doesn't become enabled, suggesting that somehow the editor hasn't noticed that I have added a note.</p>
<p>Does anyone know what's going on here?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 May '13, 10:38</strong></p>
<img src="https://secure.gravatar.com/avatar/40153527fcfbed61d7fe98b2e427c71e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robintw147&#39;s gravatar image" />
<p><span>robintw147</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robintw147 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 May '13, 01:39</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-22184" class="comments-container">
&#10;</div>
<div id="comment-tools-22184" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22184-form-container" class="comment-form-container">
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

<span id="22195"></span>

<div id="answer-container-22195" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22195-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-22195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a misunderstanding. The notes interface to iD saves notes to the key:note tag ( <a href="http://wiki.openstreetmap.org/wiki/Key:note">http://wiki.openstreetmap.org/wiki/Key:note</a> ) (as explained with its documentation). The notes features is not implemented yet but will be ( <a href="https://github.com/systemed/iD/issues/1393">https://github.com/systemed/iD/issues/1393</a> ) and since this is likely to cause further confusion, we'll remove the Key:note UI.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 May '13, 15:08</strong></p>
<img src="https://secure.gravatar.com/avatar/5eea0a101ed06779f56546479dcc80b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mcw&#39;s gravatar image" />
<p><span>mcw</span><br />
<span class="score" title="416 reputation points">416</span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mcw has one accepted answer">6%</span></p>
</div>
</div>
<div id="comments-container-22195" class="comments-container">
&#10;</div>
<div id="comment-tools-22195" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22195-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22185"></span>

<div id="answer-container-22185" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22185-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I was able to recreate the described behaviour, it seems to be a geniune bug. Could you submit a bug report via the "Report a problem" (don't have the exact name in front of me) link in the lower right corner.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 May '13, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span> </br></p>
</div>
</div>
<div id="comments-container-22185" class="comments-container">
<span id="22186"></span>
<div id="comment-22186" class="comment">
<div id="post-22186-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Bug tracker for iD is at <a href="https://github.com/systemed/iD/issues?state=open">https://github.com/systemed/iD/issues?state=open</a></p>
</div>
<div id="comment-22186-info" class="comment-info">
<span class="comment-age">(08 May '13, 12:04)</span> <span class="comment-user userinfo">Mike N</span>
</div>
</div>
</div>
<div id="comment-tools-22185" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22185-form-container" class="comment-form-container">
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

