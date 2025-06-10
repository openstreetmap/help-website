+++
type = "question"
title = "Use iD editor for custom tile server."
description = '''Can I use iD editor to edit a data on a custom tile server?'''
date = "2018-02-24T07:04:00Z"
lastmod = "2018-02-24T12:42:00Z"
weight = 62356
keywords = [ "ideditor", "tileserver" ]
aliases = [ "/questions/62356" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Use iD editor for custom tile server.](/questions/62356/use-id-editor-for-custom-tile-server)

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
<span id="post-62356-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62356-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62356-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can I use iD editor to edit a data on a custom tile server?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Feb '18, 07:04</strong></p>
<img src="https://secure.gravatar.com/avatar/3d72aab1ba0daf6b6c28de5c6daaf5af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sugandalai&#39;s gravatar image" />
<p><span>sugandalai</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sugandalai has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62356" class="comments-container">
&#10;</div>
<div id="comment-tools-62356" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62356-form-container" class="comment-form-container">
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

<span id="62367"></span>

<div id="answer-container-62367" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62367-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sugandalai has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Editable OSM data is typically stored in an API schema database (most common example provided by the "rails-port" see <a href="https://github.com/openstreetmap/openstreetmap-website">https://github.com/openstreetmap/openstreetmap-website</a> ) with access provided by the OSM API (see <a href="https://wiki.openstreetmap.org/wiki/API_v0.6">https://wiki.openstreetmap.org/wiki/API_v0.6</a> ) this is how all modern editing apps interact with the data, including iD.</p>
<p>Tile servers, essentially regardless of the concrete implementation, require that the raw OSM data be converted in to actual geometry objects (in the API schema only the nodes hold location information), and stored in a database capable of handling spatial queries on such objects.</p>
<p>So the answer is a qualified "no", what you can naturally do is replicate the setup of the central OSM system: an instance of the rails-port holding your data and then synchronizing that via the minutely diff mechanism to your tileserver.</p>
<p>This is not that difficult to do, and if we are only talking about a small amount of data doesn't require anything very performant wrt hardware. If you are considering importing the whole planet then it is non-trivial.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '18, 12:42</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Feb '18, 15:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-62367" class="comments-container">
&#10;</div>
<div id="comment-tools-62367" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62367-form-container" class="comment-form-container">
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

