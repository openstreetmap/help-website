+++
type = "question"
title = "Is it possible to load all relation members to JOSM via remote control?"
description = '''I want to load a route relation into JOSM via the remote control. I tried to use load_object, but this only loads the relation itself and not its members. Now I&#x27;m looking for a possibility to load its members via remote control as well. Is there any possibility to do that? Or does anyone know how to...'''
date = "2014-06-20T09:14:00Z"
lastmod = "2015-02-17T16:41:00Z"
weight = 34169
keywords = [ "josm", "relations", "josm_remote_control" ]
aliases = [ "/questions/34169" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is it possible to load all relation members to JOSM via remote control?](/questions/34169/is-it-possible-to-load-all-relation-members-to-josm-via-remote-control)

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
<span id="post-34169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34169-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-34169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to load a route relation into JOSM via the remote control. I tried to use <code>load_object</code>, but this only loads the relation itself and not its members. Now I'm looking for a possibility to load its members via remote control as well.</p>
<p>Is there any possibility to do that? Or does anyone know how to achieve this without adding every single member id to the remote control URL?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-josm_remote_control" rel="tag" title="see questions tagged &#39;josm_remote_control&#39;">josm_remote_control</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jun '14, 09:14</strong></p>
<img src="https://secure.gravatar.com/avatar/89aa9c2f879ec54fbdff5687463667e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mapper999&#39;s gravatar image" />
<p><span>mapper999</span><br />
<span class="score" title="91 reputation points">91</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mapper999 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Apr '15, 17:01</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-34169" class="comments-container">
&#10;</div>
<div id="comment-tools-34169" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34169-form-container" class="comment-form-container">
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

<span id="41015"></span>

<div id="answer-container-41015" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41015-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-41015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mapper999 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a new parameter if you load objects: <code>relation_members</code> if you set it <code>true</code> using the <code>load_object</code> command, you get all members of the relation. The paramater and the other commands are explained here: <a href="https://josm.openstreetmap.de/wiki/Help/Preferences/RemoteControl">https://josm.openstreetmap.de/wiki/Help/Preferences/RemoteControl</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Feb '15, 21:11</strong></p>
<img src="https://secure.gravatar.com/avatar/99ef175794b71f7d10ee58523c5848d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christopher&#39;s gravatar image" />
<p><span>Christopher</span><br />
<span class="score" title="126 reputation points">126</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christopher has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-41015" class="comments-container">
<span id="41088"></span>
<div id="comment-41088" class="comment">
<div id="post-41088-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the information. Main advantage of this solution seems to be that parent relations are loaded into the editor as well.</p>
</div>
<div id="comment-41088-info" class="comment-info">
<span class="comment-age">(17 Feb '15, 16:41)</span> <span class="comment-user userinfo">mapper999</span>
</div>
</div>
</div>
<div id="comment-tools-41015" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41015-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="34177"></span>

<div id="answer-container-34177" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34177-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-34177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The remote control interface has a generic "import" method that allows you to specify any URL to be loaded. You could use that and specify the URL <a href="http://api.openstreetmap.org/api/0.6/relation/">http://api.openstreetmap.org/api/0.6/relation/</a><em>id</em>/full to load the full relation.</p>
<p>Note however that this operation can time out if you try to load very large relations, unlike JOSM's own "download relation with members" method which loads members individually.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jun '14, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-34177" class="comments-container">
<span id="34179"></span>
<div id="comment-34179" class="comment">
<div id="post-34179-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thank you Frederik for the quick answer. This worked without timeout for a relation with 400 members. For the record the full url for the remote control is <a href="http://127.0.0.1:8111/import?url=http://api.openstreetmap.org/api/0.6/relation/">http://127.0.0.1:8111/import?url=http://api.openstreetmap.org/api/0.6/relation/</a>&lt;id&gt;/full</p>
</div>
<div id="comment-34179-info" class="comment-info">
<span class="comment-age">(20 Jun '14, 10:32)</span> <span class="comment-user userinfo">mapper999</span>
</div>
</div>
</div>
<div id="comment-tools-34177" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34177-form-container" class="comment-form-container">
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

