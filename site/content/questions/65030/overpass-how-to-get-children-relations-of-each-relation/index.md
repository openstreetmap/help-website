+++
type = "question"
title = "(overpass) How to get children relations of each relation?"
description = '''[out:csv(::type, ::id, name, admin_level, parent_id)];  rel(295480)-&amp;gt;.c; .c map_to_area; rel(area)[admin_level=4];  foreach(  convert rel ::id = id(), ::=::, parent_id=set(id()); // save as parent_id  // how to now get each set of children of the admin_level bellow?.  out;  );  // the goal is to ...'''
date = "2018-07-30T19:49:00Z"
lastmod = "2018-07-30T19:49:00Z"
weight = 65030
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/65030" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [(overpass) How to get children relations of each relation?](/questions/65030/overpass-how-to-get-children-relations-of-each-relation)

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
<span id="post-65030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65030-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<pre><code>[out:csv(::type, ::id, name, admin_level, parent_id)];
&#10;rel(295480)-&gt;.c;
.c map_to_area;
rel(area)[admin_level=4];
&#10;foreach(
  convert rel ::id = id(), ::=::, parent_id=set(id()); // save as parent_id
  // how to now get each set of children of the admin_level bellow?.
  out;  
);
&#10;// the goal is to have:
// child 1 ... parent 1
// child 2 ... parent 1
// child 3 ... parent 1
// child 1 ... parent 2
// child 2 ... parent 2
// ...</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '18, 19:49</strong></p>
<img src="https://secure.gravatar.com/avatar/7dcc267e54465a74eea1ce059e3432f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andrefrsilva&#39;s gravatar image" />
<p><span>andrefrsilva</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andrefrsilva has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65030" class="comments-container">
&#10;</div>
<div id="comment-tools-65030" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65030-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

