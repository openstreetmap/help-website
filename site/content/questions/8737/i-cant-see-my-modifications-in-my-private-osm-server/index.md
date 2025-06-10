+++
type = "question"
title = "I can&#x27;t see my modifications in my private osm server"
description = '''I&#x27;ve successfully implemented an osm server and registered potlatch with it. I don&#x27;t have anything in my db yet and i use osm&#x27;s tiles as base layer. The problem is that when i draw a line in potlatch2 and edit it&#x27;s properties i can&#x27;t see the changes in the view pane.In fact,i can&#x27;t see anything ther...'''
date = "2011-11-01T13:00:00Z"
lastmod = "2011-11-01T14:08:00Z"
weight = 8737
keywords = [ "edit", "potlatch", "changes" ]
aliases = [ "/questions/8737" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I can't see my modifications in my private osm server](/questions/8737/i-cant-see-my-modifications-in-my-private-osm-server)

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
<span id="post-8737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8737-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-8737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've successfully implemented an osm server and registered potlatch with it. I don't have anything in my db yet and i use osm's tiles as base layer.</p>
<p>The problem is that when i draw a line in potlatch2 and edit it's properties i can't see the changes in the view <a href="http://pane.In">pane.In</a> fact,i can't see anything there except the base layer (tiles). Potlatch saves successfully, i can still see my changes in the edit pane after i even restart my server + refresh page.</p>
<p>Any guesses?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-edit" rel="tag" title="see questions tagged &#39;edit&#39;">edit</span> <span class="post-tag tag-link-potlatch" rel="tag" title="see questions tagged &#39;potlatch&#39;">potlatch</span> <span class="post-tag tag-link-changes" rel="tag" title="see questions tagged &#39;changes&#39;">changes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Nov '11, 13:00</strong></p>
<img src="https://secure.gravatar.com/avatar/dc9b01669c0702f230fa57c384b947a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexz&#39;s gravatar image" />
<p><span>alexz</span><br />
<span class="score" title="225 reputation points">225</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8737" class="comments-container">
<span id="8739"></span>
<div id="comment-8739" class="comment">
<div id="post-8739-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you rendering your own tiles? Have you configured your site to point to your own tiles?</p>
</div>
<div id="comment-8739-info" class="comment-info">
<span class="comment-age">(01 Nov '11, 13:25)</span> <span class="comment-user userinfo">Jonathan Ben...</span>
</div>
</div>
<span id="8740"></span>
<div id="comment-8740" class="comment">
<div id="post-8740-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, i'm not rendering my owm tiles. Is that why i can't see my changes? Should i make my own tiles and rerender them after any change i make?</p>
</div>
<div id="comment-8740-info" class="comment-info">
<span class="comment-age">(01 Nov '11, 13:27)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
</div>
<div id="comment-tools-8737" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8737-form-container" class="comment-form-container">
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

<span id="8741"></span>

<div id="answer-container-8741" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8741-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to render a set of tiles from your data using Mapnik (or some other renderer) in order to be able to see it in the View tab. There are many questions and answers about this subject in this system already.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '11, 13:38</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-8741" class="comments-container">
<span id="8742"></span>
<div id="comment-8742" class="comment">
<div id="post-8742-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does this process goes somehow like this: export with osmosis to xml &gt; import the xml into GIS db &gt; configure mapnik to render the necessary portion &gt; do the rendering. ?</p>
</div>
<div id="comment-8742-info" class="comment-info">
<span class="comment-age">(01 Nov '11, 14:08)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
</div>
<div id="comment-tools-8741" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8741-form-container" class="comment-form-container">
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

