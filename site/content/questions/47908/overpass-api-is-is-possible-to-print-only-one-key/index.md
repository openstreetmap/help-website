+++
type = "question"
title = "[Overpass-api] Is is possible to print only one key?"
description = '''I need to know if its possible to print only the required key, for eg: i need nodes with add:street key , but what i want in the output is only that addr:street key not other tags like name,addr:city etc.'''
date = "2016-02-04T13:10:00Z"
lastmod = "2016-02-04T13:54:00Z"
weight = 47908
keywords = [ "overpassapi", "overpass" ]
aliases = [ "/questions/47908" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[Overpass-api\] Is is possible to print only one key?](/questions/47908/overpass-api-is-is-possible-to-print-only-one-key)

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
<span id="post-47908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47908-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to know if its possible to print only the required key, for eg: i need nodes with add:street key , but what i want in the output is only that addr:street key not other tags like name,addr:city etc.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Feb '16, 13:10</strong></p>
<img src="https://secure.gravatar.com/avatar/dfcf9d391ca68ff816e8f9f8ec9f3fc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arun%20Gowtham&#39;s gravatar image" />
<p><span>Arun Gowtham</span><br />
<span class="score" title="0 reputation points">0</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arun Gowtham has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47908" class="comments-container">
&#10;</div>
<div id="comment-tools-47908" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47908-form-container" class="comment-form-container">
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

<span id="47909"></span>

<div id="answer-container-47909" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47909-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Output_Format_.28out.29">out:csv</a> is one way to do this.</p>
<p>Something like (untested) <code>[out:csv(::lat,::lon,"addr:street")]</code>.</p>
<p>For ways and relations, <code>::lat</code> and <code>::lon</code> are output if you also use <code>out center</code> as your print statement. If you aren't interested in the coordinates, they can also just be omitted.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '16, 13:35</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-47909" class="comments-container">
<span id="47911"></span>
<div id="comment-47911" class="comment">
<div id="post-47911-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a> Is there any workaround for JSON format?</p>
</div>
<div id="comment-47911-info" class="comment-info">
<span class="comment-age">(04 Feb '16, 13:41)</span> <span class="comment-user userinfo">Arun Gowtham</span>
</div>
</div>
<span id="47912"></span>
<div id="comment-47912" class="comment">
<div id="post-47912-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not that I know of. I guess it is easy enough to do on the client side that filtering tags isn't a high priority.</p>
</div>
<div id="comment-47912-info" class="comment-info">
<span class="comment-age">(04 Feb '16, 13:54)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-47909" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47909-form-container" class="comment-form-container">
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

