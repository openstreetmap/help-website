+++
type = "question"
title = "Exporting administrative boundaries"
description = '''I have been trying to export the administrative boundaries for Poland at the LAU-2 level. In Polish, the level is referred to as a gmina and I can see each one if I search in OSM for gmina &amp;lt;name&amp;gt; (eg. gmina dopiewo). From this, I know that this level is present in OSM. However, I have not been...'''
date = "2013-05-24T15:11:00Z"
lastmod = "2013-05-25T20:10:00Z"
weight = 22729
keywords = [ "admin_level", "export", "administrative" ]
aliases = [ "/questions/22729" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Exporting administrative boundaries](/questions/22729/exporting-administrative-boundaries)

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
<span id="post-22729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22729-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been trying to export the administrative boundaries for Poland at the LAU-2 level. In Polish, the level is referred to as a gmina and I can see each one if I search in OSM for gmina &lt;name&gt; (eg. gmina dopiewo). From this, I know that this level is present in OSM. However, I have not been able to download this information using XAPI, JOSM or extracting the info using osmosis. Can someone point me in the right direction to getting this out of OSM so that I can use it in other programs (such as qgis)? Please don't point me to other sources (SALB, GADM, etc.) as the info is not present at this level - only the next level up. Thanks for the help. Paul</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-admin_level" rel="tag" title="see questions tagged &#39;admin_level&#39;">admin_level</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-administrative" rel="tag" title="see questions tagged &#39;administrative&#39;">administrative</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 May '13, 15:11</strong></p>
<img src="https://secure.gravatar.com/avatar/7589aa67352c782ed3e3728574f262b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pawelh&#39;s gravatar image" />
<p><span>pawelh</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pawelh has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22729" class="comments-container">
&#10;</div>
<div id="comment-tools-22729" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22729-form-container" class="comment-form-container">
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

<span id="22742"></span>

<div id="answer-container-22742" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22742-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-22742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pawelh has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use Overpass API with the expression</p>
<pre><code>(
  relation
    [&quot;boundary&quot;=&quot;administrative&quot;]
    [&quot;admin_level&quot;=&quot;7&quot;]
&#10;  ({{bbox}}) /* this is auto-completed with the
              current map view coordinates. */
&#10;);
/*added by auto repair*/
(._;&gt;;);
/*end of auto repair*/
out;</code></pre>
<p>See <a href="http://overpass-turbo.eu/s/dO">http://overpass-turbo.eu/s/dO</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '13, 19:27</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 May '13, 19:27</strong> </span></p>
</div>
</div>
<div id="comments-container-22742" class="comments-container">
<span id="22752"></span>
<div id="comment-22752" class="comment">
<div id="post-22752-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You'll have to run the query manually, the auto-run feature of overpass-turbo seems broken. just click "OK" on the error message, click inside the textbox with the query and press ctrl-enter.</p>
</div>
<div id="comment-22752-info" class="comment-info">
<span class="comment-age">(25 May '13, 08:34)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-22742" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22742-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22764"></span>

<div id="answer-container-22764" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22764-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22764-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-22764-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are not the first one asking this question.</p>
<p>Please type keywords like "extract boundaries" or "export borders" or similar in the searchbox of this FAQ site, and you will get a number of hints about your aim.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '13, 20:10</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-22764" class="comments-container">
&#10;</div>
<div id="comment-tools-22764" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22764-form-container" class="comment-form-container">
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

